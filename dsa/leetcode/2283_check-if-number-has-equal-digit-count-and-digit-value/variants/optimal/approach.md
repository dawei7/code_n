## General

**Count the fixed decimal alphabet once**

Create ten counters and scan `num`, incrementing the counter selected by each
character. This records the complete frequency of every possible digit.

Then visit each index $i$ in the string. Convert `num[i]` to its numeric value
and compare it with the stored frequency for digit $i$. If any comparison
differs, the required property is false; if every comparison agrees, it is
true.

The frequency scan counts every occurrence exactly once. The second scan
checks precisely every condition named by the contract, so accepting all of
those equalities is both necessary and sufficient.

## Complexity detail

Let $n=\lvert\texttt{num}\rvert$. Counting and verification each take $O(n)$
time. The frequency array always has ten entries, so auxiliary space is
$O(1)$. Inspecting all characters is necessary in the worst case because
changing an unread character can alter a required digit frequency.

## Alternatives and edge cases

- **Repeated string counts:** Calling a full-string count for every index is simple but takes $O(n^2)$ time in the generalized input model.
- **Hash map:** A map also works, but a ten-entry array directly represents the fixed decimal alphabet.
- **One-character string:** Neither `"0"` nor `"1"` satisfies its indexed frequency requirement.
- **Leading zeros:** The input is a string, so every leading zero remains a counted character.
- **Digits beyond the last index:** They are counted normally even though the contract has no separate requirement row for that digit.
- **Maximum length ten:** Index 9 is valid and corresponds to digit `9`.
- **Early mismatch:** Verification may return immediately after counts are complete, but the initial frequency scan must still read the whole string.
