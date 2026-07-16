# Parallel Courses II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1494 |
| Difficulty | Hard |
| Topics | Dynamic Programming, Bit Manipulation, Graph Theory, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/parallel-courses-ii/) |

## Problem Description
### Goal

There are `n` courses labeled from `1` through `n`. Each pair `[previous, next]` in `relations` means that `previous` must be completed in an earlier semester before `next` may be taken. The prerequisite graph is a directed acyclic graph, so every course can eventually be completed.

In one semester, choose at most `k` courses whose complete prerequisite sets were finished before that semester began. Courses taken together cannot satisfy prerequisites for one another during the same semester. Return the minimum number of semesters needed to finish all `n` courses.

### Function Contract
**Inputs**

Let $N$ be the number of courses and $R$ the number of prerequisite relations.

- `n`: the course count, with $1 \le N \le 15$.
- `relations`: a list of distinct directed pairs `[previous, next]`, with $0 \le R \le N(N-1)/2$.
- Every course label lies from `1` through `n`, and no relation is a self-edge.
- The directed graph described by `relations` is acyclic.
- `k`: the per-semester course limit, with $1 \le k \le N$.

**Return value**

Return the minimum number of semesters required to complete every course while respecting all prerequisites and taking at most `k` courses per semester.

### Examples
**Example 1**

- Input: `n = 4, relations = [[2,1],[3,1],[1,4]], k = 2`
- Output: `3`
- Explanation: Take courses `2` and `3`, then course `1`, then course `4`.

**Example 2**

- Input: `n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2`
- Output: `4`
- Explanation: Only two of courses `2`, `3`, and `4` fit in the first semester, so the remaining prerequisite delays courses `1` and `5`.

**Example 3**

- Input: `n = 11, relations = [], k = 2`
- Output: `6`
- Explanation: With no prerequisites, capacity alone requires $\lceil 11/2 \rceil = 6$ semesters.

### Required Complexity

- **Time:** $O(N3^N)$
- **Space:** $O(2^N + N)$

<details>
<summary>Approach</summary>

#### General

**Let completed courses define the entire future**

Because every course lasts exactly one semester and prerequisites depend only on which courses were finished earlier, the order used to reach a completed set no longer matters. Represent that set by an $N$-bit mask `done`: bit `i` is one exactly when course `i + 1` has been completed.

Define `semesters[done]` as the fewest semesters needed to reach that mask. The initial state is mask zero with value zero, and the target is the mask whose $N$ bits are all one. This merges all schedules that lead to the same completed set and keeps only their best semester count.

**Precompute prerequisite masks**

For each course, build an $N$-bit mask containing all of its direct prerequisites. A course not already in `done` is available precisely when `prerequisites[course] & done == prerequisites[course]`. Since every direct prerequisite must itself have been completed in an earlier semester, this condition enforces the source rule exactly.

For a reachable state, scan all courses and OR every currently eligible course bit into one mask `available`. The DAG guarantee ensures that a nonfinal state always has at least one available course.

**Handle the capacity-only graph directly**

When `relations` is empty, every course is available from the beginning and no subset choice can affect future eligibility. Capacity alone determines the answer as $lceil N/k ceil$. Returning that value directly avoids constructing an exponential DP for a case with a closed-form optimum.

**Take every available course when capacity permits**

If `available.bit_count() <= k`, transition using all available courses. Leaving an unused slot while postponing an already eligible course cannot improve a schedule: moving that course into the current spare slot violates no prerequisite, consumes no future capacity, and can only make its dependents available sooner.

This dominance rule removes unnecessary subset choices whenever the semester limit is not binding.

**Generate exact-k choices when capacity binds**

When more than `k` courses are available, an optimal semester can be assumed to take exactly `k`. Taking fewer leaves capacity unused; adding another currently available course cannot hurt and may help unlock future work.

Store the bits of the available courses and generate every combination of exactly `k` bits. Summing those distinct powers of two forms the semester mask `take`. For each choice, the next state is `done | take`, reached in one additional semester. Relax its DP value with `semesters[done] + 1`.

Generating combinations directly avoids walking through all $2^a$ submasks merely to discard those with the wrong cardinality, where $a$ is the number of currently available courses. It is especially important for staying within the execution-step budget on dense availability states.

The selection matters: choosing an available course that unlocks a long prerequisite chain may be better than choosing an unrelated course. Enumerating all legal exact-capacity choices is what avoids an invalid greedy tie-break.

**Why the dynamic program finds the minimum**

Every transition chooses only courses whose prerequisites are contained in `done`, and chooses no more than `k`, so every DP path is a valid semester schedule. Conversely, consider an optimal schedule from any state. By the spare-capacity arguments, its next semester may be transformed without increasing length to take all available courses when there are at most `k`, or exactly `k` of them otherwise. That transformed choice is one of the generated transitions.

Inducting over the remaining semesters shows that the transition graph contains an optimal continuation from every reachable mask. Relaxing masks in increasing numeric order is safe because every transition only sets bits, so `next_state > done`. Therefore `semesters[full_mask]` is the global minimum.

**Why prerequisite courses cannot be taken simultaneously with dependents**

`available` is computed solely from the old `done` mask. Newly selected courses are not inserted until the next state is formed, so a course taken this semester never satisfies another selected course's prerequisite during the same semester. This preserves the requirement that prerequisites be completed in previous semesters.

#### Complexity detail

There are $2^N$ completed-course masks. Computing availability scans $N$ courses per reachable mask, contributing $O(N2^N)$ time. Across all states, the number of selected-subset transitions is bounded by $O(3^N)$: each course is conceptually already completed, selected next, or outside that transition. Building one selected mask from its at-most-$N$ chosen bits costs $O(N)$ in the conservative bound, so total time is $O(N3^N)$.

The DP array stores one value for every mask and prerequisite storage holds $N$ masks, giving $O(2^N + N)$ space.

The benchmark defines size as $2^N$, the number of possible completion masks. Capacity-only instances make many course subsets reachable and force the exact-choice transition logic. A correct baseline that tests every mask of the full course universe for every reachable state performs an additional exponential factor and is rejected by scaling.

#### Alternatives and edge cases

- **Breadth-first search over masks:** process all states reachable in the same semester as one BFS layer. It explores the same transition graph and has comparable bounds, while the DP array makes relaxation and benchmarking straightforward.
- **Recursive memoized search:** return the minimum remaining semesters from `done`. It is equivalent, but iterative DP avoids recursion overhead and makes forward reachability explicit.
- **Greedy by out-degree or chain length:** a heuristic can choose the wrong subset when capacity binds because immediate unlock counts do not capture all later interactions.
- **Enumerate every subset of all courses:** remains correct after legality checks but wastes work on masks containing unavailable courses and has a larger practical exponential factor.
- **Take fewer than `k` when more are available:** never improves the result because an additional eligible course has no negative consequence.
- **One course:** exactly one semester is required, whether or not `k` is larger.
- **No relations:** the answer is $\lceil N/k \rceil$.
- **Capacity one:** every course requires its own semester, so the answer is $N$.
- **Long prerequisite chain:** prerequisites, rather than capacity, force one course per level.
- **Many courses unlock together:** enumerate choices only when their count exceeds `k`.
- **Transitive prerequisites:** direct prerequisite masks are sufficient because a direct prerequisite can be in `done` only after its own prerequisites were completed.
- **Course labels:** convert source labels `1..n` to bit positions `0..n-1` exactly once.
- **Same-semester dependency:** never compute eligibility from `done | take`; selected courses become completed only in the next state.
- **DAG guarantee:** no cycle-detection or impossible-result branch is required by the contract.

</details>
