## General

**Addition begins at the least significant digit**

The array stores the most significant digit first, so the units digit is at the final index. Adding one affects that digit first. Only when it overflows from 9 to 0 does a carry need to move left.

The loop therefore visits indices from `n - 1` down to 0. It stops as soon as a digit absorbs the increment without overflow. Digits farther left are then unchanged, exactly as in ordinary decimal addition.

**How three short statements encode carry propagation**

For the current digit, the source performs:

1. add one;
2. reduce modulo 10;
3. return if the result is not zero.

Given the contract that every entry is from 0 through 9, there are only two cases. An original digit from 0 through 8 becomes 1 through 9 after modulo, which is nonzero. It absorbs the carry, so the complete answer is ready. An original 9 becomes 10 and then 0, which means one carry must be applied to the next position on the left.

The test `digits[i] != 0` is therefore equivalent to “the carry has ended” for this exact operation. It would not be a general carry test for arbitrary added values, but it is exact when adding one to one decimal digit.

**Trace without a long carry**

For `[1,2,3]`, the loop visits only the final digit. It becomes 4, remains nonzero, and the method returns `[1,2,4]`. The first two entries are never touched.

For `[1,2,9]`, the final 9 becomes 0 and the loop continues. The 2 becomes 3, so the method returns `[1,3,0]`. The zero already written at the end is the correct result of the propagated carry.

**All nines require a new leading position**

If the loop finishes without returning, every original digit was 9 and has been changed to 0. A number such as 999 plus one is 1000, which has one more digit than the input.

`[1] + digits` constructs a new list with leading 1 followed by all of the mutated zeros. This is the only case in which the number of digits grows.

The no-leading-zero guarantee supports this conclusion. If every visited digit carried and the loop processed the whole array, the original representation was exactly a run of nines, not a form with irrelevant leading zeros.

**The carry invariant**

Before each loop iteration, every position to the right of `i` was originally 9 and has been converted to 0, and a carry of one still needs to be added at position `i`. Positions at or left of `i` still contain their original values.

If the current digit is below 9, incrementing it resolves the carry and leaves a correct full representation, so returning is valid. If it is 9, changing it to zero and moving left restores the invariant for the next iteration.

If no position resolves the carry, a leading 1 is required. These cases prove the returned digits represent the original integer plus exactly one.

**Why no whole-number conversion is needed**

The integer may contain up to 100 digits, beyond fixed-width numeric types in many languages. Operating directly on its base-10 digits avoids overflow and performs only the part of the number that a carry actually touches.

**Mutation and returned identity**

When some digit absorbs the carry, the method mutates and returns the original list object. In the all-nines case, it first turns that original list into all zeros, then returns a different concatenated list with the leading 1. A caller holding the old list will observe those zeros even though the returned object is new.

This distinction is allowed by the function contract but matters outside a judge if callers rely on object identity or input preservation.

## Complexity detail

In the worst case, every digit is 9 and the loop visits all $n$ entries. Constructing the longer result also copies $n$ zeros, so time is $O(n)$. When the last digit is below 9, the method returns after constant work.

The algorithm uses a length and loop index as scalar state. Excluding the required returned list, auxiliary space is $O(1)$. The all-nines output necessarily contains $n+1$ entries and is newly allocated; counting output storage gives $O(n)$. The manifest's $O(1)$ follows the conventional auxiliary-space convention.

## Alternatives and edge cases

- **Explicit carry variable:** Start `carry = 1`, use `divmod(digit + carry, 10)`, and stop when carry becomes zero. It generalizes more easily to adding other values.
- **Check for 9 directly:** Set a 9 to zero; otherwise increment and return. This is the competitive branch's more verbal form of the same logic.
- **Convert to an integer:** It is concise in Python but defeats the digit-array exercise and would overflow fixed-width types for long input.
- **Final digit below 9:** Only one array entry changes, giving best-case constant time.
- **Trailing run of nines:** Exactly that suffix becomes zero, and the first lower digit increments.
- **All nines:** A new leading 1 is prepended to the zeroed original digits.
- **Single zero:** It becomes `[1]`; zero is the one valid representation that may contain digit 0 alone.
- **Single nine:** The original list becomes `[0]`, and the returned new list is `[1,0]`.
- **No leading zeros:** The algorithm never needs to normalize or discard a prefix.
- **Caller-visible mutation:** The input is modified even in the branch that ultimately returns a newly allocated list.
