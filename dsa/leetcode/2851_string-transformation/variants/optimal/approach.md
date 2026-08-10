## General

**Represent a rotation by an offset, not by a whole string.** Removing a nonempty proper suffix and putting it in front is a nonzero cyclic right rotation. For a length-$n$ string, every operation chooses one of $n-1$ nonzero offsets.

Label rotation states from zero through $n-1$. State zero is the original string, and every nonzero state is one labeled cyclic rotation offset. From any current state, one operation can move to every other offset exactly once but cannot stay at the same offset.

Even if the text is periodic and several offsets produce identical strings, the offsets remain distinct states because they arise from different suffix choices and contribute different operation sequences.

**Collapse path counts into two symmetric classes.** Let $A_t$ be the number of length-$t$ operation sequences ending at state zero. Let $B_t$ be the number ending at one particular nonzero state. Every nonzero state has the same count by symmetry.

To reach zero after another operation, the previous state may be any of the $n-1$ nonzero states, each contributing $B_t$:

$$
A_{t+1}=(n-1)B_t.
$$

To reach one chosen nonzero state, the previous state may be zero, contributing $A_t$, or any of the other $n-2$ nonzero states, contributing $B_t$ each:

$$
B_{t+1}=A_t+(n-2)B_t.
$$

Initially $A_0=1$ and $B_0=0$ because no operation leaves the string at offset zero.

**Encode the recurrence as matrix multiplication.** With row vectors,

$$
[A_t,B_t]
\begin{bmatrix}
0&1\\
n-1&n-2
\end{bmatrix}
=
[A_{t+1},B_{t+1}].
$$

Therefore, $[A_k,B_k]$ is the first row of the transition matrix raised to power `k`. The code computes that power by repeated squaring and assigns its first row to `dp`.

`dp[0]` is the number of ways to reach offset zero, while `dp[1]` is the number of ways to reach each particular nonzero offset.

**Fast matrix power.** `matrixPower` starts with an identity matrix in `r` and a copy of the base matrix in `x`. For each binary bit of exponent `y`, it multiplies `r` by `x` when the bit is set, squares `x`, and shifts `y` right.

The matrices are only two by two, so each multiplication is constant-sized. Helper `mul` reduces products modulo $10^9+7$. Helper `add` adds two already reduced values and subtracts the modulus once when needed; their sum is below twice the modulus, so one subtraction is sufficient.

**Find every rotation offset whose text equals `t`.** It remains to know which labeled states correspond to target string `t`. The source changes local `s` into

`original_s + t + t`

and computes its Z-array.

For position `n + q`, where $0\le q<n$, the following $n$ characters are the length-$n$ substring of `t + t` beginning at offset $q$. The Z-value there is at least $n$ exactly when that substring equals the prefix of the combined string, which is original `s`.

Thus, `z[n + q] >= n` means rotating original `s` right by offset $q$ produces `t`. Offset zero is the identity target `s == t`; any other matching offset is a nonzero target state.

**How the Z-algorithm stays linear.** `z[i]` stores the longest prefix match beginning at `i`. Variables `left` and `right` describe the rightmost known matching interval. When `i` lies inside it and the mirrored Z-value fits completely, that value is copied. Otherwise, comparison resumes at the known boundary and extends character by character.

Whenever a new match reaches farther right, the interval is updated. Across the entire string, the right boundary advances only linearly, giving $O(n)$ work.

**Sum the counts of all target offsets.** The loop examines exactly offsets zero through $n-1$. For every textual match, it adds `dp[0]` when the offset is zero and `dp[1]` otherwise.

Periodic strings may make several offsets match `t`. Each is a distinct endpoint state and has its own operation sequences, so their counts must be added. The modular `add` keeps the result reduced.
Rotation offsets exactly model suffix operations. The two-state recurrence gives the number of length-$k$ paths to every labeled offset. The Z-array identifies exactly which offsets display `t`. Summing their path counts therefore counts every and only sequence of exactly `k` operations transforming `s` into `t`.

## Complexity detail

Let $n$ be string length. The combined string has length $3n$, and the Z-algorithm takes $O(n)$ time. Scanning the $n$ candidate offsets is another $O(n)$.

Binary exponentiation performs $O(\log k)$ constant-size matrix multiplications. Total time is

$$
O(n+\log k).
$$

The combined string and Z-array use $O(n)$ space. Matrices are fixed two by two and use $O(1)$. Total auxiliary space is $O(n)$.

All counting arithmetic is performed modulo $10^9+7$, preventing unbounded count growth.

## Alternatives and edge cases

- **KMP rotation matching:** Search `s` inside `t+t` with a prefix-function matcher. It finds the same valid offsets in $O(n)$ time and matches the manifest wording.
- **Two-state recurrence iterated `k` times:** It uses constant space but $O(k)$ time, impossible when `k` reaches $10^{15}$.
- **Full $n$-state matrix:** It models offsets directly but matrix exponentiation would be vastly more expensive; symmetry reduces it to two states.
- **`s == t`:** Offset zero matches, and periodicity may make additional nonzero offsets match too.
- **Periodic strings:** Identical displayed strings at different offsets remain distinct states and must all contribute.
- **No matching rotation:** The Z scan adds nothing and returns zero.
- **One operation:** A nonzero offset has one direct way, while offset zero has none because suffix length cannot be zero or $n$.
- **Length at least two:** This keeps $n-2$ nonnegative and guarantees at least one legal suffix choice.
- **Modulo helpers:** `add` relies on both inputs already being reduced below the modulus.
- **Local string rebinding:** `s += t + t` changes only the local immutable-string reference, not caller data.
