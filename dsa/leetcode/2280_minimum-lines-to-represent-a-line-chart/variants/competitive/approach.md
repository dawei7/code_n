## General
Given a 2D integer array `stockPrices` where $\text{stockPrices}[i] = [\text{day}_{i}, \text{price}_{i}]$ indicates the price of the stock on day $\text{day}_{i}$ is $\text{price}_{i}$. A **line chart** is created from the ..., the algorithm executes a single-pass linear scan through input elements. Edge case handling: guards against empty/null inputs via early returns, applies modulo arithmetic to prevent integer overflow.

## Complexity detail
- **Time Complexity**: $O(n log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
