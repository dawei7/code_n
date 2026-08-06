## Description

Alice has an undirected tree with `n` nodes labeled from `0` to `n - 1`. The tree is represented as a 2D integer array `edges` of length `n - 1` where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

Alice wants Bob to find the root of the tree. She allows Bob to make several **guesses** about her tree. In one guess, he does the following:

<ul>
	<li>Chooses two **distinct** integers `u` and `v` such that there exists an edge `[u, v]` in the tree.</li>
	<li>He tells Alice that `u` is the **parent** of `v` in the tree.</li>
</ul>

Bob's guesses are represented by a 2D integer array `guesses` where `guesses[j] = [u_j, v_j]` indicates Bob guessed `u_j` to be the parent of `v_j`.

Alice being lazy, does not reply to each of Bob's guesses, but just says that **at least** `k` of his guesses are `true`.

Given the 2D integer arrays `edges`, `guesses` and the integer `k`, return *the **number of possible nodes** that can be the root of Alice's tree*. If there is no such tree, return `0`.
