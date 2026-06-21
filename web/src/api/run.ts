import { apiPost } from './client';
import type { RunResponse } from '../types/api';

export type RunMode = 'practice' | 'real_test';

export interface RunArgs {
  challengeId: string;
  source: string;
  n: number;
  seed: number | null;
  mode: RunMode;
}

export function runChallenge(args: RunArgs): Promise<RunResponse> {
  return apiPost<RunResponse>(
    `/challenges/${encodeURIComponent(args.challengeId)}/run`,
    {
      source: args.source,
      // In real_test mode the server picks n + seed; we still send
      // the UI values (so the server's request validation accepts
      // the body) but the route handler ignores them.
      n: args.n,
      seed: args.seed,
      mode: args.mode,
    },
  );
}

export interface AnalyzeArgs {
  challengeId: string;
  source: string;
  n: number;
  seed: number | null;
  returned: string;
  expected: string;
  inputs: Record<string, string>;
}

export interface AnalyzeResponse {
  analysis: string;
}

export function analyzeChallenge(args: AnalyzeArgs): Promise<AnalyzeResponse> {
  return apiPost<AnalyzeResponse>(
    `/challenges/${encodeURIComponent(args.challengeId)}/analyze`,
    {
      source: args.source,
      n: args.n,
      seed: args.seed,
      returned: args.returned,
      expected: args.expected,
      inputs: args.inputs,
    },
  );
}
