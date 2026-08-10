## General

**A legal answer is determined by two cut positions**

The input has one plus sign, so splitting on `"+"` gives a left digit string `l` and a right digit string `r`. The left parenthesis must appear somewhere before the plus, and the right parenthesis somewhere after it.

Choose index `i` as the first digit inside the parentheses on the left. Then:

- `l[:i]` remains outside the parentheses as a possible left multiplier;
- `l[i:]` is the nonempty left addend inside.

Choose index `j` as the last digit inside on the right. Then:

- `r[:j + 1]` is the nonempty right addend inside;
- `r[j + 1:]` remains outside as a possible right multiplier.

The resulting syntax is

`leftOutside(leftInside + rightInside)rightOutside`,

where adjacency means multiplication. Every legal placement corresponds to exactly one pair `(i, j)` with `0 <= i < len(l)` and `0 <= j < len(r)`.

**Evaluate empty outside pieces as multiplicative identity**

The inside value is

`c = int(l[i:]) + int(r[:j + 1])`.

If the opening parenthesis is at the very beginning, `l[:i]` is empty and there is no left multiplication. The code represents that missing factor by one:

`a = 1 if i == 0 else int(l[:i])`.

Similarly, if the closing parenthesis is at the end, the missing right factor is one:

`b = 1 if j == n - 1 else int(r[j + 1:])`.

The complete numeric value is `a * c * b`. The code writes `a * b * c`, which is equal because integer multiplication is associative and commutative.

Using one is essential. Treating an absent outside piece as zero would make every boundary placement evaluate to zero, even though no multiplication by zero exists in the expression.

**Enumerate every legal expression**

The outer loop tries all `m` opening positions and the inner loop all `n` closing positions. For each pair, it calculates the exact value `t`. If `t` is strictly below the best value `mi`, it records both the new minimum and the formatted expression:

`f"{l[:i]}({l[i:]}+{r[:j + 1]}){r[j + 1:]}"`.

The slices naturally omit empty outside pieces. For example, opening at zero begins the string with `"("`, while closing at the last right digit ends it with `")"`.

`mi` begins at positive infinity, so the first candidate always becomes the current best. At least one candidate exists because both operands are positive nonempty digit strings.

**Why exhaustive boundaries guarantee the minimum**

Any valid solution must place its opening parenthesis before the plus but before at least one left digit of the inside addition. That location is one of the enumerated `i` values. Its closing parenthesis must leave at least one right digit inside, giving one enumerated `j`.

Thus, the nested loops evaluate the value of every permitted expression. The stored value never comes from an illegal boundary, and after all candidates the minimum seen cannot exceed or miss the true optimum. It is exactly the smallest achievable value.

When multiple placements have the same minimum, the strict `t < mi` comparison retains the first one encountered. The problem accepts any minimizing expression, so no special tie rule is needed.

**Trace one placement**

For `"12+34"`, choose `i = 1` and `j = 0`. The outside factors are `a = 1` from text `"1"` and `b = 4` from text `"4"`. The inside sum is `2 + 3 = 5`, so the value is `1 * 5 * 4 = 20`. Formatting produces `"1(2+3)4"`.

For `"999+999"`, the best choice opens at zero and closes at the final digit. Both outside factors become the identity one, so the value is the original sum `999 + 999`.

**Exact parsing guarantees**

The constraints use digits `1` through `9`, so operands and all nonempty slices represent positive integers and have no leading zeros. Every computed candidate fits a signed 32-bit integer by contract, though Python integers would safely support larger values.

The returned object is always a string. `ans` begins as `None` only as an internal placeholder and is assigned on the first iteration.

## Complexity detail

Let `m` and `n` be the left and right operand lengths. The algorithm examines `m n` boundary pairs. If string slicing and integer conversion over up to `m + n` characters are counted, the detailed time bound is `O(mn(m+n))`, and each stored/formatted candidate uses `O(m+n)` temporary space.

The problem caps the entire expression length at ten. Under this fixed bound, there are only constantly many boundaries and every slice has constant maximum length, so the manifest states `O(1)` time and `O(1)` space.

Only the best expression is retained; the method does not store all candidates.

## Alternatives and edge cases

- **Greedily make the inside numbers small:** A smaller inside sum may create much larger outside multipliers, so local digit choices do not guarantee the minimum product.
- **Parse expression trees:** The grammar after adding one pair of parentheses is fully determined by two boundaries, making general expression parsing unnecessary.
- **Generate strings before evaluation:** This is possible, but separately identifying the four numeric parts makes missing-factor handling and value calculation clearer.
- **Parentheses around the entire expression:** `i = 0` and `j = n - 1` represent this case with both outside factors equal to one.
- **No left outside digits:** The opening parenthesis appears at the beginning; it does not create a zero factor.
- **No right outside digits:** The closing parenthesis appears at the end and likewise uses factor one.
- **One-digit left operand:** The only opening position is zero.
- **One-digit right operand:** The only closing position is its last digit.
- **Several minimum expressions:** The first encountered is retained, which is allowed.
- **Implicit multiplication:** Outside digits adjacent to parentheses multiply the parenthesized sum; they are not concatenated with the inside result.
- **Nonempty inside operands:** Loop ranges ensure at least one digit remains on both sides of the plus inside the parentheses.
- **Input preservation:** The original string is only sliced and never modified.
