## General

**The suffix OR identifies all required bits.** For a fixed start $i$, the largest attainable OR is the OR of the entire suffix. A shorter prefix of that suffix reaches the same value exactly when it has encountered at least one occurrence of every bit that appears anywhere from $i$ onward.

**Track the closest source of each bit.** Sweep from right to left. For each of the 30 possible bit positions, store the nearest index at or after the current start where that bit is set. When processing `nums[i]`, replace the stored index for every bit it contains with $i$. These positions now describe the earliest available occurrence of every bit in the suffix.

**The furthest required occurrence fixes the answer.** Any valid subarray must extend through every stored bit occurrence, so its endpoint is at least their maximum. Conversely, extending exactly to that maximum includes a source for every suffix bit and therefore reaches the maximum OR. Thus `furthest - i + 1` is both sufficient and minimal. If the suffix OR is zero, no bit position is stored and `furthest` remains $i$, correctly giving length 1.

## Complexity detail

The sweep checks 30 fixed bit positions per element, so it takes $O(30n)=O(n)$ time. The nearest-position table uses $O(30)=O(1)$ auxiliary space, while the returned array occupies $O(n)$ space.

## Alternatives and edge cases

- **Expand every start:** Computing suffix targets and extending each subarray until it reaches its target is correct but can take $O(n^2)$ time.
- **Sliding bit counts:** A variable window can maintain bit frequencies, but determining each start's suffix target and minimum endpoint is more complicated than the backward nearest-position view.
- **All zeros:** The maximum OR is zero immediately at every index, so every answer is 1.
- **Repeated bits:** Only the nearest suffix occurrence matters; later occurrences cannot shorten the current answer.
- **Bit introduced at the end:** Every earlier start that needs that bit must extend through the final element.
- **Already complete value:** If `nums[i]` contains every bit available later, the furthest required position is $i$ and the answer is 1.
