## Description

There are $n$ open windows numbered from $1$ through $n$. The permutation `windows` gives their initial front-to-back order: its first entry is on top and its last entry is at the bottom.

Process `queries` from left to right. Each query names a window and moves that window to the top, preserving the relative order of every other window. Repeatedly selecting the window already on top leaves the order unchanged. Return the complete final front-to-back ordering after all queries.
