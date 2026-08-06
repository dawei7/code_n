## Description

You are given an integer array `score` of size `n`, where `score[i]` is the score of the `i^th` athlete in a competition. All the scores are guaranteed to be **unique**.

The athletes are **placed** based on their scores, where the `1^st` place athlete has the highest score, the `2^nd` place athlete has the `2^nd` highest score, and so on. The placement of each athlete determines their rank:

<ul>
	<li>The `1^st` place athlete's rank is `"Gold Medal"`.</li>
	<li>The `2^nd` place athlete's rank is `"Silver Medal"`.</li>
	<li>The `3^rd` place athlete's rank is `"Bronze Medal"`.</li>
	<li>For the `4^th` place to the `n^th` place athlete, their rank is their placement number (i.e., the `x^th` place athlete's rank is `"x"`).</li>
</ul>

Return an array `answer` of size `n` where `answer[i]` is the **rank** of the `i^th` athlete.
