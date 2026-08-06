## Description

Given a nonempty integer array `arr` interpreted as circular and a valid `startIndex`, return a JavaScript generator that maintains a current array position.

The first call to `next()` yields `arr[startIndex]`. Every later call supplies an integer `jump` through `next(jump)`. Move the current index right by a positive jump, left by the magnitude of a negative jump, or leave it unchanged for zero. Crossing either array boundary wraps to the opposite end, and jumps may make multiple complete circuits.

After applying the supplied jump, yield the value at the new current index and suspend again with that index preserved for the following call.

The array length is from 1 through $10^4$. A test schedule contains from 1 through 100 jumps, and every array value and jump lies between $-10^4$ and $10^4$.
