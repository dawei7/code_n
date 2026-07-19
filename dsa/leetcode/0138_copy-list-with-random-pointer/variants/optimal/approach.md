## General
**Interleaving creates an implicit original-to-clone lookup**

Walk the original `next` chain. For each node, save its original successor, allocate its clone, and insert the clone immediately after it:

```text
original -> clone -> original_successor
```

After the pass, `original.next` is the unique clone for every original. This physical adjacency replaces an $O(n)$ hash map.

**Random targets become adjacent-clone targets**

For original node `u`, its clone is `u.next`. If `u.random` is original node `r`, then `r.next` is `r`'s clone, so assign `u.next.random = u.random.next`. A null random pointer remains null.

This pass must occur before separation, while every original-to-clone adjacency still exists.

**One pass restores originals and links clones independently**

For each interleaved pair, restore `original.next` to the next original and set `clone.next` to that next original's clone when one exists. Save the first clone as the result head. After this pass, no clone pointer targets an original and the caller's list has its exact original `next` structure.

**The app encoding requires a deep row copy rather than node weaving**

The app receives `[value, random_index]` rows rather than runtime nodes, so copying each row produces an independent representation with identical pointer indices.

**Interleaving makes every target's clone locally accessible**

After the first pass, each original node is followed by exactly one newly allocated clone. Therefore the clone of any original `random` target is simply `original.random.next`, allowing all clone pointers to be assigned without a map.

The separation pass restores every original `next` edge and links clones through the adjacent clone of each original successor. Clone values and topology match the source, while every object is new and no clone pointer refers back into the original list.

## Complexity detail
Three linear passes perform constant work per node, giving $O(n)$ time and $O(1)$ auxiliary space beyond output. The app adapter copies $O(n)$ encoded rows.

## Alternatives and edge cases
- **Hash map from original to clone:** is simpler but uses $O(n)$ auxiliary space.
- **Copy only the next chain:** loses random targets.
- **Return original nodes:** violates deep-copy identity even if serialization matches.
- Empty input returns empty. Self-random pointers work because an original's adjacent clone points randomly to itself after mapping.
- Separation must restore the original list; leaving clones interleaved mutates caller-owned topology and does not produce an independent list.
