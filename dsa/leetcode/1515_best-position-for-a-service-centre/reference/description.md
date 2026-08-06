## Description

A delivery company wants to build a new service center in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new center in a position such that **the sum of the euclidean distances to all customers is minimum**.

Given an array `positions` where `positions[i] = [x_i, y_i]` is the position of the `ith` customer on the map, return *the minimum sum of the euclidean distances* to all customers.

In other words, you need to choose the position of the service center `[x_centre, y_centre]` such that the following formula is minimized:

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/25/q4_edited.jpg" />
Answers within `10^-5` of the actual value will be accepted.
