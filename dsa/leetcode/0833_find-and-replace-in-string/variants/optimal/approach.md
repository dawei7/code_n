## General
**Validate against one immutable coordinate system**

Every match must be checked in the original `s`. First inspect each parallel operation with `s.startswith(source, index)`. Record only successful operations in a map keyed by their original starting index. Nothing has been edited yet, so a longer or shorter target cannot disturb any later test. The non-overlap guarantee means that two recorded replacements never compete for the same consumed character.

**Reconstruct without shifting indices**

Walk a cursor from left to right over the original string. If no successful operation starts at the cursor, append that one original character and advance by one. If a recorded operation starts there, append its target and advance by the length of its source. Thus the cursor always denotes an original-string index, even though the output may grow or shrink.

Each original position is handled exactly once by this reconstruction. A recorded source has already been confirmed at its start, and advancing over its full length removes precisely the occurrence that must be replaced. Characters outside successful source intervals are copied unchanged and in order, so the joined pieces are exactly the simultaneous-replacement result.

## Complexity detail
Checking all sources costs the sum of their lengths in the worst case. The reconstruction scans at most $\lvert s \rvert$ original characters, and joining the pieces writes the final output, whose length is bounded by $C$. Therefore total time is $O(C)$. The successful-operation map, output pieces, and returned string together use $O(C)$ space.

## Alternatives and edge cases
- **Sort operations and splice from right to left:** Descending indices preserve the remaining original coordinates, but repeatedly forming immutable strings can copy almost the whole current string for each of the $k$ operations, leading to $O(kC)$ time.
- **Sort and stream with a source cursor:** A sorted valid-operation list can also reconstruct the answer correctly, but sorting costs $O(k \log k)$ instead of using direct indexed lookup.
- **Failed source match:** An operation whose source differs at any character makes no change, even if its target text would help another operation match.
- **Simultaneous semantics:** Matches are determined from the original `s`, never from text inserted by an earlier replacement.
- **Variable replacement lengths:** A target may be shorter or longer than its source; only the cursor over the original string advances by the source length.
- **Boundary replacements:** A successful source may begin at index `0` or end at the final character, leaving an empty unchanged prefix or suffix.
