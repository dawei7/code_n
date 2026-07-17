import { useEffect, useMemo, useRef } from 'react';
import type { ChallengeSummary } from '../types/api';

type EloGuideModalProps = {
  challenges: ChallengeSummary[];
  onClose: () => void;
};

type EloBand = {
  minimum: number | null;
  maximum: number | null;
  label: string;
  trainingDemand: string;
  interviewParallel: string;
  performanceTarget: string;
};

const ELO_BANDS: EloBand[] = [
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

const ROLE_TARGETS = [
  {
    goal: 'Internship / university graduate',
    core: '1300–1499',
    stretch: '1500–1599',
    evidence: 'Reliable fundamentals, clear communication, correct code, complexity, and basic tests.',
    beyondElo: 'Language fluency, projects, collaboration, and behavioral examples.',
  },
  {
    goal: 'Entry-level SWE / SWE I',
    core: '1400–1599',
    stretch: '1600–1699',
    evidence: 'Standard mediums solved independently within a 30–35 min coding window.',
    beyondElo: 'Code quality, debugging, testing, maintainability, and product judgment.',
  },
  {
    goal: 'Mid-level SWE / SWE II',
    core: '1500–1799',
    stretch: '1800–1899',
    evidence: 'Consistent mixed-topic performance plus explicit trade-offs and robust edge-case handling.',
    beyondElo: 'Component design, ownership, operational judgment, communication, and mentoring.',
  },
  {
    goal: 'Senior SWE',
    core: '1600–1899',
    stretch: '1900–2099 for algorithm-heavy roles',
    evidence: 'A stable coding baseline; chasing higher Elo has diminishing generalist interview value.',
    beyondElo: 'System design, ambiguity, reliability, leadership, delivery history, and behavioral depth.',
  },
  {
    goal: 'Staff / Principal generalist',
    core: 'Maintain roughly 1600–1899',
    stretch: 'No universal higher-Elo requirement',
    evidence: 'Enough coding fluency to reason precisely; Elo is not the leveling signal at this scope.',
    beyondElo: 'Architecture, cross-team influence, strategy, organizational leverage, and sustained impact.',
  },
  {
    goal: 'Algorithms / quant / competitive specialist',
    core: '1900–2199',
    stretch: '2200–2600+',
    evidence: 'Broad transfer across advanced topics, not repeated exposure to a narrow pattern set.',
    beyondElo: 'Role-specific mathematics, probability, systems, research, or performance engineering.',
  },
];

function quantile(sortedValues: number[], position: number): number | null {
  if (sortedValues.length === 0) return null;
  const index = (sortedValues.length - 1) * Math.max(0, Math.min(1, position));
  const lower = Math.floor(index);
  const upper = Math.ceil(index);
  if (lower === upper) return sortedValues[lower]!;
  const fraction = index - lower;
  return sortedValues[lower]! + (sortedValues[upper]! - sortedValues[lower]!) * fraction;
}

function countBelow(sortedValues: number[], value: number): number {
  let lower = 0;
  let upper = sortedValues.length;
  while (lower < upper) {
    const middle = Math.floor((lower + upper) / 2);
    if (sortedValues[middle]! < value) lower = middle + 1;
    else upper = middle;
  }
  return lower;
}

function formatBand(band: EloBand): string {
  if (band.minimum === null) return `< ${band.maximum}`;
  if (band.maximum === null) return `${band.minimum}+`;
  return `${band.minimum}–${band.maximum - 1}`;
}

function eloColor(value: number): string {
  const colors: ReadonlyArray<readonly [number, number, number]> = [
    [26, 152, 80],
    [102, 189, 99],
    [166, 217, 106],
    [217, 239, 139],
    [255, 255, 191],
    [254, 224, 139],
    [253, 174, 97],
    [244, 109, 67],
    [215, 48, 39],
  ];
  const position = Math.max(0, Math.min(1, (value - 1200) / 1200));
  const scaled = position * (colors.length - 1);
  const lowerIndex = Math.floor(scaled);
  const upperIndex = Math.min(colors.length - 1, lowerIndex + 1);
  const mix = scaled - lowerIndex;
  const lower = colors[lowerIndex]!;
  const upper = colors[upperIndex]!;
  const channel = (index: number) => Math.round(lower[index]! + (upper[index]! - lower[index]!) * mix);
  return `rgb(${channel(0)} ${channel(1)} ${channel(2)})`;
}

export function EloGuideModal({ challenges, onClose }: EloGuideModalProps) {
  const closeButtonRef = useRef<HTMLButtonElement>(null);
  const realRatings = useMemo(
    () => challenges
      .flatMap((challenge) => challenge.elo_rating === null ? [] : [challenge.elo_rating])
      .sort((left, right) => left - right),
    [challenges],
  );
  const snapshot = useMemo(
    () => [
      ['P10', quantile(realRatings, 0.10)],
      ['P25', quantile(realRatings, 0.25)],
      ['Median', quantile(realRatings, 0.50)],
      ['P75', quantile(realRatings, 0.75)],
      ['P90', quantile(realRatings, 0.90)],
    ] as const,
    [realRatings],
  );
  const difficultySnapshot = useMemo(
    () => ['Easy', 'Medium', 'Hard'].map((difficulty) => {
      const ratings = challenges
        .flatMap((challenge) => (
          challenge.difficulty_label === difficulty && challenge.elo_rating !== null
            ? [challenge.elo_rating]
            : []
        ))
        .sort((left, right) => left - right);
      return {
        difficulty,
        count: ratings.length,
        p10: quantile(ratings, 0.10),
        median: quantile(ratings, 0.50),
        p90: quantile(ratings, 0.90),
      };
    }),
    [challenges],
  );

  useEffect(() => {
    closeButtonRef.current?.focus();
    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') onClose();
    };
    window.addEventListener('keydown', closeOnEscape);
    return () => window.removeEventListener('keydown', closeOnEscape);
  }, [onClose]);

  return (
    <div
      className="fixed inset-0 z-[320] flex items-center justify-center bg-black/75 p-3 backdrop-blur-sm"
      role="dialog"
      aria-modal="true"
      aria-labelledby="elo-guide-title"
      onMouseDown={(event) => {
        if (event.target === event.currentTarget) onClose();
      }}
    >
      <div className="flex max-h-[94vh] w-full max-w-7xl flex-col overflow-hidden rounded-xl border border-coden-border bg-coden-surface text-coden-text shadow-2xl">
        <header className="flex shrink-0 items-start justify-between gap-4 border-b border-coden-border bg-coden-bg px-5 py-4">
          <div>
            <div className="flex items-center gap-2">
              <h2 id="elo-guide-title" className="text-lg font-bold">Elo Difficulty & Interview Practice Guide</h2>
              <span className="rounded-full border border-coden-accent/40 bg-coden-accent/10 px-2 py-0.5 text-[10px] font-bold uppercase tracking-wide text-coden-accent">
                Relative difficulty
              </span>
            </div>
            <p className="mt-1 max-w-4xl text-xs leading-5 text-coden-muted">
              A scientific reading aid for problem ratings, corpus percentiles, practice targets, and their limited relationship to Software Engineer interview levels.
            </p>
          </div>
          <button
            ref={closeButtonRef}
            type="button"
            onClick={onClose}
            className="shrink-0 rounded border border-coden-border bg-coden-surface px-2.5 py-1 text-xs font-bold text-coden-muted hover:border-coden-accent hover:text-coden-text"
            title="Close Elo guide (Escape)"
          >
            x ESC
          </button>
        </header>

        <div className="flex-1 space-y-7 overflow-y-auto p-5 text-sm leading-relaxed scrollbar-thin">
          <section className="grid gap-3 lg:grid-cols-[1.35fr_1fr]">
            <div className="rounded-lg border border-coden-border bg-coden-bg p-4">
              <h3 className="text-sm font-bold text-coden-accent">What the number measures</h3>
              <div className="mt-2 space-y-2 text-xs leading-5 text-coden-muted">
                <p>
                  <strong className="text-coden-text">Problem Elo is a relative difficulty estimate, not a user skill score.</strong>{' '}
                  cOde(n) uses real ratings from ZeroTrac, whose backend adapts the Elo system and maximum-likelihood estimation to LeetCode weekly and biweekly contest results.
                  Elo is Arpad Elo’s surname, not an acronym.
                </p>
                <p>
                  The scale is useful for ordering and grouping problems. It is not a ratio scale: Elo 2000 is not “twice as hard” as Elo 1000.
                  The original Elo family uses rating differences probabilistically, but a LeetCode problem rating must not be converted into an exact personal solve probability.
                </p>
                <p>
                  Treat differences below roughly 50 points as near-neighbors, 100 points as a useful training step, and 200 points as a substantial change in demand.
                  These are practice interpretations, not official LeetCode boundaries.
                </p>
                <div className="grid grid-cols-3 gap-1.5 pt-1 text-center">
                  {[
                    ['+100', 'about 64 / 36'],
                    ['+200', 'about 76 / 24'],
                    ['+400', 'about 92 / 8'],
                  ].map(([difference, expectation]) => (
                    <div key={difference} className="rounded border border-coden-border bg-coden-surface px-2 py-1.5">
                      <div className="font-mono text-[10px] font-bold text-coden-text">{difference}</div>
                      <div className="text-[9px] text-coden-muted">{expectation}</div>
                    </div>
                  ))}
                </div>
                <p className="text-[10px]">
                  The ratios above are classical player-versus-player Elo expectations and explain the scale’s intuition.
                  They are <strong>not</strong> your probability of solving a problem.
                </p>
              </div>
            </div>

            <div className="rounded-lg border border-coden-border bg-coden-bg p-4">
              <h3 className="text-sm font-bold text-coden-accent">Current real-rated corpus</h3>
              <p className="mt-1 text-xs text-coden-muted">
                Calculated live from {realRatings.length.toLocaleString()} real ZeroTrac ratings. Estimated legacy values are excluded.
              </p>
              <div className="mt-3 grid grid-cols-5 gap-1.5">
                {snapshot.map(([label, value]) => (
                  <div key={label} className="rounded border border-coden-border bg-coden-surface px-2 py-2 text-center">
                    <div className="text-[9px] font-bold uppercase tracking-wide text-coden-muted">{label}</div>
                    <div className="mt-0.5 font-mono text-xs font-bold" style={{ color: value === null ? undefined : eloColor(value) }}>
                      {value === null ? '—' : Math.round(value)}
                    </div>
                  </div>
                ))}
              </div>
              <div
                className="mt-4 h-2 rounded-full"
                style={{ background: 'linear-gradient(90deg, #1a9850 0%, #66bd63 12.5%, #a6d96a 25%, #d9ef8b 37.5%, #ffffbf 50%, #fee08b 62.5%, #fdae61 75%, #f46d43 87.5%, #d73027 100%)' }}
                aria-label="Elo heat scale from green at 1200 to red at 2400"
              />
              <div className="mt-1 flex justify-between font-mono text-[9px] text-coden-muted">
                <span>≤1200</span>
                <span>1500</span>
                <span>1800</span>
                <span>2100</span>
                <span>≥2400</span>
              </div>
              <p className="mt-2 text-[10px] leading-4 text-coden-muted">
                The colors are a cOde(n) display scale: green is clamped at 1200 and red at 2400. They are not Elo-system categories.
              </p>
            </div>
          </section>

          <section>
            <SectionHeading
              title="Why Elo is more granular than Easy / Medium / Hard"
              subtitle="Official difficulty remains important, but each label spans a wide range. These live real-Elo summaries show the middle 80% and median."
            />
            <div className="mt-3 grid gap-3 md:grid-cols-3">
              {difficultySnapshot.map((tier) => (
                <div key={tier.difficulty} className="rounded-lg border border-coden-border bg-coden-bg p-4">
                  <div className="flex items-center justify-between gap-2">
                    <h4 className="text-sm font-bold text-coden-text">{tier.difficulty}</h4>
                    <span className="font-mono text-[9px] text-coden-muted">{tier.count.toLocaleString()} real ratings</span>
                  </div>
                  <div className="mt-3 grid grid-cols-3 gap-1.5 text-center">
                    {[
                      ['P10', tier.p10],
                      ['Median', tier.median],
                      ['P90', tier.p90],
                    ].map(([label, value]) => (
                      <div key={String(label)} className="rounded border border-coden-border bg-coden-surface px-2 py-2">
                        <div className="text-[9px] font-bold uppercase tracking-wide text-coden-muted">{label}</div>
                        <div
                          className="mt-0.5 font-mono text-xs font-bold"
                          style={{ color: typeof value === 'number' ? eloColor(value) : undefined }}
                        >
                          {typeof value === 'number' ? Math.round(value) : '—'}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </section>

          <section>
            <SectionHeading
              title="Granular problem-difficulty ladder"
              subtitle="Corpus percentiles and counts are live. Training demands describe common reasoning pressure, not a topic guarantee."
            />
            <div className="mt-3 overflow-x-auto rounded-lg border border-coden-border">
              <table className="w-full min-w-[1050px] border-collapse text-left text-[11px] leading-4">
                <thead className="bg-coden-bg text-[9px] uppercase tracking-wide text-coden-muted">
                  <tr>
                    <th className="px-3 py-2">Elo</th>
                    <th className="px-3 py-2">Live corpus slice</th>
                    <th className="px-3 py-2">Level</th>
                    <th className="px-3 py-2">Common training demand</th>
                    <th className="px-3 py-2">Closest interview use</th>
                    <th className="px-3 py-2">Evidence before moving up</th>
                  </tr>
                </thead>
                <tbody>
                  {ELO_BANDS.map((band) => {
                    const lowerCount = band.minimum === null ? 0 : countBelow(realRatings, band.minimum);
                    const upperCount = band.maximum === null ? realRatings.length : countBelow(realRatings, band.maximum);
                    const count = Math.max(0, upperCount - lowerCount);
                    const lowerPercentile = realRatings.length === 0 ? 0 : Math.round(lowerCount / realRatings.length * 100);
                    const upperPercentile = realRatings.length === 0 ? 0 : Math.round(upperCount / realRatings.length * 100);
                    const colorValue = band.minimum === null
                      ? 1150
                      : band.maximum === null
                        ? 2700
                        : (band.minimum + band.maximum) / 2;
                    return (
                      <tr
                        key={formatBand(band)}
                        className="border-t border-coden-border align-top hover:bg-coden-bg/70"
                        style={{ borderLeft: `3px solid ${eloColor(colorValue)}` }}
                      >
                        <td className="whitespace-nowrap px-3 py-2.5 font-mono font-bold" style={{ color: eloColor(colorValue) }}>
                          {formatBand(band)}
                        </td>
                        <td className="whitespace-nowrap px-3 py-2.5 text-coden-muted">
                          P{lowerPercentile}–P{upperPercentile}
                          <span className="block text-[9px] opacity-75">{count.toLocaleString()} problems</span>
                        </td>
                        <td className="px-3 py-2.5 font-semibold text-coden-text">{band.label}</td>
                        <td className="max-w-[260px] px-3 py-2.5 text-coden-muted">{band.trainingDemand}</td>
                        <td className="max-w-[250px] px-3 py-2.5 text-coden-muted">{band.interviewParallel}</td>
                        <td className="max-w-[280px] px-3 py-2.5 text-coden-muted">{band.performanceTarget}</td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </section>

          <section>
            <SectionHeading
              title="Software Engineer and interview targets"
              subtitle="These are cOde(n) practice recommendations—not employer cutoffs, job levels, or hiring guarantees."
            />
            <div className="mt-3 overflow-x-auto rounded-lg border border-coden-border">
              <table className="w-full min-w-[980px] border-collapse text-left text-[11px] leading-4">
                <thead className="bg-coden-bg text-[9px] uppercase tracking-wide text-coden-muted">
                  <tr>
                    <th className="px-3 py-2">Goal</th>
                    <th className="px-3 py-2">Core practice band</th>
                    <th className="px-3 py-2">Useful stretch</th>
                    <th className="px-3 py-2">What Elo evidence should look like</th>
                    <th className="px-3 py-2">What Elo cannot measure</th>
                  </tr>
                </thead>
                <tbody>
                  {ROLE_TARGETS.map((target) => (
                    <tr key={target.goal} className="border-t border-coden-border align-top hover:bg-coden-bg/70">
                      <td className="px-3 py-2.5 font-semibold text-coden-text">{target.goal}</td>
                      <td className="whitespace-nowrap px-3 py-2.5 font-mono font-bold text-coden-accent">{target.core}</td>
                      <td className="px-3 py-2.5 font-mono text-coden-muted">{target.stretch}</td>
                      <td className="max-w-[290px] px-3 py-2.5 text-coden-muted">{target.evidence}</td>
                      <td className="max-w-[300px] px-3 py-2.5 text-coden-muted">{target.beyondElo}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div className="mt-3 rounded-lg border border-amber-500/30 bg-amber-500/10 px-4 py-3 text-xs leading-5 text-amber-100">
              <strong>Critical interpretation:</strong> a candidate who reliably solves Elo 1800 problems is not thereby a Senior Engineer.
              Official interview guidance also evaluates design, testing, maintainability, strategic problem solving, communication, behavioral evidence, and—for experienced roles—ownership and leadership.
              Conversely, an accomplished Senior or Staff engineer does not need Elo 2400 competitive-programming ability for most generalist roles.
            </div>
          </section>

          <section className="grid gap-3 lg:grid-cols-2">
            <div>
              <SectionHeading title="When a band is genuinely mastered" />
              <ol className="mt-3 space-y-2 rounded-lg border border-coden-border bg-coden-bg p-4 text-xs leading-5 text-coden-muted">
                <li><strong className="text-coden-text">1. Use unseen problems:</strong> sample at least 20 real-rated problems across at least five topics. Repeated problems test recall, not transfer.</li>
                <li><strong className="text-coden-text">2. Simulate the interview:</strong> no editorial or AI help; clarify the contract, state an approach, code, analyze complexity, and test inside 35–45 minutes.</li>
                <li><strong className="text-coden-text">3. Require complete evidence:</strong> count a success only when the code is correct, reaches the required complexity, handles edge cases, and can be explained coherently.</li>
                <li><strong className="text-coden-text">4. Use an operational threshold:</strong> ≥16/20 first-pass successes indicates readiness to add the next 100-point band. A small sample is noisy; 40 problems gives stronger evidence.</li>
                <li><strong className="text-coden-text">5. Verify retention:</strong> one or two weeks later, solve new problems using the same patterns. Delayed retrieval is more informative than immediate repetition.</li>
                <li><strong className="text-coden-text">6. Keep breadth:</strong> a useful weekly mix is roughly 70% target band, 20% consolidation below it, and 10% exploratory stretch above it.</li>
              </ol>
            </div>

            <div>
              <SectionHeading title="Real Elo, Est. Elo, and Frequency" />
              <div className="mt-3 space-y-3 rounded-lg border border-coden-border bg-coden-bg p-4 text-xs leading-5 text-coden-muted">
                <div>
                  <strong className="text-coden-text">Elo N</strong>
                  <p>Real ZeroTrac contest-derived rating. Only real ratings appear in the Elo problem set and in the live corpus percentiles above.</p>
                </div>
                <div>
                  <strong className="text-coden-text">Est. Elo N</strong>
                  <p>
                    cOde(n)’s explicit fallback for unrated problems. Official difficulty selects a non-overlapping real-Elo band, acceptance percentile positions the problem inside it,
                    and each legacy cohort is calibrated to average the 33rd percentile of its matching real difficulty. The stored value is refreshed by the repository metadata updater.
                  </p>
                </div>
                <div>
                  <strong className="text-coden-text">Freq N.N%</strong>
                  <p>
                    LeetCode’s mutable 0–100 Frequency attribute. It is displayed beside Elo but measures a different dimension: relative exposure or prominence in LeetCode’s data,
                    not algorithmic difficulty, acceptance rate, or the probability that a specific interviewer will ask the problem.
                  </p>
                </div>
                <div>
                  <strong className="text-coden-text">Do not mix the evidence</strong>
                  <p>Estimated Elo is useful for navigation and averages, but it is not contest evidence. Tooltips disclose the model, and the real-only Elo set excludes it.</p>
                </div>
              </div>
            </div>
          </section>

          <section>
            <SectionHeading title="Research and primary guidance" />
            <div className="mt-3 grid gap-2 md:grid-cols-2 xl:grid-cols-3">
              <SourceLink
                href="https://github.com/zerotrac/leetcode_problem_rating"
                title="ZeroTrac problem-rating project"
                detail="Elo + maximum-likelihood relative problem ratings; explicitly described as not perfectly accurate."
              />
              <SourceLink
                href="https://handbook.fide.com/chapter/B022024"
                title="FIDE rating regulations"
                detail="The underlying Elo-family scale is arbitrary and uses a 200-point class interval."
              />
              <SourceLink
                href="https://amazon.jobs/content/en/how-we-hire/sde-ii-interview-prep"
                title="Amazon SDE II interview preparation"
                detail="Coding, system design, behavioral evidence, scalability, robustness, and testing."
              />
              <SourceLink
                href="https://careers.microsoft.com/v2/global/en/hiring-tips/technical-interviewing.html"
                title="Microsoft technical interviewing"
                detail="Problem solving, design, coding, testing, algorithms, data structures, and distributed systems."
              />
              <SourceLink
                href="https://www.metacareers.com/careers/SWE-prep-onsite"
                title="Meta Full Loop preparation"
                detail="Several conversations assess technical skills and broader role fit."
              />
              <SourceLink
                href="https://pubmed.ncbi.nlm.nih.gov/16507066/"
                title="Roediger & Karpicke (2006)"
                detail="Retrieval testing improved delayed retention more than repeated study."
              />
              <SourceLink
                href="https://pubmed.ncbi.nlm.nih.gov/16719566/"
                title="Cepeda et al. (2006)"
                detail="Quantitative synthesis of distributed practice and long-term retention."
              />
            </div>
          </section>
        </div>

        <footer className="flex shrink-0 items-center justify-between gap-3 border-t border-coden-border bg-coden-bg px-5 py-3">
          <p className="text-[10px] text-coden-muted">
            Use Elo to select training difficulty. Use repeated independent performance—and the rest of the engineering interview rubric—to judge readiness.
          </p>
          <button
            type="button"
            onClick={onClose}
            className="rounded bg-coden-accent px-4 py-1.5 text-xs font-bold text-coden-accentContrast hover:opacity-90"
          >
            Close
          </button>
        </footer>
      </div>
    </div>
  );
}

function SectionHeading({ title, subtitle }: { title: string; subtitle?: string }) {
  return (
    <div className="border-b border-coden-border pb-1.5">
      <h3 className="text-sm font-bold uppercase tracking-wide text-coden-accent">{title}</h3>
      {subtitle && <p className="mt-0.5 text-[10px] leading-4 text-coden-muted">{subtitle}</p>}
    </div>
  );
}

function SourceLink({ href, title, detail }: { href: string; title: string; detail: string }) {
  return (
    <a
      href={href}
      target="_blank"
      rel="noreferrer"
      className="rounded-lg border border-coden-border bg-coden-bg p-3 transition-colors hover:border-coden-accent"
    >
      <span className="block text-xs font-semibold text-coden-text">{title}</span>
      <span className="mt-1 block text-[10px] leading-4 text-coden-muted">{detail}</span>
    </a>
  );
}
