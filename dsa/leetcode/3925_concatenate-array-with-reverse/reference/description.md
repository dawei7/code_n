## Description

An integer array `nums` contains $n$ elements. Build a new array `ans` of length $2n$ by placing an unchanged copy of `nums` in its first half and the elements of `nums` in reverse order in its second half.

More precisely, for every index $i$ from $0$ through $n-1$, position `i` of the result must equal `nums[i]`, while position `i + n` must equal `nums[n - i - 1]`. Return the newly constructed array; the values and their repetitions must be preserved exactly.
