# Implement Rand10() Using Rand7()

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 470 |
| Difficulty | Medium |
| Topics | Math, Rejection Sampling, Randomized, Probability and Statistics |
| Official Link | [LeetCode](https://leetcode.com/problems/implement-rand10-using-rand7/) |

## Problem Description
### Goal
The provided `rand7()` API returns each integer from `1` through `7` independently with equal probability. Implement `rand10()` using only calls to that API and ordinary deterministic computation.

Each `rand10()` call must return an integer from `1` through `10`, with all ten outcomes exactly equally likely. Do not call another random API or use a language's built-in random API. Combine enough `rand7()` outcomes to create an equiprobable sample space, reject any excess states that would bias the mapping, and retry as needed. Successive calls must preserve the same uniform distribution; the app uses a deterministic stream only to verify control flow.

### Function Contract
**Inputs**

- `rand7_values`: the app's deterministic cyclic stream of values from 1 through 7, used in place of LeetCode's hidden random API
- `draws`: the number of `rand10` outputs to generate in the app trace

**Return value**

- The generated output list. The native artifact exposes `Solution.rand10()` with no arguments and calls LeetCode's provided `rand7()` directly.

### Examples
**Example 1**

- Input: `rand7_values = [1, 1], draws = 3`
- Output: `[1, 1, 1]`

**Example 2**

- Input: `rand7_values = [7, 7, 1, 2], draws = 2`
- Output: `[2, 2]`

**Example 3**

- Input: `rand7_values = [6, 5], draws = 1`
- Output: `[10]`

### Required Complexity

- **Time:** $O(draws)$
- **Space:** $O(draws)$

<details>
<summary>Approach</summary>

#### General

**Create 49 equally likely outcomes**

Call `rand7()` twice. Treat the first result minus one as a base-7 row and the second as a column, producing `cell = (first - 1) * 7 + second`. Independence and uniformity make every integer from 1 through 49 equally likely.

**Keep a multiple of ten outcomes**

Accept cells 1 through 40 and reject 41 through 49. Each residue class modulo 10 then has exactly four accepted cells, so `1 + (cell - 1) % 10` is uniform on 1 through 10. Mapping all 49 cells directly would bias nine outputs because 49 is not divisible by 10.

**Repeat only after rejection**

Rejected cells reveal no accepted output and are discarded before drawing a fresh independent pair. An attempt succeeds with probability $40/49$, so the expected attempts per result are $49/40$, a constant.

**Make randomized behavior testable in the app**

The app adapter reads authored `rand7_values` cyclically, which makes rejection paths and outputs deterministic. It runs the same cell construction and rejection logic as the native method; only the source of `rand7()` calls differs.

#### Complexity detail

Each output needs a constant expected number of attempts, so generating `draws` results takes expected $O(draws)$ time. The returned trace occupies $O(draws)$ space; one native `rand10()` call uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Recycle rejected entropy:** cells 41 through 49 can be combined with another `rand7()` call to reduce expected API calls, but the bookkeeping is more involved.
- **Generate a larger base-7 range:** using more calls and rejecting down to a multiple of ten remains unbiased with different efficiency.
- **Modulo all 49 cells:** is invalid because output frequencies are unequal.
- **Boundary cell 40:** is accepted and maps to 10.
- **Cells 41 through 49:** must trigger a fresh attempt rather than an output.
- **Independent calls:** the uniformity proof assumes each provided `rand7()` call is independent and uniform.
- **Deterministic app stream:** cycling is a test harness device, not part of the native randomized API.

</details>
