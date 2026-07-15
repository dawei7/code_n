# Pairs of Songs With Total Durations Divisible by 60

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1010 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/) |

## Problem Description

### Goal

You are given a list of songs where `time[i]` is the duration, in seconds, of song `i`.

Return the number of index pairs `i`, `j` with $i<j$ whose total duration is divisible by `60`. Equivalently, count every pair satisfying `(time[i] + time[j]) % 60 == 0`; pairs are distinguished by their indices even when durations are equal, and the same song cannot be used twice.

### Function Contract

**Inputs**

- `time`: an array of $N$ song durations, where $1\le N\le6\cdot10^4$ and $1\le\texttt{time[i]}\le500$.

**Return value**

- The number of index pairs whose two durations sum to a multiple of `60`.

### Examples

**Example 1**

- Input: `time = [30, 20, 150, 100, 40]`
- Output: `3`
- Explanation: The valid index pairs have duration sums `180`, `120`, and `60`.

**Example 2**

- Input: `time = [60, 60, 60]`
- Output: `3`
- Explanation: Each of the three index pairs totals `120` seconds.

**Example 3**

- Input: `time = [10, 50, 90, 30]`
- Output: `2`
- Explanation: Remainders `10` and `50` pair, and the two remainder-`30` songs pair.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce durations to remainders:** Divisibility by `60` depends only on each duration modulo `60`. Keep a fixed 60-entry array in which `counts[r]` records how many earlier songs have remainder `r`.

**Count a pair when its later index arrives:** For the current `remainder`, an earlier song must have remainder `(60 - remainder) % 60`. Add that bucket's current count to the answer, then increment `counts[remainder]`. Updating after counting ensures every pair is counted once with its earlier index already stored and prevents pairing a song with itself.

**Handle self-complementary remainders naturally:** Remainders `0` and `30` complement themselves. The same lookup still works: each new song contributes the number of earlier songs in its own bucket, producing all distinct index pairs without special-case formulas.

For any valid pair, when its later song is processed, the earlier remainder is present in exactly the required complement bucket, so the pair is counted. Conversely, every added bucket entry forms a sum congruent to zero modulo `60`; therefore no invalid or duplicate pair enters the answer.

#### Complexity detail

Each of the $N$ durations performs constant-time remainder, lookup, and update operations, giving $O(N)$ time. The 60 counters occupy a fixed amount of memory independent of $N$, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Check every pair:** Two nested index loops are direct and correct but require $O(N^2)$ time.
- **Count first, combine later:** A frequency pass followed by pairing complementary buckets is also $O(N)$ time and $O(1)$ space, with separate combination formulas for remainders `0` and `30`.
- **One song:** No index pair exists, so return zero.
- **Repeated durations:** Equal values at different indices form distinct pairs when their sum is divisible by `60`.
- **Multiples of 60:** They pair only with other remainder-`0` durations.

</details>
