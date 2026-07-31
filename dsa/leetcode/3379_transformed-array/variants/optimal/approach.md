## General

Each output position depends only on its own index, its offset, and the unchanged input array. For index `i`, adding `nums[i]` handles both directions: positive offsets increase the index, negative offsets decrease it, and zero leaves it unchanged.

Normalize that signed destination with modulo $n$:

$$
j=(i+\texttt{nums[i]})\bmod n.
$$

The normalized $j$ is always a valid circular index from $0$ through $n-1$. Read `nums[j]` into the new result without modifying `nums`. Repeating this direct lookup for every position implements every independent movement exactly, including multiple complete wraps.

## Complexity detail

There is one constant-time index calculation and one array lookup per element, so the running time is $O(n)$. The returned array requires $O(n)$ space; excluding the required output, the auxiliary space is $O(1)$.

The benchmark defines `size` as $n$ and uses legal lengths 16, 40, and 100 with destinations spread across each array. The reference indexes the computed destination directly. A correct slower implementation linearly scans `nums` from the beginning to find each target index, taking $O(n^2)$ time while producing the same output.

## Alternatives and edge cases

- **Move one step at a time:** It follows the narrative literally but performs unnecessary repeated work for large absolute offsets.
- **Scan for each destination index:** It is correct but discards the random-access property of an array and costs $O(n^2)$ time.
- **Mutate `nums` in place:** Later positions would read transformed values, violating the independence of the actions.
- **Negative remainder in other languages:** Some `%` operators keep a negative sign; normalize with `((i + nums[i]) % n + n) % n` when required.
- **Zero offset:** The destination is the current index, so the original value is copied unchanged.
- **Offset equal to a multiple of $n$:** Any number of full wraps returns to the starting index.
- **Single element:** Every signed offset maps to index zero.
- **Maximum offset:** Values $-100$ and $100$ need no special handling because modulo removes complete wraps.
