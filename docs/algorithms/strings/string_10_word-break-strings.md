# Word Break

| | |
|---|---|
| **ID** | `string_10` |
| **Category** | strings |
| **Complexity (required)** | $O(N^2 \times M)$ Time, $O(N)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Word Break](https://leetcode.com/problems/word-break/) |

## Problem statement

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

**Input:** A string `s` and a list of strings `wordDict`.
**Output:** A boolean.

## When to use it

- To split a massive, unspaced string (like a URL or a hashtag) back into human-readable words.
- A foundational introduction to 1D Dynamic Programming over string indices.

## Approach

**1. The Flaw of Greedy Matching:**
Suppose `s = "applepenapple"` and `wordDict = ["apple", "pen"]`. A greedy approach (checking if the string starts with any word in the dictionary, slicing it, and repeating) works perfectly here.
But suppose `s = "cars"` and `wordDict = ["car", "ca", "rs"]`.
If we are greedy, we see `"car"` matches! We slice it. We are left with `"s"`. `"s"` is not in the dictionary! The algorithm returns `False`.
But wait! If we had chosen `"ca"` instead, we would be left with `"rs"`. `"rs"` IS in the dictionary! The correct answer is `True`!
Greedy matching completely fails because making a valid choice early on can mathematically block a valid sequence later.

**2. The Dynamic Programming Strategy:**
We need to track ALL possible valid breaking points simultaneously!
We create a boolean array `dp` of length N+1, initialized to `False`.
`dp[i] = True` means: "The substring `s[0...i]` can be successfully broken down into valid dictionary words."
The base case is `dp[0] = True` (an empty string is trivially valid).

**3. The DP Transitions:**
We iterate i from 1 to N. (This represents trying to find if the substring up to length i is valid).
To figure out if `dp[i]` is True, we don't start from scratch! We look BACKWARDS at every previous valid breaking point j (where `dp[j] == True`).
If `dp[j]` is True, it means we successfully segmented the string up to index j.
All we have to do is check if the REMAINING chunk of the string `s[j...i]` is a valid word in our `wordDict`!
If it is, then `dp[i]` is mathematically guaranteed to be True! We mark it `True` and immediately break to the next i!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_10: Word Break.

True iff s can be segmented into a sequence of dictionary words.
"""


def solve(s, word_dict):
    n = len(s)
    word_set = set(word_dict)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
```

</details>

## Walk-through

`s = "cars"`, `wordDict = ["car", "ca", "rs"]`.
`N = 4`. `dp = [True, False, False, False, False]`.

1. **`i = 1` (`"c"`):**
   - `j = 0`: `dp[0]` is True. `s[0:1]` is `"c"`. `"c"` not in set.
   - `dp[1] = False`.
2. **`i = 2` (`"ca"`):**
   - `j = 1`: `dp[1]` is False. Skip.
   - `j = 0`: `dp[0]` is True. `s[0:2]` is `"ca"`. `"ca"` IS in set!
   - `dp[2] = True`. Break!
3. **`i = 3` (`"car"`):**
   - `j = 2`: `dp[2]` is True. `s[2:3]` is `"r"`. `"r"` not in set.
   - `j = 1`: `dp[1]` is False. Skip.
   - `j = 0`: `dp[0]` is True. `s[0:3]` is `"car"`. `"car"` IS in set!
   - `dp[3] = True`. Break!
4. **`i = 4` (`"cars"`):**
   - `j = 3`: `dp[3]` is True. `s[3:4]` is `"s"`. `"s"` not in set.
   - `j = 2`: `dp[2]` is True. `s[2:4]` is `"rs"`. `"rs"` IS in set!
   - `dp[4] = True`. Break!

Loop terminates. Return `dp[4]` -> `True`! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \times M)$ | $O(N)$ |
| **Average** | $O(N^2 \times M)$ | $O(N)$ |
| **Worst** | $O(N^2 \times M)$ | $O(N)$ |

The outer loop runs N times.
The inner loop runs up to N times backwards. This is $O(N^2)$ iterations.
Inside the inner loop, string slicing `s[j:i]` physically copies characters to create a new string! Creating a string of length M takes $O(M)$ time (where M is the length of the sliced word). Hashing the new string to check the set also takes $O(M)$ time.
Total time complexity is $O(N^2 x M)$.
Space complexity is $O(N)$ for the `dp` array. (Assuming the Hash Set generation is excluded as standard input parsing).

## Variants & optimizations

- **Length-Bounded Inner Loop:** If the longest word in the dictionary is 10 characters long, there is ZERO REASON for the inner loop `j` to look backwards 100 characters! You can modify the inner loop to only check `max(0, i - MAX_WORD_LENGTH)`. This instantly drops the worst-case time complexity to $O(N x L^2)$ where L is the max word length!
- **Word Break II:** Instead of returning a boolean, return ALL possible valid sentences. This requires a Recursive Backtracking DFS combined with Memoization to trace the actual paths!

## Real-world applications

- **Hashtag Parsing:** Breaking `#ilovealgorithms` into `["i", "love", "algorithms"]` for Twitter trending topic analysis.
- **Asian Language NLP:** Languages like Chinese and Japanese are written without spaces between words! NLP processors must run this exact algorithm with a massive language dictionary to segment characters into distinct words before translating them.

## Related algorithms in cOde(n)

- **[dynamic_03 - Longest Increasing Subsequence](../dynamic/dp_03_longest-increasing-subsequence.md)** — The exact same "look backward at all previous valid states" DP pattern applied to integers instead of strings.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
