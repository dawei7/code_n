/**
 * Wire-format types mirroring the FastAPI Pydantic schemas in
 * `server/app/schemas.py`. The shapes are the same; we redeclare
 * them in TypeScript so the frontend has type-safety end to end.
 *
 * The per-step trace, the AI report, and the in-app debug surface
 * were all removed in the v0.9.0 pivot (the player edits + debugs
 * in VSCode). The remaining surface is the verdict + complexity
 * numbers + the ``solve()`` return value (rendered as a compact
 * string for the Result tab).
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

export interface ScalingPoint {
  n: number;
  user_ops: number;
  ref_ops: number;
  ci_low: number;
  ci_high: number;
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
  /** Short string representation of what ``solve()`` returned.
   *  Capped at ~500 chars server-side so a 10,000-element list
   *  doesn't blow up the response. The Result tab renders this
   *  as the "what my code produced" line. */
  return_value_repr: string;
  // ---- AST-derived op counts (the "scientific" metric) ----
  // Counted statically by walking the source's AST. This is
  // the SINGLE source of truth for "how many ops does your
  // code do?" — used by the Complexity tab, the verdict
  // (within_threshold), and the progress-best-ops recording.
  user_ast_ops: number | null;
  reference_ast_ops: number | null;
  /** ±5% tolerance band around the reference's AST op count. */
  reference_ci_low: number | null;
  reference_ci_high: number | null;
  scaling_data: ScalingPoint[];
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

export interface SolutionVersionsGet {
  challenge_id: string;
  active_version: number;
  versions: number[];
  version_names: Record<number, string>;
  modified_versions: number[];
  source: string;
}

export interface VersionSwitchRequest {
  version: number;
}
