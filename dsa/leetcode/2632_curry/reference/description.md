## Description

Given a JavaScript function `fn`, return a curried version of it. The returned function may receive any number of the original parameters at a time, including none. Until enough parameters have been collected, a call returns another curried function; once the original arity is reached, it returns the value that `fn` would produce from all collected arguments in order.

For example, if `sum` expects three arguments, `csum(1)(2)(3)`, `csum(1, 2)(3)`, `csum(1)(2, 3)`, and `csum(1, 2, 3)` must all behave like `sum(1, 2, 3)`. Empty calls do not change the collected sequence. If `fn.length` is zero, invoking the curried function with no arguments must immediately evaluate `fn`.
