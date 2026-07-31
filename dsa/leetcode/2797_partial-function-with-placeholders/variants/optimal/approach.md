## General

**Consume replacements only at captured placeholders**

The array supplied to `partial` is a template. Keep it in the returned closure, but do not modify it: the returned function may be called more than once with different values. On each call, create a fresh `merged` array and a `restIndex` initially equal to zero.

Scan the captured `args` from left to right. A value other than `"_"` is fixed, so copy it directly. For a placeholder, copy `restArgs[restIndex]` and advance `restIndex`. Because the contract guarantees at least as many call-time values as placeholders, every placeholder receives exactly one value. The monotone index makes the first placeholder consume the first call-time value, the second consume the second, and so on.

**Append the unused suffix and invoke once**

After the template scan, `restIndex` equals the number of placeholders. Append `restArgs` from that index onward, preserving the order of every surplus value. The resulting array therefore contains the fixed entries and replacements in template order followed by precisely the unused call-time suffix.

Invoke `fn` once with `merged` as separate arguments. Using `fn.apply(this, merged)` also forwards the dynamic receiver of the returned ordinary function; this does not change the required argument transformation and avoids unnecessarily discarding normal JavaScript call semantics.

## Complexity detail

Let $a = \lvert\texttt{args}\rvert$ and $r = \lvert\texttt{restArgs}\rvert$. Each captured entry and each unused call-time entry is visited once, so invocation takes $O(a + r)$ time. The fresh merged argument array contains at most $a + r$ values and uses $O(a + r)$ auxiliary space. Creating the closure itself takes $O(1)$ additional time and space because it retains references to `fn` and `args`.

The package uses an asymptotic-optimality certificate. Any correct algorithm must inspect all $a$ captured entries to determine which are placeholders, and the zero-placeholder case requires forwarding all $r$ call-time values. That gives a worst-case $\Omega(a + r)$ lower bound, matched by the accepted source.

## Alternatives and edge cases

- **Repeated `shift`:** Consuming `restArgs.shift()` is concise, but shifting an array repeatedly moves later elements and can make the merge quadratic.
- **Mutate the captured template:** Replacing placeholders directly in `args` can work once, but later calls observe values from the first invocation instead of fresh placeholders.
- **Multiple mapping and filtering passes:** Separate transformations can remain linear, but they allocate extra intermediate arrays and obscure which call-time values remain.
- With no placeholders, every call-time value is appended after the captured array.
- With all captured entries as placeholders, the first $a$ call-time values replace them and only the remaining suffix is appended.
- A call-time value equal to `"_"` is ordinary data; only `"_"` entries in the captured template are placeholders.
- Objects, arrays, `null`, and other JSON values must be forwarded without conversion or flattening.
- The returned function can be invoked repeatedly, so neither captured `args` nor a previous merged array may be reused as mutable output state.
