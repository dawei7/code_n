## General

Let $n$ be the array length.

**Encode the tie rule in the heap key**

Create one heap entry `(value, index)` for every array position. Tuple ordering compares the value first and the index second, so the heap root is always the current minimum and automatically chooses its earliest occurrence when values tie.

**Replace the selected entry**

For each of the `k` operations, read `(value, index)` from the root, compute `updated = value * multiplier`, and write `updated` to `nums[index]`. Replace the root with `(updated, index)` so the heap and array describe the same current state before the next operation.

Initially the heap contains exactly one accurate entry per index. Each operation changes the same selected index in both representations and leaves every other entry unchanged, preserving that correspondence. Consequently the next root implements the required minimum and tie rule. After `k` repetitions, every performed update is reflected in `nums`, which is therefore the requested final state.

## Complexity detail

Building the heap takes $O(n)$ time. Each of the $k$ root replacements costs $O(\log n)$, for $O(n + k \log n)$ total time. The heap stores $n$ pairs and uses $O(n)$ auxiliary space. Since the contract bounds $k$ by 10, the running time is also linear in $n$ when only the array length scales.

## Alternatives and edge cases

- **Scan for the minimum each operation:** A direct scan is simple and takes $O(kn)$ time; with this problem's small $k$ it is practical but does not maintain the minimum incrementally.
- **Sort the whole array each operation:** Sorting can locate the minimum but costs $O(kn \log n)$ and risks losing original positions unless indices are carried along.
- **Heap only the values:** Omitting indices cannot enforce the earliest-occurrence tie rule or update the correct array position.
- When `multiplier` is 1, the selected value never changes, so the same earliest minimum wins every operation.
- A one-element array updates that element exactly `k` times.
- Equal minima are resolved by original array index, not by insertion time after heap replacement.
- Products may exceed the original value bound; later selections use those products normally.
- The result preserves array positions and is not returned in sorted order.
