## Description

You are given a **0-indexed** 2D integer array `<font face="monospace">transactions</font>`, where `transactions[i] = [cost_i, cashback_i]`.

The array describes transactions, where each transaction must be completed exactly once in **some order**. At any given moment, you have a certain amount of `money`. In order to complete transaction `i`, `money >= cost_i` must hold true. After performing a transaction, `money` becomes `money - cost_i + cashback_i`.

Return* the minimum amount of *`money`* required before any transaction so that all of the transactions can be completed **regardless of the order** of the transactions.*
