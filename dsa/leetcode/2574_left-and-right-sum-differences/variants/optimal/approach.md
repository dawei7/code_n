## General

**Turn two side sums into running state**

Computing both sides independently at every index repeats almost all additions. Instead, begin with `left_sum = 0` and `right_sum` equal to the total array sum. Before producing the answer for the current value, subtract that value from `right_sum`; the variable then represents exactly the elements strictly after the current index. At the same moment, `left_sum` contains exactly the elements already processed, which are precisely those strictly before the index.

Append the absolute difference of those two quantities, then add the current value to `left_sum` before advancing. This order is important: the current element belongs to neither side of its own position.

At the start of each iteration, `left_sum` is the sum of the preceding prefix and `right_sum` still includes the current element and the remaining suffix. The two updates establish the required strict-left and strict-right sums for the output, then restore the same condition for the next position. Consequently every produced entry matches the definition.

## Complexity detail

Computing the initial total and scanning the array each take linear time, so the total is $O(n)$. The returned list contains $n$ integers and therefore uses $O(n)$ space; beyond that required output, the algorithm keeps only two sums and uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Separate prefix and suffix arrays:** Precompute both arrays and combine them. This is also $O(n)$ time, but stores two additional length-$n$ arrays when two running sums are enough.
- **Repeated slice sums:** Evaluate `sum(nums[:i])` and `sum(nums[i + 1:])` for every index. It directly mirrors the definition but rescans overlapping ranges and takes $O(n^2)$ time.
- **Algebra from a prefix array:** With a total and one prefix-sum array, derive both sides at each index. It is correct but uses avoidable auxiliary storage.
- **Single element:** Both strict sides are empty, so the only output is zero.
- **Large values:** The total can reach $10^8$ under the constraints; implementations should use a sum type that safely holds that range.
