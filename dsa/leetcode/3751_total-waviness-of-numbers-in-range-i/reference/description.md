## Description

You are given two integers `num1` and `num2` defining the inclusive range `[num1,num2]`.

The **waviness** of one number is the total number of its decimal digits that are peaks or valleys:

- An interior digit is a **peak** when it is strictly greater than each of its two immediate neighbors.
- An interior digit is a **valley** when it is strictly less than each of its two immediate neighbors.
- The first and final digits have only one neighbor, so they can never be counted as either.
- Consequently, every number with fewer than three decimal digits has waviness `0`.

Compute the waviness of every integer in the inclusive range and return their total sum.
