## Description

A Fibonacci tree is defined by its order. `order(0)` is empty, and `order(1)` contains one node. For $n\ge2$, `order(n)` has a new root whose left subtree is `order(n - 2)` and whose right subtree is `order(n - 1)`.

Alice and Bob play on `order(n)`, with Alice moving first. A move selects one node and removes that node together with all of its descendants. Eventually a player has no safe choice and is forced to delete the original root; that player loses. Assuming optimal play from both sides, determine whether Alice wins.
