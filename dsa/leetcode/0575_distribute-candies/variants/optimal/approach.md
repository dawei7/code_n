## General
**Two independent limits determine the answer**

Let `d` be the number of distinct values in `candyType`. The sibling cannot receive more than `d` distinct types because no other types exist. She also receives exactly $n / 2$ candies, so she cannot represent more than $n / 2$ types.

**Both limits can be attained**

If $d \le n / 2$, choose one candy of every type and fill the remaining positions with arbitrary duplicates; all `d` types are represented. If $d > n / 2$, choose one candy from any $n / 2$ different types. Thus the maximum is exactly $\min(d, n / 2)$.

**Count types with a set**

Insert every candy value into a set, then return the smaller of the set size and half the list length. No arrangement or simulation of the other sibling's share is needed.

## Complexity detail
For `n` candies, building the hash set takes $O(n)$ expected time and stores at most `n` distinct values, so the extra space is $O(n)$.

## Alternatives and edge cases
- **Sort then count changes:** also finds the number of types but costs $O(n \log n)$ time and may mutate the input.
- **Linear list of discovered types:** is correct, but membership checks can take $O(n)$ apiece and make the full scan $O(n^2)$.
- **Frequency map:** works in $O(n)$ expected time, but the counts themselves are unnecessary.
- **All candies distinct:** the half-share capacity is the binding limit.
- **All candies identical:** exactly one type can be represented.
- **Many duplicates but enough capacity:** one candy of each existing type can be selected before filling the remaining share.
- **Negative type identifiers:** are ordinary hashable values and require no special handling.
