# Vowel Spellchecker

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 966 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [vowel-spellchecker](https://leetcode.com/problems/vowel-spellchecker/) |

## Problem Description

### Goal

Given a `wordlist`, correct every string in `queries` by applying three matching rules in strict priority order. An exact case-sensitive match returns the query itself. Otherwise, a case-insensitive match returns the first matching word from `wordlist`. If neither applies, treat each vowel—`a`, `e`, `i`, `o`, or `u`—as interchangeable after ignoring case; a match under that rule also returns the first corresponding word from `wordlist`.

Vowel replacement does not insert or delete characters, and consonants must still agree. If a query matches under none of the three rules, its answer is the empty string. Return the corrections in the same order as the queries.

### Function Contract

**Inputs**

- `wordlist`: between $1$ and $5000$ English-letter strings.
- `queries`: between $1$ and $5000$ English-letter strings to correct.
- Every string has length from $1$ through $7$.
- Define the total number of input characters as

$$
S = \sum_{w \in \texttt{wordlist}} \lvert w \rvert + \sum_{q \in \texttt{queries}} \lvert q \rvert.
$$

**Return value**

Return one correction per query, preserving query order and the original capitalization of the chosen `wordlist` entry.

### Examples

**Example 1**

- Input: `wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]`
- Output: `["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]`

**Example 2**

- Input: `wordlist = ["yellow"], queries = ["YellOw"]`
- Output: `["yellow"]`

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Build one lookup per precedence level.** Store every exact word in a set. Build a lowercase map from each case-insensitive key to its first `wordlist` entry. Build a vowel-error map similarly, using the lowercase word with every vowel replaced by `*` as its key. Insert with `setdefault` so later collisions never replace the required first match.

**Normalize vowel errors without changing structure.** The signature preserves every consonant and the string length while merging all five vowels. Therefore two words share a vowel-error key exactly when case can be ignored and each vowel position may be changed independently to another vowel; missing or extra letters cannot match.

**Resolve each query in priority order.** First test the original query in the exact set. If absent, test its lowercase key, then its vowel signature, and finally use `""`. Because each lower-priority lookup is attempted only after the earlier one fails, an available exact or capitalization match cannot be displaced by a vowel match.

#### Complexity detail

Creating keys and processing all words touches each of the $S$ input characters a constant number of times, so expected time is $O(S)$. The exact set, two maps, normalized keys, and result list use $O(S)$ space.

#### Alternatives and edge cases

- **Scan `wordlist` per query:** Perform three complete passes for exact, capitalization, and vowel matching. This preserves precedence but takes quadratic time in the list counts.
- **One combined map:** Assigning every key in a single namespace risks collisions between exact, lowercase, and vowel-normalized forms unless rule types are tagged explicitly.
- **Overwriting normalized keys:** Ordinary assignment returns the last matching word, violating the required first-match rule.
- **Exact match priority:** An exact later entry must beat an earlier case-insensitive or vowel-equivalent entry.
- **Different lengths:** Vowel errors replace characters only; they never insert or remove them.
- **No match:** Append an empty string while retaining the query's position in the output.

</details>
