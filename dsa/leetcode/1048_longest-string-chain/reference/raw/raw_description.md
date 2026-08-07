## Description

You are given an array of `words` where each word consists of lowercase English letters.

`word_A` is a **predecessor** of `word_B` if and only if we can insert **exactly one** letter anywhere in `word_A` **without changing the order of the other characters** to make it equal to `word_B`.

	- For example, `"abc"` is a **predecessor** of `"ab<u>a</u>c"`, while `"cba"` is not a **predecessor** of `"bcad"`.

A **word chain*** *is a sequence of words `[word_1, word_2, ..., word_k]` with `k >= 1`, where `word_1` is a **predecessor** of `word_2`, `word_2` is a **predecessor** of `word_3`, and so on. A single word is trivially a **word chain** with `k == 1`.

Return *the **length** of the **longest possible word chain** with words chosen from the given list of *`words`.

**Example 1:**

```
**Input:** words = ["a","b","ba","bca","bda","bdca"]
**Output:** 4
**Explanation**: One of the longest word chains is ["a","<u>b</u>a","b<u>d</u>a","bd<u>c</u>a"].
```

**Example 2:**

```
**Input:** words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
**Output:** 5
**Explanation:** All the words can be put in a word chain ["xb", "xb<u>c</u>", "<u>c</u>xbc", "<u>p</u>cxbc", "pcxbc<u>f</u>"].
```

**Example 3:**

```
**Input:** words = ["abcd","dbqca"]
**Output:** 1
**Explanation:** The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
```

**Constraints:**

	- `1 <= words.length <= 1000`

	- `1 <= words[i].length <= 16`

	- `words[i]` only consists of lowercase English letters.
