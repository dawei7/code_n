## Description

There are `n` people in a line at indices `0` through `n - 1`. Each person independently chooses either `L` or `R`. Choosing `L` makes that person visible only to people on their right, while choosing `R` makes them visible only to people on their left.

Focus on the observer at index `pos`. A person at an index below `pos` is visible to the observer exactly when choosing `L`; a person above `pos` is visible exactly when choosing `R`.

Count the complete direction assignments in which the observer sees exactly `k` other people. Return the count modulo $10^9+7$.
