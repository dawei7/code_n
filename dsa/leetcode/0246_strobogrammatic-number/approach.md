## General

Rotating an entire written number by 180 degrees does two things at once: each digit changes according to its upside-down form, and the order of positions reverses. The digit originally at the left end moves to the right end, the second digit moves to the second-from-right position, and so on. Therefore, there is no need to construct the complete rotated string. We can compare mirrored positions directly with two pointers.

Under this problem's digit convention, the valid rotations are

```text
0 -> 0
1 -> 1
6 -> 9
8 -> 8
9 -> 6
```

Digits `2`, `3`, `4`, `5`, and `7` do not become valid decimal digits in the required form. A number is strobogrammatic exactly when every left digit rotates into the digit at its mirrored right position.

**How the array encodes rotation**

The exact solution stores

```text
d = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
```

The array index is an original digit, and the stored number is its rotated digit. Thus `d[6] == 9` and `d[9] == 6`. Invalid digits map to `-1`. Since every actual character in `num` converts to an integer from `0` through `9`, `-1` can never equal a real mirrored digit. The same comparison detects both an invalid digit and a valid digit paired with the wrong mirror.

An array is a natural fit because there are exactly ten possible decimal digits. It avoids hash lookup and keeps the mapping constant-sized.

**Two pointers compare the positions rotation swaps**

Pointer `i` starts at `0`, and pointer `j` starts at `len(num) - 1`. During an iteration, the solution converts `num[i]` and `num[j]` to integers `a` and `b`. It then asks whether `d[a] == b`.

This direction matters. `d[a]` is what the left digit becomes after rotation, and rotation moves it to the mirrored right position. If that result does not equal the existing right digit, the rotated number cannot match the original, so the function returns `False` immediately.

After a successful pair, `i` moves one step right and `j` moves one step left. The outer pair never needs examination again. The loop uses `i <= j`, ensuring that an odd-length number's center digit is checked rather than skipped.

**Why checking one direction per pair is enough**

The valid mapping is involutive: rotating twice restores the original digit. In particular, `0`, `1`, and `8` map to themselves, while `6` and `9` map to each other. If the left digit rotates to the right digit, then the right digit necessarily rotates back to the left digit. Therefore, checking `d[a] == b` already validates both destinations of that mirrored pair; a separate `d[b] == a` comparison would be redundant.

**Even-length trace**

For `num = "69"`, `i = 0` points to `6` and `j = 1` points to `9`. The mapping gives `d[6] = 9`, matching the right digit. The pointers cross, so every mirrored pair is valid and the function returns `True`.

For `num = "962"`, the first comparison uses left digit `9` and right digit `2`. Since `d[9] = 6`, not `2`, the number fails immediately. There is no need to examine the center `6`; one invalid mirrored pair is enough to prove the entire rotation differs.

For `num = "6889"`, the outer pair is `6` and `9`, which is valid. The inner pair is `8` and `8`, also valid. Rotating and reversing the full sequence reconstructs `6889`.

**Odd-length center behavior**

When the length is odd, the pointers eventually meet at the center. That digit stays in the same position after reversal, so it must rotate into itself. Only `0`, `1`, and `8` satisfy that condition.

The normal comparison handles this automatically. If the center is `8`, then `d[8] == 8`; if it is `6`, then `d[6] == 9`, which does not equal the center's existing `6`, so the number is rejected. A digit can be rotatable without being legal at the center: `6` and `9` require each other at different mirrored positions.

**Why all accepted numbers are valid**

After each successful iteration, the examined outer positions are exactly what the 180-degree rotation requires. The unexamined substring is the only portion whose validity remains unknown. Moving inward preserves that interpretation. If a comparison fails, at least one rotated position differs, so rejection is necessary. If the loop finishes, every position belongs to a validated mirrored pair, or is the validated center of an odd-length number. Rotating the whole string consequently recreates every digit at every position, which is precisely the strobogrammatic condition.

The input is kept as a string, which preserves positional digits and avoids numeric conversion of the entire value. That is appropriate for lengths up to `50`, beyond the range of many fixed-width integer types. Only individual characters are converted, which is always safe under the digits-only contract.

## Complexity detail

Let $n$ be the number of characters in `num`. Each iteration validates two positions, except that the final odd-length iteration validates one center position. The loop therefore runs $\lceil n/2\rceil$ times. Each iteration performs constant-time character access, single-digit conversion, array lookup, comparison, and pointer updates, giving $O(n)$ total time.

The mapping array always has exactly ten entries, independent of $n$. Apart from it, the solution stores two pointers and two digit values. Its auxiliary space complexity is $O(1)$. Unlike the rotated-copy alternative, it does not allocate an $O(n)$ builder or reversed string.

An early invalid pair can make the actual runtime shorter, but a valid number requires checking all mirrored pairs, so the worst-case bound remains linear.

## Alternatives and edge cases

- **Build the full rotated copy:** Traverse the string backward, map each digit, join the result, and compare it with the input. This is straightforward and $O(n)$ time, but it uses $O(n)$ additional space that the two-pointer check avoids.
- **Hash-map rotation table:** A dictionary such as `{'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}` can make the valid pairs self-documenting. It has the same asymptotic bounds; the exact solution uses a ten-entry integer array with `-1` sentinels.
- **Explicit valid-pair set:** Check whether `(num[i], num[j])` belongs to `{('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')}`. This is equivalent but represents pairs rather than the rotation function.
- **One digit:** The pointers meet immediately. `0`, `1`, and `8` return `True`; every other digit returns `False`.
- **Odd-length center `6` or `9`:** Both digits rotate validly in a pair but not into themselves, so either one in the center must be rejected.
- **Invalid digits `2`, `3`, `4`, `5`, or `7`:** Their table value is `-1`, which cannot match any right-side digit. The method rejects as soon as such a digit is examined from the left side of its mirrored pair.
- **A nominally invalid digit on the right:** It is still detected. If the left digit is valid, none of its mapped values equals that invalid right digit; if it is paired with another invalid digit, the left maps to `-1`, not the right's numeric value.
- **`6` paired with `6`:** This is invalid because rotating the left `6` produces `9`. Likewise, `9` paired with `9` is invalid.
- **Leading zeros:** The input contract excludes them except for the number `"0"`. The pair logic itself would still test a string such as `"00"` as visually strobogrammatic, but numeric-format validity is supplied by the caller's contract.
- **Long input:** Keeping the number as a string avoids overflow. The algorithm's behavior depends on digit positions, not on the numeric magnitude.
- **Empty input:** The documented minimum length is one. If given an empty string outside the contract, the loop would not run and the source would return `True`; callers requiring different semantics should validate input explicitly.
