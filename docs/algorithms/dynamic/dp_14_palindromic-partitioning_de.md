# Palindrome Partitioning II

| | |
|---|---|
| **ID** | `dp_14` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(N^2)$ Zeit, $O(N^2)$ Platz |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) |

## Problemstellung

Gegeben sei ein String `s`. Zerlege `s` so, dass jeder Teilstring der Partition ein Palindrom ist.
Gib die **minimale Anzahl an Schnitten** zurück, die für eine Palindrom-Partitionierung von `s` erforderlich sind.

**Eingabe:** Ein String `s`.
**Ausgabe:** Eine Ganzzahl, die die minimale Anzahl an Schnitten repräsentiert.

## Wann ist es anzuwenden?

- Wenn ein Problem die Optimierung der Gruppierung oder Segmentierung einer 1D-Sequenz erfordert, basierend auf einer Eigenschaft, die vorab berechnet werden kann (wie "ist ein Palindrom").
- Es erfordert einen klassischen **Two-Pass-DP-Ansatz**: Ein Durchlauf zur Vorberechnung der Palindrome und ein Durchlauf zur Ermittlung der minimalen Schnitte.

## Ansatz

**1. Vorberechnung der Palindrome ($O(N^2)$):**
Wenn wir `is_palindrome()` für jeden Teilstring zur Laufzeit testen, wird der Algorithmus $O(N^3)$.
Wir verwenden ein 2D-Boolean-Array `is_pal[i][j]`, das `True` ist, wenn `s[i...j]` ein Palindrom ist.
- `s[i...j]` ist ein Palindrom, WENN `s[i] == s[j]` UND `s[i+1...j-1]` ein Palindrom ist.
- Wir bauen diese Tabelle genau wie bei der Intervall-DP auf, indem wir über die Länge des Teilstrings iterieren!

**2. Minimale Schnitte finden ($O(N^2)$):**
Sei `dp[i]` die minimale Anzahl an Schnitten, die erforderlich sind, um das Präfix `s[0...i]` perfekt zu partitionieren.

**3. Die Transition finden (Die Rekursionsgleichung):**
Um `dp[i]` zu finden, versuchen wir, den *letzten Schnitt* an jedem möglichen Index `j` zu setzen (wobei 0 \le j \le i).
Wenn wir einen Schnitt vor dem Index `j` setzen, ist das letzte Stück des Strings `s[j...i]`.
Wir KÖNNEN DIESEN SCHNITT NUR DURCHFÜHREN, wenn `s[j...i]` ein gültiges Palindrom ist!
Wenn es ein gültiges Palindrom ist, wäre die Gesamtzahl der Schnitte für das Präfix `s[0...i]`:
- Die minimalen Schnitte, die für das Präfix VOR dem Schnitt erforderlich sind: `dp[j-1]`
- PLUS 1 (für den neuen Schnitt, den wir gerade gemacht haben).
Daher gilt: `dp[i] = min( dp[i], 1 + dp[j-1] )` für alle 0 \le j \le i, bei denen `is_pal[j][i]` `True` ist.

*Optimierung des Induktionsanfangs:* Wenn das gesamte Präfix `s[0...i]` bereits ein Palindrom ist (`is_pal[0][i] == True`), benötigen wir 0 Schnitte! `dp[i] = 0`.

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

## Durchlauf

`s = "aab"`. N=3.
1. **Vorberechnung `is_pal`:**
   - `"a"`: True. `"a"`: True. `"b"`: True.
   - `"aa"`: True. `"ab"`: False.
   - `"aab"`: False.
2. **DP-Durchlauf:**
   - `i = 0 ('a')`: `s[0...0]` ist `"a"`, was ein Palindrom ist! `dp[0] = 0`.
   - `i = 1 ('a')`: `s[0...1]` ist `"aa"`, was ein Palindrom ist! `dp[1] = 0`.
   - `i = 2 ('b')`: `s[0...2]` ist `"aab"`, KEIN Palindrom.
     - Versuche `j = 1 ('a')`: Suffix `s[1...2]` ist `"ab"` (False).
     - Versuche `j = 2 ('b')`: Suffix `s[2...2]` ist `"b"` (TRUE).
       - Gültiger Schnitt vor Index 2! Kosten sind `1 + dp[1] = 1 + 0 = 1`.
       - `min_cuts = 1`.
   - `dp[2] = 1`.

Das Ergebnis `dp[2]` ist 1. ✓ (Die Schnitte sind `"aa" | "b"`).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^2)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | $O(N^2)$ | $O(N^2)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(N^2)$ |

Schritt 1 (Vorberechnung) benötigt exakt $O(N^2)$ Zeit, um die Boolean-Matrix zu füllen.
Schritt 2 (DP) benötigt $O(N^2)$ Zeit, wobei i von 0 bis N und j von 0 bis i iteriert wird.
Die gesamte Zeitkomplexität beträgt $O(N^2)$.
Die Platzkomplexität beträgt $O(N^2)$ strikt für die `is_pal` Boolean-Matrix. Das `dp`-Array benötigt $O(N)$.

## Varianten & Optimierungen

- **Palindrome Partitioning I (Backtracking):** Anstatt die *minimale Anzahl* an Schnitten zurückzugeben, gib *alle möglichen* gültigen Partitionen zurück. Du verwendest exakt dasselbe `is_pal`-Vorberechnungs-Array, führst dann aber einen DFS-Backtracking-Algorithmus (`bb_01`) aus, um alle gültigen Zweige zu erkunden und an eine globale Ergebnisliste anzuhängen.
- **Zentren-Expansion (Platzoptimierung):** Du kannst den Aufbau der $O(N^2)$ `is_pal`-Matrix überspringen und stattdessen einen einzigen Durchlauf machen! Expandiere um jedes mögliche "Zentrum" (wie beim Manacher-Algorithmus) und aktualisiere das `dp`-Array zur Laufzeit. Dies reduziert die Platzkomplexität auf strikt $O(N)$!

## Anwendungen in der Praxis

- **Natural Language Processing:** Tokenisierung von kontinuierlichen Sprachströmen oder Texten ohne Leerzeichen (wie kontinuierliches Japanisch oder Hashtags) in gültige Wörter eines Wörterbuchs.

## Verwandte Algorithmen in cOde(n)

- **[dp_15 - Word Break](dp_15_word-break.md)** — Das mathematisch identische Problem, bei dem die Gültigkeit gegen ein Wörterbuch anstelle einer Palindrom-Eigenschaft geprüft wird.
- **[string_04 - Longest Palindromic Substring](../strings/string_04_longest-palindromic-substring.md)** — Verwendet exakt dieselbe $O(N^2)$ Palindrom-DP-Vorberechnungstabelle.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*