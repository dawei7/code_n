import { apiPost } from './client';
import type { RunResponse, SupportedLanguage, TutorChatMessage } from '../types/api';

export type RunMode = 'practice' | 'real_test';

export interface RunArgs {
  challengeId: string;
  source: string;
  language: SupportedLanguage;
  mode: RunMode;
  caseIds?: string[];
  customInput?: Record<string, unknown> | null;
  customCases?: Array<{ id: string; name: string; input: Record<string, unknown> }>;
}

export function runChallenge(args: RunArgs): Promise<RunResponse> {
  return apiPost<RunResponse>(
    `/challenges/${encodeURIComponent(args.challengeId)}/run`,
    {
      source: args.source,
      language: args.language,
      mode: args.mode,
      case_ids: args.caseIds ?? [],
      custom_input: args.customInput ?? null,
      custom_cases: args.customCases ?? [],
    },
  );
}

export interface AnalyzeArgs {
  challengeId: string;
  source?: string;
  language?: SupportedLanguage;
  returned?: string;
  expected?: string;
  inputs?: Record<string, string>;
  optimalSource?: string;
  question?: string;
  messages?: TutorChatMessage[];
}

export interface AnalyzeResponse {
  analysis: string;
}

export function analyzeChallenge(args: AnalyzeArgs): Promise<AnalyzeResponse> {
  return apiPost<AnalyzeResponse>(
    `/challenges/${encodeURIComponent(args.challengeId)}/analyze`,
    {
      source: args.source ?? '',
      language: args.language ?? 'python',
      returned: args.returned ?? '',
      expected: args.expected ?? '',
      inputs: args.inputs ?? {},
      optimal_source: args.optimalSource ?? '',
      question: args.question,
      messages: args.messages ?? [],
    },
  );
}
