# Modular Inverses

Consider the number $15$.

There are eight positive numbers less than $15$ which are coprime to $15$: $1, 2, 4, 7, 8, 11, 13, 14$.

The modular inverses of these numbers modulo $15$ are: $1, 8, 4, 13, 2, 11, 7, 14$ because:

- $1 \cdot 1 \equiv 1 \pmod{15}$
- $2 \cdot 8 = 16 \equiv 1 \pmod{15}$
- $4 \cdot 4 = 16 \equiv 1 \pmod{15}$
- $7 \cdot 13 = 91 \equiv 1 \pmod{15}$
- $11 \cdot 11 = 121 \equiv 1 \pmod{15}$
- $14 \cdot 14 = 196 \equiv 1 \pmod{15}$

Let $I(n)$ be the largest positive number $m < n - 1$ such that the modular inverse of $m$ modulo $n$ equals $m$ itself. So $I(15) = 11$.

Also $I(100) = 51$ and $I(7) = 1$.

Find $\sum I(n)$ for $3 \le n \le 2 \times 10^7$.
