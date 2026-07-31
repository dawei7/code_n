## Description

Design a logging system that receives messages together with their timestamps. Each distinct message may be printed no more than once within any ten-second waiting period: after a message is printed at time `t`, the next identical message may be printed starting at time `t + 10`.

Calls arrive in chronological order, and multiple messages can have the same timestamp.

Implement the `Logger` class with these operations:

- `Logger()` creates a new logger.
- `shouldPrintMessage(timestamp, message)` returns `true` when `message` may be printed at `timestamp`; otherwise it returns `false`.
