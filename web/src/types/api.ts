/**
 * Wire-format types mirroring the FastAPI Pydantic schemas in
 * `server/app/schemas.py`. The shapes are the same; we redeclare
 * them in TypeScript so the frontend has type-safety end to end.
 *
 * The remaining run surface is the verdict + complexity numbers
 * + the ``solve()`` return value. Debug state is streamed through
 * the debugger WebSocket, not this REST payload.
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

export interface TestCaseSummary {
  id: string;
  name: string;
  kind: string;
  visible: boolean;
  input_repr: string;
  expected_repr: string;
  tags: string[];
}

export type SupportedLanguage = 'python' | 'cpp' | 'java' | 'csharp' | 'javascript' | 'go' | 'kotlin' | 'sql' | 'bash';

export interface TutorChatMessage {
  role: 'user' | 'assistant';
  content: string;
}

export interface DebugCapability {
  language: SupportedLanguage;
  label: string;
  adapter_id: string;
  adapter_command: string | null;
  available: boolean;
  launch_supported: boolean;
  missing: string[];
  message: string;
  install_hint: string;
}

export interface DebugCapabilitiesResponse {
  languages: Record<SupportedLanguage, DebugCapability>;
}

export interface ChallengeSummary {
  id: string;
  name: string;
  category: string;
  categories: string[];
  difficulty_label: string;
  elo_rating: number | null;
  estimated_elo_rating: number | null;
  frequency: number | null;
  difficulty_estimate: number | null;
  acceptance_rate: number | null;
  required_complexity: string;
  description: string;
  hint: string;
  source_url: string;
  parents: string[];
  children: string[];
  max_n: number;
  unlocked: boolean;
  leetcode_title: string;
  leetcode_slug: string;
  leetcode_url: string;
  leetcode_category: string;
  leetcode_category_title: string;
  leetcode_frontend_id: string;
  leetcode_topics: Array<Record<string, unknown>>;
  leetcode_subsets: string[];
  leetcode_tags: string[];
  leetcode_company_tags: Array<Record<string, unknown>>;
  leetcode_study_plans: Array<Record<string, unknown>>;
  leetcode_external_subsets: Array<Record<string, unknown>>;
  supported_languages: string[];
  primary_language: SupportedLanguage;
  runnable_in_coden: boolean;
  has_guided_example: boolean;
  leetcode_submission_status: 'missing' | 'candidate' | 'verified';
  leetcode_submission_language: string;
  leetcode_submission_paid_only: boolean;
}

export interface ChallengeDetail extends ChallengeSummary {
  params: ParamDoc[];
  samples: Sample[];
  test_cases: TestCaseSummary[];
  starter_source: string;
  starter_sources: Record<SupportedLanguage, string>;
  optimal_source: string;
  optimal_sources?: Partial<Record<SupportedLanguage, string>>;
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

export interface RuntimeScalingPoint {
  size: number;
  user_ms: number;
  reference_ms: number;
  ratio: number;
}

export interface RunResponse {
  passed: boolean;
  correct: boolean;
  within_threshold: boolean;
  actual_complexity: string;
  required_complexity: string;
  /** Practice uses selected visible cases; real_test runs the full submission suite. */
  mode: 'practice' | 'real_test';
  /** Legacy flag. Correctness plus explicit complexity verification is the verdict gate. */
  too_efficient: boolean;
  too_efficient_reason: string;
  message: string;
  /** Short string representation of what ``solve()`` returned.
   *  Capped at ~500 chars server-side so a 10,000-element list
   *  doesn't blow up the response. The Result tab renders this
   *  as the "what my code produced" line. */
  return_value_repr: string;
  reference_return_value_repr?: string | null;
  setup_data_repr?: Record<string, string> | null;
  // ---- Legacy static-op fields ----
  // Kept nullable for older persisted UI state. New verdicts use
  // correctness plus the calibrated runtime check.

  user_ast_ops: number | null;
  reference_ast_ops: number | null;
  /** Dataset-aware lower/upper comparison bounds around the reference static op count. */
  reference_ci_low: number | null;
  reference_ci_high: number | null;
  reference_coefficient?: number | null;
  scaling_data: ScalingPoint[];
  runtime_scaling_data?: RuntimeScalingPoint[];
  runtime_check: boolean;
  runtime_passed?: boolean | null;
  runtime_user_ms?: number | null;
  runtime_reference_ms?: number | null;
  runtime_ratio?: number | null;
  runtime_limit_ms?: number | null;
  runtime_trials: number;
  runtime_message: string;
  benchmark_correct: boolean;
  /** Non-scaling complexity verification for bounded or proof-optimal contracts. */
  complexity_check: boolean;
  complexity_passed?: boolean | null;
  complexity_method: string;
  complexity_message: string;
  case_results: RunCaseResult[];
  selected_case_ids: string[];
}

export interface RunCaseResult {
  id: string;
  name: string;
  kind: string;
  correct: boolean;
  passed: boolean;
  message: string;
  input_repr: string;
  return_value_repr: string;
  expected_repr?: string | null;
  runtime_user_ms?: number | null;
  /** Hidden judge cases never expose inputs, outputs, expected values, or error details. */
  hidden: boolean;
  /** Custom cases are diagnostic during a real run and do not affect acceptance. */
  counts_toward_verdict: boolean;
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
  career_mode: boolean;
  leetcode_username: string;
  leetcode_solved: string[];
  leetcode_submissions: Record<string, {
    submission_id: string;
    accepted_at: string;
    language: string;
    status: string;
  }>;
  unlocked_leetcode: string[];
  milestones: string[];
  gemini_api_key: string;
  active_set: string;
  active_custom_set_id: string;
  sidebar_width: number;
  sidebar_position: 'left' | 'right';
  sidebar_collapsed: boolean;
  pane_font_scales: Record<string, number>;
  pane_sizes: Record<string, number>;
  accent_colors: { light: string; dark: string };
}

export interface CustomProblemNode {
  type: 'problem';
  id: string;
  challenge_id: string;
}

export interface CustomProblemGroup {
  type: 'group';
  id: string;
  name: string;
  children: CustomProblemTreeNode[];
}

export type CustomProblemTreeNode = CustomProblemNode | CustomProblemGroup;

export interface CustomProblemSet {
  id: string;
  name: string;
  description: string;
  career_mode: boolean;
  nodes: CustomProblemTreeNode[];
}

export interface CustomProblemSetsOut {
  version: number;
  sets: CustomProblemSet[];
}

export interface SolutionGet {
  challenge_id: string;
  language: SupportedLanguage;
  source: string;
  exists: boolean;
}

export interface SolutionVersionsGet {
  challenge_id: string;
  language: SupportedLanguage;
  active_version: number;
  versions: number[];
  version_names: Record<number, string>;
  modified_versions: number[];
  source: string;
  starter_source: string;
  filename: string;
}

export interface VersionSwitchRequest {
  version: number;
}

export interface VerifyLeetCodeResponse {
  success: boolean;
  message: string;
  unlocked_leetcode: string[];
  milestones: string[];
}

export interface ProfileSummary {
  name: string;
  career_mode: boolean;
  leetcode_username: string;
  completed_count: number;
  verified_leetcode_count: number;
}

export interface ProfilesResponse {
  active_profile: string;
  profiles: ProfileSummary[];
}
