# WAO-AI Architecture

## Runtime layers

```text
ChatGPT / API Client
        |
        v
   MCP / REST edge
        |
        v
  Trust Boundary
        |
        v
    CTCO Planner
        |
        v
  Execution Engine ----> OpenAI Responses API
        |
        v
 Verification + Synthesis
        |
        v
 Structured Result
```

## CTCO

**Context** captures user-provided state and references.

**Task** defines the desired outcome.

**Constraints** define limits such as format, budget, deadline and tool permissions.

**Output** defines how the result is represented.

The planner creates a minimal execution graph and verification criteria. The system should
avoid unnecessary decomposition: more planning is not automatically better planning.

## Tool trust model

Tools are classified as read-only or consequential. External content can never promote itself
to application policy. Consequential operations should use a separate approval boundary in
production deployments.

## Multimodal extension point

Image, audio and document tasks should be routed through typed adapters. The core agent should
not encode provider-specific image-generation tricks; provider adapters own modality-specific
parameters while the planner owns intent, constraints and verification.

## Scaling path

1. Add persistent sessions and idempotency keys.
2. Add a policy engine with per-tool scopes.
3. Add OpenTelemetry-compatible tracing.
4. Add evaluator datasets and regression scoring.
5. Add specialized handoff agents for research, coding, visual analysis and document work.
6. Add durable job execution for long-running tasks.
