# Accounts Merge

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 721 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/accounts-merge/) |

## Problem Description
### Goal
Each account record begins with a person's name followed by one or more email addresses. Two records definitely belong to the same person when they share at least one email, and that connection is transitive through any chain of overlapping records. Equal names alone do not prove that accounts belong to the same person.

Merge every connected group into one record containing the person's name followed by all distinct emails in lexicographic order. Records for different people may be returned in any order. All accounts belonging to one person use the same name, but different people may share that name.

### Function Contract
**Inputs**

- `accounts`: records whose first string is a name and whose remaining strings are that record's email addresses

**Return value**

- One record per connected person, containing the name followed by all distinct emails in sorted order; merged records themselves may appear in any order

### Examples
**Example 1**

- Input: `accounts = [["John","a@mail.com","b@mail.com"],["John","b@mail.com","c@mail.com"]]`
- Output: `[["John","a@mail.com","b@mail.com","c@mail.com"]]`

**Example 2**

- Input: `accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]`
- Output: `[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]`

**Example 3**

- Input: `accounts = [["Alex","x@mail.com"],["Alex","y@mail.com"]]`
- Output: `[["Alex","x@mail.com"],["Alex","y@mail.com"]]`
