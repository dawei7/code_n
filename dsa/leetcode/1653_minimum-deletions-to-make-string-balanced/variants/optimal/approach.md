## General

**What a balanced string must look like**

A string containing only `a` and `b` is balanced when no `b` appears before a later `a`. Equivalently, after deletions, the string must have the form

$$
\text{zero or more } a\text{s followed by zero or more } b\text{s}.
$$

This reformulation is useful because it exposes the only troublesome event during a left-to-right scan: seeing an `a` after some `b` characters have already appeared. A newly seen `b` can always be placed after the balanced prefix without breaking its order. A newly seen `a` may conflict with earlier `b` characters, so the algorithm must decide which side of that conflict to delete.

**The dynamic-programming state**

The array `f` has `n + 1` entries. The meaning of `f[i]` is the minimum number of deletions needed to make the first `i` characters of `s` balanced. The extra entry `f[0]` represents the empty prefix. An empty string is already balanced, so its deletion cost is zero; the zero-filled allocation establishes that base case automatically.

The loop uses `enumerate(s, 1)`. Starting enumeration at `1` makes `i` equal to the current prefix length rather than the string’s zero-based character index. Thus `f[i - 1]` always describes the prefix before the current character `c`, while `f[i]` is the value being computed after considering `c`.

The scalar `b` counts how many literal `b` characters have occurred in the original prefix scanned so far. It is not the number of `b` characters retained by one particular optimal deletion plan. That distinction is intentional and is central to the second choice made when the current character is `a`.

**Processing a `b`**

If the current character is `b`, the solution sets

`f[i] = f[i - 1]`.

Take any balanced result for the preceding prefix. Appending a `b` to it cannot create a `b`-before-`a` inversion because the new character is at the end and no later `a` has been included yet. Therefore the old minimum number of deletions remains sufficient. It is also impossible for adding a character to reduce the minimum deletions already required by the old prefix, so the same value is optimal.

The method then increments `b` because this original `b` may matter when a later `a` arrives. Notice that no deletion is charged merely for encountering it; keeping it is safe at this moment.

**Processing an `a` and deriving the two choices**

If the current character is `a`, there are two complete ways to repair all possible conflicts.

The first choice is to delete this current `a`. The first `i - 1` characters can be made balanced at cost `f[i - 1]`, and deleting the new character costs one more. This gives `f[i - 1] + 1`. Because the current `a` disappears, it creates no new violation.

The second choice is to keep the current `a`. If it remains, no earlier `b` may remain before it. The scan has counted exactly `b` such original characters, so deleting all of them costs `b`. Once those earlier `b` characters are gone, the remaining earlier characters are all `a`, and keeping the current `a` preserves a string consisting only of `a` characters so far. Thus `b` is a complete valid cost, not merely a local estimate.

The recurrence takes the cheaper choice:

`f[i] = min(f[i - 1] + 1, b)`.

It is natural to wonder why the raw count `b` is compared with a dynamic-programming value that may already reflect other deletions. The two terms describe two independent complete constructions. The first extends an optimal balanced construction for the previous prefix and deletes the new `a`. The second starts from the original current prefix, keeps the new `a`, and removes every earlier `b`. The algorithm does not combine `b` with `f[i - 1]`, because doing so could count deletions from incompatible plans twice.

For the short prefix `bba`, the two choices at the final `a` are: delete that `a` for a total cost of one, or retain it and delete both earlier `b` characters for a total cost of two. The recurrence selects one. For `abbba`, the same comparison chooses between deleting the last `a` once and deleting the three earlier `b` characters.

**Why these choices are exhaustive**

Assume `f[i - 1]` is correct for the previous prefix. For a current `b`, keeping it is always safe, so the recurrence remains optimal as argued above. For a current `a`, any balanced result either deletes this `a` or retains it; there is no third possibility. If it is deleted, at least `f[i - 1] + 1` deletions are necessary, and that bound is achievable. If it is retained, every earlier `b` must be deleted, so at least `b` deletions are necessary, and deleting exactly those characters achieves the bound. Taking the minimum therefore gives the true optimum for prefix `i`.

Starting with the empty-prefix base case, this reasoning applies inductively to every character. After the loop, `f[n]` is consequently the minimum deletion count for the entire string, which is exactly what the method returns.

## Complexity detail

Let `n` be the length of `s`. The loop processes each character once, and each iteration performs only constant-time comparisons, additions, assignments, and possibly an increment. The running time is therefore $O(n)$.

The exact implementation allocates `f` with `n + 1` integer entries, so its auxiliary space usage is $O(n)$. The scalar `b` and loop variables use $O(1)$ additional space. Although the package manifest lists $O(1)$ space, that bound describes the standard space-optimized form of this recurrence, not this exact source. Because each transition reads only `f[i - 1]`, the array can indeed be replaced by one scalar, but this implementation retains every prefix result and therefore uses linear space.

No new string is constructed. The input is only scanned, and deletion choices are represented by counts rather than by physically removing characters.

## Alternatives and edge cases

- **Scalar dynamic programming:** Replace the array with one variable holding the previous minimum, update it with the same recurrence, and keep the `b` counter. This preserves $O(n)$ time while reducing auxiliary space to $O(1)$; it is the implementation that matches the manifest’s space bound.
- **Choose a split point:** A balanced result has some boundary with retained `a` characters on the left and retained `b` characters on the right. Prefix counts can evaluate every boundary by adding the `b` count to its left and the `a` count to its right. This is also $O(n)$ time, but usually requires extra counts or a preliminary pass.
- **Stack-style cancellation:** One can match a previously seen `b` with a later `a` and count the cheaper repairs, but the state is less direct and can obscure why the result is globally minimal.
- **All `a` characters:** The `b` counter stays zero, every `a` compares deletion against zero, and the answer remains zero.
- **All `b` characters:** Every new `b` safely extends the prefix, so every `f[i]` remains zero even though `b` grows.
- **Already balanced mixed string:** For a string such as `aaabbb`, no `a` is encountered after `b` becomes positive, so no deletion is needed.
- **Reverse-ordered string:** For a string such as `bbbaaa`, each later `a` compares deleting accumulated `a` characters with deleting the earlier `b` block, allowing the minimum side of the conflict to win.
- **Ties between the two choices:** If `f[i - 1] + 1 == b`, either construction is optimal. The method stores only the common count because the problem asks for the minimum number, not an actual edited string.
- **Single character:** Either `a` or `b` alone is balanced. The recurrence returns zero in both cases.
