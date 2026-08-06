## Description

Given an array of characters `chars`, compress it using the following algorithm:

Begin with an empty string `s`. For each group of **consecutive repeating characters** in `chars`:

<ul>
	<li>If the group's length is `1`, append the character to `s`.</li>
	<li>Otherwise, append the character followed by the group's length.</li>
</ul>

The compressed string `s` **should not be returned separately**, but instead, be stored **in the input character array `chars`**. Note that group lengths that are `10` or longer will be split into multiple characters in `chars`.

After you are done **modifying the input array,** return *the new length of the array*.

You must write an algorithm that uses only constant extra space.

**Note: **The characters in the array beyond the returned length do not matter and should be ignored.
