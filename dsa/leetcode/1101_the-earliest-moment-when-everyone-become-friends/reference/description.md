## Description

A social group contains `n` people labeled from `0` through `n - 1`. Each entry `logs[i] = [timestamp_i, x_i, y_i]` records the moment when people `x_i` and `y_i` become friends.

Friendship is symmetric: if one person is a friend of another, the relationship also holds in the opposite direction. Acquaintance is transitive as well. Two people are acquainted when they are direct friends or when a chain of friendships connects them through other people.

Return the earliest timestamp at which every person is acquainted with every other person. If the friendship events never connect the whole social group, return `-1`.
