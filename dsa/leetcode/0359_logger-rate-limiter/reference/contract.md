## Function Contract

**Inputs**

- `operations`: In cOde(n), a chronological list of `["shouldPrintMessage", timestamp, message]` calls.

**Return value**

The app adapter returns one Boolean per call, in order. On LeetCode, construct `Logger` and invoke `shouldPrintMessage(int timestamp, string message)` directly; a rejected call does not change the most recent permitted-print time.
