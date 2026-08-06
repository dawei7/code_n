## Description

You are given a **0-indexed** 2D integer array `tires` where `tires[i] = [f_i, r_i]` indicates that the `i^th` tire can finish its `x^th` successive lap in `f_i * r_i^(x-1)` seconds.

<ul>
	<li>For example, if `f_i = 3` and `r_i = 2`, then the tire would finish its `1^st` lap in `3` seconds, its `2^nd` lap in `3 * 2 = 6` seconds, its `3^rd` lap in `3 * 2^2 = 12` seconds, etc.</li>
</ul>

You are also given an integer `changeTime` and an integer `numLaps`.

The race consists of `numLaps` laps and you may start the race with **any** tire. You have an **unlimited** supply of each tire and after every lap, you may **change** to any given tire (including the current tire type) if you wait `changeTime` seconds.

Return* the **minimum** time to finish the race.*
