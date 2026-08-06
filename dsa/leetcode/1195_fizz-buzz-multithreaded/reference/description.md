## Description

You have the four functions:

<ul>
	<li>`printFizz` that prints the word `"fizz"` to the console,</li>
	<li>`printBuzz` that prints the word `"buzz"` to the console,</li>
	<li>`printFizzBuzz` that prints the word `"fizzbuzz"` to the console, and</li>
	<li>`printNumber` that prints a given integer to the console.</li>
</ul>

You are given an instance of the class `FizzBuzz` that has four functions: `fizz`, `buzz`, `fizzbuzz` and `number`. The same instance of `FizzBuzz` will be passed to four different threads:

<ul>
	<li>**Thread A:** calls `fizz()` that should output the word `"fizz"`.</li>
	<li>**Thread B:** calls `buzz()` that should output the word `"buzz"`.</li>
	<li>**Thread C:** calls `fizzbuzz()` that should output the word `"fizzbuzz"`.</li>
	<li>**Thread D:** calls `number()` that should only output the integers.</li>
</ul>

Modify the given class to output the series `[1, 2, "fizz", 4, "buzz", ...]` where the `i^th` token (**1-indexed**) of the series is:

<ul>
	<li>`"fizzbuzz"` if `i` is divisible by `3` and `5`,</li>
	<li>`"fizz"` if `i` is divisible by `3` and not `5`,</li>
	<li>`"buzz"` if `i` is divisible by `5` and not `3`, or</li>
	<li>`i` if `i` is not divisible by `3` or `5`.</li>
</ul>

Implement the `FizzBuzz` class:

<ul>
	<li>`FizzBuzz(int n)` Initializes the object with the number `n` that represents the length of the sequence that should be printed.</li>
	<li>`void fizz(printFizz)` Calls `printFizz` to output `"fizz"`.</li>
	<li>`void buzz(printBuzz)` Calls `printBuzz` to output `"buzz"`.</li>
	<li>`void fizzbuzz(printFizzBuzz)` Calls `printFizzBuzz` to output `"fizzbuzz"`.</li>
	<li>`void number(printNumber)` Calls `printnumber` to output the numbers.</li>
</ul>
