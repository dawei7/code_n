# Active Parallel Package Preflights

Updated: 2026-07-29

These briefs were produced by read-only parallel workers. They are preparation,
not package completion or Accepted evidence. Before authoring each package, the
main agent must refetch the live source, confirm that the identity and content
hash still match, create the exact native candidate, and obtain remote Accepted
evidence in numeric frontend-ID order. Package edits, submissions, global
audits, and handoff updates remain centralized in the main agent.

Per the user's 2026-07-29 directive, this is now a historical read-only file.
Do not spawn or resume subagents to extend it; the active agent performs every
remaining preflight and package workflow directly.

## 3833 — Count Dominant Indices

### Identity and live structure

- Package: `dsa/leetcode/3833_count-dominant-indices`
- Public Easy algorithms problem; internal question ID `4214`.
- Title slug: `count-dominant-indices`.
- Live content SHA-256:
  `70d17123aa7dcc376b45cfba914aac4141b93a9cb51ad2b6aa6bcb60697c23d9`.
- Native Python 3 declaration:
  `Solution.dominantIndices(self, nums: List[int]) -> int`.
- Source order: Description, Note, Examples, Constraints. Use
  `reference/note.md` before `reference/examples.md`.
- Two explained examples, two constraints, and no source tables, images, or
  diagrams.

An index $i$ is dominant when `nums[i]` is strictly greater than the average of
all elements strictly to its right. The source defines average as sum divided
by element count. Its standalone Note says the rightmost element is never
dominant because its right suffix is empty.

Exact example facts:

- `[5,4,3] -> 2`: index 0 satisfies $5 > (4+3)/2 = 3.5$; index 1
  dominates `[3]`; index 2 has no element to its right.
- `[4,1,2] -> 1`: index 0 dominates `[1,2]`; index 1 does not; index 2
  has an empty right suffix.

Constraints, in order:

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

### Candidate and evidence plan

Scan from right to left while maintaining `right_sum` and `right_count`.
Initialize them with the rightmost value and count one. For each earlier index,
count it exactly when `nums[i] * right_count > right_sum`, then extend the
suffix summary. This exact integer comparison implements strict greater-than
without floating point. Expected bounds are $O(N)$ time and $O(1)$ space.

Important cases include a singleton; increasing, decreasing, and all-equal
arrays; strict equality with the suffix average; and `[6,10,1]`, where 6 is
above the suffix average even though it is not above every suffix element.
Recommended legal benchmark tiers are descending arrays of lengths 8, 32, and
100 with expected answer $N-1$. An independent forward suffix-sum scan should
pass. Recomputing each suffix sum is the principal $O(N^2)$ control and must be
calibrated to fail only scaling.

## 3834 — Merge Adjacent Equal Elements

### Identity and live structure

- Package: `dsa/leetcode/3834_merge-adjacent-equal-elements`
- Public problem; internal question ID `4213`.
- Live content SHA-256:
  `9fc3270c44f40eb63669bdac0e18aa0aae2c29288f671b887522f928863ab3b7`.
- Native Python 3 declaration:
  `Solution.mergeAdjacent(self, nums: List[int]) -> List[int]`.
- Source order: Description, Examples, Constraints.
- Three explained examples, two constraints, and no tables, images, diagrams,
  notes, or follow-up.

The operation must always merge the **leftmost** adjacent equal pair, replacing
it by their sum, until no equal neighbors remain. Preserve these exact example
facts:

- `[3,1,1,2] -> [3,4]`, with intermediate array `[3,2,2]`.
- `[2,2,4] -> [8]`, with intermediate array `[4,4]`.
- `[3,7,5] -> [3,7,5]` because no operation applies.

Constraints, in order:

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

### Candidate and evidence plan

Use an output stack. For each input value, repeatedly merge it with the stack
top while they are equal, then push the resulting value. This realizes the
source's leftmost reduction order in $O(N)$ amortized time and $O(N)$ space.
Merging preserves total sum, so fixed-width implementations need 64-bit values;
the result can reach $10^{10}$.

The stack method matched literal leftmost simulation on all 87,380 arrays of
lengths one through eight over values one through four. Preserve cases such as
`[2,1,1] -> [4]`, `[1,1,2,2] -> [4,2]`, and
`[8,4,2,1,1] -> [16]`; the second case catches an illegal right-pair-first
implementation. Proposed tiers use 512, 4,096, and 32,768 copies of `100000`,
with one summed output. Literal repeated scanning and reconstruction is the
quadratic control; calibrate it in the repository runner.

## 3835 — Count Subarrays With Cost Less Than or Equal to K

### Identity and live structure

- Package:
  `dsa/leetcode/3835_count-subarrays-with-cost-less-than-or-equal-to-k`
- Public Medium algorithms problem; internal question ID `4211`.
- Live content SHA-256:
  `32c3ca3508596df2e3795930561f9ba57a8e09b6a0407cc7f4a39b4ed1afbda9`.
- Native Python 3 declaration:
  `Solution.countSubarrays(self, nums: List[int], k: int) -> int`.
- Source order: Description, Examples, Constraints. Three live hints are outside
  the statement and must not become Reference sections.
- Three explained examples, three constraints, and no tables, images, or
  diagrams.

For nonempty `nums[l..r]`, cost is

$$
(\max(\texttt{nums}[l..r])-\min(\texttt{nums}[l..r]))(r-l+1).
$$

Count subarrays whose cost is at most `k`. Preserve every source calculation:

- `[1,3,2], k = 4 -> 5`. In source order, costs are `[0..0]: 0`,
  `[0..1]: 4`, `[0..2]: 6`, `[1..1]: 0`, `[1..2]: 2`, and
  `[2..2]: 0`; exactly five are at most four.
- `[5,5,5,5], k = 0 -> 10`. Every subarray has equal minimum and maximum,
  hence zero cost; all qualify; a length-four array has
  $(4\cdot5)/2=10$ subarrays.
- `[1,2,3], k = 0 -> 3`. Only the three singleton subarrays have zero cost.

Constraints, in order:

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= k <= 10^15`

### Candidate and evidence plan

Maintain a sliding window with a decreasing index deque for its maximum and an
increasing index deque for its minimum. Expand `right`; while range times
current length exceeds `k`, evict a deque front if its index leaves and advance
`left`. Once valid, add `right-left+1` because valid starts for a fixed end form
one suffix. Every index enters and leaves each deque at most once, giving
$O(N)$ time and $O(N)$ worst-case space. Use 64-bit cost and answer arithmetic
outside Python.

The candidate matched a quadratic oracle on 458,724 combinations: every array
over values one through four through length seven and every `k` from 0 through
20. Cases must cover exact equality, `k=0` equal-value runs, duplicate extrema,
multi-step shrinking, recovery after an outlier, and $10^9$ values.

Legal tiers use increasing `nums=[1..N]`. Let $t=N/4$ and
`k=t*(t-1)`; qualifying lengths are one through $t$, so the expected count is
$tN-t(t-1)/2$. Use `(N,t,k,answer)` values `(32,8,56,228)`,
`(128,32,992,3600)`, and `(512,128,16256,57408)`. Endpoint expansion with
maintained extrema is the correct $O(N^2)$ control; the largest tier was chosen
to remain below the traced safety cap.

## 3836 — Maximum Score Using Exactly K Pairs

### Identity and live structure

- Package: `dsa/leetcode/3836_maximum-score-using-exactly-k-pairs`
- Public Hard algorithms problem; internal question ID `4202`.
- Live content SHA-256:
  `9df705bb5f64aba51ad82cec872d47669674d227910c39b2abe4055ad91b4524`.
- Native Python 3 declaration:
  `Solution.maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int`.
- Source order: Description, Examples, Constraints. Three live hints are outside
  the statement.
- Three explained examples, four constraints, and no tables, images, or
  diagrams.

Choose exactly $k$ pairs with two independently strict index chains,
$i_1<\cdots<i_k$ in `nums1` and $j_1<\cdots<j_k$ in `nums2`. Pair score is
`nums1[i] * nums2[j]`; maximize the total.

Exact examples:

- `[1,3,2]`, `[4,5,1]`, `k=2 -> 22`: pairs `(1,0)` and `(2,1)`
  contribute $3\cdot4=12$ and $2\cdot5=10$.
- `[-2,0,5]`, `[-3,4,-1,2]`, `k=2 -> 26`: pairs `(0,0)` and
  `(2,1)` contribute $6$ and $20$.
- `[-3,-2]`, `[1,2]`, `k=2 -> -7`: products are $-3$ and $-4$.

Constraints, in order:

- `1 <= n == nums1.length <= 100`
- `1 <= m == nums2.length <= 100`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`
- `1 <= k <= min(n,m)`

### Candidate and evidence plan

Use rolling prefix/count DP, swapping arrays so the shorter one is the column
dimension. Let `previous[t][j]` be the best score after the processed prefix of
the left array, using exactly `t` pairs and the first `j` right values. Set
count-zero states to zero and all positive unreachable counts to a true
negative sentinel. The three transitions skip the current left value, skip the
current right value, or add their product to `previous[t-1][j-1]`. The diagonal
source enforces strict order and prevents reuse. Bounds are $O(nmk)$ time and
$O(k\min(n,m))$ space.

This DP matched brute force on 46,314 exhaustive cases with lengths through
four, values in `{-2,0,3}`, and every legal `k`. Cases must force negative
exact-count results, disallow crossing high products, require skips in both
arrays, cover zeros, and reach positive and negative 64-bit-scale totals.

Define benchmark size as $W=nmk$. Use all-one square arrays with
`(n,m,k)=(6,6,3)`, `(12,12,6)`, and `(24,24,12)`, giving sizes 108,
864, and 6,912 and answers 3, 6, and 12. A full 3-D prefix DP is the independent
required-time control. A correct endpoint DP that rescans every predecessor is
the principal slower class; the largest proposed tier had 846,967 traced line
events, below the benchmark safety cap.

## 3837 — Delayed Count of Equal Elements

### Identity and live structure

- Package: `dsa/leetcode/3837_delayed-count-of-equal-elements`
- Premium problem; authenticated access succeeded; internal question ID `4228`.
- Live content SHA-256:
  `2df0fb447b0274e29057af32c0806604cc658dc19600db5f33bdd27e4b62d142`.
- Native Python 3 declaration:
  `Solution.delayedCount(self, nums: List[int], k: int) -> List[int]`.
- Source order: Description, Examples, Constraints.
- Two explained examples, three constraints, two source tables, and no images
  or diagrams.

For each index $i$, `ans[i]` counts indices $j$ satisfying both
`i + k < j <= n - 1` and `nums[j] == nums[i]`. The first inequality is strict.

Preserve the complete six-column source tables (`i`, `nums[i]`, possible `j`,
`nums[j]`, satisfying indices, `ans[i]`):

- `[1,2,1,1], k=1 -> [2,0,0,0]`. Rows are
  `0 | 1 | [2,3] | [1,1] | [2,3] | 2`,
  `1 | 2 | [3] | [1] | [] | 0`, and empty candidate/satisfying lists for
  indices 2 and 3, both with answer 0. Preserve the concluding result.
- `[3,1,3,1], k=0 -> [1,1,0,0]`. Rows are
  `0 | 3 | [1,2,3] | [1,3,1] | [2] | 1`,
  `1 | 1 | [2,3] | [3,1] | [3] | 1`,
  `2 | 3 | [3] | [1] | [] | 0`, and the empty final row for index 3.
  Preserve the concluding result.

Constraints, in order:

- `1 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `0 <= k <= n - 1`

### Candidate and evidence plan

Scan indices in reverse with a frequency map for the currently eligible suffix.
At index `i`, first expose `p=i+k+1` when it is in bounds, then read the map
count of `nums[i]`. Moving one step left exposes exactly one new eligible
position, so the map represents precisely the indices strictly beyond the
delay. Expected bounds are $O(N)$ time and $O(N)$ space under expected hash
behavior.

The method matched a quadratic oracle on all 73,812 inputs formed by arrays
over values one through three through length eight and every legal `k`. Cases
must cover `k=0`, all equal values, `k=n-1`, all distinct values, strict
boundary exclusion, duplicates only inside the excluded gap, and value bounds.

Preliminary tiers use all-equal arrays with `k=0` at lengths 512, 2,048, and
8,192, with expected output `[N-1,N-2,...,0]`. A forward frequency-removal scan
is the independent $O(N)$ control. Suffix slicing plus `.count` is the intended
$O(N^2)$ control; calibrate in the real runner and reduce the largest tier if
paired trials become excessive while retaining at least a fourfold total span.
