## General

**Fix the middle soldier**

Every valid team has indices $i<j<k$. If the middle index $j$ is fixed, an increasing team needs a smaller-rated soldier on the left and a larger-rated soldier on the right. A decreasing team needs a larger-rated soldier on the left and a smaller-rated soldier on the right.

This turns a three-index enumeration into four simple counts around each possible middle soldier. The exact loop uses variable `i` for that middle index and `b` for `rating[i]`.

**Count increasing-team choices**

`l = sum(a < b for a in rating[:i])` counts left-side ratings smaller than the middle. Each comparison produces a Boolean, which Python sums as one or zero.

`r = sum(c > b for c in rating[i + 1:])` counts right-side ratings larger than the middle.

Every one of the `l` left choices can pair independently with every one of the `r` right choices. Their indices automatically satisfy left less than middle less than right, and their ratings satisfy smaller less than middle less than larger. Therefore `l * r` is exactly the number of increasing teams whose middle soldier is `i`.

**Derive decreasing counts by complement**

There are `i` soldiers to the left. Ratings are unique, so every left rating is either smaller or larger than `b`; none is equal. Since `l` are smaller, `i - l` are larger.

There are `n - i - 1` soldiers to the right. Since `r` are larger, the remaining

`n - i - 1 - r`

are smaller.

A decreasing team chooses one larger rating from the left and one smaller rating from the right, yielding

`(i - l) * (n - i - 1 - r)`

teams for this middle index.

**Why multiplication is the right combinatorial operation**

For a fixed middle, choosing the left member does not restrict which qualifying right member can be chosen. Each valid left choice pairs with all valid right choices. The Cartesian-product rule therefore multiplies their counts.

For example, if two smaller soldiers lie left of the middle and three larger soldiers lie right, there are $2\cdot3=6$ increasing triples centered there. Listing them would repeat the same structure; multiplication counts them directly.

**Following part of the first example**

For `rating = [2,5,3,4,1]` and middle value 3 at index two, the left values are 2 and 5. One is smaller and one larger, so `l=1` and `i-l=1`. The right values are 4 and 1. One is larger and one smaller, so `r=1` and the right-smaller count is one.

This middle contributes one increasing team `(2,3,4)` and one decreasing team `(5,3,1)`. Other middle positions account for the remaining valid team.

**Why no team is missed or counted twice**

Every triple $i<j<k$ has exactly one middle index $j$. If its ratings increase, it is counted in the left-smaller times right-larger product for that $j$. If they decrease, it is counted in the complementary product. A valid team cannot be both strictly increasing and strictly decreasing.

Conversely, every pair chosen by either product has the required index order because it comes from opposite sides of the fixed middle, and it has the required strict rating order by its category. Thus every counted combination is valid.

Summing both products across all middle indices therefore counts every valid team exactly once.

**Why uniqueness matters**

The complement formulas assume a left value not smaller than `b` must be larger, and a right value not larger must be smaller. Equal ratings would violate that partition and could be incorrectly counted as decreasing. The problem's unique-rating guarantee makes the subtraction exact.

**What the Python slices do**

`rating[:i]` and `rating[i + 1:]` create new lists for the left and right portions on every iteration. The generator expressions then scan those temporary lists. This keeps the code compact but has a space consequence; an index-based loop could perform the same counts without allocating slices.

## Complexity detail

For each of $n$ middle positions, the left and right scans examine $n-1$ ratings in total. Time is $O(n^2)$.

The counting idea needs only scalar variables, but the exact Python code creates slices whose combined length is $n-1$ during an iteration. Peak auxiliary space is therefore $O(n)$, even though those lists are temporary and released between iterations.

The manifest lists $O(1)$ space, which describes an index-based implementation that scans `rating` without slicing. For the exact shipped statements, $O(n)$ peak auxiliary space is the accurate bound. The time bound still matches the manifest.

## Alternatives and edge cases

- **Index-based quadratic scan:** Loop over left and right indices directly. It preserves $O(n^2)$ time while achieving the manifest's $O(1)$ auxiliary space.
- **Brute-force triples:** Test all $\binom n3$ index triples in $O(n^3)$ time. It is direct but repeats middle-side comparisons.
- **Fenwick trees:** Maintain rating frequencies on the left and right to query smaller/larger counts in $O(\log n)$ per soldier, reducing time to $O(n\log n)$.
- **Coordinate compression:** A Fenwick solution can compress the unique ratings so memory depends on $n$, not the maximum rating value.
- **Strictly increasing array:** Every three-index choice is valid, yielding $\binom n3$ teams.
- **Strictly decreasing array:** The same combination count arises from descending teams.
- **No suitable pair around a middle:** If either factor is zero, that direction contributes zero.
- **First or last soldier:** One side is empty, so neither can serve as the middle of a three-person team.
- **Unique ratings:** This is essential for deriving larger counts by subtracting smaller counts from side sizes.
- **Soldiers reused across teams:** The method counts combinations independently, as explicitly allowed.
- **No double counting:** Each triple has one middle index and one monotonic direction.
- **Temporary slices:** They do not mutate the input but raise peak space from constant to linear.
- **Boolean sums:** Python converts comparison results `True` and `False` to one and zero, respectively.
