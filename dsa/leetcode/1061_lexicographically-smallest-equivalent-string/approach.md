## General

**Equivalence pairs form connected components**

Every aligned pair `s1[i]` and `s2[i]` says that two letters are equivalent. Symmetry makes that relation undirected, and transitivity means a chain of pairs joins every letter in the same equivalence group.

This can be viewed as a graph whose 26 lowercase letters are vertices. Each given pair is an edge. Every connected component is one equivalence class: any character in that component may replace any other.

To make `baseStr` lexicographically smallest, every character should become the smallest letter in its component. Choosing a larger equivalent letter at any position could only make the result larger, and choices at different positions do not constrain each other.

The solution maintains these components with a disjoint-set union structure, also called union-find.

**Represent letters as small integer nodes**

The parent array begins as:

```python
p = list(range(26))
```

Letter `"a"` maps to node zero, `"b"` to one, and so through `"z"` at node 25. Initially `p[x] == x` for every node, so each letter is the sole member and representative of its own component.

The representative is not arbitrary in this implementation. The union operation always chooses the smaller root. As a result, a component's representative is always its lexicographically smallest character.

**Find the current component root**

The nested function is:

```python
def find(x: int) -> int:
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]
```

A root points to itself. If `p[x] == x`, the function returns `x` immediately.

Otherwise, `x` points toward another node in the same component. The recursive call follows parent links until it reaches the root. Then:

```python
p[x] = find(p[x])
```

rewrites `x`'s parent to point directly at that root. This is path compression. Later searches from `x`, and often from nodes on related paths, become shorter.

The returned value is always the current representative of `x`'s complete equivalence class, not merely its immediate parent.

**Merge every stated equivalence**

The code visits aligned pairs with:

```python
for a, b in zip(s1, s2):
```

The strings have equal length by contract, so `zip` processes every index and truncates neither string.

Each letter is converted to its zero-based node:

```python
x, y = ord(a) - ord("a"), ord(b) - ord("a")
```

`ord` returns a character's numeric code. Subtracting the code of `"a"` makes lowercase letters contiguous nodes from zero to 25.

The current roots are then found:

```python
px, py = find(x), find(y)
```

It is the roots, not necessarily the original nodes, that must be joined. Connecting roots merges whole existing components and therefore captures transitivity.

**Always preserve the smallest component representative**

The merge is:

```python
if px < py:
    p[py] = px
else:
    p[px] = py
```

If the roots differ, the numerically larger root becomes a child of the smaller root. Numeric node order is alphabetic character order, so the merged component keeps its smallest letter as root.

If `px == py`, the letters are already in the same component. The `else` branch assigns that root to itself, which changes nothing.

Why does the root remain the minimum of the whole component? Initially every singleton root is trivially its minimum. Before a merge, assume `px` and `py` are the minima of their respective components. The smaller of those two roots is also the minimum across their union, and the code makes it the new root. By induction, the invariant holds after every equivalence pair.

For example, if one component contains `"c"` and `"e"` with root `"c"`, and another contains `"a"` and `"f"` with root `"a"`, merging any member from the two components finds roots `"c"` and `"a"`. The union attaches `"c"` below `"a"`, so all four letters now map to `"a"`.

**Convert every base character through its representative**

The answer is built with:

```python
return "".join(
    chr(find(ord(c) - ord("a")) + ord("a"))
    for c in baseStr
)
```

For each character `c`:

1. Convert it to a node from zero through 25.
2. Find its component root.
3. Convert that root back to a lowercase character with `chr`.

`chr` reverses `ord`. Adding `ord("a")` turns node zero back into `"a"`, node one into `"b"`, and so on.

The generator supplies mapped characters one at a time to `join`. `join` concatenates them in the original position order, producing a string of the same length as `baseStr`.

Letters never mentioned by `s1` or `s2` remain singleton components. Their root is themselves, so they appear unchanged in the answer.

**Why mapping every position to its root is globally optimal**

For any base character, its component contains exactly the letters equivalent to it by reflexivity, symmetry, and transitivity. The root invariant says `find` returns the smallest one.

Replacing that position by the root is therefore a valid equivalence substitution and is the smallest value available at that position.

Lexicographic order examines the first position where two candidate strings differ. At that position, the root-based string cannot contain a larger character than another valid equivalent string, because it chose the minimum available character. Applying that argument from left to right proves no valid result can be lexicographically smaller.

There is no tradeoff between positions: using a character as a replacement does not consume it or change equivalence choices elsewhere. Independent per-position minima form the global minimum string.

## Complexity detail

Let `P` be the number of equivalence pairs, `B` the length of `baseStr`, and `A = 26` the lowercase alphabet size.

Initializing the parent array takes `O(A)` time. The solution performs two `find` calls for each of `P` pairs and one `find` call for each of `B` output characters. Path compression shortens parent paths, and the alphabet is a fixed 26 nodes. Under this problem's fixed-alphabet model, every operation is bounded by a constant, so total time is `O(P + B + A)`.

The parent array uses `O(A)` auxiliary space. Recursive `find` depth is at most `A`, also constant here. Excluding the required returned string, auxiliary space is `O(A)`. The output itself necessarily contains `B` characters.

The exact union policy chooses the smaller root rather than union by rank or size. For a hypothetical alphabet whose size grows without bound, parent chains can be deeper than a standard rank-balanced union-find tree, even with path compression. The fixed 26-letter contract is why the manifest's simple linear bound accurately describes this task. A generalized implementation can store the minimum letter as component metadata while using union by rank for the usual near-constant amortized operations.

## Alternatives and edge cases

- **Graph plus depth-first search:** Build an undirected graph on the alphabet, find each connected component, record its smallest character, and map `baseStr`. This takes `O(P + B + A)` time with adjacency lists and is equally valid.
- **Adjacency matrix:** A 26 by 26 Boolean matrix plus DFS is simple because the alphabet is tiny, but it uses `O(A^2)` space rather than `O(A)` disjoint-set storage.
- **Repeated transitive closure:** Floyd–Warshall can compute equivalence reachability in `O(A^3)` time. It is acceptable for 26 letters but unnecessarily heavy.
- **Union by rank with minimum metadata:** For a growing alphabet, balance trees by rank and separately store the minimum node of each component. This preserves efficient general union-find behavior without requiring the root itself to be the minimum.
- **Same character paired with itself:** Both roots are equal, and the self-parent assignment changes nothing.
- **Repeated equivalence pair:** The second and later merges find the same root and are harmless.
- **Transitive chain:** Pairs such as `a = b` and `b = c` merge all three nodes, and `find(c)` returns `a`.
- **Equivalence pair order:** Components and their minima do not depend on the order in which edges are processed. The smaller-root invariant produces the same final representative.
- **Unmentioned base character:** It remains its own representative and is copied unchanged.
- **All letters equivalent:** Every component merge eventually has root zero, so every base character becomes `"a"`.
- **No useful change:** If each base character is already the smallest in its component, the returned string equals `baseStr`.
- **Duplicate base characters:** Each occurrence is mapped independently to the same root. The generator does not cache explicitly, but path compression makes repeated finds short.
- **Equal input lengths:** `zip` relies on the contract that `s1` and `s2` have equal length. With unequal strings it would silently ignore an unmatched suffix.
- **Input preservation:** Strings are immutable. Only the private parent array changes during unions and path compression.
