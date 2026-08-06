## Description

A city train line has regular and express routes passing through the same
$n+1$ stops, numbered from 0 through $n$. You begin on the regular route at
stop 0. For each segment from stop $i-1$ to stop $i$, `regular[i]` and
`express[i]` give the respective travel costs.

Moving from regular to express costs `expressCost` every time that transfer is
made. Returning from express to regular is free, and remaining on the express
route has no additional transfer cost. Return the minimum total cost to reach
each stop 1 through $n$ from stop 0; reaching a stop on either route counts.
