## General

A substring is valid when its number of ones is at least the square of its number of zeros. If a substring contains $z$ zeros and $o$ ones, the condition is

$$
o\ge z^2.
$$

Checking all $O(n^2)$ substrings is too slow for $n$ up to $4\cdot10^4$. The square in the condition supplies the useful restriction: a valid substring containing $z$ zeros needs length at least $z+z^2$. Since its length cannot exceed $n$, only $z=O(\sqrt n)$ can be relevant. The solution fixes each starting index and visits groups of endings according to how many zeros they contain, jumping directly from one zero to the next.

**Precompute the next zero.** The array `nxt` has length `n + 1` and is initially filled with `n`, a sentinel meaning “there is no zero at or after this position.” Scanning from right to left, `nxt[i]` first inherits `nxt[i + 1]`. If `s[i] == "0"`, it is overwritten with `i`. Therefore, after preprocessing, `nxt[i]` is the smallest zero index greater than or equal to `i`, or `n` if none exists.

Fix a substring start `i`. The variable `j` identifies the most recently included zero, except in the initial zero-free state where it starts at `i`. The variable `cnt0` is the number $z$ of zeros in the current group: it begins at one if `s[i]` is zero and at zero otherwise. The next zero strictly after `j` is `nxt[j + 1]`. Every ending index from `j` through `nxt[j + 1] - 1` gives a substring with this same number of zeros. Moving the ending across `nxt[j + 1]` would add another zero and begin the next group.

The farthest ending before that next zero has

`cnt1 = (nxt[j + 1] - i) - cnt0`

ones. The span from `i` through `nxt[j + 1] - 1` has length `nxt[j + 1] - i`; subtracting its `cnt0` zeros leaves exactly its number of ones. This is the maximum number of ones available among endings in the current group.

If `cnt1 < cnt0 * cnt0`, even the farthest possible ending in the group lacks enough ones. Every earlier ending has no more ones, so the group contributes nothing. If `cnt1 >= cnt0 * cnt0`, the farthest ending is valid. Moving the ending left across one of the consecutive ones after `j` removes exactly one one while leaving the zero count unchanged. Consequently, the number of valid endings supported by the ones surplus is

`cnt1 - cnt0 * cnt0 + 1`.

The plus one includes the ending with exactly the required number of ones. However, there are only `nxt[j + 1] - j` candidate ending positions in this zero-count group. The contribution is therefore the smaller of the available positions and the surplus-based count:

`min(nxt[j + 1] - j, cnt1 - cnt0 * cnt0 + 1)`.

This formula also handles the zero-free case. When `cnt0 = 0`, the requirement is zero ones, so every nonempty all-one substring beginning at `i` is valid. Before the next zero, `j = i` and the minimum adds exactly the number of possible endings from `i` to the character before that zero.

After counting the current group, the solution jumps with `j = nxt[j + 1]`. This makes `j` the next zero rather than advancing one character at a time, and `cnt0` is incremented. The next iteration considers all endings after that zero and before the following zero. No ending is counted twice because each ending belongs to exactly one group determined by its zero count, and no ending is skipped because consecutive groups meet at successive zero positions.

For a small trace, take `s = "011"` and start at `i = 0`. Initially `cnt0 = 1` and `j = 0`. There is no later zero, so `nxt[j + 1] = 3`. The farthest substring `"011"` has `cnt1 = (3 - 0) - 1 = 2` ones. One zero needs at least one one. The contribution is `min(3 - 0, 2 - 1 + 1) = 2`, representing `"01"` and `"011"`; the ending at zero alone is invalid. Starting at index one enters the zero-free case and counts `"1"` and `"11"`. Starting at index two counts the final `"1"`.

**Why the loop stops near the square root.** The inner condition is `cnt0 * cnt0 <= n`. Once $z^2>n$, no substring of total length at most $n$ can contain the required $z^2$ ones, even before accounting for the $z$ zeros themselves. Further zero groups are impossible, so stopping is safe. The additional condition `j < n` stops when the sentinel says there is no next zero to process. The $z^2\le n$ bound is slightly looser than the exact necessary condition $z^2+z\le n$, but it still limits the iterations to $O(\sqrt n)$ and never excludes a valid substring.

**Why the total is correct.** For every fixed start `i`, the loop partitions all relevant ending positions by their exact number of zeros. Within one group, ones increase by one at each step after the last included zero, so the valid endings form a contiguous suffix. The arithmetic formula counts precisely that suffix. Groups with too many zeros cannot satisfy the dominance inequality and are safely omitted. Summing these disjoint, exact contributions over every start counts each dominant substring once and only once.

## Complexity detail

Let $n$ be the length of `s`. Building `nxt` takes $O(n)$ time and $O(n)$ space. There are $n$ choices for `i`. For each one, `cnt0` increases once per inner iteration and never exceeds $\lfloor\sqrt n\rfloor+1$ while the loop continues. Every iteration performs constant-time indexing and arithmetic, so the nested loops take $O(n\sqrt n)$ time.

The `nxt` table is the only data structure that grows with the input, giving $O(n)$ auxiliary space. Variables such as `ans`, `cnt0`, `cnt1`, and `j` use $O(1)$ additional storage. Python's integer `ans` safely holds the maximum substring count $n(n+1)/2$.

Jumping between zeros is essential to the time bound. The algorithm does not scan an $O(n)$ suffix for every start; it processes at most one constant-time group for each feasible zero count.

## Alternatives and edge cases

- **Enumerate all substrings with prefix sums:** Prefix zero and one counts make checking one substring $O(1)$, but there are still $O(n^2)$ substrings. This is useful as a brute-force verifier for small strings, not for the full constraint.
- **Editorial's reversed orientation:** One can fix a right endpoint and jump left through previous-zero positions. It uses the same grouping and arithmetic idea. The source solution fixes the left endpoint and uses next-zero positions; mixing the two orientations would make the endpoint formula incorrect.
- **Count zero-free substrings separately:** Runs of ones contribute $L(L+1)/2$ valid substrings and could be counted in a separate pass. The exact solution includes them naturally as the `cnt0 = 0` group, avoiding a separate case.
- **Use a list of zero indices:** Storing only zero positions with sentinels can support similar enumeration. The `nxt` array consumes $O(n)$ space but gives direct constant-time jumps from any starting position.
- **All ones:** Every substring has zero zeros, and $o\ge0$ always holds. For each start, the first iteration counts all remaining endings, after which `j` becomes `n`. The result is $n(n+1)/2$.
- **All zeros:** A substring containing any zero has no ones and cannot satisfy $0\ge z^2$ for positive $z$. Each group fails the `cnt1` test, so the answer is zero.
- **One zero followed by ones:** Endings become valid only after at least one following one is included. The surplus formula excludes the too-short prefix and then counts every longer ending.
- **Sentinel access:** Because `nxt` has length `n + 1`, reading `nxt[j + 1]` is safe whenever `j < n`, including `j = n - 1`. The sentinel value `n` also makes the final run of ones behave like an ordinary gap before a next zero.
- **Nonempty substrings only:** In the zero-free group, the cap `nxt[j + 1] - j` prevents the extra “plus one” in the surplus expression from accidentally counting an empty substring.
- **Large answer:** The number of valid substrings can be quadratic even though the algorithm is subquadratic. A fixed-width implementation should use a 64-bit result; Python integers expand automatically.
