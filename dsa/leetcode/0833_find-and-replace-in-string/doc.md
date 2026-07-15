# Find And Replace in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 833 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-and-replace-in-string/) |

## Problem Description
### Goal
You are given a 0-indexed string `s` and three 0-indexed parallel arrays, `indices`, `sources`, and `targets`, each containing $k$ entries. Operation $i$ examines the original string at `indices[i]`. If `sources[i]` occurs there as a substring, that occurrence must be replaced by `targets[i]`; otherwise, that operation makes no change.

All operations occur simultaneously, so one replacement must not shift the position used by another. The input guarantees that replacements which occur do not overlap. A substring is a contiguous sequence of characters. Return the string produced after every applicable replacement has been performed on `s`.

### Function Contract
**Inputs**

- `s`: the original lowercase English string, with $1 \leq \lvert s \rvert \leq 1000$.
- `indices`: $k$ starting positions in the original string.
- `sources`: $k$ nonempty lowercase strings to test at the corresponding positions.
- `targets`: $k$ nonempty lowercase replacement strings.
- The parallel arrays have equal length, with $1 \leq k \leq 100$; every source and target has length from $1$ through $50$.
- Define the total represented text size as

$$
C = \lvert s \rvert + \sum_{i=0}^{k-1}\left(\lvert \texttt{sources}[i] \rvert + \lvert \texttt{targets}[i] \rvert\right).
$$

**Return value**

Return the resulting string after applying every source that matches at its specified index in the original `s`.

### Examples
**Example 1**

- Input: `s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]`
- Output: `"eeebffff"`

Both sources match their original positions, so both replacements occur.

**Example 2**

- Input: `s = "abcd", indices = [0, 2], sources = ["ab", "ec"], targets = ["eee", "ffff"]`
- Output: `"eeecd"`

The first source matches. The second does not start at index `2`, so `"cd"` remains unchanged.

**Example 3**

- Input: `s = "abc", indices = [1], sources = ["b"], targets = ["xyz"]`
- Output: `"axyzc"`

### Required Complexity
- **Time:** $O(C)$
- **Space:** $O(C)$

<details>
<summary>Approach</summary>

#### General

**Validate against one immutable coordinate system**

Every match must be checked in the original `s`. First inspect each parallel operation with `s.startswith(source, index)`. Record only successful operations in a map keyed by their original starting index. Nothing has been edited yet, so a longer or shorter target cannot disturb any later test. The non-overlap guarantee means that two recorded replacements never compete for the same consumed character.

**Reconstruct without shifting indices**

Walk a cursor from left to right over the original string. If no successful operation starts at the cursor, append that one original character and advance by one. If a recorded operation starts there, append its target and advance by the length of its source. Thus the cursor always denotes an original-string index, even though the output may grow or shrink.

Each original position is handled exactly once by this reconstruction. A recorded source has already been confirmed at its start, and advancing over its full length removes precisely the occurrence that must be replaced. Characters outside successful source intervals are copied unchanged and in order, so the joined pieces are exactly the simultaneous-replacement result.

#### Complexity detail

Checking all sources costs the sum of their lengths in the worst case. The reconstruction scans at most $\lvert s \rvert$ original characters, and joining the pieces writes the final output, whose length is bounded by $C$. Therefore total time is $O(C)$. The successful-operation map, output pieces, and returned string together use $O(C)$ space.

#### Alternatives and edge cases

- **Sort operations and splice from right to left:** Descending indices preserve the remaining original coordinates, but repeatedly forming immutable strings can copy almost the whole current string for each of the $k$ operations, leading to $O(kC)$ time.
- **Sort and stream with a source cursor:** A sorted valid-operation list can also reconstruct the answer correctly, but sorting costs $O(k \log k)$ instead of using direct indexed lookup.
- **Failed source match:** An operation whose source differs at any character makes no change, even if its target text would help another operation match.
- **Simultaneous semantics:** Matches are determined from the original `s`, never from text inserted by an earlier replacement.
- **Variable replacement lengths:** A target may be shorter or longer than its source; only the cursor over the original string advances by the source length.
- **Boundary replacements:** A successful source may begin at index `0` or end at the final character, leaving an empty unchanged prefix or suffix.

</details>
