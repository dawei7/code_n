## General

**Separate direct bits from generated carries**

Maintain a running prefix sum and OR both each array value and the updated prefix sum into the answer. OR-ing the values handles every bit that appears directly: the singleton subsequence containing that value proves the bit is achievable. Prefix sums reveal bits created when several lower-bit contributions carry into a higher position.

To see why this captures every possible generated bit, fix bit position $b$ and suppose no array value already has that bit set. Remove multiples of $2^{b+1}$ from each value; they cannot affect bit $b$. The remaining relevant lower residue of each value lies between $0$ and $2^b-1$. If the total of all lower residues is below $2^b$, no subset can carry into bit $b$. If the total reaches $2^b$, examine prefix residue sums and take the first prefix whose total reaches that boundary. Its preceding total was below $2^b$, and adding one residue smaller than $2^b$ keeps the new total below $2^{b+1}$. That prefix sum therefore has bit $b$ set.

Thus every achievable bit is either present in an individual value or in some prefix sum, and each value and prefix is itself a valid subsequence sum. The accumulated OR contains exactly the requested bits.

## Complexity detail

Let $n$ be the array length. The algorithm performs one addition and a constant number of bitwise operations per element, taking $O(n)$ time. It stores only the running sum and answer, so auxiliary space is $O(1)$.

Python integers grow enough to hold the maximum total, at most $10^{14}$ under the stated constraints.

## Alternatives and edge cases

- **Enumerate all subsequences:** This is correct but considers $2^n$ choices and is infeasible at the maximum length.
- **Reachable-sum set:** Updating a set of all achievable sums avoids duplicate states but remains exponential or pseudo-polynomial in the total sum.
- **OR only the values:** This misses higher bits created by addition carries, such as bit $3$ from `[4,4]`.
- **OR only prefix sums:** This misses some direct bits; for `[1,3]`, prefix sums OR to $5$ while the singleton sum $3$ contributes bit $1$, making the answer $7$.
- **Zeros:** Adding zero changes neither the prefix sum nor any achievable bit.
- **Large carries:** The result may contain bits above every individual input's highest set bit because many values can accumulate into a larger sum.
