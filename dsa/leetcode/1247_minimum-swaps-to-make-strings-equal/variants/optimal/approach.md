## General
Positions where the strings already agree never need to participate in a minimum solution. Every remaining position has exactly one of two orientations: `s1` has `"x"` while `s2` has `"y"`, or `s1` has `"y"` while `s2` has `"x"`. Let their counts be $a$ and $b$, respectively.

**Why pairs of the same orientation cost one swap**

Consider two `x/y` mismatches. Swapping the `"x"` from one position in `s1` with the `"y"` at the other position in `s2` fixes both positions at once. Therefore every pair contributes one swap, giving $\lfloor a/2 \rfloor$ swaps for the first orientation and $\lfloor b/2 \rfloor$ for the second.

**Why the remaining parities decide feasibility**

A cross-string swap preserves the total number of each character across both strings. Equality requires mismatches to be eliminated in pairs, so an odd value of $a+b$ is impossible. After same-orientation pairs are removed, the only possible residue is one mismatch of each orientation. Those two cannot be fixed by one cross-string swap: the first swap changes them into two mismatches of the same orientation, and a second swap repairs that pair. Thus this residue costs exactly two swaps.

A single pass counts $a$ and $b$. If $a+b$ is odd, return `-1`; otherwise return $\lfloor a/2 \rfloor + \lfloor b/2 \rfloor + 2(a \bmod 2)$.

## Complexity detail
The scan examines each of the $n$ aligned character pairs once, so it takes $O(n)$ time. Only the two mismatch counters are retained, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Explicit mismatch lists:** Recording the indices of both mismatch orientations leads to the same greedy pairing, but uses $O(n)$ extra space without helping compute the answer.
- **Breadth-first search over swaps:** Exploring string configurations can find a minimum for tiny inputs, but the state space grows exponentially and is unnecessary once mismatch orientations are counted.
- **Already equal strings:** Both mismatch counts are zero, so the minimum is `0`.
- **One unmatched position:** An odd total mismatch count cannot be repaired and must return `-1`.
- **One mismatch of each orientation:** This is the parity residue that requires exactly two swaps, not one.
