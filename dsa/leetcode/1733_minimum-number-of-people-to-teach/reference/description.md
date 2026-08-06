## Description

On a social network consisting of `m` users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer `n`, an array `languages`, and an array `friendships` where:

<ul>
	<li>There are `n` languages numbered `1` through `n`,</li>
	<li>`languages[i]` is the set of languages the `i^​​​​​​th`​​​​ user knows, and</li>
	<li>`friendships[i] = [u_​​​​​​i​​​, v_​​​​​​i]` denotes a friendship between the users `u^​​​​​_​​​​​​i`​​​​​ and `v_i`.</li>
</ul>

You can choose **one** language and teach it to some users so that all friends can communicate with each other. Return <i data-stringify-type="italic">the</i> ***minimum** *<i data-stringify-type="italic">number of users you need to teach.</i>

Note that friendships are not transitive, meaning if `x` is a friend of `y` and `y` is a friend of `z`, this doesn't guarantee that `x` is a friend of `z`.
