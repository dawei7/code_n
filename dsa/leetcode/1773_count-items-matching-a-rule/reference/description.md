## Description

You are given an array `items`, where each `items[i] = [type_i, color_i, name_i]` describes the type, color, and name of the `i^th` item. You are also given a rule represented by two strings, `ruleKey` and `ruleValue`.

The `i^th` item is said to match the rule if **one** of the following is true:

<ul>
	<li>`ruleKey == "type"` and `ruleValue == type_i`.</li>
	<li>`ruleKey == "color"` and `ruleValue == color_i`.</li>
	<li>`ruleKey == "name"` and `ruleValue == name_i`.</li>
</ul>

Return *the number of items that match the given rule*.
