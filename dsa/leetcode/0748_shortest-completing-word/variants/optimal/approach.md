## General
**Translate the plate into a multiset requirement**

Digits and spaces do not constrain a completing word, and letter case is irrelevant. Scan the lowercased plate and increment one of 26 counters for every ASCII letter. Repeated letters increment the same counter and therefore retain their multiplicity.

**Test each candidate without losing input order**

Scan `words` from left to right. A candidate completes the plate exactly when each of its 26 counts is at least the corresponding required count. Replace the current answer only when a valid candidate is strictly shorter. Keeping the current word on equal length automatically preserves the earliest tie.

Every candidate is counted once. The counter comparison checks precisely the multiset-containment definition, so every accepted word is valid; scanning the entire list ensures that the final stored word has minimum length.

## Complexity detail
Let `C` be the number of characters in the license plate and all candidate words. Building and checking fixed 26-entry arrays takes $O(C)$ time. The required and candidate arrays each have 26 entries, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Hash-map or `Counter` comparison:** This expresses multiset containment directly and has the same asymptotic bounds, but fixed arrays are smaller and make the bounded alphabet explicit.
- **Sort candidates by length:** Checking words from shortest to longest can stop at the first match, but sorting adds $O(w \log w)$ work and must retain original order for ties.
- **Recheck every candidate against every other candidate:** This can identify a globally shortest valid word directly but repeats validation and can take quadratic time.
- **Repeated plate letters:** A word must supply every occurrence, not merely contain each distinct letter once.
- **Uppercase plate letters:** Normalize them before indexing; candidate matching is case-insensitive.
- **Digits and spaces:** Ignore them completely when building the requirement.
- **Equal-length answers:** Return the first completing word from the original list.
