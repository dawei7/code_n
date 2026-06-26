# Shortest Common Supersequence

| | |
|---|---|
| **ID** | `dp_20` |
| **Category** | dynamic |
| **Complexity (required)** | $O(M * N)$ Time, $O(M * N)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/) |

## Problem statement

Gegeben sind zwei Strings `str1` und `str2`. Gesucht ist der kürzeste String, der sowohl `str1` als auch `str2` als Teilfolgen (Subsequences) enthält. Falls es mehrere gültige Strings gibt, kann jeder davon zurückgegeben werden.
Ein String `S` ist eine Supersequence eines Strings `A`, wenn `A` eine Teilfolge von `S` ist.

**Input:** Zwei Strings `str1` (Länge M) und `str2` (Länge N).
**Output:** Ein String, der die kürzeste gemeinsame Supersequence repräsentiert. (Manchmal wird nur nach der Länge gefragt).

## When to use it

- Um absolute Beherrschung der Longest Common Subsequence (LCS) Matrix zu demonstrieren.
- Dieses Problem ist das direkte Spiegelbild von LCS. Anstatt die Schnittmenge zu finden, konstruieren wir die optimale Vereinigung!

## Approach

**Die mathematische Reduktion:**
Wenn wir `str1` und `str2` einfach hintereinanderfügen, beträgt die Länge M + N. Dies ist zwar eine gültige Supersequence, aber nicht die kürzeste.
Warum? Weil alle Zeichen, die beide Strings *in exakt derselben Reihenfolge gemeinsam haben* (ihre Longest Common Subsequence), doppelt gezählt werden!
Um die Supersequence so kurz wie möglich zu halten, müssen wir die LCS überlappen lassen.
Die Länge der Shortest Common Supersequence (SCS) ist mathematisch exakt definiert als: `M + N - LCS(str1, str2)`.

**Konstruktion des Strings:**
Wenn die Aufgabenstellung den tatsächlichen String verlangt, können wir die $O(N)$ Platzoptimierung für LCS nicht verwenden. Wir müssen die vollständige M x N DP-Tabelle aufbauen.
Sobald die Tabelle erstellt ist, beginnen wir an der unteren rechten Ecke `(m, n)` und verfolgen den Pfad zurück zu `(0, 0)`:
1. Wenn `str1[i-1] == str2[j-1]`: Dieses Zeichen ist Teil der LCS! Wir müssen es nur EINMAL schreiben. Wir fügen es unserem Ergebnis hinzu und bewegen uns diagonal nach oben links `(i-1, j-1)`.
2. Wenn sie NICHT übereinstimmen: Wir müssen das Zeichen einfügen, das zum größeren LCS-Pfad führt!
   - Wenn `dp[i-1][j] > dp[i][j-1]`, bedeutet dies, dass der optimale Pfad von oben kam. Wir fügen `str1[i-1]` hinzu und bewegen uns NACH OBEN.
   - Andernfalls kam der optimale Pfad von links. Wir fügen `str2[j-1]` hinzu und bewegen uns NACH LINKS.
3. Wenn wir den oberen Rand erreichen (`i=0`), hängen wir den Rest von `str2` an. Wenn wir den linken Rand erreichen (`j=0`), hängen wir den Rest von `str1` an.
4. Der resultierende String wird rückwärts aufgebaut, daher muss er am Ende umgekehrt werden!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_20: Shortest Common Supersequence (Length).

The shortest string that has both s1 and s2 as subsequences.
The length is n1 + n2 - LCS(s1, s2). Compute LCS first, then
combine the lengths.
"""


def solve(s1, s2, n1, n2):
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    lcs = dp[n1][n2]
    return n1 + n2 - lcs
```

</details>

## Walk-through

`str1 = "abac"`, `str2 = "cab"`. M=4, N=3.
LCS ist `"ab"`.
Matrix `dp`:
```
    c a b
  0 0 0 0
a 0 0 1 1
b 0 0 1 2
a 0 0 1 2
c 0 1 1 2
```
Traceback beginnt bei `i=4, j=3` (`dp[4][3] = 2`).
1. `str1[3] ('c') != str2[2] ('b')`. `dp[3][3]`(2) > `dp[4][2]`(1). Gehe NACH OBEN. Hänge `'c'` an. `i=3, j=3`.
2. `str1[2] ('a') != str2[2] ('b')`. `dp[2][3]`(2) >= `dp[3][2]`(1). Gehe NACH OBEN. Hänge `'a'` an. `i=2, j=3`.
3. `str1[1] ('b') == str2[2] ('b')`. Match! Gehe DIAG. Hänge `'b'` an. `i=1, j=2`.
4. `str1[0] ('a') == str2[1] ('a')`. Match! Gehe DIAG. Hänge `'a'` an. `i=0, j=1`.
5. `i=0`, Schleife terminiert.
6. Leere verbleibendes `j`: `str2` hat noch `j=1` übrig. Hänge `str2[0] ('c')` an.
Umgekehrtes Ergebnis: `"cab"` -> `"b"` -> `"ab"` -> `"aab"` -> `"caab"`.
Moment, die Umkehrung von `['c', 'a', 'b', 'a', 'c']` ist `"cabac"`. ✓

## Complexity

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M * N)$ | $O(M * N)$ |
| **Durchschnittlicher Fall** | $O(M * N)$ | $O(M * N)$ |
| **Schlechtester Fall** | $O(M * N)$ | $O(M * N)$ |

Der Aufbau der LCS-Matrix benötigt strikt $O(M \times N)$ Zeit.
Das Zurückverfolgen (Traceback) benötigt maximal $O(M + N)$ Schritte. Die Gesamtlaufzeit beträgt $O(M \times N)$.
Der Platzbedarf ist strikt $O(M \times N)$ für die DP-Matrix. Wir können dies nicht auf $O(\min(M, N))$ optimieren, da das Traceback das gesamte historische Pfadgitter benötigt, um Routing-Entscheidungen zu treffen.

## Variants & optimizations

- **Shortest Common Supersequence mehrerer Strings:** Wenn Sie K Strings haben, wird der DP-Zustand K-dimensional ($O(N^K)$), was NP-schwer ist! Normalerweise approximiert man dies mithilfe von Greedy-Algorithmen oder Hamiltonpfaden auf Überlappungsgraphen.

## Real-world applications

- **Datenkompression:** Finden des kürzesten Befehlsbandes, das zwei verschiedene Ausgabesequenzen durch Verzweigungen an bestimmten Indizes erzeugen kann (ein fundamentales Konzept der Kolmogorov-Komplexität).

## Related algorithms in cOde(n)

- **[dp_04 - Longest Common Subsequence](dp_04_longest-common-subsequence.md)** — Die exakt gleiche Tabelle.
- **[dp_08 - Edit Distance](dp_08_edit-distance.md)** — Eine weitere String-DP, die ein vollständiges Matrix-Traceback erfordert, um die exakten Editier-Anweisungen auszugeben.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*