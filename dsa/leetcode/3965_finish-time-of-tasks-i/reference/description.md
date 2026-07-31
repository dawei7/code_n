## Description

A project contains `n` tasks numbered from `0` through `n - 1`. The directed pairs in `edges` form a tree rooted at task `0`; each pair `[u, v]` states that `u` is the parent of `v`. The value `baseTime[i]` is the base duration assigned to task `i`.

A leaf finishes after exactly its base duration. For a non-leaf task, let `earliest` and `latest` be the minimum and maximum finish times among its children. Its own duration is `(latest - earliest) + baseTime[i]`, and its finish time is `latest + ownDuration`.

Compute and return the finish time of the root task `0`.
