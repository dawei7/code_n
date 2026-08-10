## General

**Operations preserve the remainder class**

Adding or subtracting `value` changes an integer by a multiple of `value`. Therefore its remainder modulo `value` never changes.

Conversely, any two integers with the same remainder differ by a multiple of `value`, so repeated operations can transform one into the other. Each input element is a flexible resource for producing any integer in its own remainder class.

The exact original values and signs are irrelevant after their remainder frequencies are known.

**Normalize negative values through modulo**

Python's `x % value` returns a remainder from zero through `value - 1` even when $x$ is negative. For example, `-10 % 5` is zero and `-1 % 5` is four.

This normalized class is exactly what repeated additions or subtractions preserve. Counter `cnt` records how many array elements are available in each class.

**Build the MEX from zero upward**

To make the MEX at least $M$, the transformed array must contain every integer

$$
0,1,2,\ldots,M-1.
$$

Target integer $i$ can be created only from an unused element whose remainder is `i % value`. The loop tries targets in ascending order.

If the required class has an available element, the algorithm spends one by decrementing its count and moves to the next target.

If the class count is zero, no remaining element can become $i$. Since all smaller targets have already been supplied, $i$ is the achieved MEX and is returned.

**Why greedy consumption is forced**

For a particular target $i$, any usable input element must come from exactly one remainder class: `i % value`. Elements in that class are interchangeable with respect to future targets because they can all transform into the same sequence

$$
r,\ r+\texttt{value},\ r+2\cdot\texttt{value},\ldots
$$

There is no advantage to saving one class member while leaving the current smaller target missing. A MEX beyond $i$ is impossible unless $i$ itself is present.

Thus spending one matching resource on each consecutive target is both necessary and optimal.

**Why the first exhausted class is an upper bound**

Suppose the loop reaches $i$ with no remaining resource in class `i % value`. Every original element of that class has already been used for smaller targets sharing the same remainder:

$$
i-\texttt{value},\ i-2\cdot\texttt{value},\ldots
$$

No operation can change an element from another remainder class into $i$. Therefore every possible transformed array that includes all those smaller targets must omit $i$, so no MEX larger than $i$ is possible.

The greedy construction already includes every value below $i$, proving MEX exactly $i$.

**Trace the first sample**

With `value=5`, the input remainder counts provide resources for:

- target $0$ from remainder zero, using $-10$;
- target $1$ from remainder one, using $1$ or $6$;
- target $2$ from remainder two, using $7$;
- target $3$ from remainder three, using $13$ or $8$.

When target $4$ is reached, remainder class four has no resource. Values zero through three can be formed, but four cannot, so the maximum MEX is four.

**Why the loop checks at most `n + 1` targets**

An array of length $n$ cannot contain all $n+1$ distinct nonnegative integers from zero through $n$. By the pigeonhole principle, its MEX is at most $n$.

The range `range(len(nums) + 1)` includes zero through $n$, guaranteeing some iteration finds an exhausted class and returns. The function needs no fallback statement.

**Resource counts, not transformed values**

The solution never chooses how many times to add or subtract `value`. Once a class member is assigned to target $i$, the required operation count exists because their difference is divisible by `value`. Since operations are unlimited and their number is not part of the objective, constructing the actual sequence is unnecessary.

## Complexity detail

Let $n$ be the array length. Building the Counter takes expected $O(n)$ time. The loop executes at most $n+1$ iterations with expected constant-time Counter access, so total expected time is $O(n)$.

The Counter stores at most $\min(n,\texttt{value})$ remainder keys, giving $O(n)$ worst-case auxiliary space, or $O(\texttt{value})$ under the remainder-domain view. The input is not modified.

## Alternatives and edge cases

- **Transform values explicitly:** Searching actual operation sequences is unnecessary because remainder equivalence completely characterizes reachability.
- **Sort chosen representatives:** Sorting can derive a MEX but does extra $O(n\log n)$ work after classes are already sufficient.
- **Array of remainder counts:** A list of length `value` replaces hashing and gives deterministic $O(n+\texttt{value})$ behavior.
- **Negative inputs:** Python modulo normalizes them into the correct nonnegative class.
- **Value one:** Every element belongs to class zero and can form consecutive targets zero through $n-1$, so MEX is $n$.
- **Missing class zero:** Target zero fails immediately and the answer is zero.
- **Duplicate remainders:** Each occurrence is a separate resource for successive targets in that class.
- **MEX upper bound:** Length $n$ guarantees a return by target $n$.
- **Counter mutation:** Only the local frequency structure is decremented; `nums` remains unchanged.
