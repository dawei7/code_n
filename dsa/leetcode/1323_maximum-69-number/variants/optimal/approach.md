## General

The number contains only digits `6` and `9`, and we may change at most one digit in either direction. To maximize the result, we should never change `9` to `6` because that strictly decreases the number. The only useful operation is changing one `6` to `9`.

If several sixes exist, the best one to change is the leftmost, most significant six. The exact Optimal implementation expresses this rule in one line:

`int(str(num).replace("6", "9", 1))`.

**Why significance decides the choice**

Changing a six at decimal position $p$, counted from zero at the right, increases the number by:

$$
(9-6)\cdot10^p=3\cdot10^p.
$$

A position farther left has a larger power of ten. Therefore, changing the leftmost six creates a larger increase than changing any later six, regardless of the remaining digits.

For `669`:

- changing the first six gives `969`, an increase of 300;
- changing the second gives `699`, an increase of 30.

The first option is larger.

This is a place-value argument, not merely a lexicographic trick. The earliest differing digit between two equal-length positive decimal strings determines which number is greater.

**Why changing a nine is never helpful**

Replacing a nine with a six decreases its contribution by $3\cdot10^p$. Because the operation is optional—“at most one”—we can always choose to do nothing instead.

Thus, an optimal solution either changes the leftmost six to nine or performs no change when no six exists. There is no useful case for the reverse direction even though the problem permits it.

**String conversion exposes digit order**

`str(num)` creates the ordinary decimal representation from most significant digit to least significant digit. Python's string `replace(old, new, count)` searches left to right.

The third argument `1` limits replacement to one occurrence. Therefore:

`replace("6", "9", 1)`

changes exactly the first six when one exists and leaves later sixes untouched.

If the string contains no six, `replace` returns an equal string. This naturally implements the “do nothing” option for a number consisting entirely of nines.

Finally, `int(...)` converts the modified digit string back to the required integer return type.

**Following the examples**

For `9669`, the first character is already nine. The search continues and finds the six in the second position, producing `9969`. Changing the later six would produce `9699`, which is smaller because the second digit would remain six.

For `9996`, the only six is last, so replacing it produces `9999`.

For `9999`, no replacement occurs and conversion returns the original number.

**Why the one-line result is optimal**

If no six exists, every allowed actual change would turn a nine into six and lower the number, so keeping the input is optimal.

If at least one six exists, changing a six always increases the number. Among all such changes, the leftmost position has the greatest place value and therefore gives the greatest increase. The string operation performs exactly that change and no other.

These cases cover every valid input, proving the returned number is maximum.

**Why leading zeros are irrelevant**

All digits are six or nine, so conversion never creates or removes a leading zero. The number of digits remains unchanged throughout.

## Complexity detail

Let $d$ be the number of decimal digits.

Converting `num` to a string takes $O(d)$ time and creates a length-$d$ string. `replace` scans for the first six and constructs another string, also taking $O(d)$ time in the worst case. Converting back to an integer processes the digits again in $O(d)$ time.

The total time is $O(d)$ and peak representation space is $O(d)$, matching the manifest.

Under the stated bound, $d$ is at most five by the numeric limit, though numbers made only of six and nine below or equal to $10^4$ have at most four such digits. The generalized digit-based bounds remain the clearest description.

## Alternatives and edge cases

- **Manual character scan:** Convert to a list, find the first six, replace it, and stop. It makes the greedy decision explicit but is longer.
- **Arithmetic digit scan:** Inspect digits from right to left, remember the highest position containing six, and add $3\cdot10^p$. This uses $O(1)$ auxiliary space.
- **Try every possible change:** It is correct but unnecessary; the place-value proof identifies the best position immediately.
- **All digits are nine:** No six is found, so the unchanged input is returned.
- **Only one six:** That digit is replaced regardless of its position.
- **Several sixes:** Only the first is replaced because the `count` argument is one.
- **First digit is six:** It is changed, producing the largest possible place-value increase.
- **Changing nine to six:** It always lowers the number and is dominated by making no change.
- **At most one operation:** Leaving an all-nine number unchanged is explicitly allowed.
- **No leading-zero concern:** The permitted digit changes preserve length and positivity.
- **String immutability:** `replace` returns a new string rather than modifying the original representation in place, which explains the $O(d)$ space.
