# Word Break

| | |
|---|---|
| **ID** | `string_10` |
| **Kategorie** | strings |
| **Komplexität (erforderlich)** | $O(N^2 \times M)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Word Break](https://leetcode.com/problems/word-break/) |

## Problemstellung

Gegeben ist ein String `s` und ein Wörterbuch `wordDict`. Gib `true` zurück, falls `s` in eine durch Leerzeichen getrennte Sequenz aus einem oder mehreren Wörtern des Wörterbuchs segmentiert werden kann.
Beachte, dass dasselbe Wort aus dem Wörterbuch mehrfach in der Segmentierung verwendet werden darf.

**Eingabe:** Ein String `s` und eine Liste von Strings `wordDict`.
**Ausgabe:** Ein Boolean.

## Wann man es verwendet

- Um einen massiven, unstrukturierten String (wie eine URL oder einen Hashtag) in für Menschen lesbare Wörter zu zerlegen.
- Als grundlegende Einführung in die 1D-Dynamische Programmierung über String-Indizes.

## Ansatz

**1. Der Fehler des Greedy-Matching:**
Angenommen, `s = "applepenapple"` und `wordDict = ["apple", "pen"]`. Ein Greedy-Ansatz (bei dem geprüft wird, ob der String mit einem Wort aus dem Wörterbuch beginnt, dieses abschneidet und den Vorgang wiederholt) funktioniert hier einwandfrei.
Aber nehmen wir an, `s = "cars"` und `wordDict = ["car", "ca", "rs"]`.
Wenn wir gierig vorgehen, sehen wir, dass `"car"` passt! Wir schneiden es ab. Übrig bleibt `"s"`. `"s"` ist nicht im Wörterbuch! Der Algorithmus gibt `False` zurück.
Aber Moment! Hätten wir stattdessen `"ca"` gewählt, bliebe `"rs"` übrig. `"rs"` IST im Wörterbuch! Die korrekte Antwort ist `True`!
Greedy-Matching scheitert hier vollständig, da eine früh getroffene, scheinbar gültige Wahl mathematisch eine gültige Sequenz zu einem späteren Zeitpunkt blockieren kann.

**2. Die Strategie der Dynamischen Programmierung:**
Wir müssen ALLE möglichen gültigen Trennpunkte gleichzeitig verfolgen!
Wir erstellen ein Boolean-Array `dp` der Länge N+1, das mit `False` initialisiert wird.
`dp[i] = True` bedeutet: "Der Teilstring `s[0...i]` kann erfolgreich in gültige Wörter des Wörterbuchs zerlegt werden."
Der Induktionsanfang ist `dp[0] = True` (ein leerer String ist trivialerweise gültig).

**3. Die DP-Übergänge:**
Wir iterieren `i` von 1 bis N. (Dies entspricht dem Versuch herauszufinden, ob der Teilstring bis zur Länge `i` gültig ist).
Um festzustellen, ob `dp[i]` `True` ist, fangen wir nicht bei Null an! Wir schauen RÜCKWÄRTS auf jeden vorherigen gültigen Trennpunkt `j` (wobei `dp[j] == True`).
Wenn `dp[j]` `True` ist, bedeutet das, dass wir den String bis zum Index `j` erfolgreich segmentiert haben.
Alles, was wir tun müssen, ist zu prüfen, ob der VERBLEIBENDE Teil des Strings `s[j...i]` ein gültiges Wort in unserem `wordDict` ist!
Wenn dies der Fall ist, ist `dp[i]` mathematisch garantiert `True`! Wir markieren es als `True` und brechen sofort zum nächsten `i` ab!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_10: Word Break.

True iff s can be segmented into a sequence of dictionary words.
"""


def solve(s, word_dict):
    n = len(s)
    word_set = set(word_dict)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
```

</details>

## Durchlauf

`s = "cars"`, `wordDict = ["car", "ca", "rs"]`.
`N = 4`. `dp = [True, False, False, False, False]`.

1. **`i = 1` (`"c"`):**
   - `j = 0`: `dp[0]` ist True. `s[0:1]` ist `"c"`. `"c"` nicht im Set.
   - `dp[1] = False`.
2. **`i = 2` (`"ca"`):**
   - `j = 1`: `dp[1]` ist False. Überspringen.
   - `j = 0`: `dp[0]` ist True. `s[0:2]` ist `"ca"`. `"ca"` IST im Set!
   - `dp[2] = True`. Abbruch!
3. **`i = 3` (`"car"`):**
   - `j = 2`: `dp[2]` ist True. `s[2:3]` ist `"r"`. `"r"` nicht im Set.
   - `j = 1`: `dp[1]` ist False. Überspringen.
   - `j = 0`: `dp[0]` ist True. `s[0:3]` ist `"car"`. `"car"` IST im Set!
   - `dp[3] = True`. Abbruch!
4. **`i = 4` (`"cars"`):**
   - `j = 3`: `dp[3]` ist True. `s[3:4]` ist `"s"`. `"s"` nicht im Set.
   - `j = 2`: `dp[2]` ist True. `s[2:4]` ist `"rs"`. `"rs"` IST im Set!
   - `dp[4] = True`. Abbruch!

Die Schleife endet. Rückgabe von `dp[4]` -> `True`! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \times M)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N^2 \times M)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N^2 \times M)$ | $O(N)$ |

Die äußere Schleife läuft N-mal.
Die innere Schleife läuft bis zu N-mal rückwärts. Dies ergibt $O(N^2)$ Iterationen.
Innerhalb der inneren Schleife kopiert das Slicing `s[j:i]` physisch Zeichen, um einen neuen String zu erstellen! Das Erstellen eines Strings der Länge M benötigt $O(M)$ Zeit (wobei M die Länge des geschnittenen Wortes ist). Das Hashing des neuen Strings zur Überprüfung im Set benötigt ebenfalls $O(M)$ Zeit.
Die gesamte Zeitkomplexität beträgt $O(N^2 \times M)$.
Die Platzkomplexität beträgt $O(N)$ für das `dp`-Array. (Unter der Annahme, dass die Erstellung des Hash Sets als Standard-Eingabeparsing nicht mitgezählt wird).

## Varianten & Optimierungen

- **Längenbegrenzte innere Schleife:** Wenn das längste Wort im Wörterbuch 10 Zeichen lang ist, gibt es KEINEN GRUND, warum die innere Schleife `j` 100 Zeichen rückwärts suchen sollte! Man kann die innere Schleife so anpassen, dass sie nur `max(0, i - MAX_WORD_LENGTH)` prüft. Dies reduziert die Zeitkomplexität im schlechtesten Fall sofort auf $O(N \times L^2)$, wobei L die maximale Wortlänge ist!
- **Word Break II:** Anstatt einen Boolean zurückzugeben, gib ALLE möglichen gültigen Sätze zurück. Dies erfordert ein rekursives Backtracking (DFS) in Kombination mit Memoization, um die tatsächlichen Pfade nachzuverfolgen!

## Anwendungen in der Praxis

- **Hashtag-Parsing:** Zerlegen von `#ilovealgorithms` in `["i", "love", "algorithms"]` für die Analyse von Twitter-Trending-Topics.
- **NLP für asiatische Sprachen:** Sprachen wie Chinesisch und Japanisch werden ohne Leerzeichen zwischen den Wörtern geschrieben! NLP-Prozessoren müssen genau diesen Algorithmus mit einem umfangreichen Sprachwörterbuch ausführen, um Zeichen in einzelne Wörter zu segmentieren, bevor sie übersetzt werden können.

## Verwandte Algorithmen in cOde(n)

- **[dynamic_03 - Longest Increasing Subsequence](../dynamic/dp_03_longest-increasing-subsequence.md)** — Dasselbe DP-Muster "Rückblick auf alle vorherigen gültigen Zustände", angewendet auf Ganzzahlen statt auf Strings.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*