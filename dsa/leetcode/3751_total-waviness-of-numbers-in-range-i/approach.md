## General

**Evaluate each number directly under the smaller bound**

The range endpoint is at most $10^5$, so the exact Optimal source enumerates every integer from `num1` through `num2` and computes its waviness independently.

The helper `f(x)` extracts decimal digits with repeated modulo ten and integer division. This stores digits from least significant to most significant, which is the reverse of their written order.

**Reversing the digit list does not change peaks or valleys**

An interior digit's two neighbors are the same two values whether the number is read left-to-right or right-to-left; their sides merely swap.

The conditions

$$
left<middle>right
$$

and

$$
left>middle<right
$$

are symmetric in `left` and `right`. Therefore an original peak remains a peak in the reversed digit list, and an original valley remains a valley.

The helper can safely inspect the extraction-order list without reversing it again.

**Check only interior digit positions**

If the digit count `m` is below three, there is no position with two neighbors, so the helper returns zero.

Otherwise it loops `i` from one through `m-2`. A digit contributes one when it is strictly greater than both neighbors or strictly less than both. The `elif` is safe because one digit cannot satisfy both strict conditions.

Equality with either neighbor gives no contribution, as required.

For `4848`, extraction produces `[8,4,8,4]`. At index one, four is below both eights and is a valley. At index two, eight is above both fours and is a peak. The reversed representation still has total waviness two.

For `120`, extraction gives `[0,2,1]`. The middle digit two is greater than zero and one, so the helper returns one.

Consider `198`. Extraction gives `[8,9,1]`, where nine is still the middle digit and remains greater than both neighbors. For `201`, extraction gives `[1,0,2]`; zero is smaller than one and two, so it is a valley. These are the same classifications described in the original written order.

An equality example such as `122` produces extraction `[2,2,1]`. The middle two equals one neighbor, so neither strict branch succeeds and waviness is zero.

**Sum independent waviness values**

The outer expression calls `f(x)` for every integer in the inclusive Python range `range(num1,num2+1)` and sums the results.

Every number contributes exactly its own peak/valley count. There is no interaction between numbers and no duplicate-removal requirement, so direct summation is exact.

The helper destructively divides its local parameter `x`, but integers are immutable and the outer range values are unaffected.

The total can count several contributions from one number. A five-digit number has three interior positions, and each is tested independently. Adjacent interior positions can alternate peak and valley, as in a pattern such as `4848`.

**Why direct enumeration matches this problem's scale**

At most 100,000 positive integers lie below the upper constraint, and each has at most six digits. The straightforward scan therefore performs a modest bounded amount of work. The digit-DP editorial becomes valuable for much larger numeric limits, but would add state complexity without changing the result here.

The source also avoids string allocation per number. Its list contains integer digits and grows only to the current number's digit length.

## Complexity detail

Let

$$
R=\texttt{num2}-\texttt{num1}+1
$$

and let `D` be the maximum decimal digit count in the range. Extracting and scanning one number takes $O(D)$ time. Across all numbers, total time is $O(RD)$.

The digit list for one number contains at most `D` entries and is discarded before the next helper call, so auxiliary space is $O(D)$. The outer `sum` consumes a generator lazily rather than storing all results.

With the stated maximum, `D<=6`, but the manifest's symbolic bounds remain informative.

## Alternatives and edge cases

- **Convert each number to a string:** Scanning triples of adjacent characters is equally correct and has the same $O(RD)$ bounds. The exact source uses arithmetic extraction.
- **Reverse the extracted list:** It is harmless but unnecessary because peak/valley comparisons are neighbor-symmetric.
- **Digit DP:** The editorial supplies a faster prefix-counting approach useful for much larger bounds. The smaller version's exact source intentionally enumerates.
- **Check first and last digits:** They lack two neighbors and must never contribute; the loop excludes them.
- **Two-digit or one-digit number:** Waviness is zero.
- **Equal adjacent digits:** Strict inequalities prevent a plateau from being called a peak or valley.
- **Both peak and valley test as separate `if` statements:** A strict digit cannot be both, but `elif` avoids redundant checking after a peak.
- **Single-number range:** The result is simply that number's waviness.
- **Inclusive upper bound:** Adding one in `range` ensures `num2` is evaluated.
- **Powers of ten:** Internal and trailing zeros are ordinary digits and participate in comparisons; leading zeros are never created in the representation.
- **Reversed extraction order:** It changes position numbering but not which original interior values satisfy the symmetric condition.
