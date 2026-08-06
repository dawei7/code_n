## Description

The positive integers in `sticks` give the lengths of a collection of sticks.

At each step, choose any two current sticks of lengths $x$ and $y$. Connecting them costs $x+y$ and replaces both selected sticks with one new stick of that same combined length. The new stick may participate in later connections.

Continue until only one stick remains. Return the smallest total connection cost achievable over all possible choices of pairs.
