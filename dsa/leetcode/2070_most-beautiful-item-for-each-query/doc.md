# Most Beautiful Item for Each Query

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2070 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/most-beautiful-item-for-each-query/) |

## Problem Description

### Goal

Each entry in `items` contains an item's positive price and beauty. For every value in `queries`, consider all items whose price is less than or equal to that query and determine the greatest beauty among them.

Return the answers in the original query order. If a query cannot afford any item, its answer is zero. Items may share a price or beauty, and a more expensive affordable item need not be more beautiful than a cheaper one.

### Function Contract

**Inputs**

- `items`: an array of $n$ pairs `[price,beauty]`, where $1 \le n \le 10^5$ and both values lie between $1$ and $10^9$.
- `queries`: an array of $q$ positive maximum prices, where $1 \le q \le 10^5$ and every query is at most $10^9$.

**Return value**

- Return an array of length $q$ whose $j$th value is the maximum beauty among items priced at most `queries[j]`, or zero when none qualify.

### Examples

**Example 1**

- Input: `items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]`
- Output: `[2,4,5,5,6,6]`
- Explanation: As the affordable price rises, the best available beauty forms the prefix maxima $2,4,5,5,6,6$.

**Example 2**

- Input: `items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]`
- Output: `[4]`
- Explanation: All four items are affordable, so the greatest beauty at the shared price is selected.

**Example 3**

- Input: `items = [[10,1000]], queries = [5]`
- Output: `[0]`
- Explanation: The only item costs more than the query.

### Required Complexity

- **Time:** $O(n\log n+q\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn sorted prices into prefix answers**

Sort the items by price. Scan that order while maintaining the greatest beauty seen so far, and store both each price and the corresponding prefix maximum. This makes the recorded beauty at any sorted position the best beauty among every item up through that price, including duplicate prices.

**Find the last affordable position**

For each query, use an upper-bound binary search to find the first stored price greater than the query. The preceding index, when it exists, is the last affordable item, and its prefix maximum is the answer. When the insertion point is zero, no item is affordable and the answer is zero.

Sorting places exactly the items with price at most a query in one prefix. The upper bound identifies the end of that prefix, and the stored maximum summarizes every beauty inside it. Processing queries independently preserves their original order, so every returned position matches its source query.

#### Complexity detail

Sorting $n$ items costs $O(n\log n)$ time. Building prefix maxima takes $O(n)$, and $q$ binary searches take $O(q\log n)$, for $O(n\log n+q\log n)$ total time. The price and prefix arrays require $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Offline query sweep:** Sort indexed queries and advance once through sorted items, achieving $O(n\log n+q\log q)$ time while restoring query order afterward.
- **Scan every item per query:** This is direct and correct but may take $O(nq)$ time.
- Duplicate prices must contribute their greatest beauty to every query reaching that price.
- A cheaper item can remain the answer for many larger queries when later beauties are smaller.
- Query results must follow the input query order, not sorted price order.
- A query below the minimum item price returns zero.
- Prices and beauties up to $10^9$ fit the comparisons without coordinate expansion.

</details>
