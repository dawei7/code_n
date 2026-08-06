## Description

There are `n` cities numbered from $1$ through $n$. Each row `[a, b, cost]` in `roads` describes a bidirectional road whose normal travel cost is `cost`. Buying one apple in city $i$ costs `appleCost[i - 1]`, and the buyer may choose any city in which to make the purchase.

For each possible starting city, find the minimum total cost of buying exactly one apple and returning to that same start. Travel toward the purchase city uses the listed road costs; after the apple is bought, every road on the return trip costs `k` times its listed amount. Return one answer for every starting city in numeric order.
