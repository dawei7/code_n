"""``POST /api/challenges/{id}/run`` — execute a player's solution.

This is the load-bearing endpoint. The body is a :class:`RunRequest`;
the response is a :class:`RunResponse` (or a 4xx with a structured
error). The actual execution is delegated to
:mod:`server.app.engine_runner` so this module stays focused on
HTTP-level concerns: input validation, error→status mapping, and
forwarding the result.
"""
from __future__ import annotations

import requests
from fastapi import APIRouter, BackgroundTasks, HTTPException

from challenges.registry import CHALLENGE_REGISTRY
from engine.special_environments import category_is_runnable

from server.app.engine_runner import (
    ChallengeNotFound,
    NTooLarge,
    NoSolveFunction,
    PlayerSyntaxError,
    UnsupportedLanguageExecution,
    run_player_code,
)
from server.app.schemas import AnalyzeRequest, AnalyzeResponse, RunRequest, RunResponse
from server.app.validated_cases import InvalidCustomCase, NoValidatedCases, select_cases_for_run


router = APIRouter()


def _prepare_run_response(result: RunResponse) -> RunResponse:
    """Attach verdict metadata and remove every hidden-case detail."""

    hidden_failures = False
    visible_official_failure = False
    hidden_index = 0
    for case_result in result.case_results:
        case_result.hidden = case_result.kind in {"real", "benchmark"}
        case_result.counts_toward_verdict = not (
            result.mode == "real_test" and case_result.kind == "custom"
        )
        if case_result.hidden:
            hidden_index += 1
            hidden_failures = hidden_failures or not case_result.correct
            case_result.name = f"Hidden case {hidden_index}"
            case_result.message = ""
            case_result.input_repr = ""
            case_result.return_value_repr = ""
            case_result.expected_repr = None
            case_result.runtime_user_ms = None
        elif case_result.counts_toward_verdict and not case_result.correct:
            visible_official_failure = True

    if result.mode == "real_test":
        # Top-level evidence historically mirrored the first failing case. It
        # must never become a side channel for a hidden judge input or output.
        public_headline = next(
            (
                case_result
                for case_result in result.case_results
                if case_result.counts_toward_verdict
                and not case_result.hidden
                and not case_result.correct
            ),
            next(
                (
                    case_result
                    for case_result in result.case_results
                    if case_result.counts_toward_verdict and not case_result.hidden
                ),
                None,
            ),
        )
        result.return_value_repr = public_headline.return_value_repr if public_headline else ""
        result.reference_return_value_repr = public_headline.expected_repr if public_headline else None
        result.setup_data_repr = None
        if hidden_failures and not visible_official_failure:
            result.message = "One or more hidden cases failed."
    return result


def _format_analysis_inputs(inputs: dict[str, str]) -> str:
    lines: list[str] = []
    for name, value in inputs.items():
        if "\n" in value:
            lines.extend([f"- {name}:", "```text", value.rstrip("\n"), "```"])
        else:
            lines.append(f"- {name}: {value}")
    return "\n".join(lines) + ("\n" if lines else "")


def _format_tutor_conversation(messages: list[object]) -> str:
    lines: list[str] = []
    for message in messages[-12:]:
        role = getattr(message, "role", "")
        content = str(getattr(message, "content", "") or "").strip()
        if not content:
            continue
        label = "Student" if role == "user" else "Tutor"
        lines.append(f"{label}:\n{content[:4000]}")
    return "\n\n".join(lines)


def _trim_prompt_block(value: str, limit: int = 12000) -> str:
    text = value.strip()
    if len(text) <= limit:
        return text
    return text[:limit] + "\n... [truncated]"


def _build_tutor_prompt(
    *,
    challenge_id: str,
    description: str,
    required_complexity: str,
    hint: str,
    language: str,
    source: str,
    optimal_source: str,
    returned: str,
    expected: str,
    inputs_text: str,
    inputs_label: str,
    returned_label: str,
    expected_label: str,
    conversation_text: str,
    question: str,
) -> str:
    raw_inputs_text = inputs_text.strip()
    has_execution_context = bool(returned.strip() or expected.strip() or raw_inputs_text)
    source_text = _trim_prompt_block(source) or "(No user solution has been provided yet.)"
    optimal_text = _trim_prompt_block(optimal_source) or "(No reference source was provided to the tutor.)"
    inputs_text = raw_inputs_text or "(No concrete run input has been captured yet.)"
    returned_text = returned.strip() or "(No user output has been captured yet.)"
    expected_text = expected.strip() or "(No reference output has been captured yet.)"
    hint_text = hint.strip() or "(No official hint is available.)"

    if question:
        chat_instructions = f"""The student is asking a question in the same AI tutor chat.

Prior Conversation:
{conversation_text or "(No prior tutor conversation was provided.)"}

Latest Student Question:
{question}

Answer the latest question directly, as a friendly algorithm tutor in a real chat.
Build on the prior conversation instead of restarting the whole analysis. Use the
challenge statement, current user code, latest execution context, and reference
solution context when relevant. Ask at most one clarifying question only if the
student's question cannot be answered from the available context.
"""
    else:
        chat_instructions = """The student requested an initial tutor response.

If a failed or suspicious execution context is present, explain:
1. What the current code appears to be trying.
2. The most likely correctness or complexity issue, tied to the exact logic.
3. The next small change or test the student should try.

If no execution context is present yet, help the student understand the task,
identify the key invariant/algorithm idea, and ask one focused question that
would help choose the next step.
"""

    execution_intro = "Latest Execution Context" if has_execution_context else "Execution Context"

    return f"""You are cOde(n)'s AI tutor: a patient, rigorous algorithm coach inside a coding practice app.

Teaching style:
- Treat this as an ongoing chat, not a one-shot report.
- Stay tightly grounded in the current challenge, the user's code, the latest run, and the reference solution context.
- Prefer Socratic guidance and concise explanations. Do not dump a full final solution unless the student explicitly asks for it.
- If the user has no code yet, help them understand the task and form a plan.
- If the user's code exists, point to the exact idea or line pattern causing trouble.
- If complexity or performance comes up, explain the theoretical cost and relate it to the calibrated runtime check against the optimal reference.
- Be honest about uncertainty and ask at most one focused clarifying question when needed.

Challenge:
- ID: {challenge_id}
- Required complexity: {required_complexity}

Challenge Description:
{description}

Official Hint:
{hint_text}

{inputs_label}:
{inputs_text}

Current User Code:
```{language}
{source_text}
```

Reference / Optimal Solution Context:
Use this privately to understand the intended approach and to compare ideas.
Do not paste it in full unless the student explicitly asks for a complete solution.
```{language}
{optimal_text}
```

{execution_intro}:
- {returned_label}: {returned_text}
- {expected_label}: {expected_text}

{chat_instructions}
"""


@router.post("/challenges/{challenge_id}/run")
def run_challenge(challenge_id: str, body: RunRequest, background_tasks: BackgroundTasks) -> RunResponse:
    """Run the player's source against the named challenge.

    The HTTP judge uses authored validated cases. Practice mode runs selected
    visible cases. ``real_test`` is the full submission run: visible system
    cases, custom diagnostic cases, hidden judge cases, and benchmark cases.
    Benchmark details remain hidden; custom failures do not reject the
    submission, and runtime gating uses the authored benchmark workloads.

    Missing case data is reported as a configuration error.
    """
    from server.app import progress_store
    from server.app.challenge_sets import normalize_algorithm_set
    if challenge_id not in CHALLENGE_REGISTRY:
        raise HTTPException(status_code=404, detail=f"Unknown challenge id: {challenge_id}")

    challenge_cls = CHALLENGE_REGISTRY[challenge_id]
    spec = getattr(challenge_cls(), "_spec", None)
    reference_metadata = getattr(spec, "reference_metadata", {}) or {}
    if not category_is_runnable(reference_metadata):
        category_title = str(reference_metadata.get("category_title") or "This LeetCode category")
        raise HTTPException(
            status_code=422,
            detail={
                "error": "challenge_not_runnable",
                "message": (
                    f"{category_title} problems are tracked for LeetCode subsets and tags, "
                    "but this cOde(n) runtime does not execute that category yet."
                ),
            },
        )
    supported_languages = {
        str(language)
        for language in reference_metadata.get("supported_languages", [])
        if isinstance(language, str)
    }
    if supported_languages and body.language not in supported_languages:
        raise HTTPException(
            status_code=422,
            detail={
                "error": "language_not_supported_for_challenge",
                "message": (
                    f"{body.language} is not a supported language for this challenge. "
                    f"Supported languages: {', '.join(sorted(supported_languages))}."
                ),
            },
        )

    progress = progress_store.load()
    active_set = normalize_algorithm_set(progress.active_set)
    if active_set == "neetcode":
        from server.app.routes.challenges import get_unlocked_challenges
        all_challenges = [cls() for cls in CHALLENGE_REGISTRY.values()]
        unlocked_set = get_unlocked_challenges(progress, all_challenges)
        if challenge_id not in unlocked_set:
            raise HTTPException(status_code=403, detail="Challenge is locked in Career Mode.")

    try:
        run_cases, benchmark_cases = select_cases_for_run(
            challenge_id,
            mode=body.mode,
            selected_case_ids=body.case_ids,
            custom_input=body.custom_input,
            custom_cases=[case.model_dump() for case in body.custom_cases],
        )
    except InvalidCustomCase as exc:
        raise HTTPException(status_code=422, detail={"error": "invalid_custom_case", "message": str(exc)})
    except NoValidatedCases as exc:
        raise HTTPException(status_code=422, detail={"error": "no_validated_cases", "message": str(exc)})
    try:
        result = run_player_code(
            challenge_id=challenge_id,
            source=body.source,
            mode=body.mode,
            language=body.language,
            run_cases=run_cases,
            benchmark_cases=benchmark_cases,
        )
        return _prepare_run_response(result)
    except ChallengeNotFound as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except NTooLarge as exc:
        raise HTTPException(
            status_code=422,
            detail={"error": "n_too_large", "requested": exc.requested, "maximum": exc.maximum},
        )
    except PlayerSyntaxError as exc:
        raise HTTPException(
            status_code=422,
            detail={"error": "syntax", "message": str(exc)},
        )
    except NoSolveFunction as exc:
        raise HTTPException(status_code=400, detail={"error": "no_solve", "message": str(exc)})
    except UnsupportedLanguageExecution as exc:
        raise HTTPException(
            status_code=501,
            detail={"error": "language_execution_not_ready", "message": str(exc)},
        )


@router.post("/challenges/{challenge_id}/analyze")
def analyze_error(challenge_id: str, body: AnalyzeRequest) -> AnalyzeResponse:
    from server.app import progress_store
    progress = progress_store.load()
    api_key = progress.gemini_api_key.strip()
    if not api_key:
        raise HTTPException(
            status_code=400,
            detail="Please configure your Gemini API Key in the Profile settings first."
        )

    # Resolve challenge description
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise HTTPException(status_code=404, detail=f"Challenge '{challenge_id}' not found.")
    challenge = challenge_cls()
    description = challenge.info.description

    inputs_label = "Input Variables"
    returned_label = "What User's Code Returned"
    expected_label = "What was Expected (Correct Return Value)"
    inputs_text = _format_analysis_inputs(body.inputs)

    conversation_text = _format_tutor_conversation(body.messages)
    prompt = _build_tutor_prompt(
        challenge_id=challenge_id,
        description=description,
        required_complexity=str(challenge.info.required_complexity),
        hint=challenge.info.hint,
        language=body.language,
        source=body.source,
        optimal_source=body.optimal_source,
        returned=body.returned,
        expected=body.expected,
        inputs_text=inputs_text,
        inputs_label=inputs_label,
        returned_label=returned_label,
        expected_label=expected_label,
        conversation_text=conversation_text,
        question=(body.question or "").strip(),
    )

    headers = {
        "Content-Type": "application/json"
    }

    models_to_try = [
        "gemma-4-31b-it",
        "gemma-4-26b-a4b-it",
        "gemini-3.5-flash",
        "gemini-2.5-flash"
    ]

    last_error_msg = ""
    last_status_code = 500

    for model in models_to_try:
        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.1
            }
        }

        try:
            try:
                import urllib3.util.connection as connection
                connection.HAS_IPV6 = False
            except Exception:
                pass
            
            response = requests.post(
                api_url,
                headers=headers,
                json=payload,
                timeout=60,
                proxies={"http": None, "https": None}
            )
            if response.status_code == 200:
                data = response.json()
                try:
                    parts = data["candidates"][0]["content"]["parts"]
                    # Filter out thinking steps (i.e. where thought is True) to get only the final answer
                    analysis_text = "".join(part["text"] for part in parts if not part.get("thought"))
                    if not analysis_text.strip():
                        # Fallback to concatenate all parts if somehow empty
                        analysis_text = "".join(part["text"] for part in parts)
                except Exception as exc:
                    analysis_text = data["candidates"][0]["content"]["parts"][0]["text"]

                return AnalyzeResponse(analysis=analysis_text)
            else:
                try:
                    error_msg = response.json().get("error", {}).get("message", response.text)
                except Exception:
                    error_msg = response.text
                last_error_msg = f"Model '{model}' failed ({response.status_code}): {error_msg}"
                last_status_code = response.status_code
        except Exception as e:
            last_error_msg = f"Model '{model}' connection failed: {e}"
            last_status_code = 500

    raise HTTPException(
        status_code=last_status_code,
        detail=f"Gemini API returned an error: {last_error_msg}"
    )
