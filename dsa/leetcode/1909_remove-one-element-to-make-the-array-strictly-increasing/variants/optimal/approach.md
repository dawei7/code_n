## General

**Find the first place strict increase fails.** Variable `i` starts at zero and advances while `nums[i] < nums[i + 1]`. When the loop stops before the end, pair `(i, i + 1)` is the first violation: `nums[i] >= nums[i + 1]`. Everything before `i` is already strictly increasing.

**Only two removals can repair that first violation.** If neither endpoint of a bad adjacent pair is removed, both values remain adjacent in their original order in the resulting array and still violate strict increase. Therefore every successful one-element removal must remove index `i` or index `i + 1`. This observation reduces up to $n$ candidates to exactly two.

Removing `i` means keeping the smaller/right value and reconnecting `nums[i - 1]`, if it exists, to `nums[i + 1]`. Removing `i + 1` keeps the left value and reconnects it to `nums[i + 2]`, if it exists. Rather than encode these boundary comparisons manually, the source validates each complete candidate with helper `check`.

**Validate a candidate in one pass.** `check(k)` sets `pre = -inf`. It scans all values, skips index `k`, and requires every kept value `x` to satisfy `pre < x`. If `pre >= x`, the resulting sequence is not strictly increasing and false is returned. Otherwise `pre` becomes `x` and scanning continues.

Negative infinity is safely below every permitted input value and removes the need for a special first-kept-element branch. The helper does not allocate a shortened array; it logically omits one index.

**Test both necessary candidates.** The final expression `check(i) or check(i + 1)` returns true if either endpoint removal makes the whole array strictly increasing. Python may short-circuit and skip the second scan when the first succeeds. If both fail, no other removal can repair the first violation, so false is certain.

**Already increasing input fits the same logic.** If every adjacent pair increases, the discovery loop advances `i` to `len(nums) - 1`. `check(i)` removes the last element, leaving an increasing prefix, and returns true. This matches the statement's explicit rule that an already increasing array should return true, even though the wording also mentions removing exactly one element.

**Trace `[1,2,10,5,7]`.** The first violation is ten followed by five, at indices two and three. `check(2)` skips ten and sees `1 < 2 < 5 < 7`, so true is returned. Testing unrelated positions is unnecessary because leaving both ten and five would retain their violation.

For `[2,3,1,2]`, the first violation is three followed by one. Removing three leaves `[2,1,2]`, invalid; removing one leaves `[2,3,2]`, also invalid. Any other removal keeps `3,1` together, so false follows.

**Why a full validation is still needed.** Repairing the local first violation can expose a new violation across the deletion boundary or leave a later preexisting violation. For example, deciding solely from the first three values is insufficient. `check` verifies every kept adjacency and safely handles both issues.

**Why the two-candidate proof is complete.** Any valid result must eliminate the first bad adjacent relation, forcing removal of one endpoint. The algorithm evaluates both possible endpoint removals exactly and accepts only after full strict-order verification. Therefore it finds a valid removal whenever one exists and never accepts an invalid result.

**Inputs remain unchanged.** The source only reads `nums` and skips a position logically. No slicing, deletion, or restoration is performed.

## Complexity detail

Let $n$ be the array length. Finding the first violation takes at most $O(n)$ time. Each `check` scans at most $n$ elements, and at most two checks run. Total time is $O(n)$.

The helper retains only a previous value and loop variables. No shortened array is built, so auxiliary space is $O(1)$. This matches the manifest.

The constraints guarantee at least two elements. After one deletion, at least one remains; a one-element array is vacuously strictly increasing, which the helper recognizes.

## Alternatives and edge cases

- **Try deleting every index:** Validating all $n$ shortened candidates costs $O(n^2)$. The first bad pair proves only two candidates matter.
- **One-pass modification counter:** A greedy scan can decide which endpoint to ignore based on neighboring values. It also achieves $O(n)$ time but is easier to get wrong at boundaries than two explicit validations.
- **Physically delete and restore:** This mutates the input and shifts indices. Logical skipping is simpler and constant-space.
- **Violation from equal values:** Strict increase rejects equality because discovery uses `<` and validation rejects `pre >= x`.
- **Violation at the start:** Candidate indices zero and one are both valid; negative infinity handles whichever first kept element remains.
- **Violation at the end:** Removing either endpoint is tested, including removing the final value.
- **Already strictly increasing:** Discovery reaches the last index, and removing that last element produces a valid sequence, so true is returned.
- **Two-element array:** Removing either one leaves a single-element increasing array; the method returns true.
- **Multiple separated violations:** Removing one endpoint of the first cannot generally fix a later violation, and full `check` correctly rejects both candidates.
