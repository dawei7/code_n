# Reorder Data in Log Files

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 937 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [reorder-data-in-log-files](https://leetcode.com/problems/reorder-data-in-log-files/) |

## Problem Description

### Goal

Each string in `logs` contains space-delimited tokens. Its first token is an identifier, followed by at least one content word. A letter-log has only lowercase English letters in its content, while a digit-log has only digits there.

Reorder the logs so every letter-log comes before every digit-log. Sort letter-logs lexicographically by their complete content; when two contents are equal, sort those logs by identifier. Digit-logs must preserve their original relative order. Return the resulting list of unchanged log strings.

### Function Contract

**Inputs**

- `logs`: between $1$ and $100$ valid log strings, each with length from $3$ through $100$ and tokens separated by single spaces.

Let $S$ be the total number of characters, $L$ the number of letter-logs, and $C$ the maximum log length.

**Return value**

Return all original log strings in the required letter-log order followed by digit-logs in stable input order.

### Examples

**Example 1**

- Input: `logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]`
- Output: `["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]`

**Example 2**

- Input: `logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]`
- Output: `["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]`

### Required Complexity

- **Time:** $O(S + LC\log L)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Split identifier from content once.** For each log, call the first-space split so the identifier and untouched remainder are available. The first character of the content determines its type because every content is guaranteed to contain either only letter words or only digit words.

**Separate the two ordering rules.** Append digit-logs directly to a dedicated list in encounter order; never sort that list. For a letter-log, store a key containing `(content, identifier)` together with the original string. Sorting these records uses the entire content first and the identifier only as the specified tie-breaker.

**Concatenate after sorting letters.** Extract the original strings from the sorted letter records and append the stable digit list. Classification is exhaustive, the tuple key exactly matches the required lexicographic rules, and preserving digit insertion order proves their relative order is unchanged.

#### Complexity detail

Parsing and storing all text takes $O(S)$ time. Sorting $L$ letter keys performs $O(L\log L)$ comparisons, each potentially examining $O(C)$ characters, so total time is $O(S + LC\log L)$. Parsed keys and the result retain $O(S)$ characters.

#### Alternatives and edge cases

- **Single mixed sort key:** Give letter-logs a key beginning with `0` and digit-logs a key beginning with `1` plus their original index. This is correct but unnecessarily sorts digit-logs too.
- **Insertion sort for letters:** It preserves the rules but can require $O(L^2C)$ time on reverse-ordered input.
- **Equal letter content:** Compare identifiers lexicographically; input order is not the tie-breaker.
- **Digit identifiers:** Only content determines the log type; an identifier may contain letters or digits.
- **All digit-logs:** Return the input order unchanged.

</details>
