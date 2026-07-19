# Search Suggestions System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1268 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Trie, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/search-suggestions-system/) |

## Problem Description

### Goal

You are given an array of product-name strings `products` and a string `searchWord`. Build a suggestion system that responds after every character of `searchWord` is typed. At each step, a product is eligible only when it starts with the entire prefix typed so far.

Return at most three eligible names for each prefix. When more than three products share that prefix, choose the three lexicographically minimum product names. The final result must contain one suggestion list for every successive character of `searchWord`, in typing order.

### Function Contract

**Inputs**

- `products`: an array of $n$ unique strings made of lowercase English letters, where $1 \le n \le 1000$.
- `searchWord`: a lowercase English string of length $m$, where $1 \le m \le 1000$.

The total number of characters across all product names is

$$
S = \sum_{p \in \texttt{products}} \lvert p \rvert,
$$

where $1 \le S \le 2 \cdot 10^4$.

**Return value**

- Return a list of $m$ lists. Entry $k$ contains the lexicographically smallest three or fewer products beginning with `searchWord[:k + 1]`.

### Examples

**Example 1**

- Input: `products = ["mobile","mouse","moneypot","monitor","mousepad"]`, `searchWord = "mouse"`
- Output: `[["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]`

**Example 2**

- Input: `products = ["havana"]`, `searchWord = "havana"`
- Output: `[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]`

**Example 3**

- Input: `products = ["bags","baggage","banner","box","cloths"]`, `searchWord = "bags"`
- Output: `[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]`
