## Description

There are $n$ people numbered from $0$ through $n-1$ and one door that takes one second to cross. The non-decreasing array `arrival` gives each person's arrival second. `state[i]` is `0` when person $i$ wants to enter and `1` when they want to exit. A person may wait after arriving, and only one person crosses in any second.

When both directions have waiting people, the previous second determines priority. If the door was unused, exiting has priority. If it was used, the same direction has priority. Among people waiting for the chosen direction, the smallest index crosses first. Return every person's actual crossing second.
