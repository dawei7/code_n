## Description

You are given an *absolute* path for a Unix-style file system, which always begins with a slash `'/'`. Your task is to transform this absolute path into its **simplified canonical path**.

The *rules* of a Unix-style file system are as follows:

<ul>
	<li>A single period `'.'` represents the current directory.</li>
	<li>A double period `'..'` represents the previous/parent directory.</li>
	<li>Multiple consecutive slashes such as `'//'` and `'///'` are treated as a single slash `'/'`.</li>
	<li>Any sequence of periods that does **not match** the rules above should be treated as a **valid directory or** **file ****name**. For example, `'...' `and `'....'` are valid directory or file names.</li>
</ul>

The simplified canonical path should follow these *rules*:

<ul>
	<li>The path must start with a single slash `'/'`.</li>
	<li>Directories within the path must be separated by exactly one slash `'/'`.</li>
	<li>The path must not end with a slash `'/'`, unless it is the root directory.</li>
	<li>The path must not have any single or double periods (`'.'` and `'..'`) used to denote current or parent directories.</li>
</ul>

Return the **simplified canonical path**.
