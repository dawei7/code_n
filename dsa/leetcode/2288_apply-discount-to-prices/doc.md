# Apply Discount to Prices

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2288 |
| Difficulty | Medium |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/apply-discount-to-prices/) |

## Problem Description

### Goal

A sentence consists of words separated by single spaces. Its characters may
be lowercase English letters, digits, spaces, or dollar signs. An entire word
is a price exactly when it starts with `"$"` and every remaining character is
a digit. Thus `"$100"` is a price, whereas `"100"`, `"$"`, `"5$"`, and
`"$1a"` are not.

For every price word, reduce its numeric value by `discount` percent. Replace
that word with a dollar sign followed by the discounted value written with
exactly two digits after the decimal point. Leave every non-price word
unchanged and preserve the word order and single-space separators.

Return the resulting sentence. Valid input prices are positive integers
without leading zeros and have at most ten digits.

### Function Contract

**Inputs**

- `sentence`: A nonempty, single-space-separated sentence with no leading or trailing space.
- `discount`: The integer percentage to subtract from every recognized price.

The sentence has length $N$ with $1 \le N \le 10^5$, and
$0 \le \texttt{discount} \le 100$.

**Return value**

The sentence after replacing every whole-word price with its discounted
two-decimal representation and leaving all other words unchanged.

### Examples

#### Example 1

- **Input:** `sentence = "there are $1 $2 and 5$ candies in the shop"`, `discount = 50`
- **Output:** `"there are $0.50 $1.00 and 5$ candies in the shop"`

#### Example 2

- **Input:** `sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$"`, `discount = 100`
- **Output:** `"1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"`
