import { apiGet, apiPut } from './client';
import type { ProgressOut } from '../types/api';

export function getProgress(): Promise<ProgressOut> {
  return apiGet<ProgressOut>('/progress');
}

export function markChallengeDone(
  challenge_id: string,
  ops: number,
  complexity: string,
): Promise<ProgressOut> {
  return apiPut<ProgressOut>('/progress', {
    mark: { challenge_id, ops, complexity },
  });
}

export function failChallenge(challenge_id: string): Promise<ProgressOut> {
  return apiPut<ProgressOut>('/progress', { fail: challenge_id });
}

export function resetProgress(): Promise<ProgressOut> {
  return apiPut<ProgressOut>('/progress', { reset: true });
}
