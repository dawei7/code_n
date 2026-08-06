## Description

An undirected tree contains $n$ vertices numbered from $0$ through $n-1$. Initially every vertex is unmarked. After one vertex is marked at time $t=0$, each subsequent second marks every still-unmarked vertex that is adjacent to at least one already marked vertex. Thus marking spreads outward across one tree edge per second.

Consider starting this process separately from every vertex `i`. Return an array `nodes` where `nodes[i]` is a vertex marked during the final second when `i` is the initial vertex. Several vertices can be marked last at the same time; in that situation, any one of those tied vertices is a valid answer for `nodes[i]`.
