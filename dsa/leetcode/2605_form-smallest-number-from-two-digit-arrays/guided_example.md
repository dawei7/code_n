# Guided Example: Form Smallest Number From Two Digit Arrays

## 1. The instance and the two regimes the answer can live in

Two arrays of distinct digits are given, and the number we build must contain at
least one digit from each array. Every digit is drawn from `1` through `9`, so `0`
never appears. This lesson works the instance

$$nums1 = [9, 6, 2, 4], \qquad nums2 = [7, 6, 4, 2],$$

whose smallest valid number is `2`.

Before any construction begins, the decisive question is whether the two arrays
share a digit. A shared digit can serve as the *entire* number, and a single digit
is smaller than every number built from more digits. So the instance splits into
two disjoint regimes, and the answer is whatever the smaller regime produces:

| regime | condition | shape of the answer |
|---|---|---|
| shared | the arrays have at least one digit in common | a one-digit number, namely the smallest shared digit |
| disjoint | the arrays have no digit in common | a two-digit number, one digit taken from each array |

Membership for the worked instance:

| digit | in `nums1`? | in `nums2`? | shared? |
|---|---|---|---|
| `2` | yes | yes | **yes** |
| `4` | yes | yes | **yes** |
| `6` | yes | yes | **yes** |
| `7` | no | yes | no |
| `9` | yes | no | no |

The three shared digits `2`, `4`, `6` put this instance in the shared regime, and
the smallest of them, `2`, is the answer. The rest of the lesson explains why
neither the number of digits nor the choice among the shared digits can be
decided in any other way.

## 2. Why the digit count is decided before the digits themselves

Every digit in play is at least `1`, so a number with $d$ digits is at least
$10^{d-1}$: the leading digit contributes at least $10^{d-1}$ on its own, and all
remaining digits are non-negative. Consequently a shorter number always beats a
longer one.

| digits used | smallest possible value | largest possible value | compared with any one-digit number |
|---|---|---|---|
| `1` | `1` | `9` | equal or smaller |
| `2` | `11` | `99` | always larger |
| `3` | `111` | `999` | always larger |

A valid number needs digits from two different arrays. The only way a one-digit
number can qualify is for that single digit to belong to **both** arrays, which is
exactly the shared regime. If no digit is shared, one digit can never qualify and
two digits are necessary, one from each array. Since no zeros exist, the two-digit
answer is at most `99` and any three-digit number is at least `111`, so nothing
beyond two digits ever needs to be considered.

This is stronger than a preference for short numbers: the digit count is forced by
the regime before any digit value matters.

## 3. Trace of the shared regime on the instance

With the regime settled, the remaining work is picking the smallest shared digit.
Scanning the membership table of section 1 in increasing digit order gives `2`
first, so the candidate set is exhausted immediately and the answer is `2`.

It is worth confirming that no two-digit number can beat it, because that check
is what makes the one-digit rule airtight. The cheapest two-digit candidates use
the smallest digit of each array, and both arrays have minimum `2`, so the best
two-digit construction would be `22` — larger than `2`. Every other two-digit
candidate is larger still.

The pairwise scan that enumerates all combinations confirms the same answer. For
each digit $a$ from the first array it records the best number that uses $a$:

| $a$ from `nums1` | digits of `nums2` available as partner | candidates generated | best candidate using $a$ |
|---|---|---|---|
| `2` | `7, 6, 4, 2` | `2` (equal), `27`, `72`, `26`, `62`, `24`, `42` | `2` |
| `4` | `7, 6, 4, 2` | `4` (equal), `47`, `74`, `46`, `64`, `42`, `24` | `4` |
| `6` | `7, 6, 4, 2` | `6` (equal), `67`, `76`, `66`, `64`, `46`, `62`, `26` | `6` |
| `9` | `7, 6, 4, 2` | `97`, `79`, `96`, `69`, `94`, `49`, `92`, `29` | `29` |

The global minimum over the four rows is `2`, produced by the pair consisting of
the digit `2` from each array. Note how the last row behaves: the digit `9` has no
partner equal to itself, so it must be paired, and the cheapest pairing puts the
smaller partner `2` in the tens place, giving `29` rather than `92`.

## 4. Trace of the disjoint regime on a contrasting instance

To see the other regime do real work, take the authored instance

$$nums1 = [9, 7, 5, 3, 1], \qquad nums2 = [8, 6, 4, 2],$$

which shares no digit at all. The membership check fails for every digit, so a
one-digit answer is impossible and the answer must be a two-digit number with one
digit from each array.

Let $m_1 = 1$ be the smallest digit of the first array and $m_2 = 2$ the smallest
digit of the second. Any valid two-digit number $10a + b$ has a leading digit $a$
that belongs to one of the arrays, so $a \ge \min(m_1, m_2) = 1$ and the number is
at least `10`. The best that can be hoped for is therefore a leading `1`, taken
from the first array.

| leading digit $a$ | possible values of $a$ | cheapest partner digit $b$ | number $10a + b$ | beatable? |
|---|---|---|---|---|
| `1` | `m_1 = 1`, from `nums1` | `m_2 = 2`, the smallest digit of the other array | `12` | best so far |
| `2` | `m_2 = 2`, from `nums2` | `1`, the smallest digit of the other array | `21` | worse than `12` |
| `3` | from `nums1` | `2` | `32` | worse |
| `4` | from `nums2` | `1` | `41` | worse |
| any larger digit | both arrays | smallest partner | at least `51` | worse |

Once the leading digit is fixed at the smallest available digit `1`, the partner
must come from the *other* array, and the cheapest such partner is that array's
minimum `2`. The resulting `12` is optimal, and it agrees with the authored
expectation for this instance.

## 5. Invariant and correctness of the decision rule

The method rests on one invariant: **the running best candidate is always a valid
number, and it is never larger than any candidate that has already been
eliminated.** Every candidate examined is either a shared digit $d$, which is
valid because $d$ lies in both arrays, or a two-digit number $10a + b$ (or its
reversal) built from a digit $a$ of the first array and a digit $b$ of the second,
which is valid because it contains a digit from each array.

**Correctness of the shared regime.** Suppose the arrays share at least one digit
and let $d^{\star}$ be the smallest shared digit. The number $d^{\star}$ is valid.
Any valid number has at least as many digits as the shortest valid number, so
consider the possibilities: a one-digit valid number must be a shared digit and is
therefore $\ge d^{\star}$; a two-digit valid number is $\ge 11 > 9 \ge d^{\star}$;
and longer numbers are even larger. Hence $d^{\star}$ is the minimum.

**Correctness of the disjoint regime.** Suppose no digit is shared, and let
$m_1 = \min(nums1)$ and $m_2 = \min(nums2)$. A valid number cannot have one digit,
so it has at least two, and any number with three or more digits is at least `111`,
while `10 * min(m_1, m_2) + max(m_1, m_2)` is a valid two-digit number and is at
most `99`. So it suffices to compare two-digit candidates. Write a candidate as
$10a + b$ where $a$ is the tens digit and $b$ the units digit, with $a$ and $b$
belonging to different arrays. Since $a$ is a digit of one of the arrays,
$a \ge \min(m_1, m_2)$, so

$$10a + b \;\ge\; 10\min(m_1, m_2) \;>\; 10\min(m_1, m_2) - 1 ,$$

and every candidate is at least $10\min(m_1, m_2)$. The bound is attained only
when $a = \min(m_1, m_2)$, and then $b$ must come from the other array, whose
cheapest digit is its own minimum. If $m_1 \le m_2$ the optimum is $10m_1 + m_2$;
if $m_2 < m_1$ it is $10m_2 + m_1$. Both cases are the single expression

$$10 \cdot \min(m_1, m_2) + \max(m_1, m_2),$$

This is why a pairwise scan over every combination can minimize over both shapes
without ever deciding the regime explicitly: whenever a one-digit candidate
exists it is smaller than every two-digit candidate, so the minimum lands in the
correct regime on its own.

| authored instance | shared digits | $m_1$ | $m_2$ | rule applied | result | expected output |
|---|---|---|---|---|---|---|
| `nums1 = [4, 1, 3]`, `nums2 = [5, 7]` | none | `1` | `5` | two digits, smallest leading | `15` | `15` |
| `nums1 = [4]`, `nums2 = [5, 7]` | none | `4` | `5` | two digits, smallest leading | `45` | `45` |
| `nums1 = [3, 5, 2, 6]`, `nums2 = [3, 1, 7]` | `3` | `2` | `1` | shared digit `3` beats `12` | `3` | `3` |
| `nums1 = [6, 4, 3, 2]`, `nums2 = [1, 5, 8]` | none | `2` | `1` | two digits, leading digit from `nums2` | `12` | `12` |
| `nums1 = [9, 6, 2, 4]`, `nums2 = [7, 6, 4, 2]` | `2, 4, 6` | `2` | `2` | smallest shared digit `2` | `2` | `2` |
| `nums1 = [9, 7, 5, 3, 1]`, `nums2 = [8, 6, 4, 2]` | none | `1` | `2` | two digits, smallest leading | `12` | `12` |
| `nums1 = [9]`, `nums2 = [8]` | none | `9` | `8` | two digits, leading digit from `nums2` | `89` | `89` |

Every row matches, including the row where the smaller leading digit comes from
the second array, which is the case a careless rule that always puts the first
array first would get wrong.

## 6. Traps and boundary conditions

| Trap | What it looks like | Correction |
|---|---|---|
| Ignoring the shared digit | On the worked instance, answering `22` from the two array minima | A shared digit is a complete valid number and any one-digit number beats every two-digit number |
| Taking the first shared digit found | Answering `6` because `6` appears early in the scan order | The smallest shared digit is required, here `2` |
| Putting the first array's minimum in the tens place unconditionally | On `nums1 = [6, 4, 3, 2]`, `nums2 = [1, 5, 8]` this gives `21` instead of `12` | The tens digit must be the smaller of the two array minima, whichever array it comes from |
| Assuming a zero digit exists to build `10`-style numbers | Trying numbers like `10` or `20` | Every digit is at least `1`; the smallest two-digit number available is `11` |
| Building three or more digits | Believing that using more arrays' digits produces a smaller number | More digits always make the number larger, since there is no zero to pad with |
| Treating equal digits inside one array as different choices | A duplicate entry in an array might suggest a different minimum | Duplicates change nothing: the minimum and the membership set are unaffected |
| Forgetting that the number must use at least one digit of *each* array | Answering `1` on a disjoint instance because `1` is the global minimum | `1` belongs to only one array, so it is invalid; the answer must draw from both |

| Boundary situation | Authored instance | Answer | Why |
|---|---|---|---|
| singleton arrays, no shared digit | `nums1 = [9]`, `nums2 = [8]` | `89` | Only one digit is available on each side, so the number is forced and the digits must be ordered with the smaller first |
| singleton first array | `nums1 = [4]`, `nums2 = [5, 7]` | `45` | The forced digit `4` leads and the cheapest partner is `5` |
| duplicate entries in one array | `nums1 = [4, 4]`, `nums2 = [5, 7]` | `45` | The duplicate does not create a shared digit and does not change the minimum |
| several shared digits | `nums1 = [9, 6, 2, 4]`, `nums2 = [7, 6, 4, 2]` | `2` | Three digits are shared, and the smallest of them wins |
| maximum array length, disjoint | `nums1 = [9, 7, 5, 3, 1]`, `nums2 = [8, 6, 4, 2]` | `12` | All nine nonzero digits appear exactly once, split by parity; the two minima lead |
| smallest possible arrays with a shared digit | `nums1 = [3, 5, 2, 6]`, `nums2 = [3, 1, 7]` | `3` | The shared digit `3` is smaller than the best two-digit alternative `12` |

## 7. Complexity of the method

The straightforward way to be sure of the answer is to examine every ordered pair
of digits, one from each array: for a pair $(a, b)$ with $a \ne b$ the two
candidates $10a + b$ and $10b + a$ are both checked, and for $a = b$ the single
digit $a$ is checked. With $n = nums1.length$ and $m = nums2.length$, that costs
$O(nm)$ time, which the constraints cap at $9 \times 9 = 81$ pairs, and $O(1)$
auxiliary space.

The decision rule of section 5 reduces the work further. A presence table over the
ten possible digit values records which array contains each digit, and the answer
is then read off from the shared digits and the two minima.

| Component | Cost | Why |
|---|---|---|
| Presence table construction | $O(n + m)$ | Each digit is written into one of ten fixed slots |
| Smallest shared digit | $O(1)$ | A scan over ten slots |
| Smallest digit of each array | $O(1)$ after the table is filled | The smallest marked slot per array |
| Pairwise enumeration alternative | $O(nm)$ | Every ordered pair is examined, at most 81 pairs |
| Auxiliary space | $O(1)$ | Ten flags, independent of the array sizes |

The essential simplification is that the digit count is settled by the regime
alone: once shared digits are known to exist, no two-digit number needs to be
considered, and once they are known to be absent, only the two smallest digits
matter.