## General

**Choose extremes according to each coefficient**

The expression is

$$
a+b-c.
$$

The coefficients of `a` and `b` are positive, so those roles should receive the two largest array occurrences. The coefficient of `c` is negative, so `c` should receive the smallest occurrence.

If the sorted values are

$$
x_1\le x_2\le\cdots\le x_n,
$$

the optimal value is

$$
x_n+x_{n-1}-x_1.
$$

Distinct indices are respected: the two maxima are two occurrences, not merely one maximum value reused twice, and the array has at least three positions. Even when extreme values tie, sorted positions remain distinct.

**Track the two largest occurrences**

`a` is the largest value seen so far and `b` is the second-largest occurrence. Both start at negative infinity.

When a new `x>=a` arrives, it becomes the new largest, while the old `a` shifts into `b`:

`a,b=x,a`.

Using `>=` rather than `>` matters for duplicates. If two equal maximum values occur, the second copy must occupy the other positive role.

If `x<a` but `x>b`, it becomes the second largest. Otherwise it cannot improve either maximum state.

After the scan, `a` and `b` are the greatest two values counting positions.

As a short state trace for `[3,1,3]`, the first three sets `a=3` and leaves `b` at negative infinity. One then becomes `b=1`. The final three satisfies `x>=a`, so it moves the old three into `b` and becomes the new `a`. The two equal maxima are retained as separate occurrences.

**Track the smallest occurrence independently**

`c` begins at positive infinity and is replaced whenever `x<c`. At the end it is the global minimum.

Although the source stores values rather than indices, the extreme formula remains realizable with distinct positions. In sorted positional order, `x_1`, `x_{n-1}`, and `x_n` refer to three positions. If all values are equal, any three distinct indices supply the same three stored values.

If `n=3`, those sorted positions are exactly all array indices. If `n>3`, the minimum position and final two positions are still distinct unless values tie; ties change only values, not the existence of three separate positions. Thus value-only tracking cannot accidentally reuse one physical element.

For `[1,4,2,5]`, the states finish as `a=5`, `b=4`, and `c=1`, returning eight.

For `[-2,0,5,-2,4]`, the two largest occurrences are five and four, and the smallest is negative two. Subtracting a negative adds two, giving eleven.

**Why no other selection can do better**

Take any valid triple. If its `a` or `b` role does not use one of the two largest available occurrences, replacing that role with a larger unused occurrence cannot decrease the expression. After assigning the top two occurrences to positive roles, the best remaining negative-coefficient role is the smallest remaining occurrence.

The global minimum is never lost through an index conflict with both top positions: with at least three sorted positions, the first and final two positions are distinct. Ties in value do not invalidate positional distinctness.

Conversely, choosing these three occurrences is legal and attains the upper bound, proving the returned expression is maximal.

Another algebraic view separates the roles: maximizing `a+b` over two distinct indices gives the sum of the two largest occurrences. Once those positions are fixed, subtracting the smallest remaining occurrence is best. When the global minimum ties a maximum value, every value is tied across enough positions for the same numeric formula to remain realizable.

## Complexity detail

Let `n` be the array length. The method makes one pass and performs constant work per element, so time complexity is $O(n)$.

It stores only `a`, `b`, `c`, and the current value, giving $O(1)$ auxiliary space. The input is not modified.

The sentinels are replaced because `n>=3`. Python infinity values compare safely with the bounded integers, and the final arithmetic uses only real array values.

## Alternatives and edge cases

- **Enumerate ordered triples:** There are $O(n^3)$ choices. Coefficient signs identify the optimal extremes directly.
- **Sort the array:** Reading the smallest and two largest positions after sorting costs $O(n\log n)$ and may mutate input. One-pass extrema are sufficient.
- **Use the maximum twice:** The roles require distinct indices. `a` and `b` track two occurrences, including duplicates when available.
- **Track only one maximum:** The second positive term needs the second-largest occurrence.
- **Choose the largest `c`:** Because it is subtracted, that would reduce rather than increase the expression.
- **All values negative:** “Largest” means least negative, while subtracting the most negative value provides a large gain.
- **All values equal:** Any three indices give one copy plus one copy minus one copy, equal to the common value.
- **Duplicate maximum:** The `x>=a` branch preserves both occurrences as `a` and `b`.
- **Duplicate minimum:** Any minimum occurrence distinct from the top positions can serve as `c`; values alone are sufficient for the score.
- **Exactly three elements:** All positions must be used, and the formula assigns their roles optimally.
- **Input order:** Roles have no positional ordering requirement, so scan order does not constrain the chosen triple.
