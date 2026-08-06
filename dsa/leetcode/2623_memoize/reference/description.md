## Description

Given a function `fn`, return a **memoized** version of that function.

A **memoized **function is a function that will never be called twice with the same inputs. Instead it will return a cached value.

You can assume there are **3 **possible input functions: `sum`**, **`fib`**, **and `factorial`**.**

<ul>
	<li>`sum`** **accepts two integers `a` and `b` and returns `a + b`. Assume that if a value has already been cached for the arguments `(b, a)` where `a != b`, it cannot be used for the arguments `(a, b)`. For example, if the arguments are `(3, 2)` and `(2, 3)`, two separate calls should be made.</li>
	<li>`fib`** **accepts a single integer `n` and returns `1` if <font face="monospace">`n <= 1` </font>or<font face="monospace"> `fib(n - 1) + fib(n - 2)` </font>otherwise.</li>
	<li>`factorial` accepts a single integer `n` and returns `1` if `n <= 1` or `factorial(n - 1) * n` otherwise.</li>
</ul>
