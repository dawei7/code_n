## General

**Only currently noncommunicating friendships matter**

If two friends already share at least one language, teaching is unnecessary for that friendship and can never break their communication.

If they share no language, the only way the chosen global teaching language can repair their friendship is for both endpoints to know that language afterward. Since neither initially shares any common language with the other, every endpoint of every failing friendship must either already know the chosen language or be taught it.

The source first identifies the union of these affected users in set `s`.

**Check whether one friendship already communicates**

The nested helper `check(u,v)` iterates every language `x` of user `u` and every language `y` of user `v`. It returns true on the first equality.

User IDs are one-indexed, so their language lists are accessed as `languages[u - 1]` and `languages[v - 1]`.

If no pair of entries matches, the lists are disjoint and the helper returns false.

The implementation deliberately compares lists directly rather than converting them to sets. This exact choice affects its running-time analysis.

**Collect each affected user once**

For every friendship that fails `check`, both user IDs are added to `s`. A user may participate in several failing friendships, but set semantics retain one copy.

This deduplication is required because a user taught the chosen language once repairs all of that user's affected friendships. Counting the same person once per friendship would overstate the answer.

Users appearing only in already communicative friendships are absent from `s` and never need teaching.

**Count which affected users already know each language**

The source creates `cnt = Counter()`. For every affected user `u`, it iterates that user's unique language list and increments `cnt[l]`.

Thus `cnt[l]` is the number of affected users who already know language `l`. The input guarantee that each user's language list contains unique values ensures one user contributes at most one to a language.

**Choose the language requiring the fewest lessons**

If language `l` is selected, all `len(s)` affected users must know it afterward. `cnt[l]` already know it, so the number needing instruction is

$$
\lvert s\rvert-\texttt{cnt}[l].
$$

Minimizing this difference is equivalent to maximizing `cnt[l]`. The exact return is

`len(s) - max(cnt.values(), default=0)`.

The default handles an empty affected set: `cnt` then has no values, the maximum defaults to zero, and the answer is zero.

**Why teaching every affected nonknower is sufficient**

After choosing the most common language among affected users, teach it to every affected user who lacks it. Every originally failing friendship has both endpoints in `s`, so both endpoints now know the selected language and can communicate.

Originally working friendships remain working because nobody forgets a language. Therefore all friendship requirements are satisfied.

**Why fewer lessons are impossible**

Fix any chosen language `l`. Consider any affected user `u` who does not know `l`. That user belongs to at least one friendship that initially had no common language.

The other endpoint learning `l` alone cannot create a shared language with `u`; no other language knowledge changes. Hence `u` itself must be taught `l`. Every affected nonknower is mandatory for that choice.

So `len(s)-cnt[l]` is both necessary and sufficient. Selecting the largest `cnt[l]` gives the global minimum.

**Trace the first example**

Users one and two know disjoint language sets, so both enter `s`. Friendships involving user three already work through language one or two as applicable.

Among affected users, language one is known by one person and language two by one person. Either choice leaves one user to teach, so the answer is one.

**Friendship transitivity is irrelevant**

Each friendship edge must communicate directly through a shared language. A language path through a third user does not help. The algorithm checks and repairs every listed edge through its endpoints, never assumes social connectivity transfers communication.

## Complexity detail

Let $F$ be the number of friendships and let $L_u$ be user $u$'s language count. The exact direct-list check costs

$$
O\!\left(\sum_{(u,v)\in\texttt{friendships}}L_uL_v\right)
$$

in the worst case because it uses nested loops. Counting languages for affected users adds $O(\sum_{u\in s}L_u)$.

This is not generally a simple linear $O(S+C)$ bound unless $C$ is explicitly defined as the total pairwise language comparisons. With at most 500 languages per user, a coarse bound is $O(Fn^2+mn)$.

The affected-user set uses $O(m)$ space for $m$ users, and the counter uses at most $O(n)$ language keys. Exact auxiliary space is $O(m+n)$, apart from input storage.

## Alternatives and edge cases

- **Convert each language list to a set:** Friendship intersection can iterate the smaller set with expected constant-time membership, reducing repeated comparison work at $O(S)$ preprocessing space.
- **Boolean language matrix:** With both users and languages at most 500, bitsets can make intersections and counts fast and predictable.
- **Teach per friendship independently:** It can teach the same user several times or choose conflicting languages; one global language must be optimized over the affected-user union.
- **All friendships already communicate:** `s` and `cnt` stay empty, and the default maximum returns zero.
- **One affected friendship:** Choose a language known by one endpoint if possible, teaching the other once; their sets are disjoint, so no language is known by both.
- **User in several failing friendships:** The set counts that user once.
- **Language known by every affected user:** No teaching is required even though some pairs originally failing would contradict this situation; in practice such a language would mean those pairs were not failing.
- **Language known by none:** It would require teaching everyone and can never beat a language already counted when `s` is nonempty.
- **Unique per-user language entries:** Counter increments represent users rather than duplicate list entries.
- **One-indexed IDs:** Subtracting one for list access is required.
- **Nontransitive friendships:** Only listed pairs are checked.
- **Input preservation:** No language list or friendship is modified.
