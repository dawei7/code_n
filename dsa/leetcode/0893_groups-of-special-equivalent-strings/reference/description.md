## Description

You are given an array of strings of the same length `words`.

In one **move**, you can swap any two even indexed characters or any two odd indexed characters of a string `words[i]`.

Two strings `words[i]` and `words[j]` are **special-equivalent** if after any number of moves, `words[i] == words[j]`.

<ul>
	<li>For example, `words[i] = "zzxy"` and `words[j] = "xyzz"` are **special-equivalent** because we may make the moves `"zzxy" -> "xzzy" -> "xyzz"`.</li>
</ul>

A **group of special-equivalent strings** from `words` is a non-empty subset of words such that:

<ul>
	<li>Every pair of strings in the group are special equivalent, and</li>
	<li>The group is the largest size possible (i.e., there is not a string `words[i]` not in the group such that `words[i]` is special-equivalent to every string in the group).</li>
</ul>

Return *the number of **groups of special-equivalent strings** from *`words`.
