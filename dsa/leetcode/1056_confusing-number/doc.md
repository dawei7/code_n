# Confusing Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1056 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/confusing-number/) |

## Problem Description

### Goal

A **confusing number** becomes a different valid number after being rotated $180$ degrees. Under this rotation, digits `0`, `1`, `6`, `8`, and `9` become `0`, `1`, `9`, `8`, and `6`, respectively. Digits `2`, `3`, `4`, `5`, and `7` become invalid.

Rotate every digit of the non-negative integer `n`, reverse their positional order as the display turns, and ignore any leading zeros in the rotated result. Return `true` only when all digits remain valid and the rotated numeric value differs from `n`.

### Function Contract

**Inputs**

- `n`: an integer satisfying $0 \le n \le 10^9$; let $D$ be its number of decimal digits, with zero having one digit.

**Return value**

- `true` if rotating `n` produces a valid different number; otherwise, `false`.

### Examples

**Example 1**

- Input: `n = 6`
- Output: `true`
- Explanation: Rotation produces `9`.

**Example 2**

- Input: `n = 89`
- Output: `true`
- Explanation: Rotation reverses the positions and maps the digits, producing `68`.

**Example 3**

- Input: `n = 11`
- Output: `false`
- Explanation: The rotated value is still `11`.

### Required Complexity

- **Time:** $O(D)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Map only valid rotated digits:** Store the five valid digit mappings. Process the original number one decimal digit at a time from right to left. If a digit is absent from the mapping, return `false` immediately.

**Build the rotated value in numeric order:** The rightmost original digit becomes the leftmost rotated digit. For every extracted digit, update `rotated = rotated * 10 + mapping[digit]`. Integer arithmetic naturally ignores leading zeros in the rotated display.

**Compare after complete validation:** Preserve the original value before consuming its digits. Once all digits have been mapped, the number is confusing exactly when the constructed rotated value is different from the original.

Each processed digit receives precisely its defined $180$-degree image, and reading from right to left accounts for the reversal of positions. An invalid digit makes the whole rotated display invalid. Otherwise the constructed integer is exactly the rotated numeric value, so the final inequality test matches the definition.

#### Complexity detail

The loop processes each of the $D$ decimal digits once, taking $O(D)$ time. The mapping has constant size and only scalar integers are stored, so space is $O(1)$.

#### Alternatives and edge cases

- **String reversal and mapping:** Map characters, reverse their order, and parse the result. It is straightforward but uses $O(D)$ extra space.
- **Repeated string rebuilding:** Prepend each mapped digit by copying the accumulated characters, taking $O(D^2)$ time.
- **Recompute every rotated prefix:** Rebuild each prefix independently with repeated prepending. It remains correct but repeats prior work and can take $O(D^3)$ time.
- **Rotation lookup for every integer:** Precomputing unrelated values is unnecessary for testing one number.
- **Invalid digit:** Any occurrence of `2`, `3`, `4`, `5`, or `7` makes the answer false.
- **Strobogrammatic value:** A valid rotation equal to the original, such as `11` or `818`, is not confusing.
- **Zero:** It rotates to zero and is not confusing.
- **Leading rotated zeros:** Rotating `8000` yields display `0008`, interpreted as numeric value `8`.
- **Upper bound:** `1000000000` is processed with ordinary integer arithmetic and rotates to `1`.

</details>
