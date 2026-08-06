## Description

Design a queue that initially contains the integers from $1$ through $n$ in ascending order. It supports a `fetch(k)` operation that selects the current $k$-th element, removes that element from its position, places it at the back of the queue, and returns its value.

Positions are one-indexed and are evaluated against the queue's current order, so every fetch can affect later results. The queue size never changes: the fetched element becomes the most recently used element at the back while all other elements preserve their relative order.
