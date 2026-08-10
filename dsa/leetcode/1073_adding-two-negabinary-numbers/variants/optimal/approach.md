## General

**Add from the least significant position**

The arrays store their most significant bit first, but addition propagates carry toward more significant positions. The solution therefore starts at the ends:

```python
i, j = len(arr1) - 1, len(arr2) - 1
c = 0
ans = []
```

`i` and `j` point to the current equal-power positions in the two inputs. `c` is the carry arriving from the previously processed lower power. `ans` receives result bits from least significant to most significant, so it will be reversed before return.

Base negative two still uses binary digits zero and one. What changes from ordinary binary addition is the meaning of the carry.

**Relate one column total to the next carry**

Suppose the current position has weight `(-2)^p`. Let `x` be the two input bits plus the incoming carry. We need an output bit `r` and next carry `c_next` satisfying:

```text
x = r - 2 * c_next
```

This equation comes from:

```text
x * (-2)^p
= r * (-2)^p + c_next * (-2)^(p + 1)
```

Since the next place value is negative two times the current place value, a positive excess at the current column creates a negative carry, while a negative current total creates a positive carry.

**Read missing input positions as zero**

The main loop continues while either input has a bit left or carry remains:

```python
while i >= 0 or j >= 0 or c:
```

The current input bits are:

```python
a = 0 if i < 0 else arr1[i]
b = 0 if j < 0 else arr2[j]
x = a + b + c
```

Once one array is exhausted, its higher positions are implicit zeros. Continuing for a nonzero carry is essential because the carry may create one or more additional most-significant bits.

Given input bits and possible carry values, `x` lies between minus one and three.

**Handle totals two and three**

The code resets the next carry before classifying `x`:

```python
c = 0
if x >= 2:
    x -= 2
    c -= 1
```

If the column total is two, choose result bit zero and next carry minus one:

```text
2 = 0 - 2 * (-1)
```

If the total is three, choose result bit one and the same carry:

```text
3 = 1 - 2 * (-1)
```

Subtracting two from `x` produces exactly those output bits, and `c -= 1` changes the reset carry to minus one.

This negative carry is the surprising part of negabinary arithmetic. In ordinary base two, a total of two carries positive one because the next weight is positive two. Here the next weight is negative two, so carrying minus one contributes positive two at the current weight.

**Handle a total of minus one**

The other exceptional case is:

```python
elif x == -1:
    x = 1
    c += 1
```

A bit cannot be negative, so represent minus one using output bit one and positive carry one:

```text
-1 = 1 - 2 * 1
```

The next higher position's negative weight compensates for the positive result bit here.

If `x` is zero or one, it is already a valid output bit and the reset carry remains zero.

These cases cover every possible column total from minus one through three.

**Append the bit and move left**

After normalization:

```python
ans.append(x)
i, j = i - 1, j - 1
```

`x` is guaranteed to be zero or one. It is appended in least-significant-first order. Both input pointers move to the next higher power.

The loop invariant is that processed lower positions in `ans`, together with carry `c` at the next unprocessed power, represent exactly the sum of all input positions processed so far. The normalization equation preserves this invariant at every step.

When both inputs are exhausted and `c` is zero, no unrepresented value remains. `ans` is then the complete negabinary sum in reverse order.

**Remove redundant high zeros**

Because `ans` is reversed internally, its most significant bits are at the end. The cleanup is:

```python
while len(ans) > 1 and ans[-1] == 0:
    ans.pop()
```

It removes leading zeros from the final representation while retaining at least one digit. The value zero must be represented as `[0]`, not an empty array.

Finally:

```python
return ans[::-1]
```

creates the required most-significant-first order.

**Why the result is correct**

At each power, the code combines both input coefficients and the incoming carry. Its case conversion chooses a legal bit and a carry satisfying `x = bit - 2 * carry`, so it preserves numeric value while moving all unresolved contribution to the next power.

The loop ends only when every input bit and carry has been processed. Therefore the accumulated bits represent the exact sum. Cleanup removes only zero coefficients above the highest meaningful power, so it does not change the value and produces the canonical no-leading-zero format.

## Complexity detail

Let `A` and `B` be the input lengths.

Each iteration consumes one position from both arrays, and only a constant number of extra iterations can be required to resolve the final carry. The running time is `O(A + B)`.

The reversed result can contain `O(A + B)` bits. `ans` stores those bits, and the final slice creates the returned reversed list. Space is `O(A + B)`, including the output and reversal copy. Apart from output storage, working variables are constant.

These exact bounds match the manifest.

## Alternatives and edge cases

- **Convert to an integer and back:** It is conceptually simple in arbitrary-precision languages but abandons digitwise constraints and requires careful negative-base conversion.
- **Use divmod with base minus two:** One can normalize each column total through arithmetic division, but language remainder rules for negative divisors can be less transparent than the explicit three cases.
- **Both inputs zero:** One zero bit is appended, cleanup keeps it, and the result is `[0]`.
- **One input zero:** The algorithm reproduces the other value, subject to normal carry processing and canonical cleanup.
- **Final negative carry:** A carry of minus one enters the next iteration and is converted to bit one with positive carry, which may require another position.
- **Final positive carry:** It is processed even after both input pointers become negative because `c` keeps the loop active.
- **Total two:** Produces bit zero and carry minus one, not ordinary binary carry plus one.
- **Total minus one:** Produces bit one and carry plus one.
- **No leading zeros:** Cleanup removes high zeros but never removes the only digit.
- **Maximum lengths:** Work remains linear and does not depend on the potentially large numeric value represented.
- **Input preservation:** The arrays are read from right to left and never modified.
- **Bit constraint:** The case range relies on input digits being only zero or one.
