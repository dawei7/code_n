## Description

You are given an integer `numberOfUsers` representing the total number of users and an array `events` of size `n x 3`.

Each <code inline="">events[i]</code> can be either of the following two types:

<ol>
	<li>**Message Event:** `["MESSAGE", "timestamp_i", "mentions_string_i"]`

	<ul>
		<li>This event indicates that a set of users was mentioned in a message at `timestamp_i`.</li>
		<li>The `mentions_string_i` string can contain one of the following tokens:
		<ul>
			<li>`id<number>`: where `<number>` is an integer in range `[0,numberOfUsers - 1]`. There can be **multiple** ids separated by a single whitespace and may contain duplicates. This can mention even the offline users.</li>
			<li>`ALL`: mentions **all** users.</li>
			<li>`HERE`: mentions all **online** users.</li>
		</ul>
		</li>
	</ul>
	</li>
	<li>**Offline Event:** `["OFFLINE", "timestamp_i", "id_i"]`
	<ul>
		<li>This event indicates that the user `id_i` had become offline at `timestamp_i` for **60 time units**. The user will automatically be online again at time `timestamp_i + 60`.</li>
	</ul>
	</li>
</ol>

Return an array `mentions` where `mentions[i]` represents the number of mentions the user with id `i` has across all `MESSAGE` events.

All users are initially online, and if a user goes offline or comes back online, their status change is processed *before* handling any message event that occurs at the same timestamp.

**Note **that a user can be mentioned **multiple** times in a **single** message event, and each mention should be counted **separately**.
