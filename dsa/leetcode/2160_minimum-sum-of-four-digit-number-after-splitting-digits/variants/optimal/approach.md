## General

The four digits must be assigned to two numbers, and leading zeros are allowed. The value of a digit depends on its positional coefficient: a units digit is multiplied by one, a tens digit by ten, and a hundreds digit by one hundred.

**Why two two-digit numbers are sufficient**

Using one three-digit number and one one-digit number creates positional coefficients $100,10,1,1$. Using two two-digit numbers creates coefficients $10,10,1,1$. Every digit is nonnegative, so replacing the coefficient 100 with 10 can never increase the sum. Therefore an optimum always exists in the two-by-two form, even when a leading zero makes one displayed number shorter.

The problem reduces to assigning four digits to two tens positions and two units positions.

**Extract every digit**

The loop repeatedly appends `num % 10` and performs `num //= 10`. Remainder modulo ten extracts the current last digit, while integer division removes it.

Although the loop condition is `while num`, the input is guaranteed to be a four-digit integer. It therefore performs exactly four iterations. Zero digits inside the number are preserved: for `4009`, extraction produces `[9,0,0,4]` before sorting.

The extracted order does not matter because the digits may be rearranged arbitrarily.

**Assign small digits to expensive positions**

After `nums.sort()`, write the digits as

$$
d_0\le d_1\le d_2\le d_3.
$$

The tens positions have coefficient ten, which is larger than the units coefficient one. To minimize a weighted sum, the two smallest digits must receive the two larger coefficients.

An exchange proves this. Suppose a larger digit $b$ occupies a tens position while a smaller digit $a$ occupies a units position. Their contribution is $10b+a$. Swapping them gives $10a+b$, reducing the sum by $9(b-a)\ge0$. Repeating such exchanges places $d_0$ and $d_1$ in the tens positions.

The remaining digits $d_2$ and $d_3$ occupy units positions. It does not matter which of the two numbers receives which tens or units digit because only their total sum is requested.

**Compute the sum directly**

The exact return expression is

`10 * (nums[0] + nums[1]) + nums[2] + nums[3]`.

This equals the sum of numbers such as `10 * nums[0] + nums[2]` and `10 * nums[1] + nums[3]`.

For `2932`, sorting gives `[2,2,3,9]`. The formula is $10(2+2)+3+9=52$, corresponding to 23 and 29.

For `4009`, sorting gives `[0,0,4,9]`. Both tens digits are zero, so the constructed numeric values are effectively 4 and 9, whose sum is 13. Leading-zero permission is what makes this representation legal.

**Why no other split can be better**

Two-by-two placement avoids unnecessary hundreds coefficients. Within those four positions, the exchange argument proves the smallest digits belong in the tens places. The remaining assignments all have the same coefficients and therefore the same total. The formula reaches the minimum over every legal split and arrangement.

**Separate number construction from sum minimization**

The method never needs to choose an explicit pair because addition is commutative. Once the four positional coefficients are fixed, only the total weighted contribution matters. This removes irrelevant pair-order choices and lets the implementation return the optimal sum directly.

## Complexity detail

The input always contains exactly four digits. Extraction runs four times, sorting handles four values, and the return uses a fixed number of arithmetic operations. Time is $O(1)$ with respect to the problem’s input size.

The list always stores four integers, so auxiliary space is $O(1)$. The local variable `num` is modified during extraction, but integers are passed by value-like object reference semantics and the caller’s integer cannot be mutated.

## Alternatives and edge cases

- **Enumerate all assignments:** Four digits have only a constant number of permutations and split points, so brute force can work, but it obscures the positional-weight proof.
- **Convert through a string:** Sorting `str(num)` is concise but still needs converting digit characters back to integers. Arithmetic extraction follows the exact source.
- **Three-digit plus one-digit split:** Its hundreds coefficient cannot improve on two tens coefficients for nonnegative digits.
- **Repeated digits:** Sorting retains all copies, and the same weighted argument applies.
- **One zero:** The zero should occupy a tens position because that removes the greatest possible place-value cost.
- **Two zeros:** Both tens positions become zero, leaving the two nonzero digits as the effective numbers.
- **Three zeros:** The minimum sum is the sole nonzero digit.
- **No zeros:** The two smallest digits become tens digits and the two largest become units digits.
- **Already sorted decimal digits:** Arithmetic extraction reverses them initially, but sorting restores the required value order.
- **Leading zeros:** They affect digit placement but not the numeric value of the constructed integers, exactly as permitted.
- **Equal choice of pairings:** Once tens digits are fixed, pairing either units digit with either tens digit leaves the sum unchanged.
- **Four-digit guarantee:** It ensures `nums[0]` through `nums[3]` always exist after the loop.
- **Pair labels:** Swapping `new1` and `new2` changes neither legality nor their sum, so no tie-breaking rule is needed.
