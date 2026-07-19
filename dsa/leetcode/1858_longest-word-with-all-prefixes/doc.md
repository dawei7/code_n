# Longest Word With All Prefixes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1858 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Depth-First Search, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-word-with-all-prefixes/) |

## Problem Description
### Goal
You are given an array `words` containing lowercase English words. A word is
eligible when every nonempty prefix obtained by taking its first $1, 2, \ldots,
\lvert w \rvert$ characters also occurs as an element of `words`. Thus the word
itself must be present, as must the one-character word that begins its prefix
chain and every intermediate length.

Return the longest eligible word. When several eligible words have the same
maximum length, choose the lexicographically smallest one. If no input word has
all of its required prefixes, return the empty string.

### Function Contract
**Inputs**

- `words`: an array of between $1$ and $10^5$ nonempty strings. Every character
  is a lowercase English letter, each word has length at most $10^5$, and the
  total number of input characters is at most $10^5$.

Define the total input length as

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Return value**

A string: the longest word whose every nonempty prefix belongs to `words`,
breaking length ties lexicographically, or `""` if no such word exists.

### Examples
**Example 1**

- Input: `words = ["k","ki","kir","kira","kiran"]`
- Output: `"kiran"`

Every prefix along the chain from `"k"` through `"kiran"` is present.

**Example 2**

- Input: `words = ["a","banana","app","appl","ap","apply","apple"]`
- Output: `"apple"`

Both five-letter words have complete prefix chains, and `"apple"` is
lexicographically smaller than `"apply"`.

**Example 3**

- Input: `words = ["abc","bc","ab","qwe"]`
- Output: `""`

No one-letter word is present, so no word can begin a complete prefix chain.

### Required Complexity
- **Time:** $O(S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Represent every prefix once**

Insert every input word into a trie. Each trie edge consumes one character, and
mark the terminal node of each inserted word with that word. A root-to-node
path therefore represents one distinct prefix shared by every word that begins
with that path.

**Traverse only complete chains**

Start at the root and visit a child only when that child is a terminal node.
This restriction exactly encodes the requirement: reaching a node at depth
$d$ means that the nodes at depths $1$ through $d$ were all terminal, so every
nonempty prefix of the node's word occurs in the input. Conversely, every
eligible word has terminal nodes at all those depths, so this traversal cannot
skip it.

Use an explicit stack rather than recursive depth-first search. An individual
word may contain $10^5$ characters, which can exceed a language runtime's call
stack even though the trie itself is valid. Whenever a reachable terminal word
is longer than the current answer, replace the answer; on equal lengths,
replace it only when it is lexicographically smaller. Because every and only
eligible word is compared, the final selection satisfies both ordering rules.

#### Complexity detail

Trie insertion processes each of the $S$ input characters once. Traversal
examines at most every created edge once, so total time is $O(S)$. The trie has
at most $S+1$ nodes, and its child maps, terminal references, and explicit
stack use $O(S)$ auxiliary space.

#### Alternatives and edge cases

- **Hash set plus every-prefix checks:** storing all words in a set is compact,
  but materializing and hashing every prefix of every word can take
  $O(\sum \lvert w \rvert^2)$ time in languages where slicing copies strings.
- **Length-ordered dynamic construction:** sorting by length and accepting a
  word when `word[:-1]` was already accepted is simple, but sorting adds
  $O(n \log n)$ comparisons and prefix slicing still needs care.
- A missing one-character prefix blocks its entire trie branch, even if many
  longer strings from that branch appear in `words`.
- A one-character input word is eligible by itself because its only nonempty
  prefix is the word itself.
- Input order has no effect, and the lexicographic rule applies only after
  maximum length has been determined.

</details>
