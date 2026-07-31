# Coupon Code Validator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3606 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/coupon-code-validator/) |

## Problem Description
### Goal

Three arrays of the same length describe a collection of coupons. At index `i`, `code[i]` is the coupon identifier, `businessLine[i]` is its category, and `isActive[i]` states whether the coupon is active.

A coupon is valid only when all three rules hold: it is active; its business line is exactly `"electronics"`, `"grocery"`, `"pharmacy"`, or `"restaurant"`; and its code is nonempty and contains only ASCII letters, decimal digits, or underscores.

Return the codes of all valid coupons. Sort categories in the fixed order electronics, grocery, pharmacy, then restaurant. Within one category, sort codes in ascending lexicographical order.

### Function Contract

**Inputs**

- `code`: The coupon identifier at each index.
- `businessLine`: The corresponding business category at each index.
- `isActive`: The corresponding active-state flag at each index.

The arrays have the same length $n$, where $1 \le n \le 100$. Each code and business-line string has length from $0$ through $100$ and contains printable ASCII characters.

**Return value**

Return the valid coupon codes in the required category and lexicographical order. Preserve repeated valid codes when they come from separate input entries.

### Examples

**Example 1**

- Input: `code = ["SAVE20", "", "PHARMA5", "SAVE@20"], businessLine = ["restaurant", "grocery", "pharmacy", "restaurant"], isActive = [true, true, true, true]`
- Output: `["PHARMA5", "SAVE20"]`
- Explanation: The empty code and the code containing `@` are invalid. Pharmacy precedes restaurant.

**Example 2**

- Input: `code = ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"], businessLine = ["grocery", "electronics", "invalid"], isActive = [false, true, true]`
- Output: `["ELECTRONICS_50"]`
- Explanation: The grocery coupon is inactive, and the last business line is not permitted.
