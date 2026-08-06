## Description

There is an infrastructure of `n` cities with some number of `roads` connecting these cities. Each `roads[i] = [a_i, b_i]` indicates that there is a bidirectional road between cities `a_i` and `b_i`.

The **network rank*** *of **two different cities** is defined as the total number of **directly** connected roads to **either** city. If a road is directly connected to both cities, it is only counted **once**.

The **maximal network rank **of the infrastructure is the **maximum network rank** of all pairs of different cities.

Given the integer `n` and the array `roads`, return *the **maximal network rank** of the entire infrastructure*.
