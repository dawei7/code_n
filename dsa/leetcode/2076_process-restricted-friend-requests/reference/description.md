## Description

You are given an integer `n` indicating the number of people in a network. Each person is labeled from `0` to `n - 1`.

You are also given a **0-indexed** 2D integer array `restrictions`, where `restrictions[i] = [x_i, y_i]` means that person `x_i` and person `y_i` **cannot **become **friends**,** **either **directly** or **indirectly** through other people.

Initially, no one is friends with each other. You are given a list of friend requests as a **0-indexed** 2D integer array `requests`, where `requests[j] = [u_j, v_j]` is a friend request between person `u_j` and person `v_j`.

A friend request is **successful **if `u_j` and `v_j` can be **friends**. Each friend request is processed in the given order (i.e., `requests[j]` occurs before `requests[j + 1]`), and upon a successful request, `u_j` and `v_j` **become direct friends** for all future friend requests.

Return *a **boolean array** *`result`,* where each *`result[j]`* is *`true`* if the *`j^th`* friend request is **successful** or *`false`* if it is not*.

**Note:** If `u_j` and `v_j` are already direct friends, the request is still **successful**.
