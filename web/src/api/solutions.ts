import { apiGet, apiPut, apiPost } from './client';
import type { SolutionGet, SolutionVersionsGet, SupportedLanguage, VersionSwitchRequest } from '../types/api';

function languageQuery(language: SupportedLanguage): string {
  return `?language=${encodeURIComponent(language)}`;
}

export function getSolution(challengeId: string, language: SupportedLanguage): Promise<SolutionVersionsGet> {
  return apiGet<SolutionVersionsGet>(`/solutions/${encodeURIComponent(challengeId)}${languageQuery(language)}`);
}

export function putSolution(challengeId: string, source: string, language: SupportedLanguage): Promise<SolutionGet> {
  return apiPut<SolutionGet>(`/solutions/${encodeURIComponent(challengeId)}${languageQuery(language)}`, { source });
}

export function switchVersion(challengeId: string, version: number, language: SupportedLanguage): Promise<SolutionVersionsGet> {
  return apiPost<SolutionVersionsGet>(`/solutions/${encodeURIComponent(challengeId)}/versions/switch${languageQuery(language)}`, { version } satisfies VersionSwitchRequest);
}

export function renameVersion(challengeId: string, version: number, name: string, language: SupportedLanguage): Promise<SolutionVersionsGet> {
  return apiPut<SolutionVersionsGet>(`/solutions/${encodeURIComponent(challengeId)}/versions/${version}/rename${languageQuery(language)}`, { name });
}


export function resetVersion(challengeId: string, version: number, language: SupportedLanguage): Promise<SolutionVersionsGet> {
  return apiPost<SolutionVersionsGet>(`/solutions/${encodeURIComponent(challengeId)}/versions/${version}/reset${languageQuery(language)}`, {});
}
