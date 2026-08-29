## General

The output itself may contain many strings, so the source generates only valid prefixes rather than examining all $2^n$ binary strings and filtering afterward.

A depth-first search processes positions from left to right. Its state contains:

- `i`: the next index to fill;
- `tot`: the sum of indices currently holding one;
- `path`: the chosen characters for positions zero through `i - 1`.

At every position, placing zero is always legal. Placing one is legal only if the previous character is not one and the new total cost does not exceed `k`.

**The zero branch**

The source first appends `"0"`, calls `dfs(i + 1, tot)`, and then pops the character.

Zero adds nothing to the cost and cannot create consecutive ones, so this branch never needs a guard. It also guarantees that every valid prefix has at least one completion: append zero at every remaining position.

Popping after recursion restores `path` to its exact state before the choice. This backtracking step is essential; otherwise the later one branch would still contain the zero just explored.

**The one branch and adjacency check**

After the zero branch has been popped, `path` again contains exactly the first `i` chosen characters. The expression

`not path or path[-1] == "0"`

means:

- at index zero, there is no previous character, so one is allowed;
- at any later index, one is allowed only when position `i - 1` contains zero.

This prevents `"11"` from ever becoming a prefix. Once two consecutive ones appear, no later suffix can repair them, so pruning at the moment of creation is complete and safe.

**The cost guard**

Placing one at index `i` adds exactly `i` to the defined cost. The new cost would be `tot + i`, so the source also requires:

`tot + i <= k`.

All future cost additions are nonnegative indices. If this inequality fails now, extending the prefix can never bring the cost back down, and the branch contains no valid output. It is therefore safe to omit it entirely.

When both guards pass, the source appends `"1"`, recurses with `tot + i`, and pops afterward.

Index zero contributes zero. This is why a one at the first position remains legal even when `k = 0`.

**Emit a string only at full length**

When `i >= n`, `path` contains exactly $n$ characters. Every one was added through both guards, so:

- no adjacent pair is `11`;
- the accumulated index sum is at most `k`.

The source joins the characters and appends the resulting string to `ans`.

It does not append incomplete prefixes. Every returned entry therefore has the required length.

**Why every valid string is generated**

Take any valid length-$n$ binary string. Follow its characters through the recursion.

Whenever the target character is zero, the unconditional zero branch exists. Whenever it is one, validity guarantees that the preceding character is not one. Its prefix cost cannot exceed the complete string's cost, which is at most `k`, so the cost guard also passes.

Thus the recursion has a path matching every valid string all the way to a leaf.

Different recursion paths differ at the first position where they choose different characters, so no two leaves produce the same string. Combined with the leaf validity argument, `ans` contains every required string exactly once.

**Generation order is irrelevant**

The source explores zero before one, which tends to produce strings in ascending binary/lexicographic order. The contract allows any order, so correctness does not depend on this choice.

The local function captures `ans` and `path` from the enclosing method. At any time, only one mutable path is stored; copying occurs only when `"".join(path)` creates a completed output string.

**A trace for the first positions**

For $n=3$ and $k=1$:

- `000` reaches a leaf with cost zero;
- `001` is pruned when placing one at index two would cost two;
- `010` reaches cost one;
- after choosing one at index one, the one branch at index two is forbidden by adjacency;
- `100` reaches cost zero;
- `101` is pruned because index-two cost would be two.

The emitted set is exactly `000`, `010`, and `100`.

## Complexity detail

Let $R$ be the number of returned strings. Materializing each output string requires joining $n$ characters, so output construction alone costs $\Theta(nR)$ time and $\Theta(nR)$ output space.

The pruned recursion tree contains prefixes of valid outputs. Every visited prefix can be charged to at least one valid zero-completed leaf, giving the stated output-sensitive $O(nR)$ time bound.

The recursion depth and mutable `path` length are at most $n$, so auxiliary space excluding returned strings is $O(n)$. Including `ans` and its strings, total storage is $O(nR)$.

These bounds match the manifest's convention of reporting $O(n)$ auxiliary space separately from required output storage.

## Alternatives and edge cases

- **Enumerate all $2^n$ strings then filter:** This wastes work on prefixes that already contain `11` or exceed the cost. Backtracking prunes both immediately.
- **Dynamic programming that only counts strings:** Counting can be faster when only a number is required, but it cannot produce the requested list without reconstruction.
- **Track remaining budget instead of total cost:** This is equivalent; subtract index `i` when placing one and require the result to remain nonnegative.
- **Check adjacency only at the leaf:** Invalid `11` prefixes would generate exponentially many useless descendants.
- **Prune a high current cost assuming later zeroes help:** Zeroes add no cost but cannot reduce it. Once above `k`, the branch is permanently invalid.
- **`n = 1, k = 0`:** Both `"0"` and `"1"` are valid because the only one would be at index zero and costs zero.
- **`k = 0` with larger `n`:** A one is possible only at index zero; all positive-index ones exceed the cost.
- **All-zero string:** It is always generated and always valid.
- **One at index zero:** It contributes no cost but still prevents a one at index one through the adjacency guard.
- **Maximum `k`:** Cost pruning may disappear, but adjacency pruning still generates only Fibonacci-many no-consecutive-one strings.
- **Backtracking pop operations:** Each append is paired with a pop, ensuring sibling branches begin from the same prefix.
- **No duplicates:** Each leaf corresponds to one unique sequence of binary choices.
- **Recursion depth:** The constraint $n\le12$ keeps Python recursion safely shallow.
