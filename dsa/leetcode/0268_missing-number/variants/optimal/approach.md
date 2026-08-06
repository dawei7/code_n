## General

**Compare the complete and observed sums**

For an array of length $n$, the complete range from zero through $n$ has arithmetic sum

$$
\frac{n(n+1)}{2}.
$$

Compute this value directly, subtract `sum(nums)`, and return the difference.

**Subtraction isolates exactly the absent value**

Let the missing value be $x$. The input contains every complete-range value except $x$, so its sum is the complete
arithmetic sum minus $x$. Subtracting the observed sum from the complete sum cancels every present value and leaves
exactly $x$. Python integers represent the largest legal sum exactly, so the calculation cannot overflow.

## Complexity detail

`sum(nums)` scans the $n$ elements once, so the candidate takes $O(n)$ time. The length, arithmetic total, and running
sum use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **XOR cancellation:** also takes $O(n)$ time and $O(1)$ space and avoids fixed-width overflow, but needs an explicit positional loop.
- **Set membership:** uses $O(n)$ extra space.
- **Test each candidate against the list:** can take $O(n^2)$.
- **Missing endpoint:** the same difference yields zero or $n$ without a special case.
- **One element:** the formula handles either legal input `[0]` or `[1]` directly.
