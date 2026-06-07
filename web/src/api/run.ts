import { apiPost } from './client';
import type { RunResponse } from '../types/api';

export interface RunArgs {
  challengeId: string;
  source: string;
  n: number;
  seed: number | null;
}

export function runChallenge(args: RunArgs): Promise<RunResponse> {
  return apiPost<RunResponse>(
    `/challenges/${encodeURIComponent(args.challengeId)}/run`,
    { source: args.source, n: args.n, seed: args.seed },
  );
}
