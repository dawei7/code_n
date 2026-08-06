## Description

You are given two integer arrays, `skill` and `<font face="monospace">mana</font>`, of length `n` and `m`, respectively.

In a laboratory, `n` wizards must brew `m` potions *in order*. Each potion has a mana capacity `mana[j]` and **must** pass through **all** the wizards sequentially to be brewed properly. The time taken by the `i^th` wizard on the `j^th` potion is `time_ij = skill[i] * mana[j]`.

Since the brewing process is delicate, a potion **must** be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be *synchronized* so that each wizard begins working on a potion **exactly** when it arrives. ​

Return the **minimum** amount of time required for the potions to be brewed properly.
