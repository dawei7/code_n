## Description

You are given a string `<font face="monospace">caption</font>` representing the caption for a video.

The following actions must be performed **in order** to generate a **valid tag** for the video:

<ol>
	<li>
	**Combine all words** in the string into a single *camelCase string* prefixed with `'#'`. A *camelCase string* is one where the first letter of all words *except* the first one is capitalized. All characters after the first character in **each** word must be lowercase.

	</li>
	<li>
	**Remove** all characters that are not an English letter, **except** the first `'#'`.

	</li>
	<li>
	**Truncate** the result to a maximum of 100 characters.

	</li>
</ol>

Return the **tag** after performing the actions on `caption`.
