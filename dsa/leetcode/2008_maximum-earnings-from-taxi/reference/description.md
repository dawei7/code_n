## Description

There are `n` points on a road you are driving your taxi on. The `n` points on the road are labeled from `1` to `n` in the direction you are going, and you want to drive from point `1` to point `n` to make money by picking up passengers. You cannot change the direction of the taxi.

The passengers are represented by a **0-indexed** 2D integer array `rides`, where `rides[i] = [start_i, end_i, tip_i]` denotes the `i^th` passenger requesting a ride from point `start_i` to point `end_i` who is willing to give a `tip_i` dollar tip.

For** each **passenger `i` you pick up, you **earn** `end_i - start_i + tip_i` dollars. You may only drive **at most one **passenger at a time.

Given `n` and `rides`, return *the **maximum** number of dollars you can earn by picking up the passengers optimally.*

**Note:** You may drop off a passenger and pick up a different passenger at the same point.
