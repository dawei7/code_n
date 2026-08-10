## General

**Remember only the final run of equal colors**

When choosing a color for the next fence post, the entire earlier coloring does not matter. The only dangerous situation is whether the current coloring already ends with two equal colors. If it does, using that same color again would create a forbidden run of three. If the last color occurs only once at the end, using it one more time is safe.

This suggests two dynamic-programming states for every prefix of the fence. In the exact source, array index `i` represents a fence of `i + 1` posts:

- `f[i]` counts valid colorings whose final color differs from the preceding post. Equivalently, the last same-color run has length one. For the one-post base case, this state also contains all colorings because there is no previous post to match.
- `g[i]` counts valid colorings whose last two posts have the same color. Because every represented coloring is valid, that final same-color run has length exactly two, never three or more.

These states are disjoint and exhaustive. Every valid nonempty coloring ends with either one copy or two copies of its final color. It cannot end with three copies because that would violate the rule. Therefore, the total number of valid colorings of `i + 1` posts is `f[i] + g[i]`.

**Establish the one-post base state**

For the first post, any of the $k$ colors may be chosen. The source sets

$$
f[0]=k,
\qquad
g[0]=0.
$$

Placing the one-post colorings in `f` means “the final run has length one,” which is the useful interpretation even though no comparison with a previous post exists. No one-post coloring can end with two equal posts, so `g[0]` is zero.

This base representation lets the same transitions handle the second post without a separate case.

**Transition by painting the new post a different color**

Take any valid coloring of the first `i` posts. It is counted in either `f[i - 1]` or `g[i - 1]`. If the new post uses a color different from the previous post, the old same-color run ends and the new final run has length one. The result belongs to `f[i]`.

For each prior coloring, exactly one of the $k$ colors matches the previous post, so there are $k-1$ different choices. Hence

$$
f[i]
=
\bigl(f[i-1]+g[i-1]\bigr)(k-1).
$$

Changing color is always safe, even when the old coloring ended with two equal posts, because the new color breaks that run. Every new coloring in this state is counted once: removing its final post reveals its unique prior coloring, and its final color is the unique chosen different color.

**Transition by repeating the previous color**

To make the final two posts equal, the new post must use exactly the previous post's color, so there is one color choice rather than $k-1$ choices. This repetition is legal only when the prior coloring ended with a run of length one, represented by `f[i - 1]`. Repeating a coloring from `g[i - 1]` would extend a length-two run to length three and must be forbidden.

Therefore,

$$
g[i]=f[i-1].
$$

The absence of a multiplication factor is intentional. Once a particular prior coloring is fixed, its last color is already known, and exactly one new color matches it.

**Why the transitions count every valid coloring exactly once**

Consider any valid coloring of `i + 1` posts. Compare its last post with the preceding post.

If they differ, deleting the last post leaves any valid length-`i` coloring, and the deleted color is one of the $k-1$ colors different from its final color. This construction is counted in the formula for `f[i]`.

If they match, validity guarantees that the two posts before the new one did not already match. Deleting the last post therefore leaves a coloring in `f[i - 1]`, and reattaching the unique matching color is counted in `g[i]`.

The two cases cannot overlap because the final pair cannot be both equal and different. Every valid coloring belongs to one case, so the recurrence omits none and double-counts none. Conversely, each transition preserves the no-three-equal rule, so it creates no invalid coloring.

**Trace `n = 3, k = 2`**

With two colors, the arrays evolve as follows:

| Posts represented | `f`: final run length 1 | `g`: final run length 2 | Total |
|---:|---:|---:|---:|
| 1 | 2 | 0 | 2 |
| 2 | $(2+0)(2-1)=2$ | 2 | 4 |
| 3 | $(2+2)(2-1)=4$ | 2 | 6 |

There are $2^3=8$ unrestricted three-post colorings. The two monochromatic colorings are forbidden, leaving six, exactly as the dynamic program reports.

For `n = 7, k = 2`, the totals are `2, 4, 6, 10, 16, 26, 42`. Each new total is split between endings with a one-post final run and endings with a two-post final run, yielding the expected answer 42.

**Return both valid ending types**

After processing all `n` posts, either state is acceptable. A fence may validly end with one occurrence of its last color or with two. The source therefore returns `f[-1] + g[-1]`.

The constraint $n\ge1$ ensures both arrays are nonempty and index `-1` refers to the state for exactly `n` posts.

## Complexity detail

The loop processes indices 1 through `n - 1`, doing constant arithmetic at each index. Time complexity is $O(n)$.

The exact source allocates two arrays of length $n$, so its auxiliary space complexity is $O(n)$. This differs from the manifest summary and $O(1)$ space bound, which describe a scalar-state optimization rather than the protected implementation.

Only the immediately preceding `f` and `g` values are needed to compute the next pair. The two arrays could therefore be replaced by two variables and updated carefully, reducing auxiliary space to $O(1)$ without changing the recurrence or $O(n)$ time. The source retains the full arrays even though older entries are never read again.

The answer is guaranteed to fit in a signed 32-bit integer. Python integers would grow safely even without that guarantee, but in fixed-width languages the stated bound prevents overflow for legal test cases.

## Alternatives and edge cases

- **Two scalar states:** Keep only the previous `different` and `same` counts, compute both next values from the old pair, and replace them together. This is the constant-space approach described by the manifest and has $O(n)$ time with $O(1)$ auxiliary space.
- **One total recurrence:** With $T(1)=k$ and $T(2)=k^2$, use $T(i)=(k-1)(T(i-1)+T(i-2))$ for later lengths. This follows from the two-state recurrence, but the explicit states make the no-three-equal reasoning easier to derive and verify.
- **Top-down memoization:** Recursively compute counts by remaining position and ending-run state. Memoization avoids exponential recomputation but uses $O(n)$ memo and call-stack space and adds recursion overhead.
- **Enumerate all colorings:** Trying all $k^n$ assignments and validating each one is exponential. The DP groups many prefixes together because only their final run length affects future choices.
- **`n = 1`:** The loop does not run, and `f[0] + g[0] = k`, one choice for each color.
- **`k = 1, n = 1`:** The one post can use the sole color, so the answer is 1.
- **`k = 1, n = 2`:** The second post may match the first, producing exactly one valid coloring. The recurrence moves the count from `f` to `g`.
- **`k = 1, n >= 3`:** The factor `k - 1` is zero, so no different-color ending can be created. After two posts, repeating again is forbidden, and all later totals become zero.
- **Two equal posts are allowed:** `g` is a valid state, not an error state. Only a transition that repeats from `g` is excluded.
- **Large number of colors:** The recurrence counts choices symbolically using $k-1$; it does not loop across colors, so runtime depends on `n`, not on `k` under standard integer arithmetic.
- **Simultaneous scalar updates:** In a constant-space rewrite, compute new values before overwriting either old state. Updating `f` first and then using that new value for `g` would implement the wrong recurrence.
- **Zero posts outside the contract:** The source allocates empty arrays and later accesses `f[0]` and `f[-1]`, so it relies on the stated $n\ge1$ precondition.
