# Word Break II (Backtracking)

| | |
|---|---|
| **ID** | `backtrack_04` |
| **Category** | backtracking |
| **Complexity (required)** | $O(N^2 + 2^N)$ Time, $O(N + 2^N)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Word Break II](https://leetcode.com/problems/word-break-ii/) |

## Problem statement

Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

**Input:** A string `s` and a list of strings `wordDict`.
**Output:** A list of strings, where each string is a space-separated valid sentence.

## When to use it

- To find ALL possible valid segmentations or partitions of a sequence based on a deterministic validation rule.
- It perfectly pairs with Dynamic Programming (`dp_15_word-break.md`), where DP answers "Is it possible?" and Backtracking answers "What are all the exact paths?".

## Approach

**1. The Decision Tree:**
At any point in the string `s` starting at index `start`, we look ahead to see if the prefix `s[start...i]` forms a valid word in `wordDict`.
If it does, we have found a valid "cut" point! We add this word to our current sentence, and recursively branch out to process the rest of the string starting at index `i + 1`.
Because we must explore EVERY valid cut, a string of all "a"s matched against a dictionary of `["a", "aa", "aaa"]` will explode into $O(2^N)$ branches!

**2. The Backtracking State:**
`backtrack(start_index, current_sentence)`:
- `start_index`: The index in the string `s` where the unparsed remaining substring begins.
- `current_sentence`: A list of words we have successfully parsed so far.

**3. Base Case:**
When `start_index == len(s)`, it means we have successfully parsed the ENTIRE string into valid dictionary words!
We join the words in `current_sentence` with a space `" ".join(...)` and append it to our global result list.

**4. The Recursive Step:**
Loop `i` from `start_index + 1` to `len(s) + 1` (because Python string slicing is exclusive at the end).
- Extract the substring: `word = s[start_index : i]`.
- If `word` is in the `wordDict`:
  - **Make Choice:** Append `word` to `current_sentence`.
  - **Recurse:** Call `backtrack(i, current_sentence)`.
  - **Backtrack:** Pop `word` from `current_sentence` so we can try a different, longer cut point in the next loop iteration.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for backtrack_04: Word Break.

Given a string s and a list of dictionary words, return True
iff s can be segmented into a sequence of one or more dict
words. Backtracking: at each step, try each dict word as a
prefix; recurse on the remaining suffix.
"""


def solve(s, dictionary, n):
    if n == 0:
        return True

    def helper(remaining):
        if not remaining:
            return True
        for word in dictionary:
            if remaining.startswith(word) and helper(remaining[len(word):]):
                return True
        return False

    return helper(s)
```

</details>

## Walk-through

`s = "catsanddog"`, `word_dict = ["cat", "cats", "and", "sand", "dog"]`.

1. `backtrack(0, [])`:
   - `i = 1, 2`: "c", "ca" not in dict.
   - `i = 3`: "cat" is in dict! Append.
     - `backtrack(3, ["cat"])`:
       - `i = 4, 5, 6`: "s", "sa", "san" not in dict.
       - `i = 7`: "sand" is in dict! Append.
         - `backtrack(7, ["cat", "sand"])`:
           - `i = 8, 9`: "d", "do" not in dict.
           - `i = 10`: "dog" is in dict! Append.
             - `backtrack(10, ["cat", "sand", "dog"])`: BASE CASE! Append `"cat sand dog"` to result.
           - Backtrack -> pop "dog".
       - Backtrack -> pop "sand".
   - `i = 4`: "cats" is in dict! Append.
     - `backtrack(4, ["cats"])`:
       - `i = 5, 6`: "a", "an" not in dict.
       - `i = 7`: "and" is in dict! Append.
         - `backtrack(7, ["cats", "and"])`:
           - `i = 8, 9`: "d", "do" not in dict.
           - `i = 10`: "dog" is in dict! Append.
             - `backtrack(10, ["cats", "and", "dog"])`: BASE CASE! Append `"cats and dog"` to result.
           - Backtrack -> pop "dog".
       - Backtrack -> pop "and".
   - `i = 5..10`: "catsa", etc. not in dict.

Result: `["cat sand dog", "cats and dog"]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^2)$ | $O(N)$ |
| **Average** | $O(2^N)$ | $O(2^N)$ |
| **Worst** | $O(N^2 + 2^N)$ | $O(N + 2^N)$ |

*Where N is the length of the string.*
In the worst case (e.g., `s = "aaaaaa"`, `dict = ["a", "aa", "aaa"]`), every single character boundary is a valid cut. This creates exactly 2^{N-1} valid sentences! Reconstructing and joining the strings takes $O(N)$, leading to $O(N \cdot 2^N)$ time.
If the string cannot be segmented at all, it takes $O(N^2)$ to check prefixes and fail.
Space complexity is $O(N)$ for the recursion stack, plus the space required to store the $O(2^N)$ massive output array.

## Variants & optimizations

- **Memoization (DP + Backtracking Hybrid):** The pure backtracking algorithm will TLE (Time Limit Exceeded) if the string is huge and contains many invalid branches! We can memoize the recursive function. Instead of passing `current_sentence` downward and popping, we make `backtrack(start_index)` RETURN a list of all valid suffix strings from that index! We cache this result in a dictionary `memo[start_index]`. This entirely prevents exploring the same invalid suffix twice!

## Real-world applications

- **Natural Language Processing:** Reconstructing spaces in stripped hashtags, URLs, or languages that don't naturally use spaces (like continuous Chinese/Japanese text) to find all grammatically valid interpretations of the text.

## Related algorithms in cOde(n)

- **[dp_15 - Word Break](../dynamic/dp_15_word-break.md)** — The DP version that only returns a boolean `True`/`False` if it's possible, executing in strictly $O(N^3)$ or $O(N^2)$ time.
- **[backtrack_03 - Combination Sum](backtrack_03_combination-sum.md)** — Another algorithm where the size of the choices dynamically changes based on a targeted sum/length.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
