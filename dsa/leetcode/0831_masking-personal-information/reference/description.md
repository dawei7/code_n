## Description

You are given a personal information string `s`, representing either an **email address** or a **phone number**. Return *the **masked** personal information using the below rules*.

<u>**Email address:**</u>

An email address is:

<ul>
	<li>A **name** consisting of **at least** two uppercase and lowercase English letters, followed by</li>
	<li>The `'@'` symbol, followed by</li>
	<li>The **domain** consisting of uppercase and lowercase English letters with a dot `'.'` somewhere in the middle (not the first or last character).</li>
</ul>

To mask an email:

<ul>
	<li>The uppercase letters in the **name** and **domain** must be converted to lowercase letters.</li>
	<li>The middle letters of the **name** (i.e., all but the first and last letters) must be replaced by 5 asterisks `"*****"`.</li>
</ul>

<u>**Phone number:**</u>

A phone number is formatted as follows:

<ul>
	<li>The phone number contains 10-13 digits.</li>
	<li>The last 10 digits make up the **local number**.</li>
	<li>The remaining 0-3 digits, in the beginning, make up the **country code**.</li>
	<li>**Separation characters** from the set `{'+', '-', '(', ')', ' '}` separate the above digits in some way.</li>
</ul>

To mask a phone number:

<ul>
	<li>Remove all **separation characters**.</li>
	<li>The masked phone number should have the form:
	<ul>
		<li>`"***-***-XXXX"` if the country code has 0 digits.</li>
		<li>`"+*-***-***-XXXX"` if the country code has 1 digit.</li>
		<li>`"+**-***-***-XXXX"` if the country code has 2 digits.</li>
		<li>`"+***-***-***-XXXX"` if the country code has 3 digits.</li>
	</ul>
	</li>
	<li>`"XXXX"` is the last 4 digits of the **local number**.</li>
</ul>
