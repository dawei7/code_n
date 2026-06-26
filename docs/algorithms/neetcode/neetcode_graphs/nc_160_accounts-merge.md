## Problem Description & Examples
### Goal
Given a list of `accounts` where each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are emails representing that account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

### Function Contract
**Inputs**

- `accounts`: List[List[str]]

**Return value**

List[List[str]] - merged accounts list

### Examples
**Example 1**

- Input: `accounts = [["John", "a@mail.com", "b@mail.com"], ["John", "b@mail.com"]]`
- Output: `[["John", "a@mail.com", "b@mail.com"]]`

**Example 2**

- Input: `accounts = [['John', 'johnsmith@mail.com', 'john_newyork@mail.com'], ['John', 'johnsmith@mail.com', 'john00@mail.com'], ['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com']]`
- Output: `[['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com']]`

**Example 3**

- Input: `custom_case_3`
- Output: `derive by applying the strategy above`

---

## Underlying Base Algorithm(s)
- [Breadth-first search](graph_02_bfs.md)
- [Depth-first search](graph_03_dfs.md)
- [Topological sort](graph_07_topological-sort.md)
- [Union-find](graph_09_union-find.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
