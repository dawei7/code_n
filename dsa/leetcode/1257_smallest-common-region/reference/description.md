## Description

The input contains lists of regions. In each list, the first region directly contains every region that follows it. These direct relationships form a hierarchy: whenever `x` directly contains `y` and `y` directly contains `z`, `x` indirectly contains `z` and every region below `z` as well.

A containing region is considered at least as large as any region inside it, whether that containment is direct or indirect. Each region also contains itself. Consequently, one of the queried regions can be the answer when it contains the other.

Given the distinct names `region1` and `region2`, return the smallest region that contains both. The input guarantees that such a region exists.
