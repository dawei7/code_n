## General

**Only remainders modulo sixty matter**

Write a duration as `60q + r`, where `r` is between zero and fifty-nine. Complete groups of sixty do not affect whether a sum is divisible by sixty.

For two durations with remainders `x` and `y`:

`(x + y) % 60 == 0`.

The needed complement of `x` is:

`y = (60 - x) % 60`.

The final modulo handles `x = 0` correctly: its complement is zero rather than sixty, since valid stored remainders stop at fifty-nine.

**Count complementary earlier songs online**

`cnt[r]` stores how many already-processed songs have remainder `r`. When the current song arrives:

1. reduce it with `x %= 60`;
2. calculate complementary remainder `y`;
3. add `cnt[y]` to the answer;
4. increment `cnt[x]`.

Every earlier song with remainder `y` forms a valid pair with the current song, so all can be counted at once.

**Why lookup happens before increment**

The required pairs satisfy `i < j`. During a left-to-right scan, the current song acts as index `j` and the counter contains only possible indices `i`.

Incrementing after the lookup prevents pairing a song with itself. It also means each unordered index pair is counted exactly once—when its later endpoint is processed.

No division by two or duplicate correction is required.

**Special remainder pairs**

Most remainders pair with a different remainder: one with fifty-nine, twenty with forty, and so on.

Two remainders pair with themselves:

- zero pairs with zero;
- thirty pairs with thirty.

The same formula handles both:

`(60 - 0) % 60 = 0` and `(60 - 30) % 60 = 30`.

As repeated songs in these groups arrive, each adds the number of earlier songs in the same group. For three durations divisible by sixty, contributions are zero, one, and two, totaling three pairs.

**Trace `[30, 20, 150, 100, 40]`**

- Thirty has remainder thirty. No earlier thirty exists, then count thirty once.
- Twenty needs remainder forty. None exists, then count twenty once.
- One hundred fifty has remainder thirty. One earlier thirty exists, so add one for pair `(30, 150)`; then count another thirty.
- One hundred has remainder forty. One earlier twenty exists, so add one for `(20, 100)`.
- Forty needs remainder twenty. One earlier twenty exists, so add one for `(20, 40)`.

The final answer is three.

**Why full durations can be discarded**

For any integers `a` and `b`:

`(a + b) % 60 = ((a % 60) + (b % 60)) % 60`.

Thus two songs with the same remainder have identical compatibility with every future song. Their identities still matter as distinct indices, which is why the counter stores frequency rather than only presence.

**The scan invariant**

Before processing position `j`, `cnt[r]` equals the number of indices before `j` whose durations have remainder `r`, and `ans` equals the number of valid pairs entirely within that processed prefix.

The current song forms a valid pair with exactly `cnt[y]` earlier positions. Adding that count includes every new pair ending at `j`. Incrementing `cnt[x]` then extends the frequency invariant to include this song.

By induction, after the final song, `ans` contains every valid `i < j` pair exactly once.

**Why a Counter is constant-sized here**

Although `Counter` is a hash map, keys can only be the sixty remainders zero through fifty-nine. Its size is therefore bounded independently of input length.

A fixed list of sixty integers would give the same asymptotic behavior; the counter makes absent remainders naturally read as zero.

**Why one lookup can add several pairs**

If `cnt[y] = m`, there are `m` different earlier indices with the needed remainder. Pairing the current index with each produces a different legal index pair even when those songs have equal durations. Adding the frequency in one step preserves all of that multiplicity without enumerating the indices individually.

The formula `(60 - x) % 60` also removes the need for a separate remainder-zero branch. Applying the outer modulo converts the mathematical complement sixty back into the stored remainder class zero.

## Complexity detail

Let `N` be the number of songs.

The method performs one constant-work iteration per duration, so time complexity is `O(N)` under expected constant-time Counter operations.

At most sixty remainder counts are stored, so auxiliary space is `O(60) = O(1)`. The numeric answer can be as large as `N(N - 1)/2`, but Python integers grow as needed.

## Alternatives and edge cases

- **Nested pair loops:** Directly test every `i < j` pair in `O(N^2)` time.
- **Frequency array after a separate counting pass:** Count all sixty remainders, then combine complementary groups using products and combinations. It is also linear but requires careful handling of remainder zero and thirty.
- **Set of remainders:** Presence alone loses multiplicity and cannot count index pairs.
- **Remainder zero:** Its complement formula maps back to zero, not sixty.
- **Remainder thirty:** Two thirty-remainder songs sum to sixty modulo sixty.
- **Repeated equal durations:** Different indices form distinct pairs and are preserved by frequencies.
- **Only one song:** No earlier complement exists, so the answer remains zero.
- **All songs divisible by sixty:** The result is `N(N - 1)/2`, accumulated online as `0 + 1 + ... + N - 1`.
- **Durations above sixty:** Modulo reduction retains all divisibility information.
- **Input preservation:** The loop rebinds local `x` to its remainder but never changes `time`.
