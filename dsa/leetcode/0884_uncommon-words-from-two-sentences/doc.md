# Uncommon Words from Two Sentences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 884 |
| Difficulty | Easy |
| Topics | Hash Table, String, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/uncommon-words-from-two-sentences/) |

## Problem Description
### Goal
A sentence is a string of lowercase-letter words separated by single spaces. Neither of the two given sentences has a leading or trailing space.

A word is uncommon when it appears exactly once in one of the sentences and does not appear at all in the other sentence. Given `s1` and `s2`, return every uncommon word. The words in the returned list may be in any order.

### Function Contract
Let $L = \lvert \texttt{s1} \rvert + \lvert \texttt{s2} \rvert$ be the total number of characters in the two sentences.

**Inputs**

- `s1`: a single-space-separated sentence of lowercase English words, with $1 \leq \lvert \texttt{s1} \rvert \leq 200$.
- `s2`: a sentence with the same format, with $1 \leq \lvert \texttt{s2} \rvert \leq 200$.

**Return value**

Return a list containing exactly the words that occur once in one sentence and zero times in the other; the result order is unrestricted.

### Examples
**Example 1**

- Input: `s1 = "this apple is sweet", s2 = "this apple is sour"`
- Output: `["sweet","sour"]`

The shared words occur in both sentences, while `sweet` and `sour` each occur only once overall.

**Example 2**

- Input: `s1 = "apple apple", s2 = "banana"`
- Output: `["banana"]`

The repeated word `apple` is not uncommon even though it is absent from `s2`.

**Example 3**

- Input: `s1 = "red blue red", s2 = "green blue gold"`
- Output: `["green","gold"]`

### Required Complexity
- **Time:** $O(L)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Turn the two-sentence definition into one frequency condition**

Split both sentences into words and count them in one shared hash table. A word that appears exactly once across the combined input must occur once in one sentence and zero times in the other. Conversely, every word satisfying the problem's definition has combined frequency one. Thus the original two-part condition is equivalent to selecting entries whose total count equals one.

**Filter the completed frequency table**

After all words have been counted, iterate over the table and return each word with count one. Words shared between the sentences have count at least two, as do words repeated within either sentence, so both kinds are excluded. Since the required output order is unrestricted, the hash table's iteration order does not affect correctness.

#### Complexity detail

Splitting, counting, and filtering process $L$ input characters in total, giving $O(L)$ expected time under standard hash-table assumptions. The split words, frequency table, and returned words together require $O(L)$ space in the worst case.

#### Alternatives and edge cases

- **Count each word by rescanning both sentences:** This directly checks the definition but can require $O(L^2)$ time when many words are distinct.
- **Maintain two frequency tables:** Counting each sentence separately is also $O(L)$ and mirrors the definition, but one combined table is sufficient because only total frequency one matters.
- **Use sorting:** Sorting all words and scanning equal runs works, but costs $O(L \log L)$ comparison time in the usual model.
- **Repeated within one sentence:** A word occurring twice in `s1` is not uncommon even if it never occurs in `s2`.
- **Present in both sentences:** A word appearing once in each sentence has combined count two and must be excluded.
- **No uncommon words:** Return an empty list when every word is repeated or shared.
- **Arbitrary result order:** Any permutation containing exactly the uncommon words is valid.

</details>
