export type FrequencyBand = {
  minimum: number;
  maximum: number;
  label: string;
  relevance: string;
};

// LeetCode Frequency is normalized to a 0-100 relative scale. Ten-point
// intervals keep every bucket equally wide and make adjacent bands comparable.
// The bands are deliberately ordered from highest to lowest to match the
// Frequency views' practice-priority order.
export const FREQUENCY_BANDS: readonly FrequencyBand[] = [
  {
    minimum: 90,
    maximum: 100,
    label: 'Highest Signal',
    relevance: 'The strongest historical relative-frequency signal; a high-priority practice band when the topic fits your goals.',
  },
  {
    minimum: 80,
    maximum: 90,
    label: 'Top Signal',
    relevance: 'Exceptionally prominent in the frozen LeetCode Frequency snapshot and generally worth prioritizing.',
  },
  {
    minimum: 70,
    maximum: 80,
    label: 'Very Strong Signal',
    relevance: 'A very strong historical prominence signal for focused interview preparation.',
  },
  {
    minimum: 60,
    maximum: 70,
    label: 'Strong Signal',
    relevance: 'A strong relative-frequency signal and a useful source of core practice problems.',
  },
  {
    minimum: 50,
    maximum: 60,
    label: 'Notable Signal',
    relevance: 'Above the middle of the Frequency scale and notably relevant for broad preparation.',
  },
  {
    minimum: 40,
    maximum: 50,
    label: 'Moderate Signal',
    relevance: 'A moderate historical signal; prioritize by topic coverage and individual learning value.',
  },
  {
    minimum: 30,
    maximum: 40,
    label: 'Developing Signal',
    relevance: 'A developing relative-frequency signal that is best selected for targeted topic practice.',
  },
  {
    minimum: 20,
    maximum: 30,
    label: 'Low Signal',
    relevance: 'A lower historical prominence signal; use selectively to fill topic or technique gaps.',
  },
  {
    minimum: 10,
    maximum: 20,
    label: 'Very Low Signal',
    relevance: 'A very low relative-frequency signal, usually secondary to higher bands for general preparation.',
  },
  {
    minimum: 0,
    maximum: 10,
    label: 'Minimal Signal',
    relevance: 'The lowest historical signal band; choose primarily for specific topics, not general priority.',
  },
];

export function formatFrequencyBand(
  band: Pick<FrequencyBand, 'minimum' | 'maximum'>,
): string {
  return band.maximum === 100
    ? `${band.minimum}–${band.maximum}`
    : `${band.minimum}–<${band.maximum}`;
}

export function frequencyBandForValue(frequency: number): FrequencyBand | null {
  return FREQUENCY_BANDS.find((band) => (
    frequency >= band.minimum
    && (band.maximum === 100 ? frequency <= band.maximum : frequency < band.maximum)
  )) ?? null;
}
