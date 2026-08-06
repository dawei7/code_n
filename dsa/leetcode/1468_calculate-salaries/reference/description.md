## Description

Calculate every employee's salary after taxes, rounding the adjusted amount to
the nearest integer.

Each company has one tax rate, selected from the maximum employee salary in
that company:

- the rate is $0\%$ when the maximum is less than $1000$;
- the rate is $24\%$ when the maximum is in the inclusive range
  $[1000,10000]$;
- the rate is $49\%$ when the maximum is greater than $10000$.

Return the result rows in any order. The example shows the required columns and
format.
