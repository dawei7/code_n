## Description

You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times.

<ul>
	<li>Remove substring `"ab"` and gain `x` points.

	<ul>
		<li>For example, when removing `"ab"` from `"c<u>ab</u>xbae"` it becomes `"cxbae"`.</li>
	</ul>
	</li>
	<li>Remove substring `"ba"` and gain `y` points.
	<ul>
		<li>For example, when removing `"ba"` from `"cabx<u>ba</u>e"` it becomes `"cabxe"`.</li>
	</ul>
	</li>
</ul>

Return *the maximum points you can gain after applying the above operations on* `s`.
