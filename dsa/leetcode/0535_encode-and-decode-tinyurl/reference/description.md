## Description

<blockquote>Note: This is a companion problem to the <a href="https://leetcode.com/discuss/interview-question/system-design/" target="_blank">System Design</a> problem: <a href="https://leetcode.com/discuss/interview-question/124658/Design-a-URL-Shortener-(-TinyURL-)-System/" target="_blank">Design TinyURL</a>.</blockquote>

TinyURL is a URL shortening service where you enter a URL such as `https://leetcode.com/problems/design-tinyurl` and it returns a short URL such as `http://tinyurl.com/4e9iAk`. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the `Solution` class:

<ul>
	<li>`Solution()` Initializes the object of the system.</li>
	<li>`String encode(String longUrl)` Returns a tiny URL for the given `longUrl`.</li>
	<li>`String decode(String shortUrl)` Returns the original long URL for the given `shortUrl`. It is guaranteed that the given `shortUrl` was encoded by the same object.</li>
</ul>
