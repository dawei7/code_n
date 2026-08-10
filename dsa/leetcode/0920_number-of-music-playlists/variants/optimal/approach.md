## General

The playlist must have exact length `goal`, use every one of the `n` songs, and avoid replaying a song until `k` other songs have appeared. Dynamic programming tracks both playlist length and how many distinct songs have been introduced.

Define

$$
f[i][j]
$$

as the number of valid playlists of length $i$ that use exactly $j$ distinct songs.

The base is `f[0][0] = 1`: there is one empty playlist using zero songs. All other zero-length or impossible states remain zero.

At the final state, `f[goal][n]` counts playlists of the required length that have used all songs at least once.

**Transition by playing a new song.** To end a length-$i$ playlist with exactly $j$ distinct songs, one possibility is to take a valid length-$(i-1)$ playlist with $j-1$ distinct songs and introduce a song never used before.

There are

$$
n-(j-1)=n-j+1
$$

unused choices. This contributes

$$
f[i-1][j-1](n-j+1).
$$

A never-used song cannot violate the replay gap because it has no earlier occurrence.

**Transition by replaying an old song.** The other possibility starts from a length-$(i-1)$ playlist already using exactly $j$ distinct songs and chooses one of those songs again.

The previous `k` positions contain `k` distinct songs: the replay restriction itself prevents any song from appearing twice within that window. Those `k` songs are temporarily unavailable. The remaining

$$
j-k
$$

used songs are eligible. This transition exists only when $j>k$ and contributes

$$
f[i-1][j](j-k).
$$

The two cases are disjoint because the final song is either new or previously used. Their counts can be added.

**Why the state needs no record of the actual last songs.** For a particular valid playlist using $j$ songs, exactly `k` used songs are blocked when $j>k$, regardless of their identities. Every song is otherwise symmetric. Therefore the number of choices depends only on $j$, not on which songs occupy the recent window.
Every valid length-$i$ playlist with $j$ distinct songs has a unique prefix of length $i-1$. If its last song first appears there, removing it yields a state with $j-1$ distinct songs and it is counted by the new-song term. Otherwise removing it yields a state with $j$ distinct songs, and validity means the chosen repeat is not among the last `k` songs, so it is counted by the replay term.

Conversely, appending any song counted by either term produces a valid playlist in state $(i,j)$. The classification is unique, so no playlist is omitted or counted twice.

For $n=2$, `goal=3`, and $k=1$, length one has two new-song choices. Length two must introduce the other song. At length three, both songs have been used but only the one not played last is available, yielding playlists `[1,2,1]` and `[2,1,2]`.

For $k=0$, no used song is blocked. The replay multiplier becomes $j$, so any previously introduced song can be played again immediately.

For $n=3$, `goal=3`, and $k=1$, reaching state `f[3][3]` can only use the new-song transition from `f[2][2]`. Each length-two playlist has used two labeled songs and has one unused choice, so all $3\cdot2\cdot1=6$ permutations are counted. A replay transition would remain in column two and therefore could not satisfy the final “all three songs” requirement.

The row index also imposes natural state bounds even though the loops visit the whole rectangle. When $j>i$, `f[i][j]` stays zero because neither transition can create more distinct songs than positions. When $j>n$, no column exists. These zero states let one uniform recurrence handle boundaries without separate cases.

Every update is reduced modulo $10^9+7$.

## Complexity detail

The table has $(\texttt{goal}+1)(n+1)$ entries, and each transition performs constant arithmetic.

- **Time complexity:** $O(n\cdot\texttt{goal})$.
- **Space complexity of the exact solution:** $O(n\cdot\texttt{goal})$ for the full table.

The manifest's $O(n)$ space corresponds to rolling the previous row because row $i$ depends only on row $i-1$. The exact `solution.py` retains every row and therefore uses two-dimensional memory.

## Alternatives and edge cases

- **Rolling-row DP:** Keep only previous and current arrays, reducing space to $O(n)$ while preserving time and matching the manifest.
- **Top-down memoization:** Cache states $(i,j)$ and use the same two transitions. Complexity is similar, with recursion overhead.
- **Enumerate all playlists:** There are $n^{\texttt{goal}}$ raw sequences before constraints, which is infeasible.
- **Combinatorial inclusion-exclusion:** A formula can count playlists more directly, but it is harder to derive and implement safely.
- **`goal == n`:** Every song must appear exactly once, so the result is $n!$ regardless of `k<n`.
- **`k = 0`:** Immediate repeats are legal.
- **`k = n - 1`:** After all songs appear, the next song is forced to be the one outside the most recent $n-1$ positions.
- **`j <= k`:** No old song is eligible, so only a new-song transition can extend the playlist.
- **Impossible states `j > i`:** They remain zero because a playlist cannot introduce more distinct songs than positions.
- **All songs required:** Returning any `f[goal][j]` with $j<n$ would count playlists that omit songs; only column `n` is valid.
- **Song identities:** The multipliers restore labeled-song choices even though the DP state stores only a count.
- **Modulo:** Both multiplication terms are added before reducing to the required residue.
