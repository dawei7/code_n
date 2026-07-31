## General

A direct left-to-right scan returns the smallest match as soon as it finds one. The value bound makes that scan even tighter. Among integers from $0$ through $999$, the largest decimal digit sum is $9+9+9=27$, while `1000` has digit sum $1$. Therefore no allowed array value can have digit sum $28$ or greater.

Consequently, every index at least `28` is impossible: its required digit sum exceeds the maximum attainable value. It is sufficient to inspect `nums[:28]`, covering indices `0` through `27` when they exist. For each inspected value, convert its at most four decimal digits and add them. If the sum equals the current index, return immediately. Since indices are visited in ascending order, that returned index is necessarily the smallest valid one. If all potentially valid positions fail, every remaining index is impossible by the bound, so return `-1`.

## Complexity detail

At most 28 values are inspected, and every allowed value has at most four decimal digits. Both limits are fixed by the contract, so the algorithm takes $O(1)$ time and $O(1)$ auxiliary space. Expressed without applying those bounds, the work is $O(\min(n,28))$ digit checks.

## Alternatives and edge cases

- **Scan the entire array:** Correct and conventionally described as $O(n)$, but positions after `27` cannot qualify and need not be visited.
- **Arithmetic digit extraction:** Repeated `% 10` and integer division avoids string conversion and has the same bounded complexity.
- **Index zero:** Only a stored value with digit sum zero qualifies, which under the constraints means `nums[0] == 0`.
- **Several matches:** Immediate return during the ascending scan guarantees the smallest index.
- **Maximum digit sum:** The value `999` can qualify at index `27`, so the cutoff must include that index.
- **Value 1000:** Its digit sum is `1`, not `28` or another four-digit magnitude.
- **Arrays longer than 28:** Their suffix cannot contain a valid index even though it remains part of the input.
