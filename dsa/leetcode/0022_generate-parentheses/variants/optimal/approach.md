## General

**Generate only prefixes that can still become valid**

A brute-force generator would make all $2^{2n}$ strings of length $2n$ and reject most afterward. The selected depth-first search prunes a prefix as soon as it violates one of the three facts every well-formed final string must satisfy:

- it cannot use more than $n$ opening parentheses;
- it cannot use more than $n$ closing parentheses; and
- in every prefix, the number of closers cannot exceed the number of openers.

The third rule is the important ordering rule. A closer needs an earlier unmatched opener. Once a prefix has more `)` than `(`, adding characters later can never repair that already-unmatched closer.

**Understand what `l`, `r`, and `t` mean**

In `dfs(l, r, t)`, `l` is the number of opening parentheses already placed, `r` is the number of closing parentheses already placed, and `t` is the exact prefix built by those choices. Consequently,

$$
\lvert t\rvert=l+r.
$$

The initial call `dfs(0, 0, "")` represents the empty prefix. Each opening branch increases `l` and appends `(`; each closing branch increases `r` and appends `)`. Keeping counts as parameters avoids rescanning `t` on every call.

**Prune all impossible states at one entrance guard**

The first condition is

```python
if l > n or r > n or l < r:
    return
```

Each operand identifies a permanently impossible prefix. `l > n` or `r > n` means the required exact count has already been exceeded. `l < r` means some closer appeared without an unmatched opener before it. The use of `or` means any single violation is enough to abandon the whole subtree.

This implementation deliberately makes both recursive calls from every non-complete valid state and lets the next call reject an illegal choice. For example, it may call the closing branch from the empty prefix, producing counts `(0, 1)` and text `")"`; that child immediately returns because `l < r`. A more selective backtracker could test legality before making each call, but both organizations enumerate the same valid leaves.

**Recognize a complete answer from the counts**

After surviving the guard, a state with

```python
if l == n and r == n:
```

has length $2n$, contains exactly the required number of each character, and has never violated the prefix rule. It is therefore well formed and is appended directly to `ans`.

The immediate `return` after appending is necessary. No more parentheses may be added to a complete result, and calling children would only create over-limit states.

**Explore opening before closing**

For every remaining valid non-leaf state, the exact source executes

```python
dfs(l + 1, r, t + "(")
dfs(l, r + 1, t + ")")
```

Depth-first execution completes the entire opening-child subtree before trying the closing child. This choice determines the returned order: more heavily nested strings tend to appear first. The contract permits any order, so ordering is not part of correctness.

Strings in Python are immutable. `t + "("` and `t + ")"` create new prefix strings, so sibling branches cannot overwrite one another. No explicit pop or undo operation is needed. This makes the source compact, though it has a real space and copying cost discussed below.

**Trace the beginning for `n = 3`**

From `(0, 0, "")`, the opening child `(1, 0, "(")` is valid; the closing child `(0, 1, ")")` will be rejected. The DFS continues preferring openings until it reaches `(3, 0, "(((")`. Another opening call exceeds `n` and returns. Closing choices then build `"((()))"`, the first completed answer.

Backtracking occurs through function returns. The search revisits the most recent state with an unexplored closing branch, eventually building `"(()())"`, `"(())()"`, `"()(())"`, and `"()()()"`. Prefixes such as `"())"` are cut off at once because their counts satisfy $l<r$.

**Why every generated string is valid**

An appended string has exactly $n$ openers and $n$ closers. Every prefix on its recursion path survived `l < r`, so no prefix has more closers than openers. These two facts are the standard characterization of a well-formed parenthesis string: each closer can match a preceding unmatched opener, and equal final counts leave none unmatched.

**Why every valid string is generated exactly once**

Take any well-formed result and read it left to right. At each position, the DFS has a corresponding branch: the opening call for `(` or the closing call for `)`. Because the target string never exceeds either count and never has more prefix closers, none of those chosen states is pruned. The search therefore reaches and appends it.

Different root-to-leaf branch sequences produce different character strings at the first position where their choices differ. Hence no valid string is appended twice. Together, the safety, completeness, and uniqueness arguments prove that `ans` is exactly the requested set.

## Complexity detail

Let

$$
C_n=\frac{1}{n+1}\binom{2n}{n}
$$

be the $n$th Catalan number, which is the number of valid outputs. Every result has length $2n$.

- **Output lower bound: $\Omega(nC_n)$.** Merely materializing $C_n$ strings of length $2n$ requires this much character work and output storage.
- **Customary backtracking time: $O(nC_n)$.** This is the manifest bound for a pruned generator with constant-time append/pop operations and $O(n)$ work to copy each completed result.
- **Exact immutable-string caveat:** This source constructs `t + "("` and `t + ")"` at every explored edge. Concatenation copies a prefix whose length can be $O(n)$. Because the valid-prefix search tree can contain $O(nC_n)$ nodes, a conservative bound for the exact Python operations is $O(n^2C_n)$. The small constraint $n\le8$ keeps this harmless, but it is important not to describe immutable concatenation as constant time.
- **Auxiliary space of the exact source: up to $O(n^2)$, excluding `ans`.** Recursion depth is $2n=O(n)$. However, frames along one path retain immutable prefix strings of lengths $0,1,\ldots,2n$, whose total character storage is $O(n^2)$. A mutable character buffer would reduce the non-output space to $O(n)$, matching the manifest. The answer itself occupies $O(nC_n)$ characters.

Thus the manifest describes the standard mutable-buffer implementation more precisely than this exact immutable-string source. The algorithmic idea remains output-optimal up to polynomial string-construction overhead.

## Alternatives and edge cases

- **Mutable-list backtracking:** Append a parenthesis, recurse, and pop it. Join only at complete leaves. This preserves the same search tree while achieving the standard $O(nC_n)$ time and $O(n)$ auxiliary-space bounds.
- **Explicit iterative event stack:** Simulate recursive calls and undo operations without Python recursion; this is the Competitive variant and maintains a single mutable path.
- **Generate all binary strings then validate:** It considers $4^n$ complete candidates and spends additional time validating them, wasting work on prefixes already known to be impossible.
- **Catalan divide and conquer:** Construct each result as `"(" + left + ")" + right` over smaller valid sets. It follows the Catalan recurrence but benefits from memoization to avoid repeating subproblems.
- **`n = 1`:** The only surviving complete path is `"()"`.
- **Maximum `n = 8`:** The output contains $C_8=1430$ strings, each of length 16; output size itself is substantial but bounded.
- **Closing at the empty prefix:** The source makes that child call, then `l < r` immediately prunes it.
- **Too many openers or closers:** The `l > n` and `r > n` guards reject these calls before they can append anything.
- **Order is incidental:** Opening-first DFS determines a stable order, but consumers must not rely on it because the contract allows any order.
- **Positive-`n` contract:** The supplied domain starts at one. If called with `n = 0`, the exact code would append and return `['']`, the conventional representation of the one empty balanced sequence.
