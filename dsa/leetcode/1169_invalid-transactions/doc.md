# Invalid Transactions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1169 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/invalid-transactions/) |

## Problem Description

### Goal

You are given transaction records encoded as comma-separated strings of the form `"name,time,amount,city"`. The time is measured in minutes, and each record must be evaluated independently even when two records have identical text.

A transaction is possibly invalid when its amount exceeds `$1000`. It is also possibly invalid when another transaction has the same name, occurs within and including `60` minutes of it, and takes place in a different city. In the second situation, both transactions satisfy the rule. Return every original transaction occurrence that is possibly invalid; the answer may be in any order.

### Function Contract

**Inputs**

- `transactions`: An array of at most $1000$ strings formatted as `"name,time,amount,city"`.
- `name` and `city` contain between $1$ and $10$ lowercase English letters.
- `time` is an integer from `0` through `1000`, and `amount` is an integer from `0` through `2000`.
- Let $n$ be the number of transaction records.

**Return value**

- All transaction strings whose corresponding occurrences satisfy at least one invalidity rule, in any order and with duplicate occurrences preserved.

### Examples

**Example 1**

- Input: `transactions = ["alice,20,800,mtv","alice,50,100,beijing"]`
- Output: `["alice,20,800,mtv","alice,50,100,beijing"]`

The records share a name, differ in city, and are only `30` minutes apart, so both are invalid.

**Example 2**

- Input: `transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]`
- Output: `["alice,50,1200,mtv"]`

The cities match, but the second amount exceeds `$1000`.

**Example 3**

- Input: `transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]`
- Output: `["bob,50,1200,mtv"]`
