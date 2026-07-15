# Super Palindromes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 906 |
| Difficulty | Hard |
| Topics | Math, String, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/super-palindromes/) |

## Problem Description
### Goal
A positive integer is a palindrome when its decimal digits read the same from left to right and from right to left. It is a super-palindrome when the integer itself is a palindrome and it is also the square of a positive integer whose decimal representation is a palindrome. Both properties are required; a palindromic square with a non-palindromic square root does not qualify.

Two positive integers, `left` and `right`, are provided as decimal strings. Count the super-palindromes whose values lie in the inclusive range from `left` through `right`.

### Function Contract
Let $L=\operatorname{int}(\texttt{left})$, $R=\operatorname{int}(\texttt{right})$, and

$$
m=\left\lfloor\sqrt{R}\right\rfloor.
$$

**Inputs**

- `left`: the decimal representation of $L$.
- `right`: the decimal representation of $R$.

Both strings contain only digits, have no leading zeros, and have lengths from $1$ through $18$. The represented values satisfy $1 \leq L \leq R \leq 10^{18}-1$.

**Return value**

Return the number of super-palindromes in the inclusive interval $[L,R]$.

### Examples
**Example 1**

- Input: `left = "4", right = "1000"`
- Output: `4`

The qualifying values are $4$, $9$, $121$, and $484$. Although $676$ is a palindrome, its square root $26$ is not a palindrome.

**Example 2**

- Input: `left = "1", right = "2"`
- Output: `1`

Only $1=1^2$ qualifies.

### Required Complexity
- **Time:** $O(\sqrt{m}\log R)$
- **Space:** $O(\log R)$

<details>
<summary>Approach</summary>

#### General

**Enumerate the much smaller set of possible roots**

Testing every integer in $[L,R]$ would be impossible near $10^{18}$. A qualifying value must have a palindromic square root no greater than $m$. Palindromes are sparse: a palindrome is determined completely by roughly its first half. Generate those roots directly, square each one, and test whether the square is also a palindrome.

**Build both palindrome lengths from a seed**

For the decimal digits of a positive seed, form an odd-length root by appending the reverse of every digit except the seed's last digit. For example, `123` produces `12321`. Form an even-length root by appending the reverse of the entire seed, so `123` produces `123321`. Increasing seeds generates each family in increasing order. Stop a family as soon as its root exceeds $m$.

The odd construction produces every positive odd-length palindrome exactly once, and the even construction does the same for even-length palindromes. Their digit-length parities differ, so the two families do not overlap. Consequently, every possible palindromic square root up to $m$ is examined exactly once.

For each generated root, compute its square. The root limit guarantees that this square is at most $R$; compare it with $L$ and compare the square's decimal string with its reverse. Count it only when both tests succeed. Every counted number is therefore a palindrome in $[L,R]$ and the square of a palindrome. Conversely, any super-palindrome in the interval has a palindromic root at most $m$, which appears in one of the two generated families and is counted, so none are missed.

#### Complexity detail

A palindrome no greater than $m$ is determined by at most half of its digits, so the two families contain $O(\sqrt{m})$ candidates. Constructing a root, squaring it, and checking its square's digits takes $O(\log R)$ digit work, for $O(\sqrt{m}\log R)$ time. The temporary decimal strings use $O(\log R)$ auxiliary space.

#### Alternatives and edge cases

- **Scan every possible square root:** Checking every integer through $m$ is correct, but costs $O(m\log R)$ time and ignores how sparse palindromic roots are.
- **Scan every value in the interval:** Testing each number for both properties takes time proportional to $R-L+1$ and is infeasible for the allowed bounds.
- **Precompute the fixed universe:** Because $R<10^{18}$, all super-palindromes can be generated once and queried by binary search, but storing a global table is unnecessary for a single call.
- **Odd and even root lengths:** Mirroring only one seed pattern omits every palindrome of the other digit-length parity.
- **Inclusive boundaries:** A qualifying value equal to $L$ or $R$ must be counted.
- **Square palindrome alone:** A palindromic square does not qualify when its square root is not itself a palindrome.
- **Value one:** $1$ is positive, palindromic, and equal to $1^2$, so it is a super-palindrome.
- **String bounds:** Convert the inputs before arithmetic; their string representation exists to preserve the full numeric range across language interfaces.

</details>
