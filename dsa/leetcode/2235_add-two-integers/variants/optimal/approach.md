## General

**Apply the requested operation directly**

The return value is defined as the arithmetic sum of the two inputs. Evaluate
`num1 + num2` once and return that result. Integer addition already handles
positive values, negative values, zero, and cancellation without any separate
case analysis.

The returned value is correct by the definition of addition: it is exactly the
quantity the contract requests, with neither input changed and no intermediate
choice that could alter the outcome.

## Complexity detail

The algorithm performs one integer addition and stores no data structure whose
size depends on the inputs, so it uses $O(1)$ time and $O(1)$ auxiliary space.

The bounded-domain certificate records that each input has only 201 legal
values. There is no honest asymptotic workload axis under this contract, so
exhaustive comparison across all 40,401 legal input pairs replaces a runtime
scaling verdict.

## Alternatives and edge cases

- **Manual sign branching:** Separating positive and negative cases merely reimplements behavior already supplied by integer addition and creates more opportunities for mistakes.
- **Bitwise addition:** Carry propagation with bit operations is useful only when the addition operator is forbidden; this problem imposes no such restriction.
- **Opposite values:** Inputs such as `-7` and `7` cancel to zero.
- **Two negative values:** Their sum remains negative, with the magnitudes added.
- **Zero:** Adding zero leaves the other input unchanged.
- **Contract boundaries:** `-100 + -100` and `100 + 100` produce `-200` and `200`, both valid return values.
