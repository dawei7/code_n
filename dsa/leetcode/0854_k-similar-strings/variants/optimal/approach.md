## General

**Search strings by number of swaps**

Each state is a string obtainable from `s1`. An edge represents one swap of two positions. The task asks for the fewest swaps reaching `s2`, so breadth-first search over this unweighted state graph is appropriate.

The queue starts with `s1` at distance zero. Each BFS level adds one swap. The first time `s2` is dequeued, the current level `ans` is the minimum possible number of swaps.

The challenge is generating only useful neighbors rather than all $\binom{n}{2}$ swaps from every state.

**Always focus on the first mismatch**

Helper `next(s)` finds the smallest index `i` for which `s[i] != s2[i]`.

Every earlier position already matches the target. The neighbor generation never touches those positions, so the correct prefix grows monotonically and is never damaged.

If `s != s2`, an anagram must contain the needed character `s2[i]` somewhere after `i`.

**Choose a swap partner that fixes index `i`**

For each `j > i`, the source requires:

- `s[j] == s2[i]`, so moving `s[j]` to `i` fixes the first mismatch;
- `s[j] != s2[j]`, so position `j` is currently wrong and the swap does not destroy a correct target character there.

Only such positions generate neighbors.

This pruning makes every produced swap increase the length of the matching prefix by at least one.

**Understand the compact string construction**

A normal swap would create:

`s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]`.

Because `s[:i] == s2[:i]` and `s[j] == s2[i]`, the first two parts equal `s2[:i+1]`. The code therefore constructs:

`s2[: i + 1] + s[i + 1 : j] + s[i] + s[j + 1 :]`.

This is exactly the swapped string, expressed using the known-correct target prefix.

**Why fixing the first mismatch is safe for an optimal solution**

Consider any shortest swap sequence from current `s` to `s2`. Position `i` must eventually receive character `s2[i]` from some later mismatched position `j`.

We can perform that corrective swap first. It fixes `i`, does not disturb the already correct prefix, and moves `s[i]` to a position that was not correct. The remaining character multiset outside the fixed prefix is still the one needed for the target.

Standard swap-cycle reasoning shows this choice does not require more swaps than leaving `i` wrong while modifying later positions first. There exists an optimal sequence whose next swap fixes the first mismatch.

Trying every eligible `j` covers all such optimal first choices, including duplicates of the needed character.

**Why avoid a currently correct `j`**

If `s[j] == s2[j]`, swapping its character away would create a new mismatch while fixing `i`. Because `s1` and `s2` are anagrams, another copy of the needed character must be available in a mismatched position whenever an optimal correction requires it.

Restricting to wrong `j` positions reduces branching without removing all optimal paths.

**Visited strings prevent repeated work**

Different swap sequences can produce the same string. `vis` stores every enqueued state.

BFS first reaches a state with the minimum number of swaps. Re-enqueuing it later cannot improve its distance or its future possibilities, so duplicate states are discarded safely.

**Trace `"abc" -> "bca"`**

The first mismatch is index 0: current `a` must become target `b`. The `b` at index 1 is mismatched, so swapping indices 0 and 1 produces `"bac"`.

Now index 0 matches. The first mismatch is index 1, which needs `c` from index 2. Swapping produces `"bca"` at BFS depth two. Therefore, the minimum is two.

**Termination**

The input strings are anagrams, so a swap sequence exists. Every generated state fixes at least the first mismatched position and preserves earlier matches, strongly restricting the state space.

The infinite loop reaches `s2` and returns; it does not need an empty-queue fallback under valid input.

**Why the BFS answer is correct**

The neighbor proof establishes that from every non-target state, the generator includes the first step of at least one optimal remaining sequence. Therefore, the pruned state graph still contains an optimal path from `s1` to `s2`.

BFS explores that graph in increasing swap count. The first target state consequently has the globally minimum number of swaps.

## Complexity detail

Let `n` be string length and `P` be the number of distinct states reached by the pruned BFS.

For one state, finding the first mismatch takes `O(n)`. It may examine `O(n)` partners. Constructing each neighbor with string slices copies `O(n)` characters, giving `O(n^2)` time per state in the worst case.

Total time is `O(n^2P)`.

The queue and visited set can store `P` strings, each of length `n`, using `O(nP)` space. One generated neighbor list also fits within that bound.

The constraint `n <= 20` and the first-mismatch pruning keep `P` manageable compared with all string permutations.

## Alternatives and edge cases

- **Generate every possible swap:** BFS remains correct but branches into many swaps that do not improve the first mismatch.

- **Depth-first search with branch-and-bound:** It can find good solutions but needs careful lower bounds to prove minimality. BFS gives shortest swap count directly.

- **A* search:** A mismatch-based heuristic can reduce explored states, but adds priority-queue and admissibility reasoning.

- **Strings already equal:** The initial state is dequeued at depth zero and returned immediately; `next` is not called.

- **Repeated letters:** Several indices may carry the needed character, so all eligible mismatched partners are explored.

- **Do not disturb the correct prefix:** Neighbor construction fixes through index `i` and copies that prefix from `s2`.

- **Partner already correct:** It is skipped to avoid trading one mismatch for another.

- **One swap solution:** A valid partner at the first mismatch produces `s2` in the next BFS level.

- **Anagram guarantee:** It ensures the needed character exists and some transformation is possible.

- **Visited duplicate:** Different swap orders reaching the same string do not cause repeated expansion.

- **Exact swap count:** Every BFS edge is one swap, so level number equals `k`.

- **Input immutability:** New strings are constructed; `s1` and `s2` are unchanged.
