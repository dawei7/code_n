## Description

You are given a string `s` that contains some bracket pairs, with each pair containing a **non-empty** key.

<ul>
	<li>For example, in the string `"(name)is(age)yearsold"`, there are **two** bracket pairs that contain the keys `"name"` and `"age"`.</li>
</ul>

You know the values of a wide range of keys. This is represented by a 2D string array `knowledge` where each `knowledge[i] = [key_i, value_i]` indicates that key `key_i` has a value of `value_i`.

You are tasked to evaluate **all** of the bracket pairs. When you evaluate a bracket pair that contains some key `key_i`, you will:

<ul>
	<li>Replace `key_i` and the bracket pair with the key's corresponding `value_i`.</li>
	<li>If you do not know the value of the key, you will replace `key_i` and the bracket pair with a question mark `"?"` (without the quotation marks).</li>
</ul>

Each key will appear at most once in your `knowledge`. There will not be any nested brackets in `s`.

Return *the resulting string after evaluating **all** of the bracket pairs.*
