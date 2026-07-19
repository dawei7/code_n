## General
**Start with letters unique to one digit name**

Some letters immediately reveal a digit count: `z` occurs only in zero, `w` only in two, `u` only in four, `x` only in six, and `g` only in eight. Their frequencies therefore give the counts of `0`, `2`, `4`, `6`, and `8` without ambiguity.

**Resolve names after their competitors are known**

The remaining useful letters become unique after subtracting already determined digits. The count of three is `h - eight`; five is `f - four`; and seven is `s - six`. Then one is `o - zero - two - four`, and nine is `i - five - six - eight`.

This order is a dependency elimination, not a guess: every subtraction removes all previously identified uses of the selected letter, leaving exactly the target digit's multiplicity.

**Emit the canonical sorted representation**

Once all ten multiplicities are known, append digit `d` exactly `count[d]` times while visiting digits from zero through nine. The input shuffle no longer matters because frequency counting discarded its order.

**Why the recovered multiset is exact**

Each first-stage unique letter forces its corresponding digit count. Each later equation accounts for every other digit name containing that letter before assigning the residue. Because the input is guaranteed to be composed of valid digit names, the residues are nonnegative and consume the same letter multiset; thus no different digit multiset can satisfy the sequence of forced equations.

## Complexity detail
Counting the `n` input letters and building an output of at most `n` characters takes $O(n)$ time. The frequency table and ten digit counters have fixed size, so auxiliary space is $O(1)$ apart from the required output.

## Alternatives and edge cases
- **Repeated multiset removal:** identify one word at a time and erase its letters from a list; linear-time removals can make this $O(n^2)$.
- **Backtracking over digit names:** can enumerate valid decompositions but needlessly explores an exponential search tree.
- **Repeated digits:** frequency equations preserve multiplicity directly.
- **Only one digit kind:** the same unique-letter or residual equation still determines its count.
- **Shuffled input:** no positional information is needed or assumed.
