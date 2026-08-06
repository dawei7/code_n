## Description

Table: `user_content`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| content_id  | int     |
| content_text| varchar |
+-------------+---------+
content_id is the unique key for this table.
Each row contains a unique ID and the corresponding text content.

```

Write a solution to transform the text in the `content_text` column by applying the following rules:

<ul>
	<li>Convert the **first letter** of each word to **uppercase** and the **remaining** letters to **lowercase**</li>
	<li>Special handling for words containing special characters:
	<ul>
		<li>For words connected with a hyphen `-`, **both parts** should be **capitalized** (**e.g.**, top-rated → Top-Rated)</li>
	</ul>
	</li>
	<li>All other **formatting** and **spacing** should remain **unchanged**</li>
</ul>

Return *the result table that includes both the original `content_text` and the modified text following the above rules*.

The result format is in the following example.
