## General

Let $n$ be the target length and let $S$ be the total length of the distinct available words.

**Treat target prefixes as states**

After any valid sequence of operations, the constructed string must equal a prefix of \`target\`; otherwise no future append can repair the mismatch. Define \`best[i]\` as the minimum cost to build exactly \`target[:i]\`. Initialize \`best[0] = 0\` and every other state as unreachable.

Process boundaries from left to right. If boundary \`start\` is reachable, test each distinct word against \`target\` beginning there. A match creates an edge to \`end = start + len(word)\` with that word's cost, so relax \`best[end]\` from \`best[start] + cost\`. Edges always move right, making this a shortest-path computation on an acyclic graph whose natural topological order is the string order.

**Compress duplicate operations**

When the same word occurs more than once, only its smallest listed cost can be useful. Replacing duplicate entries with that minimum does not remove any optimal construction: every use of a more expensive duplicate can be exchanged for the identical cheaper append. Compression also avoids repeating the same substring check.

For correctness, \`best[0]\` represents the empty operation sequence. Assume all earlier reachable prefixes have their true minimum costs. Every way to reach a later boundary ends with some available word matching immediately before it, and the relaxation examines that exact predecessor and operation. Conversely, every performed relaxation appends a matching word to a constructible prefix, so it creates a valid prefix. Induction over boundaries proves each finite state is its minimum valid cost. The last state is therefore the requested answer, while infinity means no full construction exists.

## Complexity detail

At each of $n$ starting positions, matching all distinct words inspects at most $S$ characters in total, for $O(nS)$ time. The prefix-cost array uses $O(n)$ space, and the deduplicated word map stores $O(S)$ characters, giving $O(n+S)$ auxiliary space.

## Alternatives and edge cases

- **Plain recursive enumeration:** Trying every matching word without memoizing prefix positions repeats the same suffix subproblems and can take exponential time.
- **Memoized recursion:** This has the same state graph and asymptotic work as bottom-up DP, but the iterative form avoids recursion-depth concerns.
- **Greedy cheapest next word:** A locally cheap append can force an expensive or impossible remainder, so it does not guarantee the minimum total.
- **Breadth-first search:** It minimizes the number of appended words, not their unequal costs.
- The same word may be reused any number of times.
- Duplicate words can carry different costs; only the minimum duplicate cost matters.
- A word matching the target prefix may still lead to a dead end.
- Words longer than the remaining suffix simply do not match.
- Return \`-1\`, not infinity, when the final boundary remains unreachable.
