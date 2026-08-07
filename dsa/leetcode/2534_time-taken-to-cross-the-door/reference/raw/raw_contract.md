## Function Contract

**Inputs**

- `arrival`: A non-decreasing list of $n$ non-negative integers ($1 \le n \le 10^5$, $0 \le \text{arrival}[i] \le n$).
- `state`: A list of $n$ integers aligned with `arrival`, where `0` means enter and `1` means exit.

**Return value**

Return an array `answer` of length $n$ where `answer[i]` is the exact second person $i$ crosses the door.
