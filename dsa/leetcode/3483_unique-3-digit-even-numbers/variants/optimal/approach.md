## General

**Choose positions for the units, tens, and hundreds digits.** The protected source enumerates three indices, not merely three digit values. This distinction enforces the rule that each copy in `digits` can be used only once per number while still allowing equal values from different copies.

The outer loop chooses index `i` and value `a` for the units place. A decimal number is even exactly when its units digit is even. The bit test `a & 1` is one for an odd digit, so those candidates are skipped. Values $0,2,4,6,8$ continue.

The middle loop chooses index `j` and value `b` for the tens place. `i == j` is rejected because the same physical array element cannot fill two positions.

The inner loop chooses index `k` and value `c` for the hundreds place. It rejects `c == 0` because a three-digit number cannot have a leading zero. It also rejects `k in (i, j)` so the hundreds copy differs from both already selected copies.

Every surviving ordered triple produces

`c * 100 + b * 10 + a`.

The order of the loops is units, tens, then hundreds, but the arithmetic places each chosen digit in the correct decimal position.

**Use indices to handle duplicate copies correctly.** With `digits = [0,2,2]`, the two entries containing $2$ have distinct indices. The algorithm can use one as the hundreds digit and the other as the units digit, forming $202$, or use them as hundreds and tens with zero in the units place, forming $220$. It still cannot use one index twice.

With `digits = [6,6,6]`, six different ordered index triples are possible, but all produce the same value $666$. The answer asks for distinct numbers, not distinct constructions.

**Deduplicate constructed values with a set.** `s.add(...)` stores each integer only once. Different index selections that use equal-valued copies or permute identical digits collapse to one set member. Returning `len(s)` therefore counts distinct valid numbers exactly.

The set is needed for this source because index enumeration intentionally distinguishes copies. If it incremented a counter for every valid index triple, repeated digits would overcount the same decimal number.

For `digits = [1,2,3,4]`, all values are distinct, so each valid digit ordering corresponds to one number. The outer loop permits units $2$ or $4$, the inner loop forbids leading zero automatically because none exists, and the set ends with the twelve listed results.

For `digits = [1,3,5]`, every outer-loop value is odd. No inner loops contribute a number and the empty set yields zero.

**Why every inserted number is legal.** The units test proves it is even. The hundreds test proves it has three digits. The three distinct indices prove no digit copy is reused. The decimal formula uses values present at those indices, so the number can be formed from the input. Thus the set contains no invalid result.

**Why every legal number is inserted.** Take any constructible three-digit even number and identify the three distinct input copies used for its units, tens, and hundreds digits. The outer, middle, and inner loops eventually choose exactly those indices in that positional order. The units value passes the even test, the hundreds value is nonzero, and the indices pass all distinctness checks, so the number is added. Deduplication cannot remove its presence; it only merges identical values. Therefore, the final set is exactly the set of requested numbers.

**The protected implementation differs from the manifest summary.** The manifest describes counting the ten digit values and enumerating distinct digit choices while temporarily consuming counts. That can run in $O(n)$ input-counting time plus a constant $10^3$ value enumeration. The protected source instead enumerates all ordered triples of input indices. Both are correct under $n\le10$, but their source-level complexity descriptions differ.

## Complexity detail

The outer, middle, and inner loops each range over $n$ entries in the worst case. Filters can skip work on particular inputs, but worst-case time is $O(n^3)$.

The result set can contain at most $5\cdot10\cdot9=450$ three-digit even numbers: five units choices, nine nonzero hundreds choices, and ten tens choices, with impossible copy combinations only reducing this number. Therefore, under the fixed decimal-digit universe, the set uses $O(1)$ bounded space with respect to $n$. A more general expression is $O(\min(n^3,450))$ stored results.

Because the problem itself limits $n$ to ten, the maximum number of loop iterations is only $1000$, so the cubic source is entirely practical. Nevertheless, $O(n^3)$ is the faithful input-size bound and does not match the manifest's $O(n)$ count-array technique.

## Alternatives and edge cases

- **Digit-frequency enumeration:** Count copies of digits zero through nine, try value triples, and decrement counts temporarily. This matches the manifest and has linear input processing plus constant-domain work.
- **Count valid index triples directly:** This overcounts when duplicate copies produce the same decimal number; a set or value-based enumeration is required.
- **Generate all numbers from 100 through 999:** Checking digit availability is correct and bounded by 900 candidates, but differs from the protected construction.
- **Leading zero:** Zero is legal in the tens or units place but rejected only when chosen as `c` for hundreds.
- **Even units zero:** Numbers ending in zero are correctly considered even.
- **One copy used twice:** Equal indices are forbidden even when the desired digit values match.
- **Two equal copies:** Different indices allow both copies to appear in one number.
- **All copies identical and even:** Many index triples collapse to one distinct number.
- **All units candidates odd:** No even number can be formed and the set stays empty.
- **Insufficient nonzero digits:** If every possible hundreds copy is zero, no three-digit number is added.
- **Distinctness meaning:** The output counts unique numeric values, not the number of ways to select copies.
- **Source-complexity fidelity:** The small constraint makes cubic enumeration fast, but it should not be documented as the unimplemented linear count method.
