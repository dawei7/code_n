## Description

Given four integers `length`, `width`, `height`, and `mass`, representing the dimensions and mass of a box, respectively, return *a string representing the **category** of the box*.

<ul>
	<li>The box is `"Bulky"` if:

	<ul>
		<li>**Any** of the dimensions of the box is greater or equal to `10^4`.</li>
		<li>Or, the **volume** of the box is greater or equal to `10^9`.</li>
	</ul>
	</li>
	<li>If the mass of the box is greater or equal to `100`, it is `"Heavy".`</li>
	<li>If the box is both `"Bulky"` and `"Heavy"`, then its category is `"Both"`.</li>
	<li>If the box is neither `"Bulky"` nor `"Heavy"`, then its category is `"Neither"`.</li>
	<li>If the box is `"Bulky"` but not `"Heavy"`, then its category is `"Bulky"`.</li>
	<li>If the box is `"Heavy"` but not `"Bulky"`, then its category is `"Heavy"`.</li>
</ul>

**Note** that the volume of the box is the product of its length, width and height.
