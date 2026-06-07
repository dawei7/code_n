import { apiGet, apiPut } from './client';
import type { SolutionGet } from '../types/api';

export function getSolution(challengeId: string): Promise<SolutionGet> {
  return apiGet<SolutionGet>(`/solutions/${encodeURIComponent(challengeId)}`);
}

export function putSolution(challengeId: string, source: string): Promise<SolutionGet> {
  return apiPut<SolutionGet>(`/solutions/${encodeURIComponent(challengeId)}`, { source });
}
