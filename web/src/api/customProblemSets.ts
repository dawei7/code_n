import { apiGet, apiPut } from './client';
import type { CustomProblemSet, CustomProblemSetsOut } from '../types/api';


export function getCustomProblemSets(): Promise<CustomProblemSetsOut> {
  return apiGet<CustomProblemSetsOut>('/custom-problem-sets');
}

export function replaceCustomProblemSets(
  sets: CustomProblemSet[],
): Promise<CustomProblemSetsOut> {
  return apiPut<CustomProblemSetsOut>('/custom-problem-sets', { sets });
}
