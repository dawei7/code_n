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

	- Convert the first letter of each word to uppercase

	- Keep all other letters in lowercase

	- Preserve all existing spaces

**Note**: There will be no special character in `content_text`.

Return *the result table that includes both the original `content_text` and the modified text where each word starts with a capital letter*.

The result format is in the following example.

**Example:**

<div class="example-block">
**Input:**

user_content table:

```
+------------+-----------------------------------+
| content_id | content_text                      |
+------------+-----------------------------------+
| 1          | hello world of SQL                |
| 2          | the QUICK brown fox               |
| 3          | data science AND machine learning |
| 4          | TOP rated programming BOOKS       |
+------------+-----------------------------------+
```

**Output:**

```
+------------+-----------------------------------+-----------------------------------+
| content_id | original_text                     | converted_text                    |
+------------+-----------------------------------+-----------------------------------+
| 1          | hello world of SQL                | Hello World Of Sql                |
| 2          | the QUICK brown fox               | The Quick Brown Fox               |
| 3          | data science AND machine learning | Data Science And Machine Learning |
| 4          | TOP rated programming BOOKS       | Top Rated Programming Books       |
+------------+-----------------------------------+-----------------------------------+
```

**Explanation:**

	- For content_id = 1:

		<li>Each word's first letter is capitalized: Hello World Of Sql

	</li>
	- For content_id = 2:

		<li>Original mixed-case text is transformed to title case: The Quick Brown Fox

	</li>
	- For content_id = 3:

		<li>The word AND is converted to "And": "Data Science And Machine Learning"

	</li>
	- For content_id = 4:

		<li>Handles word TOP rated correctly: Top Rated

		- Converts BOOKS from all caps to title case: Books

	</li>

</div>
