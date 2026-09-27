# Guided Example: Summary Ranges

We trace the step-by-step contiguous interval expansion, gap detection, and formatted range emission on representative sorted integer arrays:

- **Input:** $\text{nums} = [0, 1, 2, 4, 5, 7]$
- **Required output:** `["0->2", "4->5", "7"]`
- **Multiple Disjoint Singletons Instance:** $\text{nums} = [0, 2, 3, 4, 6, 8, 9] \implies \text{["0", "2->4", "6", "8->9"]}$
- **Single Element Instance:** $\text{nums} = [1] \implies \text{["1"]}$
- **All Consecutive Instance:** $\text{nums} = [1, 2, 3, 4] \implies \text{["1->4"]}$
- **Empty Array Instance:** $\text{nums} = [] \implies []$

This instance demonstrates two-pointer contiguous run grouping on sorted unique integers, proves why checking $\text{nums}[j+1] == \text{nums}[j] + 1$ cleanly separates connected ranges from gaps, details singleton vs interval string formatting, and runs in strictly $O(N)$ time with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a sorted array of unique integers:
$$
\text{nums} = [0, 1, 2, 4, 5, 7]
$$
Partition the numbers into the minimal set of contiguous ranges $[a, b]$ that cover all elements without gaps:
- Range 1: $\{0, 1, 2\}$ forms contiguous block $[0, 2] \implies \text{"0->2"}$.
- Integer $3$ is absent from `nums`, creating a gap between $2$ and $4$.
- Range 2: $\{4, 5\}$ forms contiguous block $[4, 5] \implies \text{"4->5"}$.
- Integer $6$ is absent, creating a gap between $5$ and $7$.
- Range 3: $\{7\}$ stands alone as a singleton $[7, 7] \implies \text{"7"}$.
Output: `["0->2", "4->5", "7"]`.

The algorithm must linearly group consecutive elements ($x, x+1, x+2, \dots$) without repeatedly rescanning indices or using extra memory.

---

## 2. Conceptual Foundation & Invariants

### Two-Pointer Linear Scanning Protocol
Initialize output list $\text{result} = []$ and start index $i = 0$.
While $i < N$:
1. **Initialize Run Boundary:**
   Set end pointer $j = i$.
2. **Expand While Consecutive:**
   While $j + 1 < N$ and $\text{nums}[j + 1] == \text{nums}[j] + 1$:
   $$
   j \leftarrow j + 1
   $$
3. **Format Range String:**
   - If $i == j$ (single isolated element):
     $$
     \text{result}.\text{append}(\text{str}(\text{nums}[i]))
     $$
   - If $i < j$ (multi-element contiguous range):
     $$
     \text{result}.\text{append}(\text{f"}\{\text{nums}[i]\}\text{->}\{\text{nums}[j]\}\text{"})
     $$
4. **Advance to Next Run:**
   $$
   i \leftarrow j + 1
   $$

> **Invariant.** For each range $[i, j]$, for all $k \in [i, j - 1]$, $\text{nums}[k + 1] - \text{nums}[k] == 1$, and either $j == N - 1$ or $\text{nums}[j + 1] - \text{nums}[j] > 1$.

---

## 3. Step-by-Step Worked Execution

We trace the traversal on $\text{nums} = [0, 1, 2, 4, 5, 7]$ ($N = 6$):

### Run 1 (Starts at $i = 0$, $\text{nums}[0] = 0$):
- Start with $j = 0$.
- Test $j = 0$: $j + 1 = 1 < 6$, and $\text{nums}[1] = 1 == \text{nums}[0] + 1$ ($0 + 1$). Match! Advance $j \leftarrow 1$.
- Test $j = 1$: $j + 1 = 2 < 6$, and $\text{nums}[2] = 2 == \text{nums}[1] + 1$ ($1 + 1$). Match! Advance $j \leftarrow 2$.
- Test $j = 2$: $j + 1 = 3 < 6$, but $\text{nums}[3] = 4 \ne \text{nums}[2] + 1$ ($2 + 1 = 3$). **Gap detected!**
- Run finishes at $[i = 0, j = 2]$.
- Since $i \ne j$, format as `"0->2"`.
- Append `"0->2"` to $\text{result}$.
- Advance $i \leftarrow j + 1 = 3$.

---

### Run 2 (Starts at $i = 3$, $\text{nums}[3] = 4$):
- Start with $j = 3$.
- Test $j = 3$: $j + 1 = 4 < 6$, and $\text{nums}[4] = 5 == \text{nums}[3] + 1$ ($4 + 1$). Match! Advance $j \leftarrow 4$.
- Test $j = 4$: $j + 1 = 5 < 6$, but $\text{nums}[5] = 7 \ne \text{nums}[4] + 1$ ($5 + 1 = 6$). **Gap detected!**
- Run finishes at $[i = 3, j = 4]$.
- Since $i \ne j$, format as `"4->5"`.
- Append `"4->5"` to $\text{result}$.
- Advance $i \leftarrow j + 1 = 5$.

---

### Run 3 (Starts at $i = 5$, $\text{nums}[5] = 7$):
- Start with $j = 5$.
- Test $j = 5$: $j + 1 = 6 \not< 6$ (End of array reached).
- Run finishes at $[i = 5, j = 5]$.
- Since $i == j$, format as singleton `"7"`.
- Append `"7"` to $\text{result}$.
- Advance $i \leftarrow j + 1 = 6$.

Loop terminates ($i = 6 == N$).
Final output: `["0->2", "4->5", "7"]`.

---

## 4. Complete Execution Trace

```text
nums = [0, 1, 2, 4, 5, 7]

Run 1: i=0 (0) -> nums[1]=1 (ok), nums[2]=2 (ok), nums[3]=4 (gap!)
       Range: [0, 2] -> Format: "0->2"
       i advances to 3

Run 2: i=3 (4) -> nums[4]=5 (ok), nums[5]=7 (gap!)
       Range: [3, 4] -> Format: "4->5"
       i advances to 5

Run 3: i=5 (7) -> end of array
       Range: [5, 5] -> Format: "7"
       i advances to 6

Result: ["0->2", "4->5", "7"]
```

| Iteration | Start Index $i$ | End Index $j$ | Subarray Slice | Span Condition | Formatted String | Emitted Result List |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | **0** | **2** | `[0, 1, 2]` | Consecutive | `"0->2"` | `["0->2"]` |
| **2** | **3** | **4** | `[4, 5]` | Consecutive | `"4->5"` | `["0->2", "4->5"]` |
| **3** | **5** | **5** | `[7]` | Singleton | `"7"` | **`["0->2", "4->5", "7"]`** |

### 4.1 Every Adjacency Test Performed by This Instance

The pointer trace records where the runs end, but not what decided it. Listing
every adjacency comparison makes the boundary rule explicit: the run continues
exactly when the successor is larger by one, and the *size* of a gap never
matters, only its existence.

| Index compared $j$ | Left value $\text{nums}[j]$ | Right value $\text{nums}[j+1]$ | Difference | Test outcome | Consequence |
|:---:|:---:|:---:|:---:|:---|:---|
| 0 | 0 | 1 | 1 | Equal to 1, so the run extends | $j$ advances from 0 to 1 |
| 1 | 1 | 2 | 1 | Equal to 1, so the run extends | $j$ advances from 1 to 2 |
| 2 | 2 | 4 | 2 | Not 1, so the run closes | Emit `"0->2"`; next start becomes $i = 3$ |
| 3 | 4 | 5 | 1 | Equal to 1, so the run extends | $j$ advances from 3 to 4 |
| 4 | 5 | 7 | 2 | Not 1, so the run closes | Emit `"4->5"`; next start becomes $i = 5$ |
| 5 | 7 | - | - | No successor exists | Run closes at the array end; emit `"7"` |

Rows 2 and 4 are the two closed runs, and both close for the same reason: a
difference of 2 rather than 1. This is why the algorithm never needs to compare
a difference against a threshold or inspect how many integers are missing. The
last row shows that the right boundary of the array is the second way a run can
end, and it must be handled without reading past the final element.

### 4.2 Boundary and Trap Instances

The authored trials probe conditions the main instance cannot show. Each one
lands on a distinct branch of the protocol.

| Trial input | Why it is interesting | Run boundaries found | Output | Rule that decides the outcome |
|:---|:---|:---|:---|:---|
| `[]` | The outer loop must not execute at all | none | `[]` | The guard $i < N$ fails immediately, so no formatting branch is reachable |
| `[1]` | Exactly one element and no successor to compare | $[0, 0]$ | `["1"]` | The successor test short-circuits on $j + 1 < N$, and $i == j$ selects the singleton form |
| `[1, 2, 3, 4]` | The whole array is one run | $[0, 3]$ | `["1->4"]` | The run is extended at every index and never closed early |
| `[-4, -3, -1, 0, 1, 5]` | Negative values, unequal gap sizes, and a run whose start is negative | $[0, 1], [2, 4], [5, 5]$ | `["-4->-3", "-1->1", "5"]` | Differences of 1 keep $-4$ with $-3$ and $-1$ with $0$ and $1$; the jump from $-3$ to $-1$ has difference 2 and closes the first run |

The negative trial deserves one more observation. Its middle run `-1->1` crosses
zero, yet the only test applied is $-1 + 1 = 0$ and then $0 + 1 = 1$, both of
which match. The sign of the endpoints plays no role in the boundary decision; it
matters only when each endpoint is converted to text, and the hyphen that opens
`"-4->-3"` is the number's sign rather than the range separator.

---

## 5. Algorithmic Correctness

**Soundness.** A formatted range `"a->b"` is generated only when all integers from $a$ to $b$ exist consecutively in the array. Since the array is strictly sorted and unique, every integer between $\text{nums}[i]$ and $\text{nums}[j]$ is covered with no missing values. When a gap occurs ($\text{nums}[j+1] > \text{nums}[j] + 1$), terminating the range prevents covering values not present in `nums`.

**Completeness.** The outer loop covers all indices from $0$ to $N - 1$. Each element belongs to exactly one maximal consecutive run, ensuring every input element is partitioned into the output list.

---

## 6. Traps This Instance Exposes

- **Integer Overflow in Differences:** In languages like C++, computing `nums[j + 1] - nums[j] == 1` can overflow if numbers cross negative and positive 32-bit limits (e.g. $-2^{31}$ to $2^{31}-1$). Comparing `nums[j + 1] == nums[j] + 1` or using 64-bit integers avoids overflow.
- **Empty Array:** If `nums` is empty ($N = 0$), the outer loop `i < N` immediately terminates and returns `[]`.
- **Negative Integers:** Ranges with negative numbers (e.g. `[-3, -2, -1] \implies "-3->-1"`) must preserve the minus sign in string conversions.

### 6.1 Alternatives Compared on This Instance

| Approach | How the run is found | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---|
| Two pointers $i$ and $j$ (traced above) | $j$ walks forward while the next value is exactly one larger | $O(N)$ | $O(1)$ | Chosen. Each element is compared once as a left neighbour and at most once as a right neighbour |
| Single cursor with a remembered run start | One index advances; a stored start is emitted when the successor is not `+1` | $O(N)$ | $O(1)$ | Equivalent, but the run start must be flushed by the same terminal check, so the loop needs an extra end-of-array commit |
| Iterating every integer from $\min$ to $\max$ | Walk the value domain and test membership | $O(\max - \min)$ | $O(1)$ | Fails the complexity requirement whenever the values are sparse; on this instance it would scan $0$ through $7$ instead of six elements |
| Precomputing a membership set | Hash each value, then walk the domain or the array | $O(N)$ expected | $O(N)$ | Answers the same question while destroying the $O(1)$ auxiliary-space property; the sorted order is already sufficient |
| Comparing against a counter of expected successors | Track a running expectation instead of reading the next element | $O(N)$ | $O(1)$ | Correct only because the array is strictly increasing and unique; a duplicate value would break the expectation |

The decisive phrase in the chosen method is *exactly one larger*. Every
alternative above either relaxes that test (the domain walk, the set) and pays in
time or space, or keeps it but adds bookkeeping (the single cursor). None of the
alternatives is faster, which is why the two-pointer form is the one worth
remembering.

### 6.2 Formatting the Emitted String

The two output forms are not a cosmetic detail; they encode whether the run has
more than one element.

| Run boundaries | Run length | Invariant relation | Emitted form | Instance | Trap if inverted |
|:---:|:---:|:---|:---|:---|:---|
| $[0, 2]$ | 3 | $i < j$ | `"0->2"` | `[0, 1, 2]` | Printing `"0->0"` invents a range where the problem wants a bare number |
| $[3, 4]$ | 2 | $i < j$ | `"4->5"` | `[4, 5]` | Omitting the arrow would collapse a real interval into one endpoint |
| $[5, 5]$ | 1 | $i == j$ | `"7"` | `[7]` | Printing `"7->7"` is a range of length one, which the expected output rejects |
| $[0, 1]$ | 2 | $i < j$ | `"-4->-3"` | `[-4, -3]` | Emitting without signs produces a wrong range; the separator must remain distinguishable from a minus sign |

The condition to test is equality of the two indices, not equality of the two
values. A run of length one has $i == j$ by construction; a run whose endpoints
happen to be equal cannot exist because the input is strictly increasing. That is
why `i == j` is a sound and complete discriminator between the two output forms.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of integers in `nums`. Both pointers $i$ and $j$ move strictly forward from $0$ to $N$. Each element is visited at most twice.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory (ignoring the space required for the output string list).
