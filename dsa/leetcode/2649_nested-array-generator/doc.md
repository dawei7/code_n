# Nested Array Generator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2649 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/nested-array-generator/) |

## Problem Description

### Goal

A multi-dimensional array may contain integers and further multi-dimensional arrays at any position. Write a JavaScript generator that visits this recursive structure in inorder: scan every array from left to right, yield an integer immediately when encountered, and recursively traverse an encountered array in the same fashion.

The yielded sequence must match the complete left-to-right flattening of the input, but the implementation must not first create a separate flattened array. Values should be produced lazily as the caller advances the generator.

### Function Contract

**Inputs**

- `arr`: A recursively nested array of nonnegative integers. Its fully flattened sequence contains at most $10^5$ integers, every integer is at most $10^5$, and the maximum nesting depth is at most $10^5$.

**Return value**

Return a JavaScript generator object that yields every integer in recursive left-to-right order and then reports completion.

### Examples

#### Example 1

- **Input:** `arr = [[[6]],[1,3],[]]`
- **Output:** `[6,1,3]`
- **Explanation:** Recursive left-to-right traversal reaches `6`, then `1`, then `3`; the empty array contributes nothing.

#### Example 2

- **Input:** `arr = []`
- **Output:** `[]`
- **Explanation:** There are no integers to yield.
