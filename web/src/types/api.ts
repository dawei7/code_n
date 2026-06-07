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

export interface OpRecordOut {
  op_type: 'compare' | 'swap' | 'read' | 'write' | 'call' | string;
  detail: string;
}

export interface TraceFrameOut {
  op_index: number;
  line_no: number;
  event: 'call' | 'line' | 'return' | string;
  locals: Record<string, unknown>;
  return_value: string;
  breakpoint: boolean;
  source_file: string;
  source_line: string;
}

export interface StatsOut {
  comparisons: number;
  swaps: number;
  reads: number;
  writes: number;
  calls: number;
  total: number;
}

export interface RunResponse {
  passed: boolean;
  correct: boolean;
  within_threshold: boolean;
  algorithm_match: boolean;
  algorithm_reason: string;
  actual_complexity: string;
  required_complexity: string;
  n: number;
  message: string;
  stats: StatsOut;
  ops_log: OpRecordOut[];
  trace: TraceFrameOut[];
  return_value_repr: string;
  truncated: boolean;
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
