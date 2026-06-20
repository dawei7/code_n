# Kürzeste gemeinsame Supersequenz

| | |
|---|---|
| **ID** | `dp_20` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(M * N)$ Zeit, $O(M * N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Kürzeste gemeinsame Supersequenz](https://leetcode.com/problems/shortest-common-supersequence/) |

## Aufgabenstellung

Gegeben sind zwei Zeichenketten `str1` und `str2`. Gib die kürzeste Zeichenkette zurück, die sowohl `str1` als auch `str2` als Teilsequenzen enthält. Falls es mehrere gültige Zeichenketten gibt, gib eine beliebige davon zurück.
Eine Zeichenkette `S` ist eine Supersequenz der Zeichenkette `A`, wenn `A` eine Teilsequenz von `S` ist.

**Eingabe:** Zwei Zeichenketten `str1` (Länge M) und `str2` (Länge N).
**Ausgabe:** Eine Zeichenkette, die die kürzeste gemeinsame Überfolge darstellt. (Manchmal wird nur nach der Länge gefragt).

## Wann man es anwendet

- Um absolute Beherrschung der Matrix für die längste gemeinsame Teilfolge (LCS) zu demonstrieren.
- Dieses Problem ist das buchstäbliche Spiegelbild von LCS. Anstatt die Schnittmenge zu finden, konstruieren wir die optimale Vereinigung!

## Herangehensweise

**Die mathematische Reduktion:**
Wenn wir `str1` und `str2` einfach Ende an Ende zusammenfügen, beträgt die Länge M + N. Dies ist zwar eine gültige Supersequenz, aber nicht die kürzeste.
Warum? Weil alle Zeichen, die beide Strings *in genau derselben Reihenfolge gemeinsam haben* (ihre längste gemeinsame Teilfolge), doppelt gezählt werden!
Um die Supersequenz so kurz wie möglich zu machen, müssen wir die LCS überlappen lassen.
Die Länge der kürzesten gemeinsamen Supersequenz (SCS) beträgt mathematisch nachweislich genau: `M + N - LCS(str1, str2)`.

**Konstruktion der Zeichenkette:**
Wenn in der Aufgabe nach der tatsächlichen Zeichenkette gefragt wird, können wir die Speicherplatzoptimierung $O(N)$ für die LCS nicht verwenden. Wir müssen die vollständige M × N-DP-Tabelle erstellen.
Sobald die Tabelle erstellt ist, beginnen wir in der rechten unteren Ecke `(m, n)` und arbeiten uns zurück zu `(0, 0)`:
1. Wenn `str1[i-1] == str2[j-1]`: Dieses Zeichen ist Teil des LCS! Wir müssen es nur EINMAL schreiben. Fügen wir es unserem Ergebnis hinzu und bewegen wir uns diagonal nach links oben `(i-1, j-1)`.
2. Wenn sie NICHT übereinstimmen: Wir müssen das Zeichen einbeziehen, das zum längeren LCS-Pfad führt!
   – Wenn `dp[i-1][j] > dp[i][j-1]`, bedeutet dies, dass der optimale Pfad von oben kam. Wir fügen `str1[i-1]` hinzu und bewegen uns NACH OBEN.
   - Andernfalls kam der optimale Pfad von links. Wir fügen `str2[j-1]` hinzu und bewegen uns nach links.
3. Wenn wir die obere Kante erreichen (`i=0`), hängen wir einfach den Rest von `str2` an. Wenn wir die linke Kante erreichen (`j=0`), hängen wir den Rest von `str1` an.
4. Die resultierende Zeichenkette wird rückwärts aufgebaut, also am Ende umkehren!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

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

## Schritt-für-Schritt-Anleitung

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
Der Traceback beginnt bei `i=4, j=3`(`dp[4][3] = 2`).
1. `str1[3] ('c') != str2[2] ('b')`. `dp[3][3]`(2) > `dp[4][2]`(1). Nach oben bewegen. `'c'` anhängen. `i=3, j=3`.
2. `str1[2] ('a') != str2[2] ('b')`. `dp[2][3]`(2) >= `dp[3][2]`(1). Nach OBEN bewegen. `'a'` anhängen. `i=2, j=3`.
3. `str1[1] ('b') == str2[2] ('b')`. Übereinstimmung! Diagonal verschieben. `'b'` anhängen. `i=1, j=2`.
4. `str1[0] ('a') == str2[1] ('a')`. Übereinstimmung! Diagonal verschieben. `'a'` anhängen. `i=0, j=1`.
5. `i=0`, Schleife endet.
6. Verbleibendes `j` löschen: `str2` hat noch `j=1` übrig. `str2[0] ('c')` anhängen.
Umgekehrtes Ergebnis: `"cab"` -> `"b"` -> `"ab"` -> `"aab"` -> `"caab"`.
Moment, die Umkehrung von `['c', 'a', 'b', 'a', 'c']` ist `"cabac"`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M * N)$ | $O(M * N)$ |
| **Durchschnittlicher Fall** | $O(M * N)$ | $O(M * N)$ |
| **Schlechteste** | $O(M * N)$ | $O(M * N)$ |

Das Erstellen der LCS-Matrix dauert genau $O(M \times N)$ Zeit.
Das Zurückverfolgen erfordert höchstens $O(M + N)$ Schritte. Die Gesamtzeit beträgt $O(M \times N)$.
Der Speicherbedarf für die DP-Matrix beträgt genau $O(M \times N)$. Wir können diesen nicht auf $O(\min(M, N)$ optimieren, da die Rückverfolgung das gesamte historische Pfadgitter benötigt, um Routing-Entscheidungen zu treffen.

## Varianten & Optimierungen

- **Kürzeste gemeinsame Supersequenz mehrerer Zeichenketten:** Bei K Zeichenketten wird der DP-Zustand K-dimensional ($O(N^K)$), was NP-schwer ist! Man approximiert dies üblicherweise mit Greedy-Algorithmen oder Hamilton-Pfaden auf Überlappungsgraphen.

## Praktische Anwendungen

- **Datenkompression:** Ermittlung des kürzesten Befehlsbandes, das durch Verzweigungen an bestimmten Indizes zwei verschiedene Ausgabesequenzen erzeugen kann (ein grundlegendes Konzept der Kolmogorov-Komplexität).

## Verwandte Algorithmen in cOde(n)

- **[dp_04 – Längste gemeinsame Teilsequenz](dp_04_longest-common-subsequence.md)** — Genau dieselbe Tabelle.
- **[dp_08 – Editierdistanz](dp_08_edit-distance.md)** — Eine weitere Strings-DP, die eine vollständige Matrix-Rückverfolgung erfordert, um die genauen Bearbeitungsanweisungen auszugeben.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
