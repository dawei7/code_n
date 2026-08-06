## Description

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm for `myAtoi(string s)` is as follows:

<ol>
	<li>**Whitespace**: Ignore any leading whitespace (`" "`).</li>
	<li>**Signedness**: Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.</li>
	<li>**Conversion**: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.</li>
	<li>**Rounding**: If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then round the integer to remain in the range. Specifically, integers less than `-2^31` should be rounded to `-2^31`, and integers greater than `2^31 - 1` should be rounded to `2^31 - 1`.</li>
</ol>

Return the integer as the final result.
