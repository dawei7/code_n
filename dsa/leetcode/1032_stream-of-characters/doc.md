# Stream of Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1032 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Design, Trie, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/stream-of-characters/) |

## Problem Description

### Goal

Design a `StreamChecker` that is initialized with an array of lowercase English words. Characters then arrive one at a time through calls to `query(letter)`, and every new letter is appended to the stream seen so far.

For each query, return `true` if some non-empty suffix of the current stream is exactly one of the configured words. Otherwise, return `false`. Each answer must reflect all letters received up to that call while preserving the same initialized checker.

### Function Contract

**Inputs**

- `words`: an array of $D$ lowercase words, where $1 \le D \le 2000$ and every word length is between $1$ and $200$.
- `queries`: the app-local sequence of $Q$ lowercase characters passed one by one to `query`, with at most $4\cdot10^4$ calls.
- Define
$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert
$$
and $W=\max_{w\in\texttt{words}}\lvert w\rvert$.

**Return value**

- The app-local `solve(words, queries)` adapter returns the $Q$ Boolean query results in order.
- The native artifact exposes `StreamChecker(words)` and `query(letter)` directly.

### Examples

**Example 1**

- Input: `words = ["cd","f","kl"], queries = ["a","b","c","d","e","f","g","h","i","j","k","l"]`
- Output: `[false,false,false,true,false,true,false,false,false,false,false,true]`
- Explanation: The stream ends with `"cd"` after `d`, with `"f"` after `f`, and with `"kl"` after `l`.

### Required Complexity

- **Time:** $O(S+QW)$
- **Space:** $O(S+W)$

<details>
<summary>Approach</summary>

#### General

**Reverse every dictionary word:** Insert characters from each word's end toward its beginning into a trie. A terminal marker records when the path read so far is a complete word. This converts suffix testing on the stream into prefix traversal in the reversed trie.

**Retain only relevant stream history:** No dictionary word is longer than $W$, so letters older than the newest $W$ characters cannot participate in a matching suffix. Store the recent stream in a deque whose maximum length is $W$.

**Walk backward after each query:** Append the new letter, begin at the trie root, and inspect retained characters from newest to oldest. A missing trie edge proves that no longer suffix can match. Reaching a terminal marker proves that the characters examined form a configured word and allows an immediate `true` result.

Every reported match follows a reversed trie path ending at a terminal, so it is exactly a dictionary word and a suffix of the current stream. Conversely, any matching suffix has length at most $W$ and remains in the deque; reversing its characters follows its inserted trie path to a terminal, so it cannot be missed.

#### Complexity detail

Building the reversed trie visits all $S$ dictionary characters. Each of the $Q$ queries examines at most $W$ retained characters, giving $O(S+QW)$ total time. The trie contains at most $S+1$ nodes, and the deque holds at most $W$ characters, for $O(S+W)$ space.

#### Alternatives and edge cases

- **Check every word after every query:** Test whether the current stream ends with each dictionary word. This can take $O(QS)$ time and repeats shared suffix work.
- **Aho-Corasick automaton:** Failure links process each new character in amortized $O(1)$ time after preprocessing, but the construction is more involved.
- **Single-character word:** Its matching query can return `true` immediately without older stream characters.
- **Overlapping words:** A shorter terminal may occur before a longer terminal on the same reversed path; either is sufficient.
- **Stream shorter than a word:** Traversal simply ends without a terminal and returns `false`.
- **Bounded history:** Discarding characters beyond $W$ is safe because no possible answer can use them.

</details>
