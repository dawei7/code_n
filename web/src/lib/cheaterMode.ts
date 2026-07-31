export const CHEATER_MODE_STORAGE_KEY = 'coden-cheater-mode';

export function canRevealSolution(completed: boolean, cheaterMode: boolean): boolean {
  return completed || cheaterMode;
}

export function canPreviewChallenge(locked: boolean, cheaterMode: boolean): boolean {
  return !locked || cheaterMode;
}
