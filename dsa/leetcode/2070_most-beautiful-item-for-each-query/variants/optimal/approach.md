## General
**Turn sorted prices into prefix answers**

Sort the items by price. Scan that order while maintaining the greatest beauty seen so far, and store both each price and the corresponding prefix maximum. This makes the recorded beauty at any sorted position the best beauty among every item up through that price, including duplicate prices.

**Find the last affordable position**

For each query, use an upper-bound binary search to find the first stored price greater than the query. The preceding index, when it exists, is the last affordable item, and its prefix maximum is the answer. When the insertion point is zero, no item is affordable and the answer is zero.

Sorting places exactly the items with price at most a query in one prefix. The upper bound identifies the end of that prefix, and the stored maximum summarizes every beauty inside it. Processing queries independently preserves their original order, so every returned position matches its source query.

## Complexity detail
Sorting $n$ items costs $O(n\log n)$ time. Building prefix maxima takes $O(n)$, and $q$ binary searches take $O(q\log n)$, for $O(n\log n+q\log n)$ total time. The price and prefix arrays require $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Offline query sweep:** Sort indexed queries and advance once through sorted items, achieving $O(n\log n+q\log q)$ time while restoring query order afterward.
- **Scan every item per query:** This is direct and correct but may take $O(nq)$ time.
- Duplicate prices must contribute their greatest beauty to every query reaching that price.
- A cheaper item can remain the answer for many larger queries when later beauties are smaller.
- Query results must follow the input query order, not sorted price order.
- A query below the minimum item price returns zero.
- Prices and beauties up to $10^9$ fit the comparisons without coordinate expansion.
