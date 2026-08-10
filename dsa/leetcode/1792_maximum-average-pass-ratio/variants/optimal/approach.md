## General

**Optimize the improvement, not the current ratio**

For a class with $p$ passing students out of $t$ total students, its current pass ratio is $p/t$. Assigning one guaranteed-to-pass student changes both counts, producing $(p+1)/(t+1)$.

The useful quantity for deciding where that student should go is the marginal gain

$$
\Delta(p,t)
=
\frac{p+1}{t+1}-\frac{p}{t}
=
\frac{t-p}{t(t+1)}.
$$

A class with the lowest current ratio does not necessarily have the greatest gain. Class size matters: changing one student has more influence on a small class than on a very large class. The algorithm must compare $\Delta$, not merely $p/t$, $p$, or $t$.

Because the number of classes is fixed, maximizing the average pass ratio is equivalent to maximizing the sum of class ratios. Dividing the final sum by the number of classes does not affect which assignment is optimal.

**Each class has diminishing returns**

Suppose a class has already received $x$ extra students. Its next gain is

$$
\Delta_x
=
\frac{p+x+1}{t+x+1}-\frac{p+x}{t+x}
=
\frac{t-p}{(t+x)(t+x+1)}.
$$

The numerator $t-p$ remains constant because every added student increases both passing and total counts by one. The denominator grows with $x$, so the next gain never increases. A class may deserve several students, but after each assignment its priority must be recalculated.

This diminishing-return property is what makes a greedy decision valid. At any moment, every class exposes its next available gain. Choose the largest one. If an allegedly optimal allocation used a smaller currently available gain instead, exchange that assigned student for the larger gain. The total cannot decrease. Later gains from the chosen class are no larger than its current gain, so respecting the per-class order does not create a hidden advantage that invalidates the exchange. Repeating this exchange transforms an optimal allocation into the greedy sequence.

Another view is that each class offers a descending list of marginal gains. Assigning $x$ students to that class takes the first $x$ entries of its list. The goal is to select `extraStudents` gains across all lists while respecting those prefixes. Since each list is descending, repeatedly selecting the greatest exposed head produces the greatest possible total.

**Represent a max-priority rule with Python's min-heap**

Python's heap removes the smallest key, but the desired class has the largest positive gain. The protected solution stores

`a / b - (a + 1) / (b + 1)`,

which is exactly $-\Delta(a,b)$. The largest gain becomes the most negative key, so it rises to the top of the min-heap.

Each heap entry is a tuple containing that negative gain, the current passing count `a`, and the current total `b`. The list comprehension creates one entry per class, and `heapify` organizes all entries in linear time.

For each extra student, the solution removes the top entry, increments both `a` and `b`, recomputes the class's new negative marginal gain, and pushes the updated tuple back. The heap always contains exactly one current entry for every class.

The extra tuple fields also provide deterministic tie-breaking when two floating-point gain keys compare equal. Either tied class is an optimal choice because their immediate improvements are equal.

**Following the first example**

For classes `[1,2]`, `[3,5]`, and `[2,2]`, the initial gains are

$$
\frac{2}{3}-\frac{1}{2}=\frac{1}{6},
\qquad
\frac{4}{6}-\frac{3}{5}=\frac{1}{15},
\qquad
1-1=0.
$$

The first class has the largest gain, so it receives the first extra student and becomes `[2,3]`. Its next gain is `3/4 - 2/3 = 1/12`, which is still larger than `1/15`, so it receives the second student too. The final ratios are `3/4`, `3/5`, and 1, whose average is approximately 0.78333.

**Compute the answer from the final heap state**

After all assignments, each heap tuple contains the final `a` and `b` for its class. Heap order is irrelevant to summation. The solution adds `a / b` for every tuple and divides by `len(classes)`.

The method does not mutate the input sublists. Popped counts are copied into local integers, incremented, and stored in new heap tuples.

**Why the allocation is correct**

At every step the heap key identifies the greatest available marginal improvement. Diminishing returns guarantee that future gains from a class cannot jump ahead before its current gain is taken. The exchange argument therefore proves that taking the heap's choice cannot make the best achievable final sum worse.

By induction over the number of assigned students, after each greedy step there exists an optimal complete allocation sharing the greedy prefix. After all students are assigned, the entire greedy allocation is optimal. Summing its final ratios and dividing by the unchanged class count yields the maximum average.

## Complexity detail

Let $n$ be the number of classes and $e$ be `extraStudents`. Creating the $n$ entries and calling `heapify` costs $O(n)$. Each of the $e$ assignments performs one heap removal and one insertion, each $O(\log n)$, for $O(e\log n)$ total. The final ratio sum scans $n$ entries in $O(n)$ time.

Overall time is $O(n+e\log n)$, matching the manifest. The heap holds one constant-size tuple per class, so auxiliary space is $O(n)$.

The solution uses floating-point keys and ratios. Exact rational cross-products could compare gains without rounding, but the problem explicitly accepts an absolute error up to $10^{-5}$, and the final computation uses standard floating-point arithmetic.

## Alternatives and edge cases

- **Rescan every class per student:** It makes the same greedy choice but costs $O(en)$ time, which is too slow at the maximum constraints.
- **Choose the smallest current ratio:** This ignores class size and may select a class with a smaller marginal improvement.
- **Assign all students at once to one class:** Marginal gains decrease after every assignment, so another class can become better partway through.
- **Binary search on a gain threshold:** More advanced resource-allocation methods are possible, but the heap directly implements the discrete choices within the constraints.
- **Exact fraction comparison:** Compare $(t-p)/(t(t+1))$ values by cross multiplication to avoid floating-point heap keys; integer products must use sufficient width.
- **Already perfect class:** When $p=t$, its gain is zero because adding another passing student keeps the ratio at one.
- **All classes perfect:** Every assignment has zero gain and the returned average remains exactly one.
- **One class:** Every extra student necessarily goes there; repeated pop-update-push operations produce its final ratio.
- **Repeated assignment to one class:** Its tuple is updated after each student, so the next decision uses its smaller new gain.
- **Equal gains:** Either class can be chosen without changing the best possible total.
- **Large `extraStudents`:** The loop performs exactly one allocation per student, and each maintains the heap invariant.
- **Tuple tie-breaking:** Passing and total counts may decide heap order after equal keys, but this cannot harm optimality.
- **Accepted precision:** The answer is a float and is judged with tolerance rather than exact textual equality.
- **Input preservation:** The original `classes` rows are not modified.
