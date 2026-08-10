## General

**Translate the judge rules into directed degrees**

Each trust pair `[a, b]` is a directed relationship from person `a` to person `b`.

- The number of people someone trusts is their outgoing degree.
- The number of people who trust someone is their incoming degree.

The judge trusts nobody, so the judge's outgoing degree must be zero. Every other person trusts the judge, so the judge's incoming degree must be exactly `n - 1`.

These two numbers completely characterize the judge. The algorithm does not need to build neighbor lists or traverse a graph; it only needs to count incoming and outgoing relationships for each label.

**Use arrays indexed by person label**

People are labeled from one through `n`. The solution allocates arrays `cnt1` and `cnt2` with length `n + 1` so that a person's label can be used directly as an index. Position zero is intentionally unused.

Their meanings are:

- `cnt1[p]` is how many listed people person `p` trusts;
- `cnt2[p]` is how many listed people trust person `p`.

For each pair `[a, b]`:

`cnt1[a] += 1` records one outgoing relationship, and `cnt2[b] += 1` records one incoming relationship.

The trust pairs are unique, so repeated copies cannot artificially inflate these degrees. Self-trust is forbidden, so an incoming count of `n - 1` really can represent all other people.

**Check both conditions together**

After counting, the loop examines labels one through `n`. It returns `i` only if

`cnt1[i] == 0 and cnt2[i] == n - 1`.

The outgoing condition prevents accepting a popular person who still trusts somebody. The incoming condition prevents accepting an isolated person who trusts nobody but is not trusted by everyone else.

If no label satisfies both, the method returns `-1`.

**Why incoming degree `n - 1` means everybody else**

There are exactly `n - 1` people other than candidate `i`. Every trust pair is unique, and nobody trusts themselves. Therefore, `n - 1` distinct incoming pairs to `i` must originate from all other people, with no missing person and no duplicate source relationship.

Without those input guarantees, an incoming count alone could be misleading. Under this contract, it precisely captures the universal-trust requirement.

**Trace a successful case**

For `n = 3` and `trust = [[1, 3], [2, 3]]`:

- person one has outgoing count one and incoming count zero;
- person two has outgoing count one and incoming count zero;
- person three has outgoing count zero and incoming count two.

Since `n - 1 = 2`, person three meets both judge conditions and is returned.

If `[3, 1]` is added, person three's outgoing count becomes one. Although person three is still trusted by everyone else, the judge must trust nobody, so no candidate is returned.

**Why there cannot be two valid judges**

Suppose two different people both met the conditions. Because everyone except a judge must trust that judge, each of the two would have to trust the other. But each also has outgoing degree zero and therefore trusts nobody. This is a contradiction.

Thus at most one person can satisfy both degree conditions. Returning the first match is safe even without separately counting candidates.

**The one-person town**

When `n = 1`, the only person has no one else to trust and no one else who must trust them. With an empty trust list:

- outgoing degree is zero;
- incoming degree is zero;
- `n - 1` is also zero.

The method returns label one, correctly treating the sole person as the judge under the vacuous “everybody else” condition.

**Why the degree test is both necessary and sufficient**

If a judge exists, the two defining rules directly imply outgoing degree zero and incoming degree `n - 1`, so the scan must find that person.

Conversely, if the scan finds a person with these counts, outgoing degree zero proves they trust nobody. The uniqueness and no-self-edge guarantees make incoming degree `n - 1` prove every other person trusts them. Therefore, they satisfy the complete definition.

The return value `-1` is used only after every label fails at least one necessary rule, so it correctly means no judge exists.

**Why full graph storage would be excessive**

An adjacency list would remember exactly whom each person trusts. The final decision never asks for those identities individually; it asks only how many edges enter and leave each person. Aggregating degrees while reading the input retains all relevant information and discards irrelevant structure.

## Complexity detail

Let `N` be the number of people and `E` the number of trust pairs.

The first loop processes each pair once in `O(E)` time. The candidate scan checks `N` labels, giving total time `O(N + E)`.

The two arrays contain `N + 1` integers each, so auxiliary space is `O(N)`.

If the early edge-count optimization from some formulations were added, one could return immediately when `E < N - 1`, but the exact implementation simply performs the clear `O(N + E)` process.

## Alternatives and edge cases

- **One score array:** Subtract one for every outgoing edge and add one for every incoming edge. A judge has score `n - 1`. This is more compact, though separate arrays make both requirements explicit.
- **Adjacency lists:** They can compute degrees but retain neighbor information the answer never uses.
- **Candidate elimination:** Trusting someone disqualifies the source as judge, after which a candidate can be verified. It is useful in query-based variants but unnecessary with the full edge list available.
- **Too few trust pairs:** Fewer than `n - 1` edges cannot supply the judge's required incoming degree; the normal count still returns `-1`.
- **Popular person who trusts someone:** Correctly rejected by nonzero `cnt1`.
- **Person who trusts nobody but lacks support:** Correctly rejected by incoming degree below `n - 1`.
- **Empty trust list with `n > 1`:** Every outgoing count is zero, but no incoming count reaches `n - 1`, so return `-1`.
- **Empty trust list with `n = 1`:** The sole label meets both zero-valued conditions and is returned.
- **Unique pairs:** They ensure degree counts represent distinct people rather than repeated records.
- **No self-trust:** It ensures the judge's incoming target is exactly all other `n - 1` people.
- **Maximum label:** Arrays have length `n + 1`, so label `n` is a valid direct index.
