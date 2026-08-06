## Description

You are given a binary string `binary` consisting of only `0`'s or `1`'s. You can apply each of the following operations any number of times:

<ul>
	<li>Operation 1: If the number contains the substring `"00"`, you can replace it with `"10"`.

	<ul>
		<li>For example, `"<u>00</u>010" -> "<u>10</u>010`"</li>
	</ul>
	</li>
	<li>Operation 2: If the number contains the substring `"10"`, you can replace it with `"01"`.
	<ul>
		<li>For example, `"000<u>10</u>" -> "000<u>01</u>"`</li>
	</ul>
	</li>
</ul>

*Return the **maximum binary string** you can obtain after any number of operations. Binary string `x` is greater than binary string `y` if `x`'s decimal representation is greater than `y`'s decimal representation.*
