## Description

A party has `n` people labeled from `0` through `n - 1`, and it may contain one celebrity. A celebrity is known by every other attendee but does not know any of them.

Determine the celebrity's identity, or establish that nobody satisfies the definition, while asking asymptotically as few questions of the form “Does person `A` know person `B`?” as possible.

You receive `n` and the helper API `bool knows(a, b)`, which reports whether `a` knows `b`. Implement `int findCelebrity(n)`. If a celebrity is present, that person is unique.

Return the celebrity's label when one exists; otherwise, return `-1`.

The `n x n` matrix `graph` shown in inputs is not directly available to the native solution. Relationships may be inspected only through `knows`. A value `graph[i][j] == 1` means person `i` knows person `j`; a value of `0` means person `i` does not know person `j`.
