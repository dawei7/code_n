## Description

In the classic **100 game**, two players alternate adding an integer from `1` through `10` to a shared running total. The first player to make the total reach or exceed `100` wins.

Now change the game so that an integer cannot be reused. More generally, the players draw without replacement from the common pool `1` through `maxChoosableInteger`, adding each chosen value to the running total. For example, the pool might contain `1` through `15` while the target remains `100`.

Given `maxChoosableInteger` and `desiredTotal`, return `true` if the first player can force a win. Return `false` otherwise. Both players choose optimally.
