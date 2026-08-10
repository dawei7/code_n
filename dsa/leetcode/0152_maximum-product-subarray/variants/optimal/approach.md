## General

**Why one running maximum is not enough**

For a maximum-sum subarray, a very negative running sum can usually be discarded. Products behave differently because multiplying by a negative number reverses order: a very small negative product can become the largest positive product after another negative factor.

The solution therefore tracks two values for subarrays ending at the previous index:

- `f`: the maximum product of a nonempty subarray ending there;
- `g`: the minimum product of a nonempty subarray ending there.

`ans` is the maximum product seen over endings processed so far.

Both `f` and `g` initialize to `nums[0]`, because the only nonempty subarray ending at index zero is the one-element subarray.

**Derive all possibilities at the next value**

For current value `x`, every nonempty contiguous subarray ending at `x` belongs to exactly one of three relevant choices:

1. start a new subarray containing only `x`;
2. extend the previous maximum-ending subarray, producing `f * x`;
3. extend the previous minimum-ending subarray, producing `g * x`.

Why are only the previous extremes needed? Every longer candidate ending now is some previous ending product multiplied by the same `x`.

- If `x` is positive, multiplication preserves order, so the previous maximum gives the new maximum extension and the previous minimum gives the new minimum extension.
- If `x` is negative, multiplication reverses order, so the previous minimum can give the new maximum and the previous maximum can give the new minimum.
- If `x` is zero, every extension becomes zero, and the one-element candidate is also zero.

Taking the maximum and minimum of the three candidates therefore retains exactly the information the next iteration needs.

**Save the old states before updating**

The code copies `f` and `g` into `ff` and `gg`. It then computes:

- new `f` from `x`, `ff * x`, and `gg * x`;
- new `g` from the same three old-state candidates.

This prevents the new maximum from contaminating the minimum calculation. Both recurrences describe subarrays based on the previous index, so both must read the previous states.

**Why the one-element candidate matters**

Starting fresh at `x` allows the algorithm to abandon a harmful prefix.

For example, after a zero, extending any earlier subarray produces zero. A later positive number should be able to begin a new product rather than remain tied to zero.

Likewise, if a previous product is negative and the current number is positive, `x` alone may exceed every extension. The recurrence never assumes that a best subarray must start at index zero.

**Track the best over every possible ending**

After calculating the maximum product ending at the current index, `ans = max(ans, f)` compares it with the best product ending earlier.

Every nonempty subarray has one unique ending index. Since `f` is exact for each ending when that index is processed, taking the maximum of all successive `f` values considers every possible answer.

For `[2,3,-2,4]`:

- at two, both extremes and the answer are two;
- at three, the maximum ending product becomes six;
- at negative two, the maximum ending product is negative two while the minimum becomes negative twelve;
- at four, the best ending product is four, but `ans` retains six.

For `[-2,0,-1]`, zero becomes both ending extremes and raises the global result to zero. The later negative one cannot combine across the zero to form positive two, so zero remains correct.

**A concise inductive guarantee**

Before each iteration, `f` and `g` are the true extrema among all subarrays ending immediately before `x`. The three-candidate derivation proves the update produces the true extrema ending at `x`. Initialization establishes the claim for the first element, so it holds across the array.

`ans` then records the largest maximum-ending value over all processed indices, proving the final result.

## Complexity detail

Let $n$ be the number of elements.

Each processed value performs a fixed number of multiplications and comparisons, so time is $O(n)$.

The recurrence itself uses only constant scalar state. However, the exact loop iterates over `nums[1:]`, and Python list slicing allocates a new list of $n-1$ references. Consequently, this source’s actual auxiliary space is $O(n)$, contradicting the manifest’s $O(1)$ claim.

Replacing the slice with an index loop or `itertools.islice(nums, 1, None)` would make the same recurrence genuinely $O(1)$ auxiliary space.

All subarray products fit 32-bit integers by contract; Python also avoids overflow regardless.

## Alternatives and edge cases

- **Constant-space index loop:** Iterate indices from one through `n - 1` and keep the same extrema. This is the minimal correction to meet the manifest.
- **Swap on negative:** When `x < 0`, swap current maximum and minimum before multiplying, then compare each with `x`. It is an equivalent recurrence.
- **Prefix and suffix products:** Scan from both directions, resetting at zero. It can find the answer in linear time with constant scalar state.
- **Brute-force starts:** Accumulate products for every starting index. It uses $O(1)$ space but $O(n^2)$ time.
- **One value:** Initialization returns that value, including a negative value or zero.
- **Zero:** It can be the answer and separates products on its two sides.
- **Even negatives:** A minimum negative chain may become a large positive maximum after the second negative.
- **Odd negatives:** The best subarray may exclude the prefix through the first negative or suffix after the last negative.
- **Nonempty guarantee:** The direct `nums[0]` initialization relies on at least one element.
- **Runtime dependency:** The selected source uses `List` without importing it. Standalone Python needs `from typing import List`.
- **Manifest mismatch:** Scalar variables alone are constant, but the explicit slice is input-sized storage.
