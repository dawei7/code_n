## Description

There are $n$ locks, and lock $i$ requires at least `strength[i]` units of energy to break. A sword starts with zero energy and a growth factor $X=1$. During each minute, its energy increases by the current value of $X$.

You may break any remaining lock as soon as the sword has enough energy for it. Breaking a lock resets the sword's energy to zero and permanently increases $X$ by one. Thus, before the $j$-th lock is broken, the sword gains $j$ energy units per minute, but choosing that lock also determines which strength must be paid at that rate.

Choose the order in which to break all locks so that the total elapsed time is as small as possible, and return that minimum time.
