## General

The string must be divided into codes from `1` through `26`. At any position, a valid final decoding can end in only one of two ways:

- its last letter comes from the final one digit, provided that digit is `1` through `9`; or
- its last letter comes from the final two digits, provided that pair is `10` through `26`.

Those cases are disjoint because they place the final code boundary differently. Their counts can therefore be added. This is the recurrence implemented by the selected solution.

**Definition of the DP state**

Let $f[i]$ be the number of valid ways to decode the prefix containing the first $i$ characters, namely `s[:i]`. The answer is $f[n]$, where $n$ is the string length.

The initialization `f = [1] + [0] * n` makes

$$
f[0]=1.
$$

This does not claim that the challenge's nonempty message has one visible decoding when empty. It is a counting base case: there is one way to decode no characters—make no choices. That single completed empty prefix lets the first valid code contribute one way. If $f[0]$ were zero, neither a valid first digit nor a valid first pair could ever start a decoding.

All other entries begin at zero because no valid transition into them has yet been established.

**The one-digit transition**

`enumerate(s, 1)` pairs the character `c = s[i - 1]` with a one-based prefix length `i`. If `c != "0"`, that character represents a valid code from `1` through `9`. Every decoding of the preceding prefix `s[:i - 1]` can append that letter, so the code assigns

$$
f[i]=f[i-1].

$$

If `c` is `0`, it cannot stand alone: the mapping contains no code zero. The solution consequently does not carry $f[i-1]$ forward. This is why a leading zero yields no decoding and why the zero in `10` or `20` must be handled only through the two-digit transition.

**The two-digit transition**

There must be at least two characters, checked by `i > 1`. The candidate pair is `s[i - 2:i]`. The solution requires its first character to be nonzero and its integer value to be at most `26`.

Because the input contains only digits and the first digit is then from `1` through `9`, this condition is equivalent to the pair lying between `10` and `26`. It rejects `06` through the explicit nonzero-leading check and rejects `27` through `99` through the upper bound. If the pair is valid, every decoding of `s[:i - 2]` can append the corresponding letter, so

$$
f[i]\mathrel{+}=f[i-2].

$$

The one- and two-digit contributions are added only when their respective final code is legal.

**Trace on `226`**

Initially `f = [1, 0, 0, 0]`.

1. At prefix `2`, the single digit is valid, so $f[1]=f[0]=1$. No pair exists yet.
2. At prefix `22`, the final `2` can stand alone, contributing $f[1]=1$. Pair `22` is also valid, contributing $f[0]=1$. Thus $f[2]=2$.
3. At prefix `226`, final `6` contributes $f[2]=2$. Pair `26` contributes $f[1]=1$. Therefore $f[3]=3$.

These three paths correspond to `(2,2,6)`, `(22,6)`, and `(2,26)`.

**Why the recurrence counts every decoding exactly once**

Take any valid decoding of the first $i$ digits and inspect its final code. It has length one or two because all mapping keys lie from `1` to `26`. If it has length one, removing it leaves exactly one decoding counted by $f[i-1]$, and the one-digit check accepts its nonzero digit. If it has length two, removing it leaves a decoding counted by $f[i-2]$, and the pair check accepts its value.

Conversely, appending any accepted one- or two-digit code to a decoding of the appropriate shorter prefix creates a valid decoding of `s[:i]`. No decoding is counted in both categories because its last code cannot simultaneously occupy one and two characters. Assuming earlier DP entries are correct, these facts prove $f[i]$ is correct; the initialized empty prefix starts the induction.

**Zeros are constraints on grouping, not automatic failure**

A zero is valid only as the second character of `10` or `20`. For `101`, the first pair creates one way for prefix `10`; the zero receives no single-digit contribution. The final `1` then carries that one way forward. By contrast, for `100`, the last zero cannot stand alone and pair `00` is invalid, so the final count becomes zero. The recurrence handles both without special-case branching for whole strings.

## Complexity detail

The loop visits each of the $n$ characters once. Every iteration performs constant-many character checks, an integer conversion of a two-character slice, additions, and assignments. The slice has bounded length two, so the total time is $O(n)$.

The exact selected source allocates `f` with $n+1$ integer entries. Its auxiliary space is therefore $O(n)$. This conflicts with the `O(1)` space value in `solution_variants.json`; that manifest bound would describe the rolling-variable optimization, not this array implementation. An accurate interview explanation must follow the executable source and state the mismatch rather than calling an $n+1$ array constant space.

The returned answer is one integer, so excluding output does not change that conclusion. The constraint guarantees the count fits in 32 bits, while Python integers would remain safe even without that guarantee.

## Alternatives and edge cases

- **Rolling two-state DP:** Since $f[i]$ uses only $f[i-1]$ and $f[i-2]$, retain two counts instead of the full array. This preserves $O(n)$ time and achieves the manifest's intended $O(1)$ auxiliary space.
- **Top-down memoization:** Recursively count decodings starting at each index and cache the result. It has $O(n)$ time but needs $O(n)$ memo and recursion-stack space.
- **Unmemoized recursion:** Trying one- and two-character choices directly is conceptually simple but repeats suffix subproblems and can take exponential time.
- **Leading zero:** For `0` or `06`, neither transition reaches a positive count, so the result is zero.
- **Valid zero pairs:** `10` and `20` each have exactly one decoding. The zero cannot be separated from the preceding digit.
- **Invalid zero context:** Strings such as `30`, `100`, and `230` end with no legal transition at the problematic prefix and correctly produce zero complete decodings.
- **Boundary pair `26`:** It is valid; `27` is not. The `<= 26` check preserves that inclusive boundary.
- **Nonempty-input contract:** Constraints guarantee at least one character. If called with an empty string anyway, this exact implementation returns `1` from $f[0]$; that is its internal base-case meaning, not a promised out-of-contract result.
- **Input is digit-only:** The integer conversion relies on the contract. No validation for letters, signs, or whitespace is required.
