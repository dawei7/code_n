## Description

An unknown positive integer $n$ must be recovered through a predefined interactive API. The hidden number fits in 30 bits.

Calling `commonSetBits(num)` returns how many bit positions contain `1` in both $n$ and the query value `num`. Equivalently, the response is the number of set bits in `n & num`. Every query value must remain between $0$ and $2^{30}-1$; results for values outside that interval are not guaranteed to be reliable.

Determine and return the exact hidden number $n$ using the information supplied by this API.
