## Description

Begin with one positive integer `n`. A split operation chooses a current integer `x` and replaces it with two positive integers `a` and `b` whose sum is `x`.

That operation contributes `a * b` to the running cost. Either newly created integer may be split again, and the costs of all performed operations are added together.

Continue until the original value has been divided into exactly `n` pieces, each equal to one. Determine the minimum total cost among all valid choices of split order and split sizes.
