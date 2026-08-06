## Description

A fruit market displays fruits in positions numbered from `1` through $N$.
The 1-indexed value `prices[i]` is the number of coins required to purchase
fruit `i`.

Purchasing fruit `i` grants the next `i` fruits for free, covering positions
`i + 1` through `2 * i` that exist. A fruit currently available for free may
still be purchased at its listed price; doing so starts its own offer and can
extend free coverage farther into the market.

Return the minimum number of coins needed to acquire every fruit.
