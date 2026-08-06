## Description

An undirected graph of `n` nodes is defined by `edgeList`, where `edgeList[i] = [u_i, v_i, dis_i]` denotes an edge between nodes `u_i` and `v_i` with distance `dis_i`. Note that there may be **multiple** edges between two nodes.

Given an array `queries`, where `queries[j] = [p_j, q_j, limit_j]`, your task is to determine for each `queries[j]` whether there is a path between `p_j` and `q_j`_ such that each edge on the path has a distance **strictly less than** `limit_j` .

Return *a **boolean array** *`answer`*, where *`answer.length == queries.length` *and the *`j^th` *value of *`answer` *is *`true`* if there is a path for *`queries[j]`* is *`true`*, and *`false`* otherwise*.
