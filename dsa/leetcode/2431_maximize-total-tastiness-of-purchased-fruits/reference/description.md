## Description

Two non-negative arrays, `price` and `tastiness`, describe the same $n$ fruits: `price[i]` is the cost of fruit $i$, and `tastiness[i]` is the value gained by purchasing it. Select any subset whose total paid cost does not exceed `maxAmount`, maximizing the sum of its tastiness values.

You may apply at most `maxCoupons` coupons. A coupon can be used on a purchased fruit at most once and changes its cost to `price[i] // 2`, including the downward rounding for odd prices. Every fruit can be purchased at most once. Return the greatest total tastiness achievable under these rules.
