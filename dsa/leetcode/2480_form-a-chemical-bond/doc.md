# Form a Chemical Bond

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2480 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/form-a-chemical-bond/) |

## Problem Description

### Goal

The `Elements` table records each chemical element's unique symbol, its category, and an electron count. An element is categorized as `Metal`, `Nonmetal`, or `Noble`. Noble elements have zero relevant electrons; for a metal the count describes electrons it can give, and for a nonmetal it describes electrons it needs.

A chemical bond can be formed by pairing any metal with any nonmetal. Produce every such pair, naming the metal symbol `metal` and the nonmetal symbol `nonmetal`. Noble elements do not appear in either output column, and the result may be returned in any order.

### Function Contract

**Inputs**

The database contains one table:

- `Elements(symbol, type, electrons)`: One row per element. `symbol` is the primary key, `type` is one of `Metal`, `Nonmetal`, or `Noble`, and `electrons` follows the category semantics above.

Let $r$ be the number of rows in `Elements`, and let $b$ be the number of returned metal–nonmetal pairs.

**Return value**

Return a table with columns `metal` and `nonmetal`, containing the Cartesian product of all metal symbols and all nonmetal symbols. Row order is not significant.

### Examples

#### Example 1

- **Input:** `Elements = [(He, Noble, 0), (Na, Metal, 1), (Ca, Metal, 2), (La, Metal, 3), (Cl, Nonmetal, 1), (O, Nonmetal, 2), (N, Nonmetal, 3)]`
- **Output:** All nine pairs formed by one symbol from `{Na, Ca, La}` and one symbol from `{Cl, O, N}`.
- **Explanation:** Every metal is compatible with every nonmetal; helium is Noble and is excluded.

#### Example 2

- **Input:** `Elements = [(Fe, Metal, 2), (Ne, Noble, 0)]`
- **Output:** An empty table with columns `metal` and `nonmetal`.
- **Explanation:** No nonmetal exists, so no bond pair can be formed.

#### Example 3

- **Input:** `Elements = [(Li, Metal, 1), (F, Nonmetal, 1)]`
- **Output:** `[(Li, F)]`
- **Explanation:** The only metal and the only nonmetal form the sole pair.
