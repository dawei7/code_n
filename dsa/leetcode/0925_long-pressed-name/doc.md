# Long Pressed Name

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 925 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/long-pressed-name/) |

## Problem Description

### Goal

Your friend intends to enter the string `name` on a keyboard. While a character is being typed, its key may be long pressed, causing that character to appear one or more times instead of exactly once.

Given the observed string `typed`, determine whether it could have been produced from `name` by long pressing some characters, possibly none. Every character of `name` must still appear in order, and any additional characters in `typed` must be repetitions caused by the immediately preceding intended key press.

### Function Contract

**Inputs**

- `name`: the intended name, containing only lowercase English letters and having length $m$, where $1 \le m \le 1000$.
- `typed`: the observed keyboard output, containing only lowercase English letters and having length $t$, where $1 \le t \le 1000$.

**Return value**

Return `true` if `typed` can represent `name` with zero or more long-pressed characters; otherwise return `false`.

### Examples

**Example 1**

- Input: `name = "alex", typed = "aaleex"`
- Output: `true`
- Explanation: The keys for `a` and `e` may each have been long pressed.

**Example 2**

- Input: `name = "saeed", typed = "ssaaedd"`
- Output: `false`
- Explanation: The two intended `e` characters are not both represented in `typed`.

### Required Complexity

- **Time:** $O(m+t)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Match each observed character once.** Keep a pointer `name_index` to the next unmatched character of `name`. Scan `typed` from left to right. If `typed[typed_index] == name[name_index]`, consume that intended character by advancing `name_index`.

**Recognize only genuine long presses.** When the current observed character does not match the next required name character, it is valid only if `typed[typed_index] == typed[typed_index - 1]`. That equality means the character can extend the output of the preceding key press. At the first typed position there is no preceding character, so a mismatch there must fail. A mismatch that differs from the preceding output also fails because it cannot be assigned to any intended key.

**Require the whole name to be consumed.** Finishing the `typed` scan is not sufficient by itself: `name_index` must equal $m$. This final check rejects an output that is merely a valid prefix, including cases where a repeated run in `name` is too short in `typed`. Each accepted observed character is thus accounted for either by the next intended character or by a repetition of the preceding one, which is exactly the long-press rule.

#### Complexity detail

The scan visits each of the $t$ observed characters once and advances through at most $m$ intended characters, giving $O(m+t)$ time. The two indices and no input-sized data structure require $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Run-length encoding:** Compare corresponding character runs and require every typed run to be at least as long as its name run. This is also linear, but explicitly storing both run lists uses extra space that the two-pointer scan avoids.
- **Dynamic programming over prefixes:** Model whether each pair of prefixes is compatible. It is correct but unnecessarily costs $O(mt)$ time and input-sized space.
- **Typed output shorter than the name:** It cannot contain every intended character and must be rejected.
- **Repeated letters already present in `name`:** Each intended copy must be consumed before any surplus copies can count as a long press.
- **Leading mismatch:** The first character of `typed` cannot be explained as a repetition because no earlier key press exists.

</details>
