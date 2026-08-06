## Description

There is a computer that can run an unlimited number of tasks **at the same time**. You are given a 2D integer array `tasks` where `tasks[i] = [start_i, end_i, duration_i]` indicates that the `i^th` task should run for a total of `duration_i` seconds (not necessarily continuous) within the **inclusive** time range `[start_i, end_i]`.

You may turn on the computer only when it needs to run a task. You can also turn it off if it is idle.

Return *the minimum time during which the computer should be turned on to complete all tasks*.
