## General

**Use XOR cancellation to undo a prefix**

The given relationship is

$$
\texttt{pref}[i]
=
\texttt{arr}[0]
\mathbin{\mathtt{\char94}}
\texttt{arr}[1]
\mathbin{\mathtt{\char94}}
\cdots
\mathbin{\mathtt{\char94}}
\texttt{arr}[i].
$$

XOR has the cancellation identity `x ^ x = 0` and the identity element `x ^ 0 = x`. For every $i>0$, XORing consecutive prefix values cancels every earlier array element:

$$
\begin{aligned}
\texttt{pref}[i-1] \mathbin{\mathtt{\char94}} \texttt{pref}[i]
&=
(\texttt{arr}[0] \mathbin{\mathtt{\char94}} \cdots \mathbin{\mathtt{\char94}} \texttt{arr}[i-1]) \\
&\quad \mathbin{\mathtt{\char94}}
(\texttt{arr}[0] \mathbin{\mathtt{\char94}} \cdots \mathbin{\mathtt{\char94}} \texttt{arr}[i]) \\
&= \texttt{arr}[i].
\end{aligned}
$$

Every term through `arr[i-1]` occurs twice and vanishes. Only the newly introduced `arr[i]` remains.

At index zero, `pref[0] = arr[0]`. The solution makes the same consecutive-prefix formula work there by imagining a prefix value of zero before the array:

$$
\texttt{arr}[0] = 0 \mathbin{\mathtt{\char94}} \texttt{pref}[0].
$$

**How `pairwise` creates exactly the required neighbors**

The expression `[0] + pref` creates a new list whose first value is the artificial zero and whose remaining values are the given prefix XORs. Python's `pairwise` iterator yields adjacent pairs:

`(0, pref[0])`, `(pref[0], pref[1])`, and so on.

The list comprehension computes `a ^ b` for each pair. Its first result is `pref[0]`, which recovers `arr[0]`. Every later result is `pref[i-1] ^ pref[i]`, which recovers `arr[i]` by cancellation.

For `pref = [5,2,0,3,1]`, the augmented sequence is `[0,5,2,0,3,1]`. Adjacent XORs are `0^5=5`, `5^2=7`, `2^0=2`, `0^3=3`, and `3^1=2`. The returned array is `[5,7,2,3,2]`.

**Why the recovered array is unique**

The first element is forced because it must equal `pref[0]`. Once the prefix through index $i-1$ is known, the equation for `pref[i]` forces the next element. XORing the known previous prefix with the new prefix yields exactly one integer.

The adjacent-pair construction applies these forced equations at every index. It produces an array that recreates the supplied prefix values, and no different value could be chosen at any position without changing the corresponding prefix. This proves both correctness and uniqueness.

**A useful running verification**

Let the generated result at index $i$ be `r[i]`. For $i=0$, `r[0]=pref[0]`. Assume the XOR of `r[0]` through `r[i-1]` equals `pref[i-1]`. Then

$$
\begin{aligned}
\texttt{r}[0] \mathbin{\mathtt{\char94}} \cdots \mathbin{\mathtt{\char94}} \texttt{r}[i]
&=
\texttt{pref}[i-1]
\mathbin{\mathtt{\char94}}
(\texttt{pref}[i-1] \mathbin{\mathtt{\char94}} \texttt{pref}[i]) \\
&= \texttt{pref}[i].
\end{aligned}
$$

Thus every prefix of the returned array matches the input definition.

The code relies on `pairwise` being available from Python's iterator utilities in the surrounding execution environment. It consumes adjacent pairs lazily, although the augmented list itself is allocated eagerly.

## Complexity detail

Let $n$ be the length of `pref`. Creating `[0] + pref` copies $n$ references into a new $n+1$ element list, taking $O(n)$ time and space. `pairwise` then yields $n$ adjacent pairs, and the comprehension performs one XOR per pair, taking another $O(n)$ time.

Total time is $O(n)$. The returned array uses $O(n)$ space, and the augmented temporary list also uses $O(n)$ auxiliary space. Thus the exact implementation's additional storage is $O(n)$ even if output space is excluded.

An alternative loop can avoid the augmented list and use one previous-prefix scalar, reducing auxiliary space beyond the required output to $O(1)$. The manifest's $O(n)$ space remains correct for this exact concise expression.

Values are at most $10^6$, so XOR operates on a bounded number of bits and is treated as constant-time.

## Alternatives and edge cases

- **One previous-prefix variable:** Set `prev=0`, append `prev ^ current` for each prefix, then update `prev=current`. This keeps $O(n)$ output time while avoiding the $O(n)$ augmented list.
- **Modify `pref` in place from right to left:** For each index from $n-1$ down to 1, replace `pref[i]` by `pref[i] ^ pref[i-1]`. This uses $O(1)$ auxiliary space but mutates the caller's input.
- **Forward in-place mutation:** Updating from left to right would destroy the previous prefix value before it is used for the next element, so a right-to-left order or saved scalar is required.
- **Single element:** The only pair is `(0,pref[0])`, and the result correctly contains that value.
- **Zero prefix values:** XOR identities handle zero naturally; a zero can represent cancellation rather than an absent element.
- **Repeated prefix values:** If `pref[i] == pref[i-1]`, then `arr[i]` is zero because equal values XOR to zero.
- **Uniqueness:** No search or tie-breaking is necessary because each adjacent XOR forces exactly one element.
- **Input preservation:** The augmented list and result are new lists, so `pref` remains unchanged.
- **Library availability:** `pairwise` is part of modern Python iterator tools; older runtimes would need an explicit loop or equivalent pairing logic.
