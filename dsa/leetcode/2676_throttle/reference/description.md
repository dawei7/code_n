## Description

Given a function `fn` and an interval `t` in milliseconds, return a throttled function. Its first invocation must call `fn` immediately. Until that invocation's $t$-millisecond window ends, further invocations must not execute `fn`; instead, retain only the most recently supplied arguments.

When the window ends, execute `fn` once with those latest pending arguments, if any. That trailing execution begins another full interval, during which new calls follow the same overwrite rule. If a window ends without a pending call, the next invocation may execute immediately.
