## Description

A company wants to evaluate every advertisement represented in `Ads`. Its performance measure is the click-through rate (CTR), based only on clicks and views; ignored actions do not enter either count.

Let $C$ be an advertisement's number of `Clicked` rows and $V$ its number of `Viewed` rows. The source formula is reproduced accessibly below:

| Condition | CTR |
|---|---:|
| $C + V = 0$ | $0$ |
| $C + V > 0$ | $\dfrac{C}{C+V}\times 100$ |

Find the CTR of every advertisement and round it to two decimal places. Return advertisements by CTR in descending order; when rounded rates tie, order those rows by `ad_id` in ascending order.
