## Description

A positive integer is called fair when its decimal representation contains the same number of even digits and odd digits. Digit parity is based on the digit itself, so `0` is even. Consequently, a fair integer must contain an even total number of digits.

Given a positive integer `n`, return the smallest fair integer greater than or equal to `n`. The answer may have more digits than `n`: if no fair integer remains at the current even length, or if `n` has odd length, the search continues at the next possible even digit length.
