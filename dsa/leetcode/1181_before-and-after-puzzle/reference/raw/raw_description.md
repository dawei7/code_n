## Description

Given a list of `phrases`, generate a list of Before and After puzzles.

A *phrase* is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

*Before and After puzzles* are phrases that are formed by merging two phrases where the **last word of the first phrase** is the same as the **first word of the second phrase**. Note that only the *last word of the first phrase* and the *first word of the second phrase* are merged in this process.

Return the Before and After puzzles that can be formed by every two phrases `phrases[i]` and `phrases[j]` where `i != j`. Note that the order of matching two phrases matters, we want to consider both orders.

You should return a list of **distinct** strings **sorted lexicographically**, after removing all *duplicate* phrases in the generated Before and After puzzles.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">phrases = ["writing code","code rocks"]</span>

**Output:** <span class="example-io">["writing code rocks"]</span>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">phrases = ["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"]</span>

**Output:** <span class="example-io">["a chip off the old block party","a man on a mission impossible","a man on a mission statement","a quick bite to eat my words","chocolate bar of soap"]</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">phrases = ["a","b","a"]</span>

**Output:** <span class="example-io">["a"]</span>

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">phrases = ["ab ba","ba ab","ab ba"]</span>

**Output:** <span class="example-io">["ab ba ab","ba ab ba"]</span>

</div>

**Constraints:**

	- `1 <= phrases.length <= 100`

	- `1 <= phrases[i].length <= 100`
