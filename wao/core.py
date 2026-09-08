from __future__ import annotations

import json
import uuid
from typing import Any

from openai import AsyncOpenAI
from openai.types.responses import Response

from .config import settings
from .models import ExecutionResult, TaskPlan, TaskRequest
from .prompts import SYSTEM_INSTRUCTIONS
from .security import assess_untrusted_content


class WAOEngine:
    def __init__(self, client: AsyncOpenAI | None = None) -> None:
        if client is None:
            if not settings.openai_api_key:
                raise RuntimeError("WAO_OPENAI_API_KEY is required for model execution")
            client = AsyncOpenAI(api_key=settings.openai_api_key)
        self.client = client

    def normalize(self, request: TaskRequest) -> TaskPlan:
        assessment = assess_untrusted_content(request.task)
        policy = 'read_only' if assessment.untrusted else ('normal' if request.allow_tools else 'none')
        return TaskPlan(
            objective=request.task.strip(),
            normalized_context=request.context,
            constraints=request.constraints,
            subtasks=[
                'Identify the required outcome and material assumptions.',
                'Execute the minimum sufficient reasoning/tool work.',
                'Verify factual, logical and format requirements.',
                'Synthesize the final response for the requested audience.'
            ],
            verification_criteria=[
                'No unsupported claims of completed actions or tool use.',
                'Material assumptions are explicit.',
                'Requested output format is satisfied.'
            ],
            tool_policy=policy,
        )

    def _input(self, request: TaskRequest, plan: TaskPlan) -> str:
        return json.dumps(
            {
                'context': request.context,
                'task': request.task,
                'constraints': request.constraints,
                'requested_output_format': request.output_format,
                'execution_plan': plan.model_dump(),
            },
            ensure_ascii=False,
            indent=2,
        )

    async def execute(self, request: TaskRequest) -> ExecutionResult:
        request_id = str(uuid.uuid4())
        plan = self.normalize(request)
        response: Response = await self.client.responses.create(
            model=settings.openai_model,
            instructions=SYSTEM_INSTRUCTIONS,
            input=self._input(request, plan),
            max_output_tokens=settings.max_output_tokens,
        )
        output = response.output_text.strip()
        warnings: list[str] = []
        assessment = assess_untrusted_content(request.task)
        if assessment.untrusted:
            warnings.append('Prompt-injection indicators detected; tool policy reduced to read-only.')
        return ExecutionResult(
            request_id=request_id,
            status='completed',
            response=output,
            plan=plan,
            warnings=warnings,
            metadata={'model': settings.openai_model, 'response_id': response.id},
        )


async def run_wao(request: TaskRequest) -> ExecutionResult:
    return await WAOEngine().execute(request)
