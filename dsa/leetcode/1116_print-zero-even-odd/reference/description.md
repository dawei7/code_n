## Description

You have a function `printNumber` that can be called with an integer parameter and prints it to the console.

<ul>
	<li>For example, calling `printNumber(7)` prints `7` to the console.</li>
</ul>

You are given an instance of the class `ZeroEvenOdd` that has three functions: `zero`, `even`, and `odd`. The same instance of `ZeroEvenOdd` will be passed to three different threads:

<ul>
	<li>**Thread A:** calls `zero()` that should only output `0`'s.</li>
	<li>**Thread B:** calls `even()` that should only output even numbers.</li>
	<li>**Thread C:** calls `odd()` that should only output odd numbers.</li>
</ul>

Modify the given class to output the series `"010203040506..."` where the length of the series must be `2n`.

Implement the `ZeroEvenOdd` class:

<ul>
	<li>`ZeroEvenOdd(int n)` Initializes the object with the number `n` that represents the numbers that should be printed.</li>
	<li>`void zero(printNumber)` Calls `printNumber` to output one zero.</li>
	<li>`void even(printNumber)` Calls `printNumber` to output one even number.</li>
	<li>`void odd(printNumber)` Calls `printNumber` to output one odd number.</li>
</ul>
