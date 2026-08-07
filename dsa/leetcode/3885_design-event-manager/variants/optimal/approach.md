## General
Given an initial list of events, where each event has a unique `eventId` and a `priority`, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((E+Q) log(E+Q))$ — Operation count bound.
- **Space Complexity**: $O(E+Q)$ — Auxiliary memory allocation bound.
