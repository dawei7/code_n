## General
**Processing requests in the required order**

Folder availability changes after every assignment, so scan `names` from left to right and append each actual assignment immediately. Sorting or grouping equal requests would lose the chronology that determines which suffixes are already occupied.

**Giving the hash map two roles**

Maintain `next_suffix`, keyed by every assigned string. The presence of a key means that exact folder name is occupied. Its integer value is the first suffix worth testing if that exact string is requested again.

For a newly assigned literal name, store value one. For a duplicate base, begin at its saved value instead of restarting at one.

**Assigning a fresh request**

If `name` is absent, append it unchanged and set `next_suffix[name] = 1`. This records both its occupancy and the fact that a future duplicate should first consider `name + "(1)"`.

No suffix is added merely because the name contains parentheses or digits. Only exact-string membership determines whether it is free.

**Resolving a collision with the smallest suffix**

For an occupied `name`, let `k = next_suffix[name]`. Form `candidate = f"{name}({k})"` and advance `k` while that candidate is already a key. Once a free candidate is found:

- append the candidate;
- store `next_suffix[name] = k + 1`, because all smaller suffixes for this base are now known occupied;
- store `next_suffix[candidate] = 1`, because the generated string is itself an assigned name.

Recording the generated string is essential. A later request may equal it exactly, in which case it must receive its own nested suffix.

**Why the suffix is minimal**

Before resolving a duplicate, the saved value for its base is the smallest suffix not already disproven by an earlier search. The loop tests candidates in increasing order and stops at the first absent string. Every smaller positive suffix was either skipped by the saved lower bound because it is occupied or checked during this search and found occupied. Therefore the chosen `k` is precisely the smallest valid positive integer.

**Why suffix probing is amortized linear**

For one base name, its saved pointer only moves forward; a suffix rejected for that base is never tested again by a later duplicate of the same base. Across the scan, hash membership and updates are expected constant time, and the number of pointer advances is proportional to the assignments. With the input-length bound, constructing and hashing each assigned name is bounded, giving expected $O(N)$ total work.

## Complexity detail
Each request performs expected $O(1)$ hash-map operations plus amortized constant suffix advancement. The full scan therefore takes expected $O(N)$ time. The result and map store $N$ assigned names, using $O(N)$ space. String construction contributes the total output-character cost, bounded per name under the problem constraints and generated suffix range.

## Alternatives and edge cases
- **Restart suffix search at one:** Keep only a used-name set and begin every duplicate at `k = 1`. It is correct but repeatedly revisits occupied candidates and can take $O(N^2)$ time for many identical requests.
- **Per-base counter without membership checks:** A counter alone fails when names such as `"gta(1)"` were requested before the duplicate base and already occupy a future candidate.
- **Sort equal names together:** This destroys request order and changes which literal or generated name claims a string first.
- **Parse existing parentheses:** Do not interpret `"a(1)"` as metadata for base `"a"`; it is an independent exact string unless a collision forces a new suffix.
- **Nested suffixes:** A duplicate of `"a(1)"` may correctly become `"a(1)(1)"`.
- **Preoccupied gap:** If `"x(2)"` exists but `"x(1)"` does not, the next duplicate `"x"` must use `"x(1)"`.
- **Generated-name request:** If the system generated `"doc(1)"` and that string is later requested, it is occupied and receives a nested suffix.
- **Repeated base:** Successive duplicates receive increasing free suffixes, not necessarily consecutive ones when literal requests preoccupied some candidates.
- **All names unique:** Every request passes through unchanged.
- **Maximum-length input name:** Appending a generated suffix is allowed even when the requested name already has length 20.
- **Exact spelling:** Membership is based on the full string; no case folding or normalization is performed.
