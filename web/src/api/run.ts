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
