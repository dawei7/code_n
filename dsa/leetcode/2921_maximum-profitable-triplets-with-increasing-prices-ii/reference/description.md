## Description

Two 0-indexed arrays, `prices` and `profits`, describe $n$ store items.
Item $i$ has price `prices[i]` and contributes `profits[i]` when selected.
Choose exactly three indices $i<j<k$ whose prices are also strictly increasing:
$\texttt{prices[i]}<\texttt{prices[j]}<\texttt{prices[k]}$.

The selected triplet earns
`profits[i] + profits[j] + profits[k]`. Return the greatest profit obtainable
from any triplet satisfying both the index and price orders. If no such three
items exist, return `-1`.
