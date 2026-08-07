## Description

You are given a string `s` consisting of digits.

An index `i` is called **good** if there exists a substring of `s` that ends at index `i` and is equal to the decimal representation of `i`.

Return an integer array of all good indices in **increasing order**.
### Function Contract

**Inputs**

- `s`: A non-empty string containing only decimal digits.

Let $N=\lvert\texttt{s}\rvert$, and let $D$ be the greatest number of decimal digits in an index from $0$ through $N-1$. The decimal representation of an index uses no leading zero, except that zero itself is represented by `"0"`.

A qualifying substring must be contiguous and must end at the index it represents. Because equality requires the same length, each index has exactly one candidate substring to test: the suffix of `s[0..i]` whose length is the number of digits in `i`.

**Return value**

Return an integer array containing precisely the good indices in increasing order.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "0234567890112"

**Output:** [0,11,12]

**Explanation:​​​​​​​**

- At index 0, the decimal representation of the index is `"0"`. The substring $s[0]$ is `"0"`, which matches, so index `0` is good.

- At index 11, the decimal representation is `"11"`. The substring `s[10..11]` is `"11"`, which matches, so index `11` is good.

- At index 12, the decimal representation is `"12"`. The substring `s[11..12]` is `"12"`, which matches, so index `12` is good.

No other index has a substring ending at it that equals its decimal representation. Therefore, the answer is `[0, 11, 12]`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "01234"

**Output:** [0,1,2,3,4]

**Explanation:**

For every index `i` from 0 to 4, the decimal representation of `i` is a single digit, and the substring $s[i]$ matches that digit.

Therefore, a valid substring ending at each index exists, making all indices good.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "12345"

**Output:** []

**Explanation:**

No index has a substring ending at it that matches its decimal representation.

Therefore, there are no good indices and the result is an empty array.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` only consists of digits from `'0'` to `'9'`.