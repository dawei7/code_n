## Description

You are given two integers `memory1` and `memory2` representing the available memory in bits on two memory sticks. There is currently a faulty program running that consumes an increasing amount of memory every second.

At the `i^th` second (starting from 1), `i` bits of memory are allocated to the stick with **more available memory** (or from the first memory stick if both have the same available memory). If neither stick has at least `i` bits of available memory, the program **crashes**.

Return *an array containing *`[crashTime, memory1_crash, memory2_crash]`*, where *`crashTime`* is the time (in seconds) when the program crashed and *`memory1_crash`* and *`memory2_crash`* are the available bits of memory in the first and second sticks respectively*.
