import type { ChallengeSummary } from '../types/api';

export type EloDisplay = {
  value: number;
  estimated: boolean;
};

export type EloAverage = {
  value: number;
  problemCount: number;
  estimatedCount: number;
};

export type FrequencyAverage = {
  value: number;
  problemCount: number;
};

type MetricChallenge = Pick<
  ChallengeSummary,
  'id' | 'elo_rating' | 'estimated_elo_rating' | 'frequency'
>;

export function eloDisplayForChallenge(
  challenge: MetricChallenge,
): EloDisplay | null {
  if (challenge.elo_rating !== null) {
    return { value: challenge.elo_rating, estimated: false };
  }
  return challenge.estimated_elo_rating === null
    ? null
    : { value: challenge.estimated_elo_rating, estimated: true };
}

export function compareFrequencyPriority(
  left: MetricChallenge,
  right: MetricChallenge,
): number {
  if (left.frequency !== null && right.frequency !== null) {
    const byFrequency = right.frequency - left.frequency;
    if (byFrequency !== 0) return byFrequency;
  } else if (left.frequency !== null) {
    return -1;
  } else if (right.frequency !== null) {
    return 1;
  }

  const leftElo = eloDisplayForChallenge(left)?.value ?? Number.POSITIVE_INFINITY;
  const rightElo = eloDisplayForChallenge(right)?.value ?? Number.POSITIVE_INFINITY;
  return leftElo - rightElo;
}

export function calculateDirectEloAverage(
  challenges: MetricChallenge[],
): EloAverage | null {
  const uniqueChallenges = new Map<string, MetricChallenge>();
  for (const challenge of challenges) {
    uniqueChallenges.set(challenge.id, challenge);
  }

  let sum = 0;
  let problemCount = 0;
  let estimatedCount = 0;
  for (const challenge of uniqueChallenges.values()) {
    const display = eloDisplayForChallenge(challenge);
    if (display === null) continue;
    sum += display.value;
    problemCount += 1;
    if (display.estimated) estimatedCount += 1;
  }

  return problemCount === 0
    ? null
    : {
        value: sum / problemCount,
        problemCount,
        estimatedCount,
      };
}

export function calculateDirectFrequencyAverage(
  challenges: MetricChallenge[],
): FrequencyAverage | null {
  const uniqueChallenges = new Map<string, MetricChallenge>();
  for (const challenge of challenges) {
    uniqueChallenges.set(challenge.id, challenge);
  }

  let sum = 0;
  let problemCount = 0;
  for (const challenge of uniqueChallenges.values()) {
    if (challenge.frequency === null) continue;
    sum += challenge.frequency;
    problemCount += 1;
  }

  return problemCount === 0
    ? null
    : {
        value: sum / problemCount,
        problemCount,
      };
}
