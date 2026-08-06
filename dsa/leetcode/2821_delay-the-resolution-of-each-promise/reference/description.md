## Description

You receive an array named `functions`. Each element is a function that returns a promise. You also receive a nonnegative duration `ms`, measured in milliseconds.

Create a new array of functions in the same order. Calling one of the new functions must call its corresponding original function, wait for that source promise to settle, and then postpone the same outcome for another `ms` milliseconds. A fulfilled source promise must eventually fulfill with its original value; a rejected source promise must eventually reject with its original reason.

Constructing the array must not eagerly call the source functions. Each returned function represents an independent delayed invocation.
