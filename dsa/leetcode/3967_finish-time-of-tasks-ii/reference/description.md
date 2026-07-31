## Description

A project contains `n` tasks numbered from `0` through `n - 1`. The pairs in `edges` are undirected connections and together form a tree. The value `baseTime[i]` is the base completion time assigned to task `i`.

Choose any task as the tree's root. Under that choice, a task with no children is a leaf and finishes at `baseTime[i]`. For a non-leaf task, let `earliest` and `latest` be the minimum and maximum finish times among its children. Its own duration is `(latest - earliest) + baseTime[i]`, and its finish time is `latest + ownDuration`.

Each possible root gives the tree a different parent-child orientation and may therefore produce a different finish time for that root. Return the minimum root finish time obtainable over all `n` choices.
