## Description

You are given a list of `preferences` for `n` friends, where `n` is always **even**.

For each person `i`, `preferences[i]` contains a list of friends **sorted** in the **order of preference**. In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from `0` to `n-1`.

All the friends are divided into pairs. The pairings are given in a list `pairs`, where `pairs[i] = [x_i, y_i]` denotes `x_i` is paired with `y_i` and `y_i` is paired with `x_i`.

However, this pairing may cause some of the friends to be unhappy. A friend `x` is unhappy if `x` is paired with `y` and there exists a friend `u` who is paired with `v` but:

<ul>
	<li>`x` prefers `u` over `y`, and</li>
	<li>`u` prefers `x` over `v`.</li>
</ul>

Return *the number of unhappy friends*.
