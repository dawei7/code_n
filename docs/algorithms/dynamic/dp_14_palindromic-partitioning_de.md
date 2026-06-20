# Palindrom-Partitionierung II

| | |
|---|---|
| **ID** | `dp_14` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(N^2)$ Zeit, $O(N^2)$ Speicherplatz |
| **Schwierigkeitsgrad** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Palindrom-Partitionierung II](https://leetcode.com/problems/palindrome-partitioning-ii/) |

## Aufgabenstellung

Gegeben sei eine Zeichenkette `s`. Partitioniere `s` so, dass jede Teilzeichenkette der Partition ein Palindrom ist.
Gib die **minimale Anzahl von Schnitten** zurück, die für eine Palindrom-Partitionierung von `s` erforderlich ist.

**Eingabe:** Eine Zeichenkette `s`.
**Ausgabe:** Eine ganze Zahl, die die minimale Anzahl an Schnitten angibt.

## Wann man es verwendet

- Wenn ein Problem die Optimierung der Gruppierung oder Segmentierung einer eindimensionalen Sequenz auf der Grundlage einer Eigenschaft erfordert, die im Voraus berechnet werden kann (wie z. B. „ist ein Palindrom“).
- Es erfordert einen klassischen **Zwei-Durchlauf-DP**-Ansatz: einen Durchlauf zur Vorberechnung der Palindrome und einen Durchlauf zur Ermittlung der minimalen Schnitte.

## Vorgehensweise

**1. Palindrome vorab berechnen ($O(N^2)$):**
Wenn wir `is_palindrome()` für jede Teilzeichenfolge im laufenden Betrieb prüfen, wird der Algorithmus zu $O(N^3)$.
Wir verwenden ein zweidimensionales boolesches Array `is_pal[i][j]`, das `True` ist, wenn `s[i...j]` ein Palindrom ist.
- `s[i...j]` ist ein Palindrom, WENN `s[i] == s[j]` UND `s[i+1...j-1]` ein Palindrom ist.
- Wir erstellen diese Tabelle genau wie bei der Intervall-DP, wobei wir über die Länge der Teilzeichenfolgen iterieren!

**2. Minimale Schnitte finden ($O(N^2)$):**
Sei `dp[i]` die minimale Anzahl an Schnitten, die erforderlich ist, um das Präfix `s[0...i]` perfekt zu partitionieren.

**3. Die Übergangsbeziehung (die Rekursionsbeziehung) ermitteln:**
Um `dp[i]` zu ermitteln, versuchen wir, den *letzten Schnitt* an jedem möglichen Index `j` zu setzen (wobei 0 \le j \le i gilt).
Wenn wir einen Schnitt vor dem Index `j` setzen, ist das letzte Teil der Zeichenkette `s[j...i]`.
Wir KÖNNEN DIESEN SCHNITT NUR VORNEHMEN, wenn `s[j...i]` ein gültiges Palindrom ist!
Wenn es sich um ein gültiges Palindrom handelt, wäre die Gesamtzahl der Schnitte für das Präfix `s[0...i]` wie folgt:
- Die minimale Anzahl an Schnitten, die für das Präfix VOR dem Schnitt erforderlich ist: `dp[j-1]`
- ZUZÜGLICH 1 (für den neuen Schnitt, den wir gerade vorgenommen haben).
Daher gilt `dp[i] = min( dp[i], 1 + dp[j-1] )` für alle 0 \le j \le i, wobei `is_pal[j][i]` gleich `True` ist.

*Optimierung des Basisfalls:* Wenn das gesamte Präfix `s[0...i]` bereits ein Palindrom ist (`is_pal[0][i] == True`), benötigen wir 0 Schnitte! `dp[i] = 0`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_14: Palindromic Partitioning.

Min cuts to partition a string into all-palindromic substrings.
"""


def solve(s):
    n = len(s)
    if n <= 1:
        return 0
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or is_pal[i + 1][j - 1]:
                    is_pal[i][j] = True
    INF = float("inf")
    dp = [INF] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if is_pal[j + 1][i] and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
    return dp[n - 1]
```

</details>

## Schritt-für-Schritt-Anleitung

`s = "aab"`. N = 3.
1. **Vorberechnung `is_pal`:**
   - `"a"`: Wahr. `"a"`: Wahr. `"b"`: Wahr.
   - `"aa"`: Wahr. `"ab"`: Falsch.
   - `"aab"`: Falsch.
2. **DP-Durchlauf:**
   - `i = 0 ('a')`: `s[0...0]` ist `"a"`, was ein Palindrom ist! `dp[0] = 0`.
   - `i = 1 ('a')`: `s[0...1]` ist `"aa"`, was ein Palindrom ist! `dp[1] = 0`.
   - `i = 2 ('b')`: `s[0...2]` ist `"aab"`, KEIN Palindrom.
     - Versuche `j = 1 ('a')`: Das Suffix `s[1...2]` ist `"ab"` (Falsch).
     - Versuche `j = 2 ('b')`: Das Suffix `s[2...2]` ist `"b"` (WAHR).
 - Gültiger Schnitt vor Index 2! Die Kosten betragen `1 + dp[1] = 1 + 0 = 1`.
       - `min_cuts = 1`.
   - `dp[2] = 1`.

Das Ergebnis `dp[2]` ist 1. ✓ (Die Schnitte sind `"aa" | "b"`).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^2)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | $O(N^2)$ | $O(N^2)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(N^2)$ |

Schritt 1 (Vorberechnung) benötigt genau $O(N^2)$ Zeit, um die Boolesche Matrix zu füllen.
Schritt 2 (DP) benötigt $O(N^2)$ Zeit, wobei i von 0 bis N und j von 0 bis i durchlaufen wird.
Die gesamte Zeitkomplexität beträgt $O(N^2)$.
Die Platzkomplexität beträgt streng genommen $O(N^2)$ für die `is_pal` Boolesche Matrix. Das `dp`-Array benötigt $O(N)$.

## Varianten & Optimierungen

- **Palindrom-Partitionierung I (Backtracking):** Anstatt die *minimale Anzahl* von Schnitten zurückzugeben, werden *alle möglichen* gültigen Partitionen zurückgegeben. Man verwendet genau dasselbe `is_pal` Vorberechnungsarray, führt dann aber einen DFS-Backtracking-Algorithmus (`bb_01`) aus, um alle gültigen Verzweigungen zu erkunden und an eine globale Ergebnisliste anzuhängen.
- **Zentrumsausdehnung (Speicheroptimierung):** Man kann auf die Erstellung der $O(N^2)$ `is_pal`-Matrix verzichten und stattdessen einen einzigen Durchlauf durchführen! Man expandiert um jedes mögliche „Zentrum“ herum (wie beim Manacher-Algorithmus) und aktualisiert das `dp`-Array während der Ausführung. Dadurch sinkt die Speicherplatzkomplexität auf streng $O(N)$!

## Praktische Anwendungen

- **Verarbeitung natürlicher Sprache:** Tokenisierung von fortlaufenden Sprachströmen oder Text ohne Leerzeichen (wie fortlaufendes Japanisch oder Hashtags) in gültige Wörter aus dem Wörterbuch.

## Verwandte Algorithmen in cOde(n)

- **[dp_15 – Worttrennung](dp_15_word-break.md)** – Das mathematisch identische Problem, bei dem die Gültigkeit anhand eines Wörterbuchs statt anhand einer Palindrom-Eigenschaft überprüft wird.
- **[string_04 – Längste palindromische Teilzeichenfolge](../strings/string_04_longest-palindromic-substring.md)** — Verwendet genau dieselbe $O(N^2)$ Palindrom-DP-Vorberechnungstabelle.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
