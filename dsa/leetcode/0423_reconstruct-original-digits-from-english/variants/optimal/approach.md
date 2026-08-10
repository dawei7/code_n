## General

**Letter order is lost, but letter counts are preserved**

The input was formed by spelling some multiset of digits in English and shuffling all letters. Shuffling destroys word boundaries and order, so searching for contiguous words cannot work. It does preserve how many times each letter occurs. `Counter(s)` captures exactly this surviving information.

The goal is then to solve a small system of letter-count equations. A naive plan that repeatedly removes `"zero"`, then `"one"`, and so on is order-dependent because many digit names share letters. For example, `o` occurs in `zero`, `one`, `two`, and `four`. Consuming it prematurely could assign letters to the wrong digit.

The optimal method chooses marker letters in an elimination order. It first counts digit names that contain a globally unique letter. Once those digits are known, subtracting their contribution makes other marker letters unique among the unresolved names.

**First recover the five digits with unique marker letters**

Across the English names `zero` through `nine`:

- `z` appears only in `zero`, so `cnt[0] = counter['z']`;
- `w` appears only in `two`, so `cnt[2] = counter['w']`;
- `u` appears only in `four`, so `cnt[4] = counter['u']`;
- `x` appears only in `six`, so `cnt[6] = counter['x']`; and
- `g` appears only in `eight`, so `cnt[8] = counter['g']`.

Each marker occurs exactly once in its digit name. Therefore its frequency equals the number of copies of that digit directly; no division is needed.

For instance, if `z` occurs three times, the valid-input guarantee means exactly three copies of `zero` were present. No other digit could have supplied those `z` characters.

**Use the known even digits to isolate three more names**

The letter `h` appears in `three` and `eight`. Since the number of eights is already known, every remaining `h` must come from `three`:

`cnt[3] = counter['h'] - cnt[8]`.

Similarly, `f` appears in `four` and `five`. Removing the known fours isolates fives:

`cnt[5] = counter['f'] - cnt[4]`.

The letter `s` appears in `six` and `seven`. Removing the known sixes isolates sevens:

`cnt[7] = counter['s'] - cnt[6]`.

Again, each relevant name contains its marker once. The order is crucial: these formulas are valid only because counts for `8`, `4`, and `6` were established first.

**Finish with one and nine**

After zero, two, and four are known, the letter `o` isolates `one`. It occurs once in each of `zero`, `one`, `two`, and `four`, and nowhere else. Therefore

`cnt[1] = counter['o'] - cnt[0] - cnt[2] - cnt[4]`.

Finally, `i` occurs once in `five`, `six`, `eight`, and `nine`. The first three of those counts are already known, so

`cnt[9] = counter['i'] - cnt[5] - cnt[6] - cnt[8]`.

At this point every digit from zero through nine has a determined multiplicity. The input guarantee that `s` is a valid shuffled collection ensures all subtractions are nonnegative and that no unexplained letters remain.

**A worked reconstruction**

For `s = "owoztneoer"`, the counter contains one `z` and one `w`, so the algorithm immediately finds one zero and one two. It contains no `u`, `x`, or `g`, so digits 4, 6, and 8 have count zero. There are no residual markers for 3, 5, or 7.

The three `o` occurrences are explained by one zero, one two, and one remaining one:

`cnt[1] = 3 - 1 - 1 - 0 = 1`.

No `i` occurs, so there is no nine. The reconstructed multiset is one each of 0, 1, and 2.

**Produce the required ascending order**

The return expression iterates `i` from zero through nine. `cnt[i] * str(i)` repeats that digit character by its recovered multiplicity. Joining these ten pieces naturally sorts the output in ascending numeric order while preserving duplicates.

This construction does not attempt to recover the original order of digit words, which is unknowable after shuffling and not requested.

**Why the reconstruction is unique and correct**

Each assignment uses either a letter unique among all digit names or a letter whose other contributing names have already been counted. Consequently, at each step the formula is forced by the observed letter totals. Any valid underlying multiset must have exactly the computed count for that digit.

Following the dependency order determines all ten counts. The produced digits therefore account for the same letter multiset as `s`. Since every count was forced, no different digit multiset could produce the valid input, and the returned ascending representation is correct.

## Complexity detail

Let $n = \lvert s \rvert$. Building `Counter(s)` takes $O(n)$ time. The ten count formulas perform constant work. Constructing the output writes one character per reconstructed digit, at most $O(n)$ characters because every digit name contains at least three letters. Total time is $O(n)$.

The counter can contain only the fixed lowercase alphabet, and `cnt` always has ten integers, so auxiliary working space is $O(1)$. The returned string requires $O(d)$ output space for $d$ reconstructed digits; output space is normally excluded from the auxiliary-space bound.

## Alternatives and edge cases

- **Repeatedly search for whole digit names:** Shuffling removes contiguity, and greedy word removal can misassign shared letters. It also performs avoidable repeated scans.
- **General backtracking over digit counts:** Trying combinations could eventually match letter frequencies, but the unique-marker dependency makes exponential search unnecessary.
- **Solve a full linear system:** Ten digit variables and letter equations can be handled algebraically, but the elimination order used here is that system reduced to simple integer formulas.
- **Use `n` to find one:** The name `nine` contains two `n` characters while `one` and `seven` contain one, making the equation easier to mishandle. The exact solution uses `o` after zero, two, and four are known.
- **Repeated digits:** Marker frequencies scale linearly, and string multiplication preserves every multiplicity.
- **Only one digit:** Its markers and dependent equations recover one count, and the output is the corresponding one-character digit string.
- **No occurrence of a digit:** Its formula evaluates to zero and contributes an empty piece to the join.
- **Invalid shuffled letters:** Subtractions could become negative for arbitrary input. The contract guarantees validity, so defensive rejection logic is unnecessary.
- **Ascending order:** Iterating indices `0..9` is essential; iterating a counter's arbitrary discovery order would not satisfy the output contract.
