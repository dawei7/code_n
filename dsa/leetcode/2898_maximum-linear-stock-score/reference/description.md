## Description

You are given a 1-indexed integer array `prices`, where `prices[i]` is a stock's price on day $i$. Select a nonempty subsequence of day indices in increasing order.

The selection is *linear* when every pair of consecutive selected days has the same change in price as the elapsed number of days. For selected indices `indexes[1], indexes[2], ..., indexes[k]`, this requires

$$
\texttt{prices[indexes[j]]}-\texttt{prices[indexes[j-1]]}
=\texttt{indexes[j]}-\texttt{indexes[j-1]}
$$

for every $1<j\le k$.

The score is the sum of the prices at all selected indices. Return the maximum score of any linear selection.
