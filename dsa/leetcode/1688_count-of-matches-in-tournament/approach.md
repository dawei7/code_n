## General

**Count eliminations instead of simulating rounds**

The round rules look different for even and odd team counts, but every actual match has one invariant outcome: exactly one team loses and is eliminated. The winning team remains in the tournament.

The tournament starts with `n` teams and ends when exactly one champion remains. Therefore exactly `n - 1` teams must be eliminated.

Since every match eliminates exactly one team, the number of matches is also exactly `n - 1`. The source returns that expression directly.

**Why a bye does not affect the count**

In an odd-sized round, one team advances without playing. That bye eliminates no team and counts as no match. The other `n - 1` teams form pairs, and each match eliminates one of them.

The bye changes when eliminations occur, not how many eliminations are ultimately necessary. All nonchampion teams must still lose one match at some later or current round.

For seven teams, three first-round matches eliminate three teams and one team receives a bye, leaving four. Two more matches leave two teams, and one final match selects the champion. The distribution is `3 + 2 + 1`, but the total is simply six, or `7 - 1`.

**A one-to-one correspondence**

Every match can be paired with the unique team that loses that match. No team loses twice because its first loss removes it permanently. The champion never loses.

Thus the set of matches is in one-to-one correspondence with the set of nonchampion teams:

- each match contributes one distinct eliminated team;
- each of the `n - 1` nonchampions must be eliminated by some match.

This is stronger than merely observing examples. It proves that no legal arrangement of pairings or byes can change the total.

**Why the tournament rules guarantee completion**

Whenever more than one team remains, at least one match is played. In an even round, half the teams remain. In an odd round greater than one, `(n - 1)/2 + 1` teams remain, which is fewer than `n`. The count therefore eventually reaches one.

The formula does not need to know how many rounds that takes. It counts the permanent decrease in team count across the entire process.

**Matches are not rounds**

The answer counts individual pairings, not stages of the bracket. One round may contain many simultaneous matches, while a bye belongs to a round but is not a match. For eight teams there are three rounds but seven matches. The elimination invariant targets the requested quantity directly: each match corresponds to one loss, whereas the number of rounds depends on how quickly the active count is halved.

**Telescoping view**

Another way to see the same invariant is to let `t_r` be the number of teams before round `r` and `t_{r+1}` the number after it. The matches in that round equal the number eliminated:

$$
t_r-t_{r+1}.
$$

Adding over all rounds makes intermediate counts cancel:

$$
(t_0-t_1)+(t_1-t_2)+\cdots+(t_{last}-1)
=t_0-1
=n-1.
$$

Even and odd formulas both satisfy this identity. The direct return is therefore the closed form of the full simulation.

**Why the result is correct**

There must be at least `n - 1` matches because every one of the `n - 1` nonwinning teams needs a loss, and one match can eliminate only one team. There cannot be more than `n - 1` matches because every match eliminates a previously active team and only `n - 1` teams can be removed before one remains.

The lower and upper bounds are equal, proving the exact answer `n - 1`.

## Complexity detail

The implementation performs one subtraction and one return, independent of `n`. Its time complexity is $O(1)$ and its auxiliary space complexity is $O(1)$.

It allocates no collection and does not mutate `n`. Integer size is bounded by the constraint `n <= 200`, so arithmetic is ordinary constant-time work.

This improves on round simulation, which would take $O(\log n)$ iterations while still producing the same result.

## Alternatives and edge cases

- **Round simulation:** Repeatedly add `floor(n/2)` matches and replace `n` with `ceil(n/2)`. It is correct but takes $O(\log n)$ time and obscures the elimination invariant.
- **Recursive simulation:** It mirrors the tournament tree but adds unnecessary call-stack overhead.
- **One team:** No match is needed, and `n - 1` correctly returns zero.
- **Two teams:** One match eliminates one team and selects the winner; the formula returns one.
- **Odd team count:** A bye eliminates nobody and therefore adds nothing beyond the matches that actually occur.
- **Even team count:** Every team is paired, but only one member of each pair is eliminated, matching one elimination per match.
- **Random bye selection:** Which team advances freely can affect identities and bracket shape, never the total number of nonchampions.
- **Different winners:** Any possible champion leaves exactly the other `n - 1` teams to be eliminated.
- **No draws assumed:** The rules state that half of each matched pair advances, so every match has exactly one loser; the proof relies on this.
- **Closed-form insight:** The answer depends only on initial and final active counts, not the number of rounds.
