## Description

Given an asynchronous function `fn` and a time `t` in milliseconds, return a new **time limited** version of the input function. `fn` takes arguments provided to the **time limited **function.

The **time limited** function should follow these rules:

<ul>
	<li>If the `fn` completes within the time limit of `t` milliseconds, the **time limited** function should resolve with the result.</li>
	<li>If the execution of the `fn` exceeds the time limit, the **time limited** function should reject with the string `"Time Limit Exceeded"`.</li>
</ul>
