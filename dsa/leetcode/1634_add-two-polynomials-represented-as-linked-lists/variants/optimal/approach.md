## General
**Merge by descending power.** Keep one pointer at the current term of each input. If one power is larger, that term must appear next in the output because neither list contains any later term with that power; append a copy and advance that pointer. If the powers match, add the coefficients, append the term only when the sum is nonzero, and advance both pointers.

**Attach the remaining suffix.** Once one list ends, every term in the other list has a distinct smaller power and cannot combine with anything else. Copy that suffix in order. A dummy head makes output construction uniform even when early terms cancel or the result is empty.

At every step, the algorithm emits or resolves the greatest unprocessed power. The strict input ordering ensures no skipped term can later match an emitted power. Equal powers are combined exactly once, zero sums are omitted, and unmatched terms retain their coefficients, so the final descending list represents precisely the polynomial sum in standard form.

## Complexity detail
Each of the $n+m$ input nodes is inspected and advanced past once, so the merge takes $O(n+m)$ time. A newly allocated result can contain at most $n+m$ nodes and therefore uses $O(n+m)$ output space; aside from that required output, the pointer workspace is $O(1)$.

## Alternatives and edge cases
- **Power-to-coefficient map:** Accumulate both lists in a dictionary, remove zeros, and sort surviving powers. This takes $O(n+m+k\log k)$ time for $k$ distinct powers and loses the benefit of already sorted inputs.
- **Repeated sorted insertion:** Insert every term into an output list by scanning for its power. This is correct but can take $O((n+m)^2)$ time.
- **Reuse input nodes:** Relinking existing nodes can reduce allocation, but it mutates caller-owned lists and requires careful handling of cancellations.
- Either or both input lists may be empty.
- Equal-power coefficients can cancel completely, including every term in both polynomials.
- Negative coefficients are ordinary terms and are omitted only when their combined value is exactly zero.
- The result must remain strictly descending by power with no zero coefficients.
