## Description

Mario travels forward along a two-lane freeway. At mile `i`, driving in lane 1 changes his coin total by `lane1[i]`, while driving in lane 2 changes it by `lane2[i]`; positive values award coins and negative values charge a toll. He may enter at any mile and leave after any later visited mile, but the trip must include at least one mile and all visited indices must be contiguous.

Mario enters in lane 1 and may switch between the two lanes at most twice while moving forward. A switch may happen immediately after entering, so the first visited mile can effectively be in lane 2, and it may also happen just before he exits. Return the largest total obtainable over every valid entry point, exit point, and sequence of no more than two lane switches.
