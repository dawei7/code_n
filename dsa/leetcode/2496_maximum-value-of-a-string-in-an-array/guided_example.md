# Guided Example: Maximum Value of a String in an Array

## 1. The instance we will solve

Each string in an alphanumeric array has a **value** determined by a two-branch rule:
if the string consists of digits only, its value is the number it represents in base
`10`; otherwise its value is the number of characters in it. The task is to report the
largest value appearing anywhere in the array.

We trace the first official instance:

- `strs = ["alic3", "bob", "3", "4", "00000"]`
- required output: `5`

The instance is deliberately unbalanced: two strings are mixed, two are single digits,
and one is a run of five zeroes. The run of zeroes is the interesting row, because it
is the case where the *numeric* branch produces a value far smaller than the string's
own length.

## 2. The value rule is a two-branch case split

Write $\lvert s \rvert$ for the length of a string $s$ and let $\text{digits}(s)$ mean
"every character of $s$ is one of `0` through `9`". The rule is then

$$
\text{value}(s) =
\begin{cases}
\displaystyle\sum_{i=0}^{\lvert s \rvert - 1} d_i \cdot 10^{\lvert s \rvert - 1 - i}, & \text{if } \text{digits}(s), \\[2mm]
\lvert s \rvert, & \text{otherwise,}
\end{cases}
$$

where $d_0 d_1 \dots d_{\lvert s \rvert - 1}$ are the characters of $s$ read as decimal
digits. Three facts about this rule drive the whole method.

1. **The branch test is a single scan.** Because the alphabet is exactly lowercase
   letters and digits, "not digits only" is the same as "contains at least one
   letter". One pass over the characters decides the branch; no parsing or conversion
   is needed to decide it.
2. **The two branches have different scales.** Since the constraint caps every string
   at $9$ characters, a text-branch value is at most $9$, while a numeric-branch value
   can be as large as $999999999$. A long digit string is therefore an extremely
   strong candidate, but a long digit string full of leading zeroes is not.
3. **Leading zeroes are value-bearing, not length-bearing.** The numeric branch reads
   the digits; `"00000"` denotes the integer $0$, not the integer $5$ or the length
   $5$. This is the trap the traced instance exposes.

## 3. Classifying and evaluating the five strings

Applying the branch test to each string, then evaluating the chosen branch, gives the
following per-string values.

| String $s$ | Contains a letter? | Branch taken | Computation | `value(s)` |
|:---|:---|:---|:---|:---|
| `"alic3"` | yes (`a`, `l`, `i`, `c`) | length | five characters | 5 |
| `"bob"` | yes | length | three characters | 3 |
| `"3"` | no | numeric | single digit `3` | 3 |
| `"4"` | no | numeric | single digit `4` | 4 |
| `"00000"` | no | numeric | five zero digits, value $0$ | 0 |

The largest value in the column is $5$, produced by `"alic3"`, and no other string
reaches it: `"bob"` gives $3$, the single digits give $3$ and $4$, and the zero run
gives $0$. The expected output is `5`.

## 4. Invariant: a running maximum over a total order

The values are integers, so they are totally ordered and a single pass suffices.
Maintain the invariant

$$
M_t = \max\{\, \text{value}(s_0), \dots, \text{value}(s_t) \,\}
$$

after examining the first $t+1$ strings, and update it with
$M_t = \max(M_{t-1}, \text{value}(s_t))$.

| Step $t$ | String $s_t$ | `value(s_t)` | $M_{t-1}$ before | $M_t$ after | Did the maximum change? |
|:---|:---|:---|:---|:---|:---|
| 0 | `"alic3"` | 5 | none | 5 | first string, maximum established |
| 1 | `"bob"` | 3 | 5 | 5 | no |
| 2 | `"3"` | 3 | 5 | 5 | no |
| 3 | `"4"` | 4 | 5 | 5 | no |
| 4 | `"00000"` | 0 | 5 | 5 | no |

**Correctness.** The invariant is trivially true after step 0. Each later step keeps
it true, because the maximum over a longer prefix is either the previous maximum or
the newly added value. At termination, $M$ is the maximum over every string in the
array, which is the required answer. No value is skipped, so the result is complete;
no string outside the array is ever considered, so the result is attainable. Note
that the maximum is taken over the *values*, not over the strings, and the two
branches are compared on the same integer scale, which is what makes a text string of
length $9$ comparable with a numeric string such as `"999999999"`.

## 5. Boundaries and traps

The leading-zero family of cases is the sharpest trap in this problem, because a
digit-only string's length is *not* its value. The table below contrasts the two
readings for the second official instance.

| String $s$ | Length $\lvert s \rvert$ | Numeric value | Correct `value(s)` | If length were used instead |
|:---|:---|:---|:---|:---|
| `"1"` | 1 | 1 | 1 | 1 |
| `"01"` | 2 | 1 | 1 | 2 |
| `"001"` | 3 | 1 | 1 | 3 |
| `"0001"` | 4 | 1 | 1 | 4 |
| `"00000"` | 5 | 0 | 0 | 5 |

For $strs = ["1","01","001","0001"]$ the correct answer is `1` — every string has
value $1$ — whereas the length reading would wrongly report `4`. The zero run in the
traced array is the same defect in a different costume: `"00000"` has value $0$, and
any method that reports its length instead would answer `5` for the wrong reason.

| Boundary or trap | Instance | Correct reading | Answer |
|:---|:---|:---|:---|
| Digit string with leading zeroes | `["1", "01", "001", "0001"]` | the numeric branch ignores the zeroes | 1 |
| A single digit | `["0"]` | digits only, value $0$ | 0 |
| Several zero-only strings | `["000000000", "000", "00"]` | all have numeric value $0$ | 0 |
| Large numeric string | `["999999999", "abcdefgh", "12345678x"]` | numeric value beats every text length | 999999999 |
| Letter anywhere in the string | `["1a2345678", "1234567b", "c123456"]` | one letter switches the whole string to the length branch | 9 |
| Single letter | `["a"]` | length branch, one character | 1 |
| Numeric value larger than any length | `["abcde", "999", "12x"]` | $999 > 5$, and `"12x"` is a text string of length 3 | 999 |
| Text length larger than some numeric values | `["000", "abcdefghi", "7z"]` | $9$ beats the numeric $0$ | 9 |

## 6. Alternative formulations

| Method | Idea | Cost | Assessment |
|:---|:---|:---|:---|
| Single pass with a running maximum | classify, evaluate, keep the larger value | $O(S)$ | the method traced above; optimal and simplest |
| Compute all values, then sort | build the value list and read its last element | $O(m \log m)$ for $m$ strings | correct but pays a sort for information a maximum gives for free |
| Parse every string as an integer and fall back on failure | attempt numeric conversion, use the length when it fails | $O(S)$ | works only if the conversion of a digit-only string never overflows and if the fallback is applied exactly on failure, which is a subtler branch test |
| Compare lengths only | take the longest string | $O(S)$ | wrong: `"999999999"` has length 9 but value 999999999, and `"0001"` has length 4 but value 1 |
| Compare numeric values only | parse the digit strings and ignore the rest | $O(S)$ | wrong: a mixed string such as `"alic3"` has value 5 even though it has no numeric value |

## 7. Complexity: time and auxiliary space

Let $m$ be the number of strings and let

$$
S = \sum_{s \in \texttt{strs}} \lvert s \rvert
$$

be the total number of characters. Each string is scanned once to decide its branch,
and each character of a numeric string is consumed once while accumulating its value,
so the total time is

$$
O(S),
$$

which is at most $O(9 \cdot 100)$ under the stated constraints: at most 100 strings of
at most 9 characters each. The running maximum adds one comparison per string, which
is absorbed by the term above.

Auxiliary space is

$$
O(1).
$$

Only two scalars are kept — the current value and the running maximum — and no copy
of the array or of any string is created. If a string is converted to an integer, the
converted value is a machine-sized integer bounded by $999999999$ (nine digits), so
that conversion costs constant space and cannot overflow a 32-bit signed integer.