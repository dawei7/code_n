## General

For a list of even length $n$, node $i$ is paired with node $n-1-i$ for every $0 \le i < n/2$. The first node pairs with the last, the second with the second-to-last, and so forth until the two middle nodes form the final pair. The difficulty is not the addition; it is that a singly linked list supports forward traversal but does not provide direct access from the end.

**Materialize forward traversal as random-access values**

The exact solution resolves that mismatch by copying every node value into a Python list named `s`:

`while head:`

During each iteration, `s.append(head.val)` records the current value and `head = head.next` advances to the following node. If the linked-list values in order are $v_0,v_1,\ldots,v_{n-1}$, then after the loop the array obeys `s[i] == v_i` for every valid index.

This representation is useful because Python lists support constant-time indexing from either end. Once the values have been copied, a twin pair can be addressed directly without walking backward through linked nodes.

Notice that the local variable `head` is advanced until it becomes `None`. This does not remove nodes or alter any `next` pointer. Reassigning the local reference merely changes which node the method currently points to; the linked-list structure itself remains intact.

**Translate the twin formula into Python indexing**

The number of values is recorded as `n = len(s)`. For a first-half index `i`, the mathematical twin index is $n-1-i$. Python’s negative indexing offers an equivalent expression:

- `s[-1]` is the last value, at ordinary index $n-1$;
- `s[-2]` is the second-to-last value, at ordinary index $n-2$;
- in general, `s[-(i + 1)]` is the value at index $n-1-i$.

Therefore, the expression

`s[i] + s[-(i + 1)]`

is exactly the twin sum for first-half node `i`. For `[4,2,2,3]`, index `0` produces `4 + 3 = 7`, and index `1` produces `2 + 2 = 4`.

**Visit every pair exactly once**

Because $n$ is even, there are exactly $n/2$ distinct twin pairs. The expression `n >> 1` shifts the nonnegative integer $n$ right by one bit, which equals integer division by two. Thus `range(n >> 1)` generates

$$
0,1,\ldots,\frac{n}{2}-1.
$$

These are precisely the allowed first-half indexes from the definition. Stopping there is essential. Continuing into the second half would revisit the same pairs in reverse order, adding work without introducing a new sum.

The generator expression computes one twin sum for each of those indexes:

`(s[i] + s[-(i + 1)] for i in range(n >> 1))`

The outer `max(...)` retains and returns the largest generated value. The list is guaranteed to contain an even number of nodes and at least two nodes, so `n >> 1` is at least one. The generator is consequently non-empty, and `max` never faces an undefined empty input.

**Why the maximum is correct**

Every legal twin pair has a unique smaller index $i$ in the first half. The range visits that index once. At that iteration, negative indexing selects exactly the pair’s larger index $n-1-i$, so the generated value is exactly that pair’s sum. No legal pair is skipped, and no unrelated pair is generated. Since `max` is applied to the complete set of twin sums, its result is the required maximum.

This solution is especially direct for beginners because the array positions mirror the mathematical definition. It makes a full first pass to gain random access, then performs a half-length pass to evaluate all mirrored pairs.

**Distinguish the exact code from the manifest summary**

The local Optimal manifest describes an in-place reversal of the second half and lists constant auxiliary space. That is a valid algorithm discussed by the editorial, but the exact stored `variants/optimal/solution.py` does not implement it. The stored code constructs `s` with all $n$ values. This document follows the exact solution as requested, so its space analysis is necessarily linear. Nothing in the source file reverses links or achieves $O(1)$ auxiliary space.

## Complexity detail

Let $n$ be the number of linked-list nodes. The first `while` loop visits every node once and appends one value, taking $O(n)$ time. The generator then evaluates $n/2$ twin pairs. Each Python list access, addition, and maximum comparison takes $O(1)$ time, so this phase is also $O(n)$. The consecutive phases give total time $O(n)$.

The list `s` stores all $n$ values and therefore uses $O(n)$ auxiliary space. The generator consumed by `max` is lazy: it produces one sum at a time rather than constructing another list of $n/2$ sums, so its iteration state uses $O(1)$ additional space. The total auxiliary space of the exact implementation remains $O(n)$.

The returned integer needs constant space. The existing linked-list nodes are input storage and are not counted as auxiliary memory. The method does not mutate them.

## Alternatives and edge cases

- **Reverse the second half in place:** A slow/fast pointer can find the midpoint, the second half can be reversed, and two forward pointers can then enumerate mirrored pairs in $O(n)$ time and $O(1)$ auxiliary space. This is asymptotically more space-efficient, but it is not the exact stored solution and it mutates links unless the second half is restored afterward.
- **Stack of values:** Pushing values onto a stack and pairing popped end values with nodes from the start is also $O(n)$ time and $O(n)$ space. It expresses reverse order explicitly but offers no asymptotic benefit over the array.
- **Repeatedly find the tail:** Starting from the head and rescanning to locate each matching node near the end avoids an array but can require $O(n^2)$ time, which is unnecessary for up to $10^5$ nodes.
- **Recursive traversal:** Recursion can pair nodes while unwinding, but the call stack grows to $O(n)$ and may exceed Python’s recursion limit on large legal inputs.
- **Two nodes:** `n >> 1` equals one, so the generator evaluates the sole pair and returns the sum of both nodes.
- **All twin sums equal:** `max` returns that shared value; it does not matter which pair first produced it.
- **Maximum values:** A pair can sum to `200000`, which Python integers represent safely.
- **Even-length guarantee:** The algorithm relies on every first-half node having a distinct second-half twin. No special middle-node rule is needed because odd lengths are excluded.
- **Negative indexing:** The parentheses in `-(i + 1)` matter. They deliberately map `i = 0` to `-1`, `i = 1` to `-2`, and so on.
- **Right shift:** For a nonnegative even `n`, `n >> 1` equals `n // 2`. Division with `/` would produce a floating-point value and could not be passed directly to `range`.
- **Non-empty generator:** The minimum legal length is two, so `max` always receives at least one sum. Without that guarantee, an explicit default or empty-list branch would be required.
- **Local `head` reassignment:** Advancing `head` inside the method does not change the caller’s node links. It only exhausts this local reference.
- **Input preservation:** Unlike the in-place reversal alternative, the exact implementation leaves the list topology unchanged, which may be desirable even though it costs linear extra memory.
