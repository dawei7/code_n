## Description

Given a string `s`, determine if it is **valid**.

A string `s` is **valid** if, starting with an empty string `t = ""`, you can **transform **`t`** into **`s` after performing the following operation **any number of times**:

<ul>
	<li>Insert string `"abc"` into any position in `t`. More formally, `t` becomes `t_left + "abc" + t_right`, where `t == t_left + t_right`. Note that `t_left` and `t_right` may be **empty**.</li>
</ul>

Return `true` *if *`s`* is a **valid** string, otherwise, return* `false`.
