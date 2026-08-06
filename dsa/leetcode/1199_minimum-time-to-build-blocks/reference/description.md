## Description

You are given a list `blocks`, where `blocks[i] = t` means that the $i$th block takes `t` time units to construct. Exactly one worker is required to build any one block.

A worker has two choices. The worker may split into two workers, increasing the total worker count by one, or may build one block and then go home. Each choice consumes time.

Splitting one worker costs `split` time units. When multiple workers split concurrently, those operations run in parallel, so that round still adds only `split` to the elapsed time.

There is exactly one worker initially. Return the minimum elapsed time required to finish every block.
