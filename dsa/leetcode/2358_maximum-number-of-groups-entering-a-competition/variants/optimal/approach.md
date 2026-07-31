## General

**Derive the unavoidable student-count bound.** If there are $k$ groups, their
positive integer sizes must increase strictly. The smallest possible sequence
of sizes is therefore $1,2,\ldots,k$, which needs

$$
1+2+\cdots+k=\frac{k(k+1)}{2}
$$

students. Thus $k$ groups are impossible whenever this triangular number
exceeds $n=\lvert\texttt{grades}\rvert$.

**Show that the count bound is sufficient.** Sort the students conceptually by
grade and assign the smallest 1 grade to the first group, the next 2 grades to
the second, and so on through a group of size $k$. Put any surplus students
into the final group. Every grade is positive, every later block contains more
students, and all of its grades are at least those in the preceding block.
Consequently its grade sum is strictly larger as well. The construction works
for every $k$ satisfying the triangular bound, regardless of the actual grade
values; sorting need not be performed by the implementation.

**Solve the bound exactly.** The maximum feasible $k$ satisfies

$$
k=\left\lfloor\frac{\sqrt{8n+1}-1}{2}\right\rfloor.
$$

Use an integer square root for `8 * n + 1` to avoid floating-point boundary
errors. Since only `len(grades)` is inspected, all students are still accounted
for by the proof even though their individual values are not read.

## Complexity detail

Obtaining a list's length and evaluating the fixed integer formula take $O(1)$
time and $O(1)$ auxiliary space under the problem's bounded integer range. No
sorting, traversal, or group construction is required.

## Alternatives and edge cases

- **Greedy triangular loop:** Repeatedly reserve group sizes
  $1,2,3,\ldots$ until the next size does not fit; this is simple and correct
  but takes $O(\sqrt n)$ iterations.
- **Binary search on group count:** Search for the largest $k$ satisfying
  $k(k+1)/2\le n$ in $O(\log n)$ time.
- **Sort and construct groups:** Explicitly sorting grades proves feasibility
  constructively but costs $O(n\log n)$ time and is unnecessary for the count.
- **Surplus students:** After reserving sizes 1 through $k$, all extra students
  can join the last group, increasing both its size and positive grade sum.
- **Equal grades:** Positive equal values still yield increasing sums when
  group sizes increase.
- **Triangular boundaries:** When $n=k(k+1)/2$, exactly $k$ minimal-size groups
  fit; one fewer student permits at most $k-1$ groups.
