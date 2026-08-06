## Description

A village has $n$ houses labeled from `1` through `n`, and every house must be supplied with water. At house $i$, one option is to build a well there for cost `wells[i - 1]`. A house may instead receive water through pipes from any house that has access to a well, including through a chain of other houses.

Each entry `pipes[j] = [house1_j, house2_j, cost_j]` offers a bidirectional connection between the two named houses for `cost_j`. Several offers may connect the same pair of houses at different prices.

Choose any combination of wells and offered pipes. Return the minimum total cost that gives every house access to water.
