import { apiGet, apiPut, apiPost } from './client';
import type { SolutionGet, SolutionVersionsGet, VersionSwitchRequest } from '../types/api';

export function getSolution(challengeId: string): Promise<SolutionVersionsGet> {
  return apiGet<SolutionVersionsGet>(`/solutions/${encodeURIComponent(challengeId)}`);
}

export function putSolution(challengeId: string, source: string): Promise<SolutionGet> {
  return apiPut<SolutionGet>(`/solutions/${encodeURIComponent(challengeId)}`, { source });
}

export function switchVersion(challengeId: string, version: number): Promise<SolutionVersionsGet> {
  return apiPost<SolutionVersionsGet>(`/solutions/${encodeURIComponent(challengeId)}/versions/switch`, { version } satisfies VersionSwitchRequest);
}

export function renameVersion(challengeId: string, version: number, name: string): Promise<SolutionVersionsGet> {
  return apiPut<SolutionVersionsGet>(`/solutions/${encodeURIComponent(challengeId)}/versions/${version}/rename`, { name });
}


export function resetVersion(challengeId: string, version: number): Promise<SolutionVersionsGet> {
  return apiPost<SolutionVersionsGet>(`/solutions/${encodeURIComponent(challengeId)}/versions/${version}/reset`, {});
}
