## Description

A password is considered strong if the below conditions are all met:

<ul>
	<li>It has at least `6` characters and at most `20` characters.</li>
	<li>It contains at least **one lowercase** letter, at least **one uppercase** letter, and at least **one digit**.</li>
	<li>It does not contain three repeating characters in a row (i.e., `"B<u>**aaa**</u>bb0"` is weak, but `"B**<u>aa</u>**b<u>**a**</u>0"` is strong).</li>
</ul>

Given a string `password`, return *the minimum number of steps required to make `password` strong. if `password` is already strong, return `0`.*

In one step, you can:

<ul>
	<li>Insert one character to `password`,</li>
	<li>Delete one character from `password`, or</li>
	<li>Replace one character of `password` with another character.</li>
</ul>
