## General
**Maintain counts at two levels.** One hash map stores each value's current occurrence count. A second map stores how many distinct values currently have each frequency. When a new array element arrives, decrement the bucket for its old positive frequency, increment its value count, and increment the bucket for the new frequency. Also retain the maximum current frequency $M$.

**Recognize the only repairable frequency shapes.** Let the current prefix length be $\ell$, and let $F_r$ be the number of distinct values whose frequency is $r$. Exactly one removal succeeds only in one of three configurations:

- $M=1$, so every value is a singleton and any one may be removed.
- $M F_M=\ell-1$, so all but one occurrence belong to frequency-$M$ groups and the remaining value is a singleton to remove.
- $(M-1)(F_{M-1}+1)=\ell-1$, so exactly one value has frequency $M$ and removing one of its occurrences makes every group have frequency $M-1$.

Whenever one condition holds, record $\ell$ as the latest valid prefix.

**Why no other shape can work.** One removal changes only one value's frequency, and changes it by exactly one (or removes a singleton entirely). Therefore all untouched values must already share a frequency, while the changed value must be either a singleton or exactly one occurrence above that common frequency. The three tests enumerate those possibilities, so rejecting every other frequency distribution is sound.

## Complexity detail
Each of the $n$ elements triggers a constant expected number of hash-map updates and condition checks, giving $O(n)$ expected time. The maps contain at most $n$ value or frequency entries, so space is $O(n)$.

## Alternatives and edge cases
- **Recount every prefix:** Building frequencies from scratch for each endpoint is correct but takes $O(n^2)$ time.
- **Try every removal explicitly:** Recomputing the remaining frequency multiset for every index adds another unnecessary factor.
- **All singleton values:** Every prefix is valid because removing any element leaves all remaining frequencies equal to one.
- **One distinct value:** Every prefix is valid; remove one occurrence and the sole remaining positive frequency is still uniform.
- **One singleton among equal groups:** Remove the singleton itself rather than lowering one of the larger groups.
- **One overfull group:** Remove an occurrence from the unique group at frequency $M$.
- **Exactly one removal:** A prefix whose frequencies are already equal may still be valid only if one removal preserves equality, as covered by the stated shapes.
