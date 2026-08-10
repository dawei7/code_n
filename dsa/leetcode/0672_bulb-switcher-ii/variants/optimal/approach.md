## General

**Only the parity of each button count matters**

Pressing a button flips a fixed set of bulbs. Pressing the same button twice returns every affected bulb to its previous state. Therefore, for each of the four buttons, the final effect depends only on whether it was pressed an odd or even number of times.

The order of button presses also does not matter. Flipping bulb states is XOR, and XOR operations commute.

Every possibly long sequence can therefore be summarized by a four-bit `mask`:

- bit zero says whether button one was pressed an odd number of times;
- bit one does the same for button two;
- bit two for button three;
- bit three for button four.

There are only `2 ** 4 = 16` parity masks to examine.

**Not every parity mask is reachable with exactly `presses`**

Let `cnt = mask.bit_count()`, the number of buttons that must be pressed an odd number of times.

At least `cnt` presses are required: press each odd-parity button once. Any additional presses must preserve all four parities, so they must be added in pairs. Pressing any one button twice supplies such a pair.

Thus a mask is reachable exactly when:

- `cnt <= presses`;
- `cnt` and `presses` have the same parity.

The code checks `cnt % 2 == presses % 2`. If both conditions hold, the difference `presses - cnt` is a nonnegative even number and can be filled with canceling pairs.

**Why six bulbs are enough**

The four button patterns depend on:

- whether a label is even or odd, which repeats every two;
- whether it is congruent to one modulo three, which repeats every three;
- the all-bulbs operation, which is constant.

The combined pattern repeats every least common multiple of two and three, which is six. Bulb `j` and bulb `j + 6` are affected identically by every button.

Therefore, for `n > 6`, the first six bulb effects determine all later bulbs. Replacing `n` with `min(n, 6)` loses no information about distinct statuses.

**Represent the four operations as six-bit toggle masks**

Reading bits from the most significant of the six toward the least significant as bulbs one through six:

- `0b111111` flips every bulb;
- `0b010101` flips labels two, four, and six;
- `0b101010` flips labels one, three, and five;
- `0b100100` flips labels one and four.

For a reachable button-parity mask, the inner loop XORs the operation pattern for every selected button into `t`. The resulting six bits describe which bulbs are toggled an odd number of times.

All bulbs start on, but the code stores only the toggle pattern rather than XORing it with the all-on state. This is safe because mapping `toggle` to `initial XOR toggle` is one-to-one: two different toggle patterns always produce two different final states, and equal toggle patterns produce equal states.

**Keep only the bulbs that exist**

`t &= (1 << 6) - 1` restricts the value to six bits. The operation constants already fit, so this is defensive and explicit.

For `n < 6`, the first `n` bulbs occupy the high part of the six-bit pattern. Shifting right by `6 - n` discards effects for nonexistent later bulbs. For `n = 6`, the shift is zero.

The truncated pattern is inserted into `vis`. Different button masks can have the same effect, especially when very few bulbs exist, and the set collapses those duplicates.

**A one-bulb example**

With one bulb and one press:

- button one toggles the bulb;
- button two affects only even labels, so it leaves bulb one unchanged;
- button three toggles bulb one;
- button four also toggles bulb one.

Four choices produce only two distinct states. After truncation, the set contains the two distinct one-bit toggle patterns, so the answer is two.

**Why enumeration is complete and correct**

Every actual press sequence has a unique parity mask. Its count of odd buttons is no greater than the total presses and has the same parity, so the enumeration includes that mask. XORing its selected operation masks reproduces exactly the sequence's net toggles.

Conversely, every mask passing the two reachability tests can be realized by pressing each selected button once and spending the remaining even number of presses in canceling pairs. Thus every pattern inserted into `vis` corresponds to at least one legal exact-length sequence.

Truncation preserves exactly the bulbs present, and the set counts distinct effects. Therefore, `len(vis)` is exactly the number of possible final statuses.

## Complexity detail

The algorithm examines exactly 16 masks. For each, it performs constant-time tests and at most four XOR operations. Its running time is `O(1)`, independent of `n` and `presses`.

The set contains at most 16 integer patterns, also a fixed constant. Auxiliary space is `O(1)`.

The bound remains constant even when `presses` is one thousand because only parity and the comparison against four odd buttons matter.

## Alternatives and edge cases

- **Closed-form case analysis:** The first three bulbs actually determine all states, allowing a small formula based on capped `n` and whether presses is zero, one, two, or at least three. It is faster only by a constant and less directly connected to the operations.

- **Breadth-first simulation by press count:** Repeatedly apply four buttons to every current state. Capping to six bulbs keeps the state universe small, but parity enumeration reaches the answer more directly.

- **Enumerate all operation sequences:** There are `4 ** presses` sequences, which is impossible for large `presses` and repeats many equivalent parities.

- **Track all `n` bulbs:** This is unnecessary because operation patterns repeat every six positions.

- **Zero presses:** Only mask zero passes, producing the original all-on status, so the answer is one.

- **Very large press count:** Every parity-compatible mask with at most four set bits is reachable because extra presses can be added in pairs.

- **One bulb:** Several buttons become equivalent after truncation, and the set correctly merges them.

- **Two or three bulbs:** Some six-bit patterns also collapse after shifting, which is why counting masks directly would be wrong.

- **Exactly versus at most presses:** The parity condition is essential. A mask requiring one odd press is not reachable with exactly two presses because one extra press would change some parity.

- **Repeated same button:** Two additional presses cancel and are the constructive reason any even surplus is allowed.

- **Initial bulbs are on:** Counting toggle patterns is still valid because XOR with the fixed initial pattern is a bijection.

- **Bit orientation:** The high six-bit position represents bulb one. The right shift for small `n` relies on this convention.

- **Period six:** It comes from the combined modulo-two and modulo-three button patterns. Capping at a different unexplained number could lose distinctions.
