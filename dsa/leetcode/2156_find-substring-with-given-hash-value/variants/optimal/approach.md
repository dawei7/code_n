## General

Computing the hash of every length-$k$ substring from scratch would inspect $k$ characters per start. The polynomial structure allows a rolling update in constant time, but its exponent direction makes scanning from right to left especially convenient.

**Build the final window’s hash**

The desired hash gives a substring’s leftmost character exponent zero, the next exponent one, and so on. The initialization processes the last length-$k$ window from its rightmost character toward its leftmost character.

Starting with `h = 0`, each step performs

`h = (h * power + val) % modulo`.

For three characters $a,b,c$ processed in order $c,b,a$, the successive algebra becomes

$$
c,\qquad cp+b,\qquad cp^2+bp+a.
$$

The final expression is $a p^0+b p^1+c p^2$, exactly the required orientation.

Character value is calculated as `ord(s[i]) - ord("a") + 1`, mapping `a` through `z` to one through 26.

**Prepare the outgoing coefficient**

The variable `p` ends initialization as

$$
p=\textit{power}^{k-1}\bmod\textit{modulo}.
$$

It is multiplied by `power` after every processed character except the final leftmost one. This is the coefficient of the rightmost character in any length-$k$ window, which is the character removed when shifting one position left.

For $k=1$, no multiplication occurs and `p = 1`, correctly representing exponent zero.

**Roll one position to the left**

Suppose `h` is the hash for substring `s[i+1 : i+k+1]`. The outgoing rightmost character is `s[i+k]`, stored as `pre`, and its contribution is `pre * p`.

After removing that term, every remaining character must move one exponent higher because a new character will be inserted at exponent zero. Multiplication by `power` performs that shift. Finally `cur`, the value of `s[i]`, is added:

`h = ((h - pre * p) * power + cur) % modulo`.

Taking the remainder at every update keeps integers bounded. Python’s modulo operation returns a nonnegative remainder even if the intermediate subtraction is negative.

**Keep the earliest matching start**

The scan runs `i` from `n - k - 1` down through zero, so it encounters candidate starts from right to left. Whenever `h == hashValue`, it assigns `j = i`.

Later assignments in this reverse scan have smaller indexes. Therefore, after all candidates are checked, `j` is the leftmost, or first, matching substring.

The variable starts as `j = n - k`, the final window’s start. The initialization does not explicitly compare that window with `hashValue`. This is still safe under the existence guarantee: if the last window is the only or earliest match, the default is correct; if it is not a match, some earlier guaranteed match is found and overwrites `j`.

**Return the exact window**

`s[j : j + k]` contains exactly $k$ characters beginning at the chosen start. String slicing creates the required substring without changing `s`.

**Why every hash is correct**

Initialization establishes the polynomial hash for the last window. The rolling equation algebraically removes exactly the old highest-power term, shifts every retained term up by one exponent, and inserts the new left character at exponent zero. By induction, `h` is the required hash at every tested start. The overwrite rule then selects the smallest matching index.

Hash collisions are not a concern for correctness here: the problem asks for equality of this hash value, not necessarily character equality with some hidden pattern.

## Complexity detail

Let $n$ be the string length. Initialization processes $k$ characters. The rolling loop processes the other $n-k$ starts once, with constant arithmetic per start. Total time is $O(n)$.

The rolling computation uses $O(1)$ auxiliary state. The returned slice contains $k$ characters and therefore requires $O(k)$ output space, which is the manifest’s reported bound. Excluding the required return string, auxiliary space is $O(1)$.

Python integer products may temporarily exceed `modulo` before the remainder, but arbitrary-precision integers preserve exact arithmetic.

## Alternatives and edge cases

- **Hash every substring independently:** This costs $O((n-k+1)k)$ time and repeats almost all character work.
- **Forward rolling hash:** It is possible with a modular inverse or a differently oriented polynomial, but the given exponent convention makes right-to-left rolling simpler and avoids requiring an inverse that may not exist.
- **Store all prefix hashes:** Prefix techniques can answer substring hashes but require powers and $O(n)$ arrays. The exact rolling window uses constant state.
- **k equals one:** `p` remains one, each roll removes the old character and inserts the new one correctly.
- **k equals n:** There is only the initialized window; the rolling loop is empty and `j=0`.
- **Several matching hashes:** Reverse scanning continually replaces `j`, leaving the smallest start.
- **Last window matches:** Its default start is retained unless an earlier match is found.
- **Last window does not match:** The guaranteed earlier match overwrites the default before return.
- **power equals one:** Every window hash is just its character-value sum modulo `modulo`; the same update remains valid.
- **modulo equals one:** Every hash is zero and the repeated assignments leave `j=0`, the first substring.
- **Negative intermediate:** Python modulo normalizes it into the range from zero through `modulo - 1`.
- **Character mapping:** The added one is essential because `val('a')` is one, not zero.
- **No collision verification:** Hash equality itself is the contract, so comparing source substrings is neither needed nor appropriate.
- **Input preservation:** The method reads characters and returns a new slice without modifying `s`.
