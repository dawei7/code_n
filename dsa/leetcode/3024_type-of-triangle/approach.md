## General

**Sort the three side lengths first.** Let the sorted values be

$$
a\le b\le c.
$$

Sorting gives one consistent role to each value: $c$ is the longest proposed side. This makes both triangle validation and equality classification simple. The exact source calls `nums.sort()`, so it rearranges the caller's three-element list in place.

**Why only one triangle inequality must be tested.** Three positive lengths form a nondegenerate triangle exactly when each pair sums to more than the remaining side:

$$
a+b>c,\qquad a+c>b,\qquad b+c>a.
$$

After sorting and using the guarantee that side lengths are positive, the last two inequalities hold automatically. Since $c\ge b>0$, we have $a+c>b$. Since $c\ge a>0$, we have $b+c>a$. The only inequality that can fail is the one opposing the largest side:

$$
a+b>c.
$$

That is why the source checks only `nums[0] + nums[1] <= nums[2]`. If this condition is true, the strict inequality fails and the method returns `"none"`.

Equality is deliberately rejected. If $a+b=c$, the three segments lie flat along one line and enclose zero area; this is a degenerate triangle, not a valid triangle under the problem definition. Hence the invalid condition uses `<=`, not merely `<`.

**Classify only after validity is established.** Once $a+b>c$, the lengths form a triangle. The categories then depend on how many sides are equal.

If `nums[0] == nums[2]`, then $a=c$. Combined with $a\le b\le c$, this forces $a=b=c$. The triangle is equilateral. Comparing only the smallest and largest is enough after sorting because the middle value cannot lie outside them.

If the triangle is not equilateral, the source checks `nums[0] == nums[1] or nums[1] == nums[2]`. Either condition means exactly two side lengths are equal, so the triangle is isosceles. Sorting guarantees that equal values are adjacent; there is no need to separately test $a=c$, because that case was already identified as all three equal.

If neither adjacent equality holds, all three values differ and the triangle is scalene.

**The order of checks is important.** Consider lengths `[1,1,2]`. Two sides are equal, but they do not form a valid triangle because $1+1=2$. If equality classification happened first, the method might incorrectly call this isosceles. The exact solution validates the strict triangle inequality before examining type, so it correctly returns `"none"`.

Similarly, the equilateral check comes before the general isosceles check. An equilateral triangle technically has at least two equal sides, but the problem expects the more specific label `"equilateral"`. The ordering ensures the categories are mutually exclusive in the returned result.

**A complete case trace.** For `[5,3,4]`, sorting produces `[3,4,5]`. Because $3+4>5$, the triangle is valid. Neither smallest equals largest nor either adjacent pair equals, so the result is `"scalene"`.

For `[5,5,3]`, sorting gives `[3,5,5]`. The inequality $3+5>5$ holds. Smallest and largest differ, but the final two values match, so the result is `"isosceles"`.

For `[6,6,6]`, smallest equals largest and the result is `"equilateral"`.

For `[2,3,5]`, $2+3\le5$, so it returns `"none"` before equality classification.

**Why the method is exhaustive.** Every three-value input first falls into one of two groups: it either fails the largest-side inequality or satisfies it. The first group is exactly the invalid configurations. In the valid group, the number of distinct sorted values is one, two, or three, corresponding exactly to equilateral, isosceles, or scalene. Thus every input receives one correct label, and no other state is possible.

## Complexity detail

The list always contains exactly three values. Sorting three values performs only a bounded number of comparisons, and all later work is a bounded sequence of arithmetic and equality tests. With respect to input size, time complexity is $O(1)$ and auxiliary space is $O(1)$.

If one mechanically writes the sorting cost as $O(3\log3)$, it simplifies to $O(1)$. Python's in-place sort may use a small amount of implementation workspace, but with a fixed three-element input that too is constant.

The method mutates `nums` by sorting it. Mutation is not additional asymptotic space, but it is a meaningful behavioral detail for a caller that might reuse the list. A version using `a, b, c = sorted(nums)` would preserve the input while allocating a new three-element list; that would still be $O(1)$ under the fixed-size contract.

## Alternatives and edge cases

- **Check all three inequalities:** This is correct but redundant for sorted positive lengths. The largest-side inequality implies the other two automatically.
- **Avoid sorting with a maximum:** One can find the largest side and compare it with the sum of the other two, then count equalities. That remains $O(1)$ but tends to require more bookkeeping than sorting three items.
- **Use a set for classification:** The number of distinct lengths distinguishes equilateral, isosceles, and scalene after validity is known. Creating a set works, but direct comparisons avoid an extra container.
- **Degenerate equality $a+b=c$:** It must return `"none"` because the required inequality is strict and the segments enclose no area.
- **One side longer than the other two combined:** The same `<=` condition rejects it immediately.
- **All three sides equal:** Positivity guarantees validity, and comparing the sorted smallest with largest correctly identifies equilateral.
- **Exactly two sides equal:** The equal values become adjacent after sorting, so one of the isosceles comparisons succeeds.
- **Three distinct valid sides:** Both equality checks fail, leaving scalene.
- **Positive-length guarantee:** The proof that two inequalities are automatic relies on positive sides. If zeros or negative values were allowed, the validation would need additional checks, but they are outside this contract.
- **Input order:** Any permutation produces the same sorted triple and therefore the same classification.
- **Input mutation:** The protected source leaves `nums` sorted. This does not change the returned answer, but callers should not assume the original ordering remains.
