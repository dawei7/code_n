## Description

Table: $\text{user}_{content}$

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

Write a solution to transform the text in the $\text{content}_{text}$ column by applying the following rules:

- Convert the **first letter** of each word to **uppercase** and the **remaining** letters to **lowercase**

- Special handling for words containing special characters:

		<li>For words connected with a hyphen `-`, **both parts** should be **capitalized** (**e.g.**, top-rated → Top-Rated)

	</li>
- All other **formatting** and **spacing** should remain **unchanged**

Return *the result table that includes both the original $\text{content}_{text}$ and the modified text following the above rules*.

The result format is in the following example.

**Example:**

<div class="example-block">
**Input:**

user_content table:

```
+------------+---------------------------------+
| content_id | content_text                    |
+------------+---------------------------------+
| 1          | hello world of SQL              |
| 2          | the QUICK-brown fox             |
| 3          | modern-day DATA science         |
| 4          | web-based FRONT-end development |
+------------+---------------------------------+
```

**Output:**

```
+------------+---------------------------------+---------------------------------+
| content_id | original_text                   | converted_text                  |
+------------+---------------------------------+---------------------------------+
| 1          | hello world of SQL              | Hello World Of Sql              |
| 2          | the QUICK-brown fox             | The Quick-Brown Fox             |
| 3          | modern-day DATA science         | Modern-Day Data Science         |
| 4          | web-based FRONT-end development | Web-Based Front-End Development |
+------------+---------------------------------+---------------------------------+
```

**Explanation:**

- For content_id = 1:

		<li>Each word's first letter is capitalized: "Hello World Of Sql"

	</li>
- For content_id = 2:

		<li>Contains the hyphenated word "QUICK-brown" which becomes "Quick-Brown"

- Other words follow normal capitalization rules

	</li>
- For content_id = 3:

		<li>Hyphenated word "modern-day" becomes "Modern-Day"

- "DATA" is converted to "Data"

	</li>
- For content_id = 4:

		<li>Contains two hyphenated words: "web-based" → "Web-Based"

- And "FRONT-end" → "Front-End"

	</li>

</div>
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Constraints

- $\text{context}_{text}$ contains only English letters, and the characters in the list $['\', ' ', '@', '-', '/', '^', ',']$