## General

Each original number needs a numeric sorting key produced by replacing every decimal digit according to `mapping`. The output must still contain the original numbers, and equal mapped keys must preserve input order.

The exact solution computes a mapped integer for every element, pairs that key with the element's original index, sorts those pairs, and uses the sorted indices to retrieve the untouched values.

**Map a nonzero integer from right to left**

Helper `f(x)` uses `divmod(x, 10)` to remove one decimal digit at a time. It returns:

- the quotient, which becomes the remaining unprocessed prefix;
- the remainder `v`, which is the current last digit.

The digit is replaced with `mapping[v]`. Variable `k` is its decimal place value: one for units, ten for tens, one hundred for hundreds, and so on.

The statement `y = k * v + y` inserts the mapped digit into the same positional place in the new integer. Multiplying `k` by ten prepares for the next original digit.

For an original number with digits $d_pd_{p-1}\ldots d_0$, the constructed value is

$$
\sum_{q=0}^{p}10^q\cdot\texttt{mapping}[d_q].
$$

That is exactly the integer obtained by digit replacement.

**Handle original zero separately**

The decimal representation of zero contains one digit, zero. The normal `while x` loop would execute zero times and incorrectly leave mapped value zero regardless of `mapping[0]`.

The special return `mapping[0]` applies the rule to that single digit. This matters because zero may map to any digit from zero through nine.

**Let numeric construction discard mapped leading zeros**

If an original leading digit maps to zero, its high-place contribution is zero. The resulting integer naturally has no visible leading zero.

For the example mapping, 338 becomes digit sequence `007`. Arithmetic construction produces numeric value seven, which is exactly how the mapped value should compare.

Lower internal or trailing positions are still preserved through their powers of ten. Only leading zeros disappear, as they do in ordinary integer notation.

**Decorate every value with key and original index**

The generator creates `(f(x), i)` for every `(i, x)` from `enumerate(nums)`. The first component is the mapped sorting key; the second records original position.

The original value itself need not be stored in the pair because it can later be recovered as `nums[i]`.

This decorate-sort-undecorate pattern cleanly separates comparison data from returned data.

**Sort by mapped value and preserve equal-key order**

Python sorts tuples lexicographically. It compares mapped values first. When those are equal, it compares original indices.

Since indices increase in the input order, equal mapped values are arranged by their original positions. This explicitly satisfies stability even without relying only on Python's stable-sort guarantee.

For mapped keys of 338 and 38 both equal to seven, their pairs might be `(7, 0)` and `(7, 1)`. The smaller index remains first.

**Return originals rather than mapped values**

The final comprehension `[nums[i] for _, i in arr]` ignores each mapped key and looks up the original number.

Thus mapping affects only ordering. It never replaces an element in the returned array, exactly as the note requires.

**Why the sorted result meets all requirements**

For each input occurrence, `f` computes its precise mapped numeric value and the decorated array contains one pair. Tuple sorting orders all pairs non-decreasingly by that first component.

When first components tie, ascending original indices reproduce the input relative order. The undecoration step returns each original occurrence once in the pair order. Therefore the output is a permutation of `nums` sorted exactly by mapped values with stable ties.

The mapping itself is a permutation, but the proof does not depend on mapped numeric keys being unique. Different original lengths and leading mapped zeros can produce equal keys, which is why index tie-breaking remains necessary.

## Complexity detail

Let $n$ be the number of input values and $D$ the maximum decimal digit count. Mapping all numbers takes $O(nD)$ time. Sorting $n$ pairs takes $O(n\log n)$ comparisons, each comparing constant-size integers and indices under the usual model.

Because `nums[i] < 10^9`, $D\le9$ for positive values and zero has one digit. Thus $D$ is a fixed bound, and total time simplifies to $O(n\log n)$.

The decorated list and returned list each hold $O(n)$ entries. Python sorting may also use linear temporary storage, so auxiliary/output construction space is $O(n)$, matching the manifest.

## Alternatives and edge cases

- **String conversion:** Convert each number to text, replace characters through `mapping`, then parse the result. It is easy to visualize but creates temporary strings.
- **Stable sort with key only:** Python's stable `sorted(nums, key=f)` would preserve equal-key order automatically and avoid explicit indices, though `f` might be recomputed only once by Python's key decoration.
- **Counting sort by mapped value:** The numeric key range approaches $10^9$, so a direct counting array is impractical.
- **Original value zero:** It maps to `mapping[0]`, not automatically to zero.
- **Mapped leading zeros:** They disappear in numeric comparison, so `007` and `07` both equal seven.
- **Equal mapped keys:** Original indices preserve the required relative order.
- **Duplicate original numbers:** Each occurrence has its own index and remains a separate output element.
- **Identity mapping:** Keys equal originals, producing ordinary non-decreasing numeric order.
- **Mapping is not applied to output:** The final lookup returns original values.
- **Maximum digit length:** Values below $10^9$ have at most nine decimal digits.
- **Place-value update:** `k *= 10` is necessary to reconstruct digits in their original positions while scanning backward.
- **Input preservation:** `nums` and `mapping` are read only; `x` inside `f` is a local integer.
- **Tuple ordering:** The second component matters only when mapped keys tie.
