## Description

You are given a **0-indexed** binary string `s` which represents the types of buildings along a street where:

<ul>
	<li>`s[i] = '0'` denotes that the `i^th` building is an office and</li>
	<li>`s[i] = '1'` denotes that the `i^th` building is a restaurant.</li>
</ul>

As a city official, you would like to **select** 3 buildings for random inspection. However, to ensure variety, **no two consecutive** buildings out of the **selected** buildings can be of the same type.

<ul>
	<li>For example, given `s = "0<u>**0**</u>1<u>**1**</u>0<u>**1**</u>"`, we cannot select the `1^st`, `3^rd`, and `5^th` buildings as that would form `"0**<u>11</u>**"` which is **not** allowed due to having two consecutive buildings of the same type.</li>
</ul>

Return *the **number of valid ways** to select 3 buildings.*
