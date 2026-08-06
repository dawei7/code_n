## Description

You are given an integer `num`. You know that Bob will sneakily **remap** one of the `10` possible digits (`0` to `9`) to another digit.

Return *the difference between the maximum and minimum values Bob can make by remapping **exactly** **one** digit in *`num`.

**Notes:**

<ul>
	<li>When Bob remaps a digit <font face="monospace">d1</font> to another digit <font face="monospace">d2</font>, Bob replaces all occurrences of `d1` in `num` with `d2`.</li>
	<li>Bob can remap a digit to itself, in which case `num` does not change.</li>
	<li>Bob can remap different digits for obtaining minimum and maximum values respectively.</li>
	<li>The resulting number after remapping can contain leading zeroes.</li>
</ul>
