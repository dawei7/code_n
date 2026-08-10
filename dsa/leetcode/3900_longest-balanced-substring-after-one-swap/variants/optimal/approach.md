## General

Represent each `'1'` as $+1$ and each `'0'` as $-1$. Then a substring is balanced exactly when the sum of its encoded values is zero.

The optional global swap expands the useful substring sums slightly. One swap can repair a substring with two extra ones or two extra zeros, provided the opposite character exists outside that substring. The source tracks prefix balances and the earliest positions that can start each of these three kinds of window.

**Prefix balance turns substring counts into subtraction**

Let $P_i$ be the balance of prefix `s[0..i]`:

$$
P_i
=
\#1\text{s in }s[0..i]
-
\#0\text{s in }s[0..i].
$$

Define the empty prefix before index 0 to have balance $P_{-1}=0$. For a substring from $j+1$ through $i$, its balance is

$$
P_i-P_j.
$$

If $P_i=P_j$, the substring has equally many zeros and ones. Its length is $i-j$.

The dictionary `pos` maps each prefix balance to all indices where that balance has occurred. It begins with `{0: [-1]}` so a balanced substring starting at index 0 is handled by the same formula as every other substring.

At index `i`, the source updates `pre` to $P_i$, appends `i` to `pos[pre]`, and uses the earliest occurrence `pos[pre][0]`. Among all earlier positions with the same balance, the earliest produces the longest zero-balance substring ending at `i`:

```text
ans = max(ans, i - pos[pre][0])
```

**What one swap can change inside a chosen substring**

Swapping two positions both inside the substring does not change its counts. Swapping two positions both outside also does not change them. A useful swap exchanges one character inside with one character outside.

If a substring has two more ones than zeros, exchanging an inside `'1'` with an outside `'0'` changes its balance by

$$
-1-1=-2.
$$

The removed inside one decreases the one count, and the inserted zero increases the zero count. A balance of $+2$ becomes zero.

Symmetrically, a substring with two extra zeros has balance $-2$. Swapping an inside zero for an outside one changes the balance by $+2$ and makes it balanced.

No other nonzero balance can be repaired by one swap. A cross-boundary swap changes the encoded substring sum only by $-2$, $0$, or $+2$. Therefore every answer window must have original balance

$$
0,\quad +2,\quad\text{or}\quad -2.
$$

**Finding a window with two extra ones**

For a window $j+1..i$ to have balance $+2$, its earlier prefix must satisfy

$$
P_j=P_i-2.
$$

That is why the source looks for `pre - 2` in `pos`.

Let $j$ be the earliest occurrence of that prefix balance and let the window length be

$$
\ell=i-j.
$$

If the window has $o$ ones and $z$ zeros, then

$$
o+z=\ell
\quad\text{and}\quad
o-z=2.
$$

Solving gives

$$
z=\frac{\ell-2}{2}.
$$

The source has already counted all zeros in the entire string as `cnt0`. An outside zero exists exactly when

$$
\frac{\ell-2}{2}<\texttt{cnt0}.
$$

This appears as

```text
(i - p[0] - 2) // 2 < cnt0
```

When the condition holds, the earliest prefix gives a repairable window of length `i - p[0]`.

The needed inside one is guaranteed: a balance-$+2$ window has two more ones than zeros, so it cannot contain no ones.

**Why the second occurrence is the right fallback**

Suppose the longest $+2$ window starting after `p[0]` contains every zero in the entire string. Then it has no outside zero and cannot be repaired.

If the same prefix balance occurred again at `p[1]`, the segment from `p[0] + 1` through `p[1]` has balance zero because its endpoint prefix balances are equal. It is nonempty, so it contains at least one zero and one one.

Starting the candidate after `p[1]` removes that balanced segment from the window. The removed zero is now outside, while removing equal numbers of zeros and ones preserves the candidate's $+2$ balance. The new window is repairable.

Among all later occurrences of that prefix balance, `p[1]` is earliest and hence gives the longest fallback window. This explains:

```text
elif len(p) > 1:
    ans = max(ans, i - p[1])
```

If there is no second occurrence, every candidate with that required prefix balance starts at the same earliest point and contains all zeros, so none can obtain the needed outside zero.

**The symmetric two-extra-zero case**

A balance-$-2$ window satisfies

$$
P_j=P_i+2,
$$

so the source also looks up `pre + 2`.

For length $\ell$, such a window contains

$$
\frac{\ell-2}{2}
$$

ones. It can be repaired if that number is less than the total `cnt1`, meaning at least one one lies outside. If the earliest window contains all ones, the second occurrence of the same earlier prefix removes a nonempty balanced block and places an outside one at the algorithm's disposal.

**Why taking all three cases is complete**

Every substring that is balanced without a swap appears through equal prefix balances. Every substring repairable by exchanging one inside and one outside character has balance $+2$ or $-2$ and is examined through the corresponding shifted prefix balance.

For each ending index and each balance case, the source chooses the earliest feasible starting prefix, which gives the longest feasible window for that endpoint. Taking the maximum over all endpoints therefore finds the globally longest balanced substring obtainable after at most one swap.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. The initial `s.count("0")` scans the string once, costing $O(N)$ time. The main loop also scans all $N$ characters once.

Dictionary lookup, list append, and access to the first two list entries take expected $O(1)$ time per iteration. The total expected running time is

$$
O(N).
$$

Every prefix index is appended to exactly one list in `pos`. Across all dictionary values, the lists therefore hold $N+1$ indices, including the sentinel $-1$. The auxiliary-space complexity is

$$
O(N).
$$

Only the first two occurrences of each balance are queried, so a memory-optimized variant could store two indices per distinct balance. There can still be $O(N)$ distinct balances, leaving the same asymptotic bound.

The answer is always even because every balanced substring contains equal counts. It is at most $N$, and the source returns zero when no nonempty window is repairable.

## Alternatives and edge cases

- **Enumerate all swaps:** Trying $O(N^2)$ swaps and then searching each resulting string is far too slow; the balance-change observation represents all useful swaps implicitly.
- **Longest zero-sum substring only:** Equal-prefix logic without the $\pm2$ cases misses windows that become balanced through one cross-boundary swap.
- **Store only two prefix positions:** The source stores every occurrence, but its feasibility logic reads only the earliest and second-earliest positions for each balance.
- **No swap needed:** A balance-zero window is accepted directly; “at most one” does not require changing the string.
- **All characters identical:** There is no opposite character anywhere to exchange, so no nonempty balanced substring can be formed and the result is zero.
- **Outside character may be on either side:** The total-count test covers characters before and after the candidate; their location outside the substring does not matter because any two indices may be swapped.
- **Inside majority character always exists:** A $+2$ window necessarily contains a one, and a $-2$ window necessarily contains a zero, so only the outside opposite needs an explicit test.
- **Endpoint sentinel:** Prefix index $-1$ allows candidates beginning at string index 0 to have length `i - (-1) = i + 1`.
- **Second-occurrence fallback:** Equal prefix balances enclose a nonempty balanced block, guaranteeing that shortening past it releases both a zero and a one outside without changing the $\pm2$ imbalance.
- **Odd-length substring:** It cannot contain equal counts, and it also cannot have balance $\pm2$ because balance parity matches length parity; such a window is never selected.
- **Swapping equal characters:** It changes nothing and is already covered by the no-swap balance-zero case.
