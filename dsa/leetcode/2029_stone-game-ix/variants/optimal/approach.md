## General

**Only residues modulo three affect the game**

Whether the running sum is divisible by three depends only on each stone's remainder after division by three. The source counts stones in three groups: `cnt[0]`, `cnt[1]`, and `cnt[2]`.

A residue-zero stone leaves the running remainder unchanged. A residue-one stone adds one modulo three, and a residue-two stone adds two, which is the same as subtracting one modulo three. The original magnitudes no longer matter after these counts are built.

**Why Alice must begin with residue one or residue two**

The running sum starts at remainder zero. Removing a residue-zero stone immediately keeps the sum divisible by three, so Alice would lose on her first move. A winning first move must therefore use residue one or residue two.

The helper `check(cnt)` analyzes the possibility that Alice starts with the group stored at index one. The source calls it twice. First, `c1` has the natural order `[count0,count1,count2]`, so it tests starting with residue one. Then `c2 = [count0,count2,count1]` swaps the two nonzero groups, so the same helper tests starting with residue two.

If `cnt[1]` is zero, that proposed starting move is unavailable and the helper returns false.

**The forced safe pattern after starting with residue one**

After Alice removes a residue-one stone, the running remainder is one. A residue-two stone would make the remainder zero and cause the mover to lose immediately. Ignoring zeros for a moment, the next safe nonzero stone must therefore be another residue one, moving the running remainder to two.

From remainder two, a residue-one stone would be losing, so the next safe nonzero stone must be residue two, returning the remainder to one. The safe nonzero continuation alternates:

`1, 2, 1, 2, ...`

after the initial starting residue-one stone. This explains the helper's paired count

`min(cnt[1], cnt[2]) * 2`.

The helper first consumes the initial residue-one stone with `cnt[1] -= 1` and counts that move in `r`. It can then form as many safe one-two pairs as the smaller remaining nonzero group permits.

**How one additional residue-one move fits**

After all complete pairs, the running remainder is again one. If more residue-one stones remain than residue-two stones, one additional residue-one move is safe and changes the running remainder to two. The code detects `cnt[1] > cnt[2]`, adds one to the safe-move count, and decrements `cnt[1]` once for the later leftover test.

No second unpaired residue-one move is safe at that point, because adding another one to remainder two would reach zero. If residue-two stones are the surplus instead, even the first surplus residue-two stone is unsafe while the remainder is one.

**What residue-zero stones do**

As long as the running remainder is one or two, taking a residue-zero stone is safe because it does not change that remainder. Each such stone nevertheless consumes a turn, so its count affects which player eventually faces the first unavoidable losing move.

That is why `r` includes `cnt[0]`. The helper is counting the total number of safe removals before play reaches a leftover nonzero stone that cannot be selected without making the sum divisible by three.

The exact order in which safe zero stones are interleaved is not important to the remainder progression. Their total parity is what changes the identity of the player to move afterward.

**Why a leftover stone is necessary**

If the safe sequence consumes every stone, Bob wins automatically under the problem's special exhaustion rule, even if it would otherwise be Alice's turn. Alice therefore needs play to end because Bob is forced to take a losing stone, not merely because an odd number of safe moves was made.

The final condition `cnt[1] != cnt[2]` checks for this leftover after accounting for the initial and possible extra residue-one move. The code does not subtract the paired stones explicitly, but equality captures whether pairing exhausts both groups. If the second group is larger, its surplus is immediately unsafe. If the first group was larger, the earlier decrement represents its one safe extra; inequality afterward means at least one further unsafe surplus remains.

**Why the parity condition identifies Alice's win**

Alice makes safe move number one. After an odd number of safe moves, it is Bob's turn. If an unsafe leftover remains then, Bob cannot remove it without making the cumulative sum divisible by three and losing. Therefore Alice wins exactly when `r` is odd and the leftover test succeeds.

If `r` is even, Alice is the player facing the losing continuation. If no leftover exists, exhaustion awards the game to Bob. The helper consequently returns

`r % 2 == 1 and cnt[1] != cnt[2]`.

**Connection to the compact residue criterion**

The helper's two symmetric trials encode a familiar closed form. When `count0` is even, Alice can win exactly when both nonzero residue groups are present. When `count0` is odd, she needs the two nonzero counts to differ by more than two.

The source does not write that formula directly. Its safe-sequence simulation reaches the same result while explicitly accounting for a chosen starting residue. Calling `check(c1) or check(c2)` lets Alice use whichever nonzero start is winning.

**Mutation is confined to disposable count arrays**

`check` decrements entries in the list it receives. This does not alter `stones`. Also, `c2` is constructed from the original counts before either helper call is evaluated, so mutation of `c1` cannot corrupt the symmetric trial.

Python's `or` short-circuits: if the first trial wins, the second need not run. That is safe because the requested result is only whether at least one winning first choice exists.

## Complexity detail

Let $N$ be the number of stones. Counting residues takes $O(N)$ time. Each `check` call performs only a fixed number of arithmetic operations and comparisons, so the remaining work is $O(1)$. Total time is $O(N)$.

The three residue counts, their swapped copy, and scalar helper state occupy $O(1)$ space. The count arrays always have length three regardless of $N$.

## Alternatives and edge cases

- **Direct closed-form test:** Use the parity of `count0` and either the presence of both nonzero groups or `abs(count1 - count2) > 2`; it is shorter but hides the safe-turn derivation.
- **Full game-state minimax:** State counts can be enormous and exploring individual stones ignores that equal residues are interchangeable.
- **Start with residue zero:** Alice loses immediately because the running sum remains divisible by three.
- **Only residue-zero stones:** Neither helper has a legal nonzero start, so Bob wins.
- **Only one nonzero stone:** Alice can remove it safely, but exhaustion then awards Bob the win.
- **Both nonzero groups with even zero count:** The symmetric checks allow the winning starting group.
- **Odd zero count:** The extra safe pass changes whose turn reaches the forced losing residue.
- **Equal nonzero counts:** Exhaustion behavior is crucial; no unsafe surplus remains after the safe pattern.
- **Large surplus in one nonzero group:** The surplus eventually creates an unavoidable move to remainder zero.
- **Starting symmetry:** Swapping residue one and residue two preserves the game's structure.
- **Short-circuit evaluation:** The second helper is unnecessary once the first finds a winning opening.
- **Local mutation:** `check` changes only count copies, never the input list.
- **Original stone values:** Values with the same remainder modulo three are strategically identical.
