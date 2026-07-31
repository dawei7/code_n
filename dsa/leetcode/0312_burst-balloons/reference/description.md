## Description

There are `n` balloons indexed from `0` to `n - 1`, and `nums[i]` is the number painted on balloon $i$. Burst every balloon in an order of your choice.

When the current balloon $i$ is burst, it earns `nums[i - 1] * nums[i] * nums[i + 1]` coins using its then-adjacent surviving neighbors. If either neighbor is outside the current array, treat that side as a balloon painted with `1`.

Return the maximum total coins obtainable by choosing the burst order wisely.
