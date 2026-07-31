export type EloBand = {
  minimum: number | null;
  maximum: number | null;
  label: string;
  trainingDemand: string;
  interviewParallel: string;
  performanceTarget: string;
};

export const ELO_BANDS: readonly EloBand[] = [
  {
    minimum: null,
    maximum: 1200,
    label: 'Foundation',
    trainingDemand: 'Direct observations, loops, counting, basic simulation, and precise reading.',
    interviewParallel: 'Warm-up and basic programming fluency before internship preparation.',
    performanceTarget: 'Solve independently in 15–20 min; explain the bound and test every stated edge.',
  },
  {
    minimum: 1200,
    maximum: 1300,
    label: 'Core foundation',
    trainingDemand: 'Arrays, strings, hash maps/sets, sorting, and direct greedy choices.',
    interviewParallel: 'Internship fundamentals and early online-assessment questions.',
    performanceTarget: 'Solve at least 8/10 unseen problems in ≤25 min with clean complexity analysis.',
  },
  {
    minimum: 1300,
    maximum: 1400,
    label: 'Structured foundation',
    trainingDemand: 'Two pointers, prefix sums, binary search basics, and elementary BFS/DFS.',
    interviewParallel: 'Intern or graduate coding-screen core.',
    performanceTarget: 'Recognize the pattern without hints and produce independent edge-case tests in ≤30 min.',
  },
  {
    minimum: 1400,
    maximum: 1500,
    label: 'Interview core I',
    trainingDemand: 'Standard medium patterns, stacks, intervals, trees, and careful state tracking.',
    interviewParallel: 'Entry-level Software Engineer coding-screen core.',
    performanceTarget: 'Reach a correct optimal solution in ≤30 min and narrate the invariant while coding.',
  },
  {
    minimum: 1500,
    maximum: 1600,
    label: 'Interview core II',
    trainingDemand: 'Multi-step mediums, heaps, graph traversal, binary-search-on-answer, and basic DP.',
    interviewParallel: 'Strong entry-level target; general Software Engineer interview baseline.',
    performanceTarget: 'Solve 8/10 unseen, mixed-topic problems in ≤35 min with executable, tested code.',
  },
  {
    minimum: 1600,
    maximum: 1700,
    label: 'Applied reasoning',
    trainingDemand: 'Less explicit reductions, greedy justification, DP state design, and data-structure choice.',
    interviewParallel: 'General SWE and mid-level coding-round core.',
    performanceTarget: 'State the model and complexity before coding; finish a robust solution in ≤35 min.',
  },
  {
    minimum: 1700,
    maximum: 1800,
    label: 'Advanced interview',
    trainingDemand: 'Advanced mediums, graph/DP combinations, stronger invariants, and implementation discipline.',
    interviewParallel: 'Strong mid-level coding performance and selective company screens.',
    performanceTarget: 'Solve 8/10 unseen problems in ≤40 min and defend alternatives and trade-offs.',
  },
  {
    minimum: 1800,
    maximum: 1900,
    label: 'High interview',
    trainingDemand: 'Introductory hard problems, non-obvious transformations, and proof-driven greedy or DP.',
    interviewParallel: 'Advanced mid-level or Senior coding-round preparation.',
    performanceTarget: 'Solve most unseen problems in one 45-min interview slot without editorial assistance.',
  },
  {
    minimum: 1900,
    maximum: 2000,
    label: 'Advanced algorithmic',
    trainingDemand: 'Harder DP, graph reasoning, range structures, and correctness arguments with many cases.',
    interviewParallel: 'Stretch target for algorithm-heavy Senior interviews.',
    performanceTarget: 'Produce a correct approach quickly enough to leave time for code review and testing.',
  },
  {
    minimum: 2000,
    maximum: 2100,
    label: 'Specialist threshold',
    trainingDemand: 'Complex state spaces, advanced data structures, and deeper mathematical reductions.',
    interviewParallel: 'Very selective or algorithm-specialist interview stretch.',
    performanceTarget: 'Prioritize derivation quality over speed; independently validate the proof and complexity.',
  },
  {
    minimum: 2100,
    maximum: 2200,
    label: 'Algorithm specialist',
    trainingDemand: 'Advanced hard problems, uncommon combinations, and high implementation risk.',
    interviewParallel: 'Specialist, competitive-programming-adjacent, or unusually algorithmic roles.',
    performanceTarget: 'Solve consistently across topics; one memorized technique is not evidence of mastery.',
  },
  {
    minimum: 2200,
    maximum: 2400,
    label: 'Very hard',
    trainingDemand: 'Non-obvious algorithms, sophisticated proofs, and contest-hard implementation.',
    interviewParallel: 'Beyond the normal generalist SWE return on practice time.',
    performanceTarget: 'Treat as advanced depth work; document the derivation and revisit it after a delay.',
  },
  {
    minimum: 2400,
    maximum: 2600,
    label: 'Elite contest',
    trainingDemand: 'Top-end contest problems requiring rare techniques or exceptionally deep combinations.',
    interviewParallel: 'Competitive-programming and algorithm-specialist development, not a Senior-title requirement.',
    performanceTarget: 'Use deliberate study and post-solve reconstruction; interview speed is not the main metric.',
  },
  {
    minimum: 2600,
    maximum: null,
    label: 'Extreme contest',
    trainingDemand: 'The most difficult tail of the corpus: novel reductions, proofs, and specialist knowledge.',
    interviewParallel: 'Elite competitive-programming territory with little direct generalist interview calibration.',
    performanceTarget: 'Measure learning by independent reconstruction and transfer to unfamiliar variants.',
  },
];

export function formatEloBand(band: Pick<EloBand, 'minimum' | 'maximum'>): string {
  if (band.minimum === null) return `< ${band.maximum}`;
  if (band.maximum === null) return `${band.minimum}+`;
  return `${band.minimum}–${band.maximum - 1}`;
}

export function eloBandForRating(rating: number): EloBand | null {
  return ELO_BANDS.find((band) => (
    (band.minimum === null || rating >= band.minimum)
    && (band.maximum === null || rating < band.maximum)
  )) ?? null;
}
