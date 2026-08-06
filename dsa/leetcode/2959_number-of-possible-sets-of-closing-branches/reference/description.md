## Description

There is a company with `n` branches across the country, some of which are connected by roads. Initially, all branches are reachable from each other by traveling some roads.

The company has realized that they are spending an excessive amount of time traveling between their branches. As a result, they have decided to close down some of these branches (**possibly none**). However, they want to ensure that the remaining branches have a distance of at most `maxDistance` from each other.

The **distance** between two branches is the **minimum** total traveled length needed to reach one branch from another.

You are given integers `n`, `maxDistance`, and a **0-indexed** 2D array `roads`, where `roads[i] = [u_i, v_i, w_i]` represents the **undirected** road between branches `u_i` and `v_i` with length `w_i`.

Return *the number of possible sets of closing branches, so that any branch has a distance of at most *`maxDistance`* from any other*.

**Note** that, after closing a branch, the company will no longer have access to any roads connected to it.

**Note** that, multiple roads are allowed.
