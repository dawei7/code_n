import { ChallengeSummary, ProgressOut } from '../../types/api';

export interface TopicRoadmapNode {
  id: string;
  name: string;
  phase: number;
  phaseName: string;
  description: string;
  prerequisites: string[];
  tags: string[];
  recommendedElo: number;
}

export const DSA_TOPIC_ROADMAP: TopicRoadmapNode[] = [
  // Phase 1: Core Fundamentals
  {
    id: 'arrays-hashing',
    name: 'Arrays & Hashing',
    phase: 1,
    phaseName: 'Core Fundamentals',
    description: 'Hash maps, frequency tables, prefix sums, and index invariants.',
    prerequisites: [],
    tags: ['Array', 'Hash Table', 'Prefix Sum'],
    recommendedElo: 1200,
  },
  {
    id: 'two-pointers',
    name: 'Two Pointers',
    phase: 1,
    phaseName: 'Core Fundamentals',
    description: 'Opposite-end and fast-slow pointer scans on sorted and linked sequences.',
    prerequisites: ['arrays-hashing'],
    tags: ['Two Pointers'],
    recommendedElo: 1300,
  },
  {
    id: 'sliding-window',
    name: 'Sliding Window',
    phase: 1,
    phaseName: 'Core Fundamentals',
    description: 'Dynamic and fixed-size contiguous subarray and substring optimization.',
    prerequisites: ['two-pointers'],
    tags: ['Sliding Window'],
    recommendedElo: 1400,
  },
  {
    id: 'stack',
    name: 'Stack & Monotonic Stack',
    phase: 1,
    phaseName: 'Core Fundamentals',
    description: 'LIFO parsing, parenthesization, and monotonic range extrema lookup.',
    prerequisites: ['arrays-hashing'],
    tags: ['Stack', 'Monotonic Stack'],
    recommendedElo: 1450,
  },
  {
    id: 'binary-search',
    name: 'Binary Search',
    phase: 1,
    phaseName: 'Core Fundamentals',
    description: 'Logarithmic search spaces, predicate monotonicity, and answer-space bisection.',
    prerequisites: ['arrays-hashing'],
    tags: ['Binary Search'],
    recommendedElo: 1400,
  },

  // Phase 2: Data Structures
  {
    id: 'linked-list',
    name: 'Linked List',
    phase: 2,
    phaseName: 'Linear & Hierarchical Structures',
    description: 'Pointer manipulation, reversal, cycle detection, and merge routines.',
    prerequisites: ['two-pointers'],
    tags: ['Linked List'],
    recommendedElo: 1350,
  },
  {
    id: 'trees',
    name: 'Binary Trees & BST',
    phase: 2,
    phaseName: 'Linear & Hierarchical Structures',
    description: 'DFS/BFS traversals, LCA, tree construction, and BST properties.',
    prerequisites: ['stack'],
    tags: ['Tree', 'Binary Tree', 'Binary Search Tree'],
    recommendedElo: 1500,
  },
  {
    id: 'tries',
    name: 'Tries (Prefix Trees)',
    phase: 2,
    phaseName: 'Linear & Hierarchical Structures',
    description: 'Prefix lookups, word dictionaries, and bitwise XOR tries.',
    prerequisites: ['trees'],
    tags: ['Trie'],
    recommendedElo: 1600,
  },
  {
    id: 'heap',
    name: 'Heap / Priority Queue',
    phase: 2,
    phaseName: 'Linear & Hierarchical Structures',
    description: 'Top-K elements, streaming medians, and greedy task scheduling.',
    prerequisites: ['trees'],
    tags: ['Heap (Priority Queue)'],
    recommendedElo: 1550,
  },

  // Phase 3: Search & Graphs
  {
    id: 'backtracking',
    name: 'Backtracking',
    phase: 3,
    phaseName: 'Search & Graph Algorithms',
    description: 'Permutations, combinations, subset generation, and constraint pruning.',
    prerequisites: ['trees'],
    tags: ['Backtracking'],
    recommendedElo: 1600,
  },
  {
    id: 'graphs',
    name: 'Graphs (BFS & DFS)',
    phase: 3,
    phaseName: 'Search & Graph Algorithms',
    description: 'Connected components, topological sort, flood fill, and bipartite matching.',
    prerequisites: ['trees', 'backtracking'],
    tags: ['Graph', 'Depth-First Search', 'Breadth-First Search', 'Topological Sort'],
    recommendedElo: 1650,
  },
  {
    id: 'advanced-graphs',
    name: 'Advanced Graphs & Disjoint Set',
    phase: 3,
    phaseName: 'Search & Graph Algorithms',
    description: 'Dijkstra, Bellman-Ford, Kruskal, Prim, and Union-Find with path compression.',
    prerequisites: ['graphs', 'heap'],
    tags: ['Union Find', 'Shortest Path', 'Minimum Spanning Tree'],
    recommendedElo: 1800,
  },

  // Phase 4: Dynamic Programming
  {
    id: '1d-dp',
    name: '1-D Dynamic Programming',
    phase: 4,
    phaseName: 'Dynamic Programming',
    description: 'State transitions, prefix subproblems, climbing stairs, and house robber.',
    prerequisites: ['backtracking'],
    tags: ['Dynamic Programming', 'Memoization'],
    recommendedElo: 1650,
  },
  {
    id: '2d-dp',
    name: '2-D & Grid Dynamic Programming',
    phase: 4,
    phaseName: 'Dynamic Programming',
    description: 'Longest common subsequence, knapsack, edit distance, and grid paths.',
    prerequisites: ['1d-dp'],
    tags: ['Dynamic Programming'],
    recommendedElo: 1800,
  },

  // Phase 5: Advanced Optimization
  {
    id: 'greedy-intervals',
    name: 'Greedy & Intervals',
    phase: 5,
    phaseName: 'Advanced Topics',
    description: 'Interval merging, non-overlapping scheduling, and local optimal choices.',
    prerequisites: ['arrays-hashing'],
    tags: ['Greedy'],
    recommendedElo: 1500,
  },
  {
    id: 'bit-manipulation',
    name: 'Bit Manipulation & Math',
    phase: 5,
    phaseName: 'Advanced Topics',
    description: 'Bitwise XOR tricks, bitmask DP, fast power, and modular arithmetic.',
    prerequisites: ['arrays-hashing'],
    tags: ['Bit Manipulation', 'Math'],
    recommendedElo: 1600,
  },
];

interface TopicRoadmapViewProps {
  challenges: ChallengeSummary[];
  progress: ProgressOut;
  onSelectTopic: (topicId: string, tagNames: string[]) => void;
}

export function TopicRoadmapView({
  challenges,
  progress,
  onSelectTopic,
}: TopicRoadmapViewProps) {
  const completedIds = new Set(progress.completed || []);

  // Compute stats per topic
  const topicStats = DSA_TOPIC_ROADMAP.map((topic) => {
    const topicChallenges = challenges.filter((c) => {
      const topicNames = (c.leetcode_topics || []).map((t: any) =>
        typeof t === 'string' ? t : t.name
      );
      return topic.tags.some((tag) => topicNames.includes(tag) || c.category === tag);
    });

    const totalCount = topicChallenges.length;
    const solvedCount = topicChallenges.filter((c) => completedIds.has(c.id)).length;
    const pct = totalCount > 0 ? Math.round((solvedCount / totalCount) * 100) : 0;
    const isMastered = pct >= 80 && totalCount >= 5;

    return {
      ...topic,
      totalCount,
      solvedCount,
      pct,
      isMastered,
    };
  });

  const phases = [
    { id: 1, name: 'Phase 1: Core Fundamentals' },
    { id: 2, name: 'Phase 2: Linear & Hierarchical Structures' },
    { id: 3, name: 'Phase 3: Search & Graph Algorithms' },
    { id: 4, name: 'Phase 4: Dynamic Programming' },
    { id: 5, name: 'Phase 5: Specialized Optimization' },
  ];

  return (
    <div className="space-y-6">
      {/* Header Banner */}
      <div className="rounded-lg border border-coden-border bg-gradient-to-r from-coden-surface via-coden-surface/80 to-coden-accent/10 p-5">
        <div className="flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-coden-accent/20 text-coden-accent">
            <svg className="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
            </svg>
          </div>
          <div>
            <h2 className="text-lg font-bold text-coden-text">DSA Skill Dependency Roadmap</h2>
            <p className="text-xs text-coden-muted">
              Structured progressive curriculum mapping foundational algorithm patterns to advanced DP & graphs.
            </p>
          </div>
        </div>
      </div>

      {/* Phase Sections */}
      <div className="space-y-6">
        {phases.map((phase) => {
          const phaseTopics = topicStats.filter((t) => t.phase === phase.id);
          if (phaseTopics.length === 0) return null;

          return (
            <div key={phase.id} className="space-y-3">
              <div className="flex items-center gap-2 border-b border-coden-border pb-2">
                <span className="flex h-5 w-5 items-center justify-center rounded-full bg-coden-accent/20 text-[11px] font-bold text-coden-accent">
                  {phase.id}
                </span>
                <h3 className="text-sm font-bold text-coden-text">{phase.name}</h3>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                {phaseTopics.map((topic) => (
                  <div
                    key={topic.id}
                    onClick={() => onSelectTopic(topic.id, topic.tags)}
                    className="group relative cursor-pointer rounded-lg border border-coden-border bg-coden-surface/70 p-4 transition-all hover:border-coden-accent/80 hover:bg-coden-surface hover:shadow-md"
                  >
                    <div className="flex items-start justify-between gap-2">
                      <h4 className="font-bold text-sm text-coden-text group-hover:text-coden-accent transition-colors flex items-center gap-1.5">
                        {topic.name}
                        {topic.isMastered && (
                          <span className="text-emerald-400 font-bold text-xs" title="Topic Mastered">✓</span>
                        )}
                      </h4>
                      <span className="rounded bg-coden-border/60 px-2 py-0.5 text-[10px] font-mono text-coden-muted">
                        ~{topic.recommendedElo} Elo
                      </span>
                    </div>

                    <p className="mt-1.5 text-xs text-coden-muted leading-relaxed line-clamp-2">
                      {topic.description}
                    </p>

                    {/* Progress Bar */}
                    <div className="mt-3">
                      <div className="flex items-center justify-between text-[11px] font-mono text-coden-muted mb-1">
                        <span>{topic.solvedCount} / {topic.totalCount} solved</span>
                        <span className="font-bold text-coden-accent">{topic.pct}%</span>
                      </div>
                      <div className="h-1.5 w-full bg-coden-border/60 rounded-full overflow-hidden">
                        <div
                          className="h-full bg-gradient-to-r from-coden-accent to-emerald-400 rounded-full transition-all duration-500"
                          style={{ width: `${topic.pct}%` }}
                        />
                      </div>
                    </div>

                    {/* Tags preview */}
                    <div className="mt-3 flex flex-wrap gap-1">
                      {topic.tags.slice(0, 2).map((t) => (
                        <span key={t} className="rounded border border-coden-border bg-coden-surface/50 px-1.5 py-0.5 text-[10px] text-coden-muted">
                          {t}
                        </span>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
