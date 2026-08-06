## Description

A hidden array `nums` contains only `0` and `1`. You cannot read its entries directly. Instead, an `ArrayReader` exposes its length and lets you query four distinct indices in strictly increasing order.

For indices $a < b < c < d$, `reader.query(a, b, c, d)` reports only the distribution of the four hidden bits: it returns `4` when all four are equal, `2` when one bit differs from the other three, and `0` when the group contains two zeros and two ones. At most $2n$ calls to `query` are allowed, where $n$ is the hidden-array length.

Return any index containing the more frequent bit. If zeros and ones occur equally often, return `-1`.
