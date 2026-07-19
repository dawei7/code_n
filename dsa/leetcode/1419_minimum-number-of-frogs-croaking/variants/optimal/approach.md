## General
**Track how many sounds occupy each stage.** Maintain counts for frogs that have emitted `c`, `cr`, `cro`, and `croa` and are waiting for the next character. A new `c` starts a sound and increases the active-frog count. Any later character must advance one frog from the immediately preceding stage; if none exists, the ordering is invalid.

When a `k` completes a sound, decrease the active count instead of placing it in another waiting stage. Record the maximum active count reached during the scan. A frog whose sound completes can immediately begin another sound later, so this peak concurrency is both necessary and sufficient.

Every accepted character advances exactly one partial `"croak"` through its next required stage. Rejecting a missing predecessor catches an out-of-order character. After the scan, every waiting-stage count and the active count must be zero; otherwise at least one sound is incomplete. For a valid recording, the peak active count is therefore the minimum frog supply.

## Complexity detail
Each of the $n$ characters performs a constant number of stage-count operations, so time is $O(n)$. The four counters and concurrency totals use $O(1)$ space.

## Alternatives and edge cases
- **Track each frog separately:** Store every active frog's next expected character and search for a match. This is correct but can take $O(nf)$ time for $f$ concurrent frogs.
- **Repeated substring removal:** Removing visible `"croak"` substrings fails because valid sounds may be interleaved.
- **Incomplete ending:** A prefix such as `"croa"` is invalid even though all seen characters were ordered.
- **Character without predecessor:** An `o` requires an available `"cr"` stage, not merely an earlier `c` somewhere.
- **Sequential sounds:** `"croakcroak"` needs one reusable frog, not two.
- **Fully overlapping sounds:** A block such as `"ccrrooaakk"` reaches concurrency two.
- **Length not divisible by five:** No collection of complete sounds can produce it.
