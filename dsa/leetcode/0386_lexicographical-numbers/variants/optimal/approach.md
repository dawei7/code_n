## General

**Lexicographical order is a traversal order**

Lexicographical order compares the decimal representations as if they were words. It first compares the first character; only when those match does it compare the next character. This is why `10` comes immediately after `1` and before `2`.

The integers from `1` through `n` can be imagined as nodes in a decimal prefix tree:

- the roots are `1`, `2`, ..., `9` when they do not exceed `n`;
- a number `v` can have children `v * 10`, `v * 10 + 1`, ..., `v * 10 + 9` when those values are at most `n`.

For example, node `1` has descendants `10` through `19`; node `10` may have descendants `100` through `109`. A preorder depth-first traversal—visit a node, then visit its children from digit `0` to `9`—produces exactly lexicographical order.

A recursive DFS would make that model explicit, but its call stack uses space proportional to the number of digits. The exact solution simulates the traversal with one current integer `v`, so it meets the constant-extra-space requirement.

**Generate exactly one next number at a time**

The result starts empty and `v` starts at `1`, the first positive integer lexicographically. The outer loop runs exactly `n` times because the range `[1, n]` contains exactly `n` values. At each iteration, it appends the current `v`, then computes the lexicographical successor for the next iteration.

There are two possible movements in the prefix tree:

1. descend to the smallest child if one exists;
2. otherwise, move to the next available sibling, climbing to ancestors first when necessary.

The two branches of the code implement precisely those movements.

**Descending to the smallest child**

If `v * 10 <= n`, then appending digit zero produces a valid number. That child is the lexicographically smallest value whose decimal representation begins with the full representation of `v`. It must come immediately after `v`, before any sibling of `v`.

The solution therefore executes `v *= 10`. For example, after emitting `1` with `n = 130`, it moves to `10`; after emitting `10`, it moves to `100`. This is the iterative equivalent of making the first recursive DFS call.

It always tries digit zero first because children are ordered by their appended digit. If `v0` is not valid because it exceeds `n`, no larger child `v1` through `v9` can be valid either. In that case the subtree has no children, so the traversal must move sideways or upward.

**Finding the next sibling**

When no child is available, the natural next candidate is `v + 1`. This changes the last digit to the next digit, which corresponds to moving to the next sibling in the prefix tree.

That increment is legal only when:

- `v` does not end in `9`, because a digit-nine node has no next sibling under the same parent;
- `v + 1 <= n`, because the sibling must lie inside the requested range.

The while loop checks the opposite condition:

```text
while v % 10 == 9 or v + 1 > n:
    v //= 10
```

Integer division by ten removes the final decimal digit, moving from a node to its parent. The loop keeps climbing until it reaches an ancestor that has a valid next sibling. It then executes `v += 1` to enter that sibling.

**Why both while-loop conditions are needed**

The `v % 10 == 9` condition handles a completed sibling group. After `19`, incrementing directly would produce `20`, but lexicographically the traversal must finish the entire `1` prefix and then move to root `2`. Removing the trailing `9` changes `19` to parent `1`, and incrementing produces `2`.

The `v + 1 > n` condition handles a partially populated final branch. Suppose `n = 13` and the current value is `13`. It does not end in `9`, but `14` is outside the range. Dividing by ten moves to `1`, whose next sibling `2` is valid. Without this boundary check, the output could contain values above `n`.

Sometimes both conditions cause several upward moves. After a value such as `1999`, every trailing `9` belongs to a completed sibling group. Repeated division climbs past all of them before the increment reaches the next lexicographical branch.

**Tracing `n = 13`**

The state evolves as follows:

| Emitted `v` | How the successor is found | Next `v` |
|---:|---|---:|
| `1` | child `10` is valid | `10` |
| `10` | child `100` is too large; next sibling is valid | `11` |
| `11` | next sibling is valid | `12` |
| `12` | next sibling is valid | `13` |
| `13` | `14 > 13`, climb to `1`, then increment | `2` |
| `2` | no child; next sibling is valid | `3` |
| `3` through `8` | move to next root | `4` through `9` |
| `9` | final emitted value; subsequent state is irrelevant | — |

The appended sequence is `[1,10,11,12,13,2,3,4,5,6,7,8,9]`, exactly the dictionary ordering of the decimal strings.

**The current-value invariant**

At the start of each outer iteration, `v` is the smallest valid number that has not yet been emitted in lexicographical order.

It is true initially because `1` is the first number. Assume it is true when `v` is appended.

- If a valid child `v * 10` exists, that child is the smallest unvisited string extending `v`; every number outside the subtree differs at an earlier digit and comes later. Descending preserves the invariant.
- If no child exists, all descendants are absent. The next lexicographical position must be the nearest next sibling of `v` or one of its ancestors. The while loop skips exactly the ancestors whose final child has been exhausted or whose next sibling exceeds `n`. The subsequent increment reaches the first valid sibling. No unvisited value can lie between the completed subtree and that sibling.

Thus the successor computation neither skips a valid number nor revisits one. Running exactly `n` iterations appends all `n` values in the correct order.

**Why no string conversion or sorting is necessary**

Converting all values to strings and sorting would reproduce the desired comparison rule, but it would cost $O(n\log n)$ comparisons and additional storage. The prefix-tree view derives the next item directly using decimal arithmetic. Multiplication by ten appends a digit zero, division by ten removes the last digit, and addition by one moves to a sibling. These operations simulate string-prefix navigation without allocating strings.

## Complexity detail

The outer loop appends exactly $n$ numbers. Most iterations perform constant work, but one iteration can execute the inner while loop several times while removing trailing digits.

Those divisions are amortized across the traversal. Every descent `v *= 10` moves one level deeper, and every division moves one level back up. The traversal cannot climb more levels in total than it previously entered, apart from a constant number of root transitions. Across all `n` outputs, the total number of upward moves is $O(n)$. Therefore the complete running time is $O(n)$, not $O(n\log n)$.

The returned list `ans` necessarily contains $n$ integers and occupies $O(n)$ output space. Excluding that required output, the algorithm stores only `v` and loop bookkeeping, so auxiliary space is $O(1)$. It uses no recursion, explicit stack, string array, or sorting workspace.

Under the problem’s bounded integer range, arithmetic is safe in Python. In a fixed-width language with a much larger possible `n`, the test `v * 10 <= n` should be written in an overflow-safe form such as `v <= n / 10`.

## Alternatives and edge cases

- **Recursive decimal-tree DFS:** Visit roots `1` through `9` and recursively try children formed by appending digits `0` through `9`. This also runs in $O(n)$ time and is conceptually direct, but uses $O(\log n)$ call-stack space rather than the requested constant auxiliary space.

- **Convert to strings and sort:** Sorting `1` through `n` by their decimal strings is straightforward but takes $O(n\log n)$ time and $O(n)$ extra storage, failing both desired bounds.

- **Priority queue of next prefixes:** A heap can generate values in lexical order but introduces $O(\log n)$ work per removal and stores many candidates. Direct tree navigation is simpler and faster.

- **`n = 1`:** The loop appends `1` once. Any successor computation after that is irrelevant because there is no next iteration.

- **`n < 10`:** No value has a valid decimal child. The algorithm simply increments through the roots from `1` to `n`.

- **Crossing from a `9` suffix:** Values ending in `9` cannot increment within the same sibling group. Repeated division removes one or more exhausted suffix digits before moving to the next ancestor sibling.

- **A truncated subtree near `n`:** A value such as `13` when `n = 13` has no valid child or sibling. The `v + 1 > n` test forces a climb even though its final digit is not `9`.

- **Powers of ten:** When `n = 100`, the beginning is `1, 10, 100, 11, ...`. Descending is correct because a longer string with prefix `1` precedes the next sibling `2`.

- **No leading-zero branch:** Positive integer representations never begin with zero, so roots start at `1`. Zero may be appended inside a number through multiplication by ten.

- **Output space convention:** The $O(1)$ claim excludes the list that the function is required to return. Counting the result itself, total memory is $O(n)$.

- **State computed after the final output:** The loop always computes a successor, even after appending the last lexicographical value. That successor is never read, so it need not represent another valid unvisited number.
