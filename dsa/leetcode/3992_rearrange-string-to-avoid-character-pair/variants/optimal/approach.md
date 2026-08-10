## General

The requirement says every occurrence of `y` must appear before every occurrence of `x`. It places no restrictions on where other letters appear relative to `x`, and it does not require lexicographically smallest output.

A sufficient construction is therefore:

1. move every `y` into a prefix;
2. leave every non-`y` character somewhere after that prefix.

Since `x\ne y`, every `x` belongs to the non-`y` suffix. All `y` positions then precede all `x` positions automatically.

The source implements this as an in-place partition on a temporary character list.

**Why a list is created**

Python strings are immutable, so individual character swaps cannot be performed directly on `s`. The source creates:

```python
t = list(s)
```

This list contains exactly the same characters and multiplicities as the input.

**Boundary pointer invariant**

The pointer `i` is the next position where a discovered `y` should be placed.

Before processing scan position `j`, the invariant is:

- positions `0` through `i-1` all contain `y`;
- processed positions `i` through `j-1` contain no `y`;
- positions `j` onward are not yet classified by the scan.

Initially `i=0` and the processed region is empty, so the invariant holds.

**Handling a non-`y` character**

If current `c` is not `y`, no swap occurs. It remains in the processed non-`y` region, and `i` does not move.

The invariant extends to include position `j`.

**Handling a `y` character**

When `c==y`, the source swaps:

```python
t[i], t[j] = c, t[i]
i += 1
```

If `i==j`, this is effectively a self-swap and simply extends the `y` prefix.

If `i<j`, invariant says `t[i]` is a processed non-`y` character. The assignment puts the discovered `y` at boundary position `i` and moves that non-`y` character to current position `j`. Both locations now satisfy their new regions, and incrementing `i` extends the prefix by one.

Although the loop enumerates a list that is being modified, the moved character goes to the current already-processing position, not to a future unvisited position. No character is skipped or classified twice.

**Why the output is a permutation**

Every change is a swap of two existing list entries. Swaps preserve:

- total length;
- every character's multiplicity.

Joining the final list therefore produces a permutation of `s`.

**Why every `y` precedes every `x`**

At loop completion, all discovered `y` characters occupy exactly prefix `t[0:i]`. No `y` remains in `t[i:]`.

Because `x` and `y` are distinct, every `x` lies in suffix `t[i:]`. Hence the last `y` index is less than the first `x` index whenever both occur.

If either distinguished letter is absent, the required universal ordering is vacuously true. The partition still returns a valid permutation.

**The exact source is a two-way partition**

The manifest summary describes three groups: all `y` characters, neutral characters, then all `x` characters. The stored source does not separately move `x` to the end. It partitions only into:

- `y`;
- everything that is not `y`.

This is fully sufficient for the contract because every `x` is in the second group. Neutral characters may appear before, between, or after `x` characters inside that suffix.

For example, with `s="aabc"`, `x="a"`, and `y="c"`, moving `c` to the front may produce `"caba"` rather than the sample's `"cbaa"`. Both are valid because all `c` occurrences precede all `a` occurrences.

**Stability is not required**

Swapping a found `y` with the boundary can change the relative order of non-`y` characters. The problem asks for any permutation satisfying the distinguished-letter order, so preserving neutral-character order is unnecessary.

All `y` characters are identical as values, making their own internal order unobservable.

## Complexity detail

Let `n=\lvert s\rvert`. Creating `t` takes `O(n)` time. The scan visits every position once and performs at most one constant-time swap per character, costing `O(n)`. Joining the list into a result string also costs `O(n)`. Total time complexity is `O(n)`.

The character list uses `O(n)` auxiliary space, and the returned string uses `O(n)` output space. All pointer and loop state is constant.

The original string is immutable and remains unchanged.

## Alternatives and edge cases

- **Build three explicit groups:** Concatenating all `y`, neutral characters, and all `x` is valid and matches the manifest summary, but the exact source uses one temporary list and a two-way partition.

- **Sort the entire string:** Sorting may place `x` before `y` depending on alphabetic order and costs `O(n\log n)`. The required order is custom and much simpler.

- **Count characters and rebuild alphabetically:** This can work with special ordering but uses a frequency structure and imposes unnecessary order on neutral letters.

- **Stable filtering:** `y` characters followed by all non-`y` characters preserves suffix order and is easy to express, but needs separately constructed groups. Stability is not required.

- **No `y` present:** The scan performs no swaps and returns the original string, which is valid.

- **No `x` present:** Any permutation is valid; moving `y` to the front remains acceptable.

- **All characters are `y`:** This can occur only with `x` absent because `x\ne y`. Every loop iteration advances `i` and the string remains unchanged.

- **All characters are `x`:** No `y` is found, so the string remains unchanged and the condition is vacuously satisfied.

- **Both letters occur once:** The partition moves the one `y` into the prefix, guaranteeing it precedes the one `x`.

- **Neutral characters:** They may appear anywhere after the `y` prefix, including after or before `x`. The contract does not constrain them.

- **Mutation during enumeration:** Swaps move a processed non-`y` character to the current position, never into an unprocessed future position, so the invariant stays valid.

- **Distinct-letter guarantee:** It ensures no character must simultaneously belong to both ordered groups.

- **Manifest mechanism mismatch:** A separate final `x` group is not constructed. The two-way `y` versus non-`y` partition is the faithful source behavior.
