import { apiGet } from './client';
import type { ChallengeDetail, ChallengeSummary } from '../types/api';

export function listChallenges(): Promise<ChallengeSummary[]> {
  return apiGet<ChallengeSummary[]>('/challenges');
}

export function getChallenge(id: string): Promise<ChallengeDetail> {
  return apiGet<ChallengeDetail>(`/challenges/${encodeURIComponent(id)}`);
}
