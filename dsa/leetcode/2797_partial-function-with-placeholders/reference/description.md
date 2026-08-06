## Description

Given a function `fn` and an array of partially supplied arguments, create a new function. An entry equal to the string `"_"` is a placeholder rather than a fixed argument.

When the returned function is called, consume its arguments from left to right to replace the placeholders in the captured array. If call-time arguments remain after every placeholder is filled, append those values to the end. Invoke `fn` with the completed sequence passed as separate arguments and return its result.
