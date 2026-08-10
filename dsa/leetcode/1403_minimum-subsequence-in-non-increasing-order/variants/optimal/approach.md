## General

**Rephrase the sum condition**

Let $S$ be the sum of all array values and $T$ the sum of the chosen subsequence. The unchosen sum is $S-T$. The requirement is

$$
T>S-T,
$$

or equivalently $2T>S$.

We need the fewest selected elements that make this strict inequality true. Among solutions with that size, we need the greatest selected sum.

**For any fixed size, choose the largest values**

Suppose a size-$r$ selection contains value $a$ while an unselected value $b>a$ exists. Replacing $a$ with $b$ increases the chosen sum without changing the size. Repeating this exchange shows that the maximum sum attainable with exactly $r$ elements is the sum of the $r$ largest array values.

Therefore it is enough to sort values in descending order and examine prefixes. No other size-$r$ subsequence can beat the descending prefix's sum.

**Grow the prefix until it crosses half**

The code computes `s = sum(nums)` and initializes chosen sum `t = 0`. It iterates through `sorted(nums, reverse=True)`, adding each next-largest value to `t` and appending it to `ans`.

After every addition, `t > s - t` tests the original condition directly. The first time it succeeds, the loop stops.

For `[4,3,10,9,8]`, descending order is `[10,9,8,4,3]`. Choosing 10 alone gives selected sum 10 and remaining sum 24, so it fails. Adding 9 gives 19 against remaining 15, so `[10,9]` succeeds and is returned.

**Why the first successful prefix has minimum size**

Suppose the first successful prefix has size $r$. The prefix of size $r-1$ did not satisfy the strict inequality. That prefix has the greatest possible sum among every $(r-1)$-element selection. If even it fails, no selection of $r-1$ or fewer elements can succeed.

The size-$r$ prefix does succeed, so $r$ is both achievable and smaller than no other achievable size. It is the minimum.

**Why it also maximizes the sum among minimum-size answers**

Among all $r$-element selections, the $r$ largest values have maximum total by the exchange argument. The algorithm returns exactly those values. Thus it satisfies the secondary tie breaker automatically.

The returned list is already in non-increasing order because it is a prefix of the descending sorted list.

**Why strict greater-than matters**

Equality is not enough. In the second example, two sevens sum to 14 and the remaining values also sum to 14. The condition `t > s - t` correctly continues and adds six, producing `[7,7,6]`.

Changing the comparison to greater-than-or-equal would stop too early and violate the contract.

**Why a solution always appears**

Every input value is positive. If all values are selected, `t=S` and the remaining sum is zero, so $S>0$ succeeds. The loop therefore always breaks by the final element.

Positivity also makes prefix sums grow monotonically, so once the condition becomes true, adding more elements is unnecessary and would violate the minimum-size objective.

**Subsequence versus sorted output**

Ordinarily, a subsequence preserves original relative order. This problem additionally requires the answer sorted non-increasingly and allows choosing elements by value. The returned multiset corresponds to occurrences from the original array, and duplicates remain available with their multiplicities. Sorting the chosen values is explicitly required.

**Why the algorithm is correct**

For every size $r$, the descending prefix is the maximum-sum selection of that size. The algorithm finds the smallest $r$ for which this strongest candidate exceeds the complement. No smaller selection can work, and the chosen size-$r$ prefix has the largest sum among all minimum-size solutions. It is returned in the requested order, proving every requirement.

## Complexity detail

Let $n$ be the array length. Computing the total takes $O(n)$ time. Sorting a copy takes $O(n\log n)$, and the prefix scan takes at most $O(n)$. Total time is $O(n\log n)$.

`sorted` creates a new list of $n$ values, and `ans` stores up to $n$ selected values. Python sorting may also use temporary workspace. Peak extra space is $O(n)$, matching the manifest. The original `nums` list is not mutated.

## Alternatives and edge cases

- **Sort ascending and pop from the end:** It makes the same greedy choices but mutates a working list and is slightly less direct.
- **Max-heap:** Repeatedly extract the largest value until the sum condition holds. It also costs $O(n\log n)$ and needs heap construction.
- **Counting frequencies:** Values lie between one and 100, so scan a frequency array from 100 downward for $O(n+100)$ time.
- **Choose arbitrary large-enough subset:** It may satisfy the inequality but fail minimum size or maximum-sum tie breaking.
- **Equality of sums:** The algorithm must continue because the requirement is strictly greater.
- **Single element:** Selecting it leaves sum zero and succeeds immediately.
- **All equal values:** The method selects the smallest count whose total exceeds the remaining total; duplicates are preserved.
- **Duplicate maximum values:** Each occurrence can be chosen, and descending sorting keeps all needed copies.
- **All positive values:** This guarantees eventual success and monotonic chosen sum.
- **Already descending input:** `sorted` still creates a copy, but the greedy order is unchanged.
- **Input immutability:** Using `sorted` rather than `sort` leaves `nums` untouched.
- **Output ordering:** Appending from the descending scan directly satisfies non-increasing order.
