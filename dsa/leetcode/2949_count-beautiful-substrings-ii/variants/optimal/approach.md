## General

For a substring, let $v$ and $c$ be vowel and consonant counts. The first requirement $v=c$ means its length is $2v$. The second becomes

$$
v\cdot c=v^2\equiv0\pmod{k}.
$$

We need characterize which $v$ values have $k\mid v^2$.

**Build the smallest required divisor**

Factor

$$
k=\prod p^{e_p}.
$$

For $v^2$ to contain at least exponent $e_p$ of prime $p$, $v$ must contain at least $\lceil e_p/2\rceil$. Define

$$
R=\prod p^{\lceil e_p/2\rceil}.
$$

Then $k\mid v^2$ exactly when $R\mid v$. Because substring length is $2v$, a balanced substring satisfies divisibility exactly when its length is a multiple of

$$
\texttt{period}=2R.
$$

The source obtains $R$ by trial division. For each factor exponent, it multiplies `required` by `factor ** ((exponent + 1) // 2)`. If a prime factor greater than the final square root remains, its exponent is one and it is multiplied once.

**Prefix balance encodes equal counts**

Assign $+1$ to a vowel and $-1$ to a consonant. Let `balance` be the prefix sum through position `end`.

A substring between prefix positions $p$ and $q$ has equal vowels and consonants exactly when the two prefix balances are equal:

$$
B_q-B_p=0.
$$

Its length $q-p$ is divisible by `period` exactly when

$$
q\bmod\texttt{period}=p\bmod\texttt{period}.
$$

Therefore a valid substring corresponds precisely to two prefix positions with the same pair

`(balance, position % period)`.

**Count matching earlier prefix states**

Before reading characters, prefix position zero has balance zero and residue zero, so

`frequency[(0, 0)] = 1`.

For each one-based prefix endpoint:

1. Add one for a vowel or subtract one for a consonant.
2. Form `state = (balance, end % period)`.
3. Every earlier occurrence of that state defines one beautiful substring ending here, so add its frequency.
4. Increment the state's frequency for future endpoints.

Each pair of equal states has a unique earlier and later prefix position, so every beautiful substring is counted once.

**Why both original conditions are covered**

Equal balance proves $v=c$. Equal residue proves length $2v$ is divisible by $2R$, hence $R\mid v$ and $k\mid v^2=v\cdot c$. Conversely, any beautiful substring has both properties and therefore produces matching states.

No substring contents need to be stored; only aggregated prefix-state frequencies matter.

## Complexity detail

Trial division tests factors through at most $\sqrt{k}$ in the worst case, taking $O(\sqrt{k})$ arithmetic steps. The string scan is $O(n)$ expected time because dictionary operations are expected constant time. Total expected time is $O(n+\sqrt{k})$.

The frequency dictionary may contain $O(n)$ distinct states, so auxiliary space is $O(n)$. The vowel set and factorization variables are constant-size.

## Alternatives and edge cases

- **Enumerate all substrings:** Version I's nested loops take $O(n^2)$ time and are too slow for $n=50000$.
- **Track balance only:** This counts equal vowels and consonants but ignores the product divisibility requirement.
- **Track length modulo $2k$:** It is sufficient in some cases but not minimal; factor exponents produce the exact smaller period $2R$.
- **$k=1$:** `required=1` and period two, so every balanced even-length substring qualifies.
- **Prime $k$:** $R=k$ and the balanced half-length must be divisible by $k$.
- **Perfect-square factors:** Exponent halving can make $R$ much smaller than $k$.
- **Initial prefix state:** Omitting `(0,0)` would miss valid substrings beginning at index zero.
- **Vowel set:** Only `a,e,i,o,u` contribute $+1$.
- **Dictionary key:** Both balance and residue are necessary; matching only one is insufficient.
- **Nonempty substrings:** Earlier prefix positions are counted before the current state is inserted, so no zero-length pair is added.
- **Why ceiling halves exponents:** Squaring a value doubles every prime exponent. The smallest exponent in $v$ whose double reaches $e$ is precisely $\lceil e/2\rceil$.
- **Composite trial factors:** The loop may test composite integers, but their prime factors have already been divided from `remaining`, so they contribute exponent zero and do no harm.
- **Shrinking factorization bound:** The condition uses the current `remaining`. Removing factors can end trial division early; any residue above one is necessarily prime.
- **Prefix position versus character index:** `end` starts at one because it denotes the number of processed characters. Substring length is a difference of prefix positions, which makes residue comparison exact.
- **Negative balances:** Dictionary tuples handle them normally; consonant-heavy prefixes need no offset.
- **Frequency addition before increment:** Every previously seen equal state forms a distinct start. Inserting the current state afterward prevents pairing a prefix with itself.
- **Period may exceed string length:** Then equal residues require the same actual prefix offset within this range; valid counted substrings still follow the exact divisibility rule.
- **Expected dictionary time:** Hash operations are expected $O(1)$; pathological collision behavior is not the standard complexity model.
- **Answer needs no modulo:** The source returns the exact number of qualifying substrings.
