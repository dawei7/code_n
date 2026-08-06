## Description

You are given three **positive** integers `n`, `x`, and `y`.

In a city, there exist houses numbered `1` to `n` connected by `n` streets. There is a street connecting the house numbered `i` with the house numbered `i + 1` for all `1 <= i <= n - 1` . An additional street connects the house numbered `x` with the house numbered `y`.

For each `k`, such that `1 <= k <= n`, you need to find the number of **pairs of houses** `(house_1, house_2)` such that the **minimum** number of streets that need to be traveled to reach `house_2` from `house_1` is `k`.

Return *a **1-indexed** array *`result`* of length *`n`* where *`result[k]`* represents the **total** number of pairs of houses such that the **minimum** streets required to reach one house from the other is *`k`.

**Note** that `x` and `y` can be **equal**.
