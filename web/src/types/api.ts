/**
 * Wire-format types mirroring the FastAPI Pydantic schemas in
 * `server/app/schemas.py`. The shapes are the same; we redeclare
 * them in TypeScript so the frontend has type-safety end to end.
 */

export interface ParamDoc {
  name: string;
  doc: string;
  type_hint: string;
}

export interface Sample {
  input_repr: string;
  output_repr: string;
}

export interface ChallengeSummary {
  id: string;
  name: string;
  category: string;
  difficulty: number;
  required_complexity: string;
  description: string;
  hint: string;
  source_url: string;
  parents: string[];
  children: string[];
  max_n: number;
}

export interface ChallengeDetail extends ChallengeSummary {
  params: ParamDoc[];
  samples: Sample[];
  starter_source: string;
  optimal_source: string;
  /** Per-algorithm analysis notes for the scientific panel.
   *  Keys are labels (best/average/worst/space/stable/in_place);
   *  values are short human-readable strings. Empty for algorithms
   *  that haven't been annotated yet. */
  complexity_notes: Record<string, string>;
}

export interface TraceFrameOut {
  /** The frame's own position in the trace's frame list.
   *  The frontend's step-player slider drives the slider
   *  off this index directly (``trace[opIndex]``). */
  frame_index: number;
  line_no: number;
  event: 'call' | 'line' | 'return' | string;
  locals: Record<string, unknown>;
  return_value: string;
  breakpoint: boolean;
  source_file: string;
  source_line: string;
}

export interface AiReport {
  challenge_id: string;
  challenge_name: string;
  category: string;
  description: string;
  required_complexity: string;
  test: { n: number; seed: number | null };
  user_source: string;
  result: {
    passed: boolean;
    correct: boolean;
    within_threshold: boolean;
    actual_complexity: string;
    message: string;
    /** AST-derived op count (the sole "how many ops" metric
     *  since v0.8.5). Used by the AI report's hint prompt. */
    ops_total: number;
    too_efficient: boolean;
    too_efficient_reason: string;
  };
  locals_at_failure: {
    line_no: number;
    event: string;
    locals: Record<string, unknown>;
    return_value: string;
  } | null;
  algorithm_hint: string;
  // AST-derived op counts and tolerance band. Used by the
  // LLM to reason about how close the user is to optimal.
  user_ast_ops: number | null;
  reference_ast_ops: number | null;
  reference_ci_low: number | null;
  reference_ci_high: number | null;
}

export interface RunResponse {
  passed: boolean;
  correct: boolean;
  within_threshold: boolean;
  actual_complexity: string;
  required_complexity: string;
  n: number;
  /** The actual seed used (echoed from the request, or the
   *  server-picked value in real_test mode). */
  seed: number | null;
  /** What mode produced this run. Echoes the request so the UI
   *  can label the n/seed as "real test" without re-deriving it. */
  mode: 'practice' | 'real_test';
  /** True if the run was flagged as too efficient (AST scan or
   *  op-count ratio). In that case `passed` is also False. */
  too_efficient: boolean;
  too_efficient_reason: string;
  message: string;
  trace: TraceFrameOut[];
  return_value_repr: string;
  truncated: boolean;
  // ---- AST-derived op counts (the "scientific" metric) ----
  // Counted statically by walking the source's AST. This is
  // the SINGLE source of truth for "how many ops does your
  // code do?" — used by the Complexity tab, the verdict
  // (within_threshold), the AI report, and the
  // progress-best-ops recording.
  user_ast_ops: number | null;
  reference_ast_ops: number | null;
  /** ±5% tolerance band around the reference's AST op count. */
  reference_ci_low: number | null;
  reference_ci_high: number | null;
  /** Structured AI report — always populated. The AI Report
   *  tab renders it; the local Ollama hint endpoint takes it
   *  as input. The optimal source is NEVER in this report
   *  (it's added server-side only when the LLM prompt is
   *  built, so it can't leak through the UI). */
  ai_report: AiReport;
}

export interface LevelRecordOut {
  challenge_id: string;
  best_ops: number;
  complexity_achieved: string;
  attempts: number;
}

export interface ProgressOut {
  player_name: string;
  completed: string[];
  last_status: Record<string, string>;
  records: Record<string, LevelRecordOut>;
}

export interface SolutionGet {
  challenge_id: string;
  source: string;
  exists: boolean;
}
