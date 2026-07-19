## General
**Describe a prefix only by its number of distinct songs**

Let $D_{\ell,u}$ be the number of valid prefixes of length $\ell$ that have used exactly $u$ distinct songs. Song identities remain symmetric once $u$ is known, so this state contains enough information to count both ways to extend a prefix.

To finish a prefix with $u$ distinct songs, the last play is either new or repeated. If it introduces a new song, the previous state used $u-1$ songs and offers $n-u+1$ unused choices. If it repeats an already used song, the previous state already used $u$ songs. The most recent $k$ distinct songs are unavailable, leaving $\max(u-k,0)$ eligible choices. Thus

$$
D_{\ell,u}
=
D_{\ell-1,u-1}(n-u+1)
+
D_{\ell-1,u}\max(u-k,0).
$$

**Build playlist lengths in order**

Start with $D_{0,0}=1$ and all other states zero. For each new length, compute a fresh row from the preceding row and reduce every update modulo $10^9+7$. Only states with $u\le\min(\ell,n)$ are reachable.

The two transition cases are disjoint because the final song either appeared earlier or did not, and their choice counts cover every legal final play. Removing that last play maps each counted playlist back to exactly one preceding state, so the recurrence neither omits nor duplicates a playlist. After `goal` positions, requiring all songs means the answer is $D_{\textit{goal},n}$.

## Complexity detail
There are `goal` rows and at most $n$ reachable distinct-song counts per row. Each transition takes constant arithmetic work, so time is $O(n\cdot\textit{goal})$. Keeping only the previous and current rows uses $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate playlists:** Backtracking over song identities is direct but grows exponentially and is unusable near the limits.
- **Two-dimensional table:** Storing every $D_{\ell,u}$ is conceptually simple and has the same time bound, but uses $O(n\cdot\textit{goal})$ space.
- **Explicitly enumerate symmetric choices:** Summing the same predecessor once for every eligible song instead of multiplying by the choice count adds an unnecessary factor of $n$.
- **No replay restriction:** When $k=0$, all $u$ previously used songs are eligible for a repeat.
- **Playlist length equals song count:** Every song appears exactly once, so the answer is $n!$ regardless of $k$.
- **Large separation:** When $u\le k$, no previously used song can be replayed yet.
- **Modulo arithmetic:** Reduce after each transition so intermediate combinatorial counts do not grow without bound.
