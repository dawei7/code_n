## Description

You are given a string array `words` and a **binary** array `groups` both of length `n`.

A <span data-keyword="subsequence-array">subsequence</span> of `words` is **alternating** if for any two *consecutive* strings in the sequence, their corresponding elements at the *same* indices in `groups` are **different** (that is, there *cannot* be consecutive 0 or 1).

Your task is to select the **longest alternating** subsequence from `words`.

Return *the selected subsequence. If there are multiple answers, return **any** of them.*

**Note:** The elements in `words` are distinct.

**Example 1:**

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
**Input:** <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">words = ["e","a","b"], groups = [0,0,1]</span>

**Output:** <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">["e","b"]</span>

**Explanation:** A subsequence that can be selected is `["e","b"]` because `groups[0] != groups[2]`. Another subsequence that can be selected is `["a","b"]` because `groups[1] != groups[2]`. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is `2`.

</div>

**Example 2:**

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
**Input:** <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">words = ["a","b","c","d"], groups = [1,0,1,1]</span>

**Output:** <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">["a","b","c"]</span>

**Explanation:** A subsequence that can be selected is `["a","b","c"]` because `groups[0] != groups[1]` and `groups[1] != groups[2]`. Another subsequence that can be selected is `["a","b","d"]` because `groups[0] != groups[1]` and `groups[1] != groups[3]`. It can be shown that the length of the longest subsequence of indices that satisfies the condition is `3`.

</div>

**Constraints:**

	- `1 <= n == words.length == groups.length <= 100`

	- `1 <= words[i].length <= 10`

	- `groups[i]` is either `0` or `1.`

	- `words` consists of **distinct** strings.

	- `words[i]` consists of lowercase English letters.
