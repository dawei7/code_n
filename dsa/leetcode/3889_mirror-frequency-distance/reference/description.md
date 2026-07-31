## Description

The string `s` contains only lowercase English letters and decimal digits. Each character belongs to one of those two ordered character sets, and its **mirror** is found by reversing the corresponding order:

- among letters, `a` mirrors `z`, `b` mirrors `y`, and the pattern continues inward;
- among digits, `0` mirrors `9`, `1` mirrors `8`, and so on.

Let $\operatorname{freq}(x)$ be the number of appearances of character $x$ in `s`. For every distinct mirror pair $(c,m)$ represented by the string, its contribution is

$$
\left\lvert \operatorname{freq}(c)-\operatorname{freq}(m) \right\rvert.
$$

The reversed ordering does not create a second pair: $(c,m)$ and $(m,c)$ identify the same mirror pair and must contribute only once. Return the sum of the frequency differences over all distinct mirror pairs.
