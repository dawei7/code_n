## General

All decimal digits are nonnegative, so replacing either member of a pair with a larger available digit can only increase or preserve the product. The optimal pair is therefore the two largest digits, counting separate occurrences. It is unnecessary to store or sort every digit.

Extract digits from right to left with remainder and integer division by `10`. Maintain `largest` and `second_largest`. When a digit is at least `largest`, move the old maximum into the second position before installing the new maximum. The comparison is deliberately non-strict: a second occurrence equal to the maximum must occupy both retained positions. A digit below the maximum replaces `second_largest` only when it is larger than that value.

After each processed digit, the two variables contain the two largest values from distinct positions in the processed suffix. Each update preserves that fact, so after the scan their product is the maximum product over the entire number.

## Complexity detail

If $D$ is the number of decimal digits, the scan performs $D$ iterations and uses only two retained digits, for $O(D)=O(\log n)$ time and $O(1)$ space. The legal input range limits $D$ to at most ten; this bounded source domain is recorded by the package's complexity certificate because such a short range cannot support reliable runtime scaling.

## Alternatives and edge cases

- **Sort all digits:** Sorting also finds the two largest values but takes $O(D\log D)$ time and $O(D)$ storage after materializing the digits.
- **Compare every pair:** Brute force is correct but performs $O(D^2)$ products instead of one linear scan.
- **Use a strict maximum comparison:** With repeated largest digits such as `22` or `909`, a strict-only update can lose the second occurrence and return too small a product.
- **Zeros:** A zero may be one of the two largest digits, and the correct maximum can be zero, as for `10`.
- **Maximum legal input:** `1000000000` contains ten digits but still requires only the same bounded-state scan.
