## General
The small limit of 14 words permits exploring the include-or-exclude choice for every word. Precompute each word's letter-frequency map and score so a recursive branch can test feasibility without rescanning the word's characters repeatedly.

**State and branching**

At word index `i`, first explore skipping the word. Then check whether the remaining letter multiset contains every required occurrence. If it does, subtract those counts, explore the branch that includes the word, add its precomputed score, and take the larger result. Copying the remaining counts keeps sibling branches independent.

**Why the search finds the optimum**

Every subset has a unique sequence of include and exclude decisions, so the recursion examines it exactly once. A branch is discarded only when its selected words require more of some letter than is available; adding more words can never repair that shortage. Thus every feasible subset remains represented, and maximizing over both choices at each level returns the best score.

The empty subset supplies a score of zero, which is important when no candidate word is feasible or all relevant letter scores are zero.

## Complexity detail
There are at most $2^w$ decision paths. Across feasibility checks and count updates, a conservative bound is $O(2^wL)$ time. Precomputed word counts contain $O(L)$ entries in total, and recursion plus branch-local count storage uses $O(w+L)$ live space under the small fixed alphabet.

## Alternatives and edge cases
- **Bitmask enumeration:** Evaluate every subset mask and aggregate its letter needs; it has the same exponential subset count but naively rebuilding counts adds repeated work.
- **Memoization by remaining counts:** It can merge repeated states, but the state key is larger and the 14-word limit already makes direct backtracking practical.
- **Greedy score ordering:** Choosing the highest-scoring word first can consume letters needed by a better combination and is not correct.
- **Duplicate candidate words:** Each list position is a separate selectable word, while letter multiplicities still limit how many copies can be formed.
- **Unformable word:** Its inclusion branch is skipped without affecting other candidates.
- **Zero scores:** Such letters still consume availability even though they add nothing to the objective.
