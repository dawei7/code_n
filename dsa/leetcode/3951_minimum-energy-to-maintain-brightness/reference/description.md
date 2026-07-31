## Description

There are `n` light bulbs in a line, indexed from `0` through `n - 1`. You are also given a required `brightness` and a collection of inclusive time `intervals`. At every integer time contained in at least one interval, the lighting requirement must be met.

At any time unit, each bulb may be independently on or off. A bulb that is on illuminates its own position and either adjacent position that exists. Total illumination is the number of distinct positions illuminated; a position reached by several bulbs is still counted only once.

During every covered time unit, total illumination must be at least `brightness`. All bulbs may be off at uncovered times. Keeping one bulb on for one time unit costs one unit of energy.

Return the minimum total energy needed across all required time units.
