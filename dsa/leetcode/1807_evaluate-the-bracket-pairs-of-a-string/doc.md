# Evaluate the Bracket Pairs of a String

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/) |
| Frontend ID | 1807 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The string `s` contains zero or more bracket pairs. Every pair encloses a non-empty key, as in `(name)` and `(age)` within `"(name)is(age)yearsold"`. Bracket pairs are properly closed and never nested, so each opening round bracket begins one complete key and its matching closing bracket ends it.

The array `knowledge` supplies known key-value associations. Each entry has the form `[key, value]`, and every key in this array is unique. Evaluate every bracket pair in `s`: replace the entire pair, including its brackets, with the associated value when its key is known, or with `"?"` when it is unknown. Lowercase letters outside brackets remain literal even if they spell a known key. Return the resulting string after all pairs have been evaluated.

### Function Contract

**Inputs**

- `s`: a string of lowercase English letters and round brackets, with $1 \le \lvert s \rvert \le 10^5$. Every opening bracket has a matching closing bracket, enclosed keys are non-empty, and pairs are not nested.
- `knowledge`: a list of at most $10^5$ two-string entries `[key, value]`. Every key is unique; keys and values contain from 1 through 10 lowercase English letters.
- Let $n = \lvert s \rvert$ and let

$$
k = \sum_{[\textit{key},\textit{value}] \in \texttt{knowledge}}
  \left(\lvert \textit{key} \rvert + \lvert \textit{value} \rvert\right).
$$

**Return value**

- Return a string in which every bracket pair has been replaced by its known value or by `"?"`, while all text outside bracket pairs retains its original order.

### Examples

**Example 1**

- Input: `s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]`
- Output: `"bobistwoyearsold"`

Both enclosed keys are known, so `(name)` becomes `"bob"` and `(age)` becomes `"two"`.

**Example 2**

- Input: `s = "hi(name)", knowledge = [["a","b"]]`
- Output: `"hi?"`

The key `"name"` is absent from `knowledge`.

**Example 3**

- Input: `s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]`
- Output: `"yesyesyesaaa"`

The same bracketed key may be evaluated repeatedly. The trailing unbracketed letters are not evaluated.

### Required Complexity

- **Time:** $O(n + k)$
- **Space:** $O(n + k)$

<details>
<summary>Approach</summary>

#### General

**Turn the knowledge list into direct lookups**

The input presents associations as a list, but repeatedly searching that list would revisit unrelated entries for every bracket pair. Build a hash map from each key to its value once. Uniqueness guarantees that no later entry can conflict with an earlier mapping.

**Scan literal text and keys in one direction**

Maintain an index into `s` and an output-parts list. When the current character is not `"("`, append it unchanged and advance once. At an opening bracket, find its guaranteed matching `")"`, slice out the non-empty key, and append either the map value or `"?"`. Resume immediately after the closing bracket. Because pairs are not nested, no stack or recursive parsing state is needed.

**Why every character receives the correct treatment**

Each scan step consumes either one literal character or one complete bracket pair, so the consumed regions are disjoint and cover all of `s` in order. Literal regions are copied exactly. For a bracket region, the hash map implements the specified known-key replacement, and its default implements the unknown-key rule. Concatenating the appended parts therefore produces precisely the fully evaluated string.

#### Complexity detail

Constructing the map reads $k$ knowledge characters. The forward scan examines the $n$ characters of `s` once apart from bounded hash work per key, and joining the result is also $O(n)$ because every replacement value has length at most 10 while every replaced pair consumes at least three input characters. Total time is $O(n + k)$. The map, output parts, and returned string occupy $O(n + k)$ space.

#### Alternatives and edge cases

- **Linear search through `knowledge`:** It avoids a map but can inspect all knowledge entries for every bracket pair, producing quadratic work when both counts grow.
- **Repeated whole-string replacement:** Replacing one key pattern at a time repeatedly scans and reallocates the string, and it still needs a separate pass for unknown keys.
- **Stack-based parsing:** A stack can match arbitrary nested delimiters, but nesting is forbidden here, so a direct closing-bracket search is simpler.
- **No bracket pairs:** Return `s` unchanged; the knowledge list may be empty or entirely unused.
- **Unknown key:** Replace the complete bracket pair with exactly one question mark, not with the key text or empty text.
- **Repeated key occurrence:** Reuse the same map entry for every occurrence without consuming or removing it.
- **Unbracketed matching text:** A literal key name outside round brackets is copied and never substituted.
- **Adjacent pairs:** After consuming one closing bracket, the next character may immediately open another pair; resuming at the following index handles this without a separator.

</details>
