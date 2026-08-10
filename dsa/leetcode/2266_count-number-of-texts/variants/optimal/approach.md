## General

**Different consecutive keys create independent runs**

One letter is entered by pressing the same phone key one or more times. Therefore, a letter can never consume presses from two different digits. Whenever the received string changes from one digit to another, that boundary must also separate two letters in every possible original message.

For example, in `"22233"`, no letter can combine a press from the `'2'` run with a press from the `'3'` run. The choices for interpreting `"222"` and `"33"` are independent. The total number of complete messages is the number of choices for the first run multiplied by the number for the second run.

The call `groupby(pressedKeys)` yields each maximal consecutive equal-digit run as a pair `(c, s)`, where `c` is its digit and `s` is an iterator over the presses in that run. Converting `s` to a list and taking its length obtains the run length `m`.

**Interpret one run as a composition of its length**

Most keys represent three letters. For such a key, one letter can consume one, two, or three consecutive presses:

- one press selects the first letter on the key;
- two presses select the second;
- three presses select the third.

Thus, interpreting a run of length `m` is equivalent to splitting `m` into ordered parts of size one, two, or three. The order of parts matters because each part represents the next letter in the decoded message.

Keys `'7'` and `'9'` each represent four letters, so their allowed part sizes are one through four. This is why the implementation uses one recurrence table `f` for ordinary three-letter keys and another table `g` for the two four-letter keys.

**Derive the three-choice recurrence**

Let `f[m]` be the number of ways to decode a length-`m` run on a three-letter key. Consider the final letter:

- If it consumes one press, the preceding `m - 1` presses can be decoded in `f[m - 1]` ways.
- If it consumes two presses, the preceding part contributes `f[m - 2]` ways.
- If it consumes three presses, the preceding part contributes `f[m - 3]` ways.

These cases are disjoint because their final letter consumes a different number of presses, and they cover every valid decoding. Therefore,

$$
f[m] = f[m-1] + f[m-2] + f[m-3].
$$

The initial values are `f[0] = 1`, `f[1] = 1`, `f[2] = 2`, and `f[3] = 4`. The empty run has one neutral decoding, which makes the recurrence work when a final letter consumes the entire run. Length one has one split, length two has `1+1` and `2`, and length three has `1+1+1`, `1+2`, `2+1`, and `3`.

**Derive the four-choice recurrence**

For keys seven and nine, the final letter may consume four presses as well. The same last-part reasoning gives

$$
g[m] = g[m-1] + g[m-2] + g[m-3] + g[m-4].
$$

The first four entries are again `[1, 1, 2, 4]` because no run shorter than four can use the extra four-press letter. The first difference is length four: `f[4] = 7`, while `g[4] = 8` because `g` includes the additional single part `4`.

**Precompute all permitted run lengths**

At module load time, the code starts both lists with their four base values and performs 100,000 append operations. Each new `f` entry sums the previous three; each new `g` entry sums the previous four. Every append applies modulo `10^9 + 7`.

The resulting lists are longer than strictly necessary but safely include index 100,000, the greatest possible run length. Precomputation means a run's decoding count can later be retrieved by one table lookup rather than recomputing a recurrence for every group.

Applying the modulus during precomputation is valid because modular addition preserves the final remainder. It also prevents the stored counts from growing to enormous integers.

**Multiply choices across runs**

The method begins with `ans = 1`, the multiplicative identity. For each group, it chooses `g[m]` when `c in "79"` and `f[m]` otherwise. Digits two through six and eight all have three letters, while only seven and nine have four.

If one run has `A` interpretations and the next has `B` interpretations, every interpretation of the first can be paired with every interpretation of the second, producing `AB` combined messages. Repeating this product over all forced run boundaries counts every full text exactly once.

After each multiplication, the code reduces `ans` modulo `10^9 + 7`. The identity

$$
(ab) \bmod M
=
\big((a \bmod M)(b \bmod M)\big) \bmod M
$$

proves that reducing at every step yields the same required remainder as multiplying the unbounded exact counts first.

**Trace the example** `"22233"`

The first group has digit two and length three, so it contributes `f[3] = 4`. Its splits are `1+1+1`, `1+2`, `2+1`, and `3`.

The second group has digit three and length two, contributing `f[2] = 2` through splits `1+1` and `2`. The digits differ, so the boundary between the groups cannot move. The Cartesian product gives `4 \cdot 2 = 8` complete messages.

**Why the product contains all and only valid messages**

Within each run, the recurrence enumerates every ordered split into allowed press counts and no forbidden split. Each split uniquely determines the sequence of letters on that key because a part's size selects one fixed letter.

Between runs, digit changes force letter boundaries, so choosing a valid split independently for every run creates a valid decoding of the entire press string. Conversely, every possible original message induces exactly one allowed split within each maximal run. This is a bijection between complete messages and tuples of run decodings, which is why multiplying the run counts is correct.

## Complexity detail

Let `n` be the length of `pressedKeys` and let `L = 100000` be the precomputed maximum run length. Module initialization performs `L` constant-time recurrence updates for each of two tables, taking `O(L)` time and `O(L)` stored space.

For one call, `groupby` scans all `n` characters. Converting every group iterator to a list processes each character once across all groups, so total call time is `O(n)`. Table lookups and one multiplication per group are constant time. Including one-time initialization, total work is `O(L + n)`; when tables are already loaded and reused, a call itself is `O(n)`.

The exact source does not have literal constant auxiliary space. The global `f` and `g` lists store `O(L)` entries. In addition, `list(s)` materializes the current group, requiring up to `O(n)` temporary space when the entire input is one run. Thus, the implementation's peak auxiliary storage is `O(L + n)`, or `O(L)` under the constraint `n \le L`.

The manifest's `O(1)` space summary describes a possible constant-state recurrence strategy, not these actual precomputed lists and materialized groups.

## Alternatives and edge cases

- **Dynamic programming sized to the input:** Build three-step and four-step arrays only through the longest run. This avoids the fixed 100,000-entry over-precomputation but still uses linear table space.
- **Constant-state recurrence per run:** Because each recurrence depends on only three or four previous values, it can be evaluated with a rolling window in `O(m)` time and `O(1)` space for a run.
- **Stream run lengths without** `list(s)`: Counting iterator elements directly or scanning indices avoids materializing an entire group and reduces per-call temporary space.
- **Recursive decoding:** Memoization can express the same recurrence, but iterative precomputation avoids recursion depth and repeated call overhead.
- **Multiply raw run lengths:** A run's number of interpretations is not its length; it is the number of ordered partitions under the key's press limit.
- **Keys seven and nine:** They require `g` because four consecutive presses may encode one letter. Using `f` would omit valid messages.
- **Other permitted keys:** Digits two through six and eight use `f` because no letter on those keys needs four presses.
- **Single press:** Both `f[1]` and `g[1]` are one, so a one-character input has exactly one possible text.
- **One long run:** Its table value is the whole answer, and `list(s)` reaches its worst temporary size.
- **Alternating digits:** Every run has length one and contributes one, so the complete message is unambiguous.
- **Several groups:** A digit change is a forced boundary, which justifies multiplication instead of addition.
- **Modulo arithmetic:** Reduction is applied during both table construction and product accumulation, preventing huge intermediate counts.
- **Maximum length:** The precomputed arrays include index 100,000, so the longest legal single run is safe.
- **No zero or one:** The source guarantee excludes keys without letters, so every press belongs to one of the two recurrence categories.
- **Module-level state:** Tables are built once per module load and reused by multiple method calls; that can save repeated time but still consumes memory.
- **Input preservation:** `groupby` reads the string lazily, and no character in `pressedKeys` is changed.
