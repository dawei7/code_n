## General

**Match the hash's exponent direction**

In each window, the leftmost character has exponent zero and powers increase
toward the right. Scanning windows from right to left makes the update simple.
If the current window hash is $H$, prepending a character of value $v$ produces
`(H * power + v) % modulo`.

**Remove the character beyond the window**

After prepending `s[i]`, a window longer than `k` has one outgoing character
at `s[i + k]`. Its contribution is its alphabet value times
$\texttt{power}^k$, so precompute that power modulo `modulo` and subtract the
contribution. Python's modulo operation keeps the resulting residue
nonnegative.

At every position $i \le n-k$, the maintained value is therefore exactly the
defined hash of `s[i:i + k]`. Whenever it matches `hashValue`, remember $i$.
Because the scan moves toward smaller indices, overwriting the remembered
position leaves the leftmost match at the end. The guaranteed match makes that
slice well-defined.

## Complexity detail

Let $n=\lvert s\rvert$. Modular exponentiation costs $O(\log k)$ time, and the
right-to-left scan costs $O(n)$ time, so the total is $O(n)$. Apart from the
returned length-$k$ substring, the algorithm stores only constant-size
integers; output-inclusive space is $O(k)$ and auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Recompute every hash:** Evaluating all $k$ character contributions for
  every window is direct but takes $O(nk)$ time.
- **Prefix polynomial hashes:** Prefix values can answer windows in constant
  time, but aligning this problem's low-power-left convention requires modular
  normalization and may invite invalid modular division when inverses do not
  exist.
- Hash collisions are intentional: return the first matching hash without
  comparing substring contents.
- When `k` equals the string length, there is exactly one candidate window.
- With `modulo = 1`, every residue and `hashValue` are zero.
- `power` may be a multiple of `modulo`, so the update must rely only on modular
  arithmetic rather than an inverse.
