## General
**Count new pairs when their later endpoint arrives**

Scan the array from left to right and store how many times each value has already appeared. Suppose the current value has occurred $f$ times. Each of those $f$ earlier indices forms one new good pair with the current index, and there are no other new pairs ending here. Add $f$ to the answer, then increase that value's frequency.

This assigns every good pair to its unique later endpoint. A pair is counted when that endpoint is processed, never before and never again, so the running total is exact after the final element.

**Connection to the combination formula**

If a value appears $k$ times overall, its contribution is

$$
0+1+\cdots+(k-1)=\frac{k(k-1)}{2}.
$$

The streaming method accumulates this same sequence as occurrences arrive. It avoids a second pass over the frequency table and directly respects the $i<j$ direction. Contributions for different values are disjoint because equality is required, so adding them yields the global count.

## Complexity detail
The scan performs one expected constant-time hash lookup and update per element, giving $O(n)$ time. The frequency map stores one entry for each of the $u$ distinct values, so it uses $O(u)$ auxiliary space.

Because the source contract restricts values to 1 through 100, a fixed 101-entry count array could make storage constant with respect to $n$. The hash-map statement remains the representation-independent bound.

## Alternatives and edge cases
- **Frequency combinations:** count all frequencies first, then sum $k(k-1)/2$ for each value. This is also $O(n)$ time and $O(u)$ space, but requires a second pass over distinct values.
- **Nested index loops:** test every pair directly. It is simple and correct but takes $O(n^2)$ time.
- **Fixed count array:** exploit the value range 1 through 100 for deterministic constant-size storage; this is less general than a map.
- **Single element:** no two distinct indices exist, so the answer is zero.
- **All distinct:** every prior frequency is zero and no pair is added.
- **All equal:** the answer reaches its maximum $n(n-1)/2$.
- **Several duplicate groups:** compute each value's pairs independently; pairs never cross values.
- **Index order:** counting unordered choices is valid only because every two distinct indices have one unique ordering with $i<j$.
