## General

**Describe one painting by an ordered color pair and split**

Choose distinct colors `i` and `j`. If the first segment has length `x`, the second has length `n-x`.

Both must be nonempty, so $1\le x\le n-1$. Capacity constraints require

$$
x\le limit[i]
\quad\text{and}\quad
n-x\le limit[j].
$$

Color order matters because exchanging the two colors changes which sheets receive each color.

Once colors and `x` are fixed, the painting is forced: the first `x` sheets use the first color and all remaining sheets use the second. Counting triples $(i,j,x)$ therefore counts paintings exactly.

**Cap capacities at the largest usable segment**

No segment can exceed `n-1` because the other color must receive at least one sheet.

The source replaces each limit with

`min(value,n-1)`

and sorts these effective capacities. This changes no valid painting but keeps later formulas within the relevant range.

Let `threshold=n-1` and effective capacities be $a$ and $b$.

**Derive the number of splits for one ordered pair**

The second capacity condition rearranges to

$$
x\ge n-b.
$$

Together with `x<=a`, valid integer split lengths range from `n-b` through `a`. Their count is

$$
\max(0,a-(n-b)+1)
=\max(0,a+b-(n-1)).
$$

Thus an ordered pair contributes `max(0,a+b-threshold)` ways.

The task becomes summing this expression over all ordered pairs of distinct color indices.

**Find contributing partners with binary search**

For fixed capacity `value=a`, a partner contributes positively when

$$
b>threshold-a.
$$

`bisect_right(capacities,threshold-value)` returns the first index `first` whose value is strictly greater than that boundary.

Every capacity from `first` onward contributes. Their count is

`partner_count = color_count-first`.

**Sum all partner contributions at once**

For each qualifying partner $b$, contribution is

$$
a+b-threshold.
$$

Summing over the suffix gives

$$
partnerCount\cdot(a-threshold)+\sum b.
$$

The prefix array stores cumulative capacities, so suffix sum is

`prefix[color_count]-prefix[first]`.

This produces the source update

`partner_count*(value-threshold)+prefix[color_count]-prefix[first]`.

It counts partners by list occurrence, not by distinct capacity value. Different colors with equal limits remain separate valid choices.

Sorting preserves multiplicity. Since only capacities affect the formula, original color IDs need not be carried after each occurrence remains represented.

**Remove the forbidden self-pair**

The suffix calculation includes the current color itself whenever

$$
2a>threshold.
$$

Its artificial contribution would be `2a-threshold`. Since the two colors must be distinct, the source subtracts

`max(0,2*value-threshold)`.

If self would contribute zero, it was not included by the strict binary-search boundary and subtraction is zero.

After self-removal, the iteration for first color `i` counts every valid second color `j!=i`. Iterating all first colors intentionally counts reverse color order separately.

With duplicate capacities, each iteration subtracts only its own artificial self-pair and retains the other equal-capacity colors as legitimate partners.

**Trace the first example**

For `n=4`, threshold is three and capacities from `[3,1,2]` sort to `[1,2,3]`.

For first capacity three, partners one, two, and three initially contribute one, two, and three. The self contribution three is subtracted, leaving ordered choices with the other two colors: three ways total.

Repeating for capacities one and two counts their directions separately, producing the six paintings in the example.

**Why the total is exact**

Every valid painting determines a unique first color, second color, and split length. The ordered-pair formula counts that split once.

Every counted unit corresponds to an integer `x` satisfying both effective capacities and nonempty-segment bounds. Self-pair subtraction enforces distinct colors.

Therefore the sum includes all valid paintings and no invalid or duplicate painting.

## Complexity detail

Sorting $M$ capacities takes $O(M\log M)$ time. Prefix construction is $O(M)$. Each capacity performs one $O(\log M)$ binary search and constant arithmetic, so the loop costs $O(M\log M)$.

Total time is $O(M\log M)$.

The sorted capacity list and prefix array use $O(M)$ auxiliary space. The answer is reduced modulo $10^9+7$ only at return; Python integers safely hold the intermediate sum.

## Alternatives and edge cases

- **Enumerate all color pairs and splits:** This can cost $O(M^2N)$, impossible for the constraints.
- **Enumerate ordered pairs only:** Using the closed formula gives $O(M^2)$, still too slow.
- **Treat equal capacities as one color:** Colors are distinct by index even when limits tie.
- **Count unordered pairs:** Segment order matters, so $(i,j)$ and $(j,i)$ are separate.
- **Allow a zero-length segment:** Both colors must be used, which is why capacities cap at `n-1`.
- **Forget self subtraction:** This counts illegal use of one color for both segments.
- **Use `bisect_left` at the boundary:** Contribution must be strictly positive; equality gives zero ways.
- **Limit above `n-1`:** Capping it loses no feasible segment.
- **Exactly two colors:** Both ordered directions are considered.
- **No compatible pair:** Every suffix count is empty or self-cancelled, yielding zero.
- **Modulo:** Only the final residue is returned.
- **Large `n`:** The algorithm never iterates over split positions.
- **Duplicate limits:** Each occurrence remains a distinct color.
- **Forced coloring:** One valid ordered pair and split corresponds to one painting.
