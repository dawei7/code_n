## Description

Given a list of `phrases`, generate a list of Before and After puzzles.

A *phrase* is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

*Before and After puzzles* are phrases that are formed by merging two phrases where the **last word of the first phrase** is the same as the **first word of the second phrase**. Note that only the *last word of the first phrase* and the *first word of the second phrase* are merged in this process.

Return the Before and After puzzles that can be formed by every two phrases $\text{phrases}[i]$ and $\text{phrases}[j]$ where $i \neq j$. Note that the order of matching two phrases matters, we want to consider both orders.

You should return a list of **distinct** strings **sorted lexicographically**, after removing all *duplicate* phrases in the generated Before and After puzzles.
### Function Contract

**Inputs**

- `phrases`: The list of lowercase, single-space-separated phrases from which ordered pairs are chosen.

Define the total input character count as

$S = \sum_{x \in \texttt{phrases}} \lvert x \rvert.$

Let $G$ be the total number of characters across all compatible merged candidates before duplicate strings are removed, and let $R$ be the number of distinct returned puzzles.

**Return value**

- Return the distinct valid merges as a lexicographically sorted list of strings. A phrase may not be paired with itself at the same index, even when its first and last words match.

### Examples

#### Example 1

<div class="example-block">
**Input:** phrases = ["writing code","code rocks"]

**Output:** ["writing code rocks"]

</div>
#### Example 2

<div class="example-block">
**Input:** phrases = ["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"]

**Output:** ["a chip off the old block party","a man on a mission impossible","a man on a mission statement","a quick bite to eat my words","chocolate bar of soap"]

</div>
#### Example 3

<div class="example-block">
**Input:** phrases = ["a","b","a"]

**Output:** ["a"]

</div>
#### Example 4

<div class="example-block">
**Input:** phrases = ["ab ba","ba ab","ab ba"]

**Output:** ["ab ba ab","ba ab ba"]

</div>
### Constraints

- $1 \le \text{phrases.length} \le 100$

- $1 \le \text{phrases}[i].length \le 100$