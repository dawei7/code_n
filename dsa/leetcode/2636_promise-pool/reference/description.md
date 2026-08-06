## Description

Given an ordered array of asynchronous functions and a positive pool limit `n`, return a promise that resolves after every function's promise has resolved. At no instant may more than `n` produced promises remain pending.

Start as many functions as the limit allows. Functions must begin in array order: `functions[i]` starts before `functions[i + 1]`. Whenever one pending promise resolves, immediately start the next unstarted function if one exists, keeping the pool as full as possible until the input is exhausted. When the final pending promise resolves, the returned promise must resolve as well.

All input functions are guaranteed not to reject. The resolving value of the returned promise is unrestricted.
