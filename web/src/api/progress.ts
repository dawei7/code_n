import { apiGet, apiPut, apiPost } from './client';
import type { ProgressOut, VerifyLeetCodeResponse } from '../types/api';

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

export type ProgressResetScope = 'all' | 'coden' | 'leetcode';

export function resetProgress(
  scope: ProgressResetScope,
  challenge_ids: string[],
  confirmation: string,
): Promise<ProgressOut> {
  return apiPost<ProgressOut>('/progress/reset', {
    scope,
    challenge_ids,
    confirmation,
  });
}

export interface ProgressSettingsUpdate {
  career_mode?: boolean;
  leetcode_username?: string;
  player_name?: string;
  gemini_api_key?: string;
  active_set?: string;
  sidebar_width?: number;
  sidebar_position?: string;
  sidebar_collapsed?: boolean;
  pane_font_scales?: Record<string, number>;
  pane_sizes?: Record<string, number>;
  accent_colors?: { light: string; dark: string };
}

export function updateProgressSettings(update: ProgressSettingsUpdate): Promise<ProgressOut> {
  return apiPut<ProgressOut>('/progress', update);
}

export function verifyLeetCode(challenge_id: string): Promise<VerifyLeetCodeResponse> {
  return apiPost<VerifyLeetCodeResponse>('/progress/verify-leetcode', {
    challenge_id,
  });
}
