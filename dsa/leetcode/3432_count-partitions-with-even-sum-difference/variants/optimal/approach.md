## General

Let $T$ be the sum of the entire array and let $L$ be the sum of the prefix on the left of any partition. The right sum is $T-L$, so the requested difference is

$$
L-(T-L)=2L-T.
$$

The term $2L$ is always even. Therefore, the difference is even exactly when $T$ is even; the position of the partition and the particular prefix sum do not affect that parity. This converts what appears to be a prefix-sum counting problem into one global test.

An array of length $n$ has exactly $n-1$ positions between adjacent elements, and every one splits it into two non-empty subarrays. If the total sum is even, all $n-1$ positions qualify. If the total is odd, none qualifies.

## Complexity detail

Computing the total sum reads all $n$ elements once, so time complexity is $O(n)$. The parity test and answer calculation use $O(1)$ auxiliary space. Reading every input element is necessary in the general case because changing an unseen element can change the total parity.

## Alternatives and edge cases

- **Compute both sums at every split:** Summing slices independently takes $O(n^2)$ time and repeats nearly all work.
- **Running prefix sum:** Updating left and right sums gives a correct $O(n)$ method, but checking each partition is unnecessary once the global parity identity is known.
- **Minimum length:** With two elements there is exactly one possible partition, valid precisely when their total is even.
- **All-even values:** The total is even, so every partition is valid.
- **Odd number of odd values:** The total is odd, so no partition is valid.
- **Even number of odd values:** Their parity contributions cancel and every partition is valid.
