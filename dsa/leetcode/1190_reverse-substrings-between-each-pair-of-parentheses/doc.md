# Reverse Substrings Between Each Pair of Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1190 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/) |

## Problem Description

### Goal

You are given a string `s` made of lowercase English letters and parentheses. Every opening parenthesis has a matching closing parenthesis, and the pairs may be nested.

Reverse the string inside each matching pair, processing the innermost pair before any pair that contains it. Those inner transformations therefore become part of the contents reversed by their enclosing pairs. Return the fully transformed sequence of letters with every parenthesis removed from the result.

### Function Contract

**Inputs**

- `s`: A string of length $n$, where $1\le n\le2000$, containing only lowercase English letters and balanced parentheses.

**Return value**

- The string produced after all matched-parenthesis reversals have been applied from the inside out and all parentheses have been omitted.

### Examples

**Example 1**

- Input: `s = "(abcd)"`
- Output: `"dcba"`

**Example 2**

- Input: `s = "(u(love)i)"`
- Output: `"iloveu"`

First reverse `"love"` within the inner pair, then reverse the contents of the outer pair.

**Example 3**

- Input: `s = "(ed(et(oc))el)"`
- Output: `"leetcode"`

The reversals successively affect `"oc"`, its enclosing contents, and finally the entire outer contents.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Pair the structural boundaries.** Scan `s` once. Push each opening-parenthesis index onto a stack; when a closing parenthesis appears, pop its matching opening index and record the two-way mapping between them. Balanced parentheses guarantee that every pop and every final pairing is valid.

**Treat each pair as a direction-changing portal.** Start at index zero and walk with `direction = 1`. A letter is appended to the answer. On reaching either endpoint of a parenthesis pair, jump directly to its partner and perform `direction = -direction`; then advance one position in the new direction. Crossing a boundary therefore enters the enclosed interval from the opposite end, which visits its letters in reversed order. A nested boundary flips the direction again, exactly matching the required inside-out reversal semantics.

**Account for every character once.** The walk never appends parentheses. After jumping between a matched pair, the direction change sends the traversal through an as-yet-unvisited neighboring region, so each letter is appended exactly once. Every nesting level contributes one reversal through its direction flip, and leaving the valid index range means the complete transformed string has been produced.

#### Complexity detail

Building the matching-index table scans the $n$ characters once. The second walk also processes each index once, with constant-time jumps and direction changes, so the total time is $O(n)$. The pairing table, stack, and output buffer each require at most $O(n)$ space.

#### Alternatives and edge cases

- **Stack of character buffers:** Start a fresh buffer at `(`, reverse it at `)`, and append it to the enclosing buffer. This is intuitive, but repeatedly reversing long contents at many nesting levels can take $O(n^2)$ time.
- **Repeated innermost replacement:** Locate a closing parenthesis, find its nearest opening partner, and splice the reversed substring back into `s`. It is correct but repeated searches and string copies can also require $O(n^2)$ time.
- **No parentheses:** The walk appends every letter in its original order.
- **Adjacent pairs:** Each pair changes direction only within its own interval; after one pair is exited, traversal continues correctly into the next.
- **Deep nesting:** Every additional pair flips direction once, so an even number of enclosing reversals preserves order and an odd number reverses it.
- **Empty parenthesized content:** Matching endpoints are still paired and crossed, but they contribute no output characters.
- **Balanced-input guarantee:** No recovery logic is needed for an unmatched opening or closing parenthesis.

</details>
