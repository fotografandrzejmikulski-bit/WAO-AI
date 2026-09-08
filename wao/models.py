from typing import Any, Literal
from pydantic import BaseModel, Field


class TaskRequest(BaseModel):
    task: str = Field(min_length=1, max_length=100_000)
    context: dict[str, Any] = Field(default_factory=dict)
    constraints: list[str] = Field(default_factory=list)
    output_format: Literal['auto', 'text', 'json', 'markdown'] = 'auto'
    allow_tools: bool = True


class TaskPlan(BaseModel):
    objective: str
    normalized_context: dict[str, Any]
    constraints: list[str]
    subtasks: list[str]
    verification_criteria: list[str]
    tool_policy: Literal['none', 'read_only', 'normal'] = 'normal'


class ExecutionResult(BaseModel):
    request_id: str
    status: Literal['completed', 'failed', 'blocked']
    response: str
    plan: TaskPlan
    evidence: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
