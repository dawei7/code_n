## General
**Ignore the shared prefix**

Advance to the first index where the sensors differ. The failure cannot be identified before this point because both arrays record the same values there. If no mismatch exists, either sensor could explain the data, so return `-1`.

**Test both possible one-position shifts**

If sensor 1 is faulty, each `sensor1[i]` from the first mismatch through the penultimate position must equal `sensor2[i + 1]`. Test this alignment across the suffix. Symmetrically, sensor 2 is a valid explanation when `sensor2[i] == sensor1[i + 1]` throughout that range. The final value of the purported faulty sensor is deliberately ignored because it is arbitrary.

**Resolve only a unique explanation**

Return a sensor number only when its alignment succeeds and the other alignment fails. If both succeed, the repeated values make either sensor consistent with the fault. If the first mismatch is only at the last position, the tested suffix is empty and both hypotheses likewise remain possible.

## Complexity detail
The shared-prefix scan and the two simultaneous suffix checks each inspect at most $n$ positions, so time is $O(n)$. Boolean hypothesis flags and indices use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Try every failure position:** Reconstructing and comparing both shifted arrays for every candidate position is correct but can take $O(n^2)$ time.
- **Slice comparison:** Comparing `sensor1[i:-1]` with `sensor2[i+1:]` is concise and linear, but allocates $O(n)$ temporary space.
- **Identical arrays:** Return `-1`; the arbitrary replacement can preserve all observed values.
- **Mismatch only at the last index:** No shifted pair remains to test, so the result is ambiguous.
- **Repeated readings:** They can allow both directional alignments and require `-1`.
- **Failure at the first position:** The shared prefix is empty, but the same suffix checks apply.
- **Arbitrary last reading:** Never use the purported faulty sensor's final entry as alignment evidence.
