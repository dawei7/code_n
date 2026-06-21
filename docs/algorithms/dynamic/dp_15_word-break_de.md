# Word Break

| | |
|---|---|
| **ID** | `dp_15` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Word wrap problem](https://en.wikipedia.org/wiki/Word_wrap_problem) (verwandt) |

## Problemstellung

Gegeben ist ein String `s` und ein Wörterbuch `wordDict` aus Strings.
Bestimme, ob `s` in eine Sequenz aus einem oder mehreren Wörtern des Wörterbuchs segmentiert werden kann. Wörter dürfen **wiederverwendet** werden.

**Eingabe:** ein String `s`, eine Liste von Wörtern `wordDict`.
**Ausgabe:** `True`, falls `s` segmentiert werden kann, andernfalls `False`.

**Beispiel:**

| s | wordDict | Antwort | Segmente |
|---|---|---|---|
| `"leetcode"` | `["leet", "code"]` | True | `"leet" + "code"` |
| `"applepenapple"` | `["apple", "pen"]` | True | `"apple" + "pen" + "apple"` |
| `"catsandog"` | `["cats", "dog", "sand", "and", "cat"]` | False | — |
| `"a"` | `["a"]` | True | `"a"` |
| `"abcd"` | `["a", "abc", "b", "cd"]` | True | `"a" + "b" + "cd"` |

## Wann man es verwendet

- Das kanonische DP-Problem zur **String-Segmentierung**. Es testet, ob man den 1D-DP-Zustand, die Überprüfung von Teilstrings und die Optimierung des Wörterbuchs als Set identifizieren kann.
- Die Grundlage für mehrere schwierigere Probleme: **Word Break II**
  (Rückgabe aller Segmentierungen), **Concatenated Words** und viele Aufgaben im Bereich der natürlichen Sprachverarbeitung.

## Ansatz

Sei `dp[i]` = kann das Präfix `s[0..i-1]` (Länge `i`) in Wörter des Wörterbuchs segmentiert werden?

**Rekurrenz:** Betrachte für jedes `i` jedes `j < i`. Wenn
`dp[j]` True ist UND `s[j..i-1]` im Wörterbuch enthalten ist, dann ist
`dp[i]` True.

```
dp[i] = any(dp[j] and s[j:i] in word_set for j in 0..i-1)
```

**Induktionsanfang:** `dp[0] = True` (ein leerer String kann trivial segmentiert werden).

**Antwort:** `dp[len(s)]`.

**Optimierung:** Wandle `wordDict` in ein Set um, um eine $O(1)$
Mitgliedschaftsprüfung zu ermöglichen. Optional können `min_word_len` und
`max_word_len` verfolgt werden, um irrelevante `j`-Werte zu überspringen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_15: Word Break.

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

`s = "applepenapple"`, `wordDict = ["apple", "pen"]`.
`word_set = {"apple", "pen"}`. `n = 13`.

`dp = [T, F, F, F, F, F, F, F, F, F, F, F, F, F]`.

| i | check j's | s[j:i] | dp[j] & in set? | dp[i] |
|---:|---|---|---|---|
| 1 | j=0 | "a" | F | F |
| 2 | j=0,1 | "ap", "p" | F | F |
| 3 | j=0,1,2 | "app", "pp", "p" | F | F |
| 4 | j=0..3 | "appl", "ppl", "pl", "l" | F | F |
| 5 | j=0..4 | "apple", "pple", "ple", "le", "e" | T (j=0, "apple") | **T** |
| 6 | j=0..5 | ... | — (j=5 T, "p" F) | F |
| 7 | j=0..6 | ... | — (j=5 T, "pe" F) | F |
| 8 | j=0..7 | ... | — (j=5 T, "pen" T) | **T** |
| 9 | j=0..8 | ... | F | F |
| ... | | | | |
| 13 | j=0..12 | "applepenapple" | T (j=8, "apple") | **T** |

`dp[13] = T`. ✓ (Segmentierung: "apple" + "pen" + "apple".)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n²)$ | $O(n)$ |
| **Durchschnittlicher Fall** | $O(n²)$ | $O(n)$ |
| **Schlechtester Fall** | $O(n²)$ | $O(n)$ |

Die Doppelschleife ist $O(n²)$. Die Erstellung des Teilstrings `s[j:i]` ist jeweils $O(n)$, daher beträgt die Gesamtlaufzeit naiv $O(n³)$. Verwende String-Slicing-Interning (Python) oder die Optimierung der Teilstring-Suche, um sie bei $O(n²)$ zu halten. Mit einer Trie-Suche kann der schlechteste Fall $O(n·L)$ betragen, wobei L die maximale Wortlänge ist.

## Varianten & Optimierungen

- **Word Break II** — gib ALLE Segmentierungen zurück, nicht nur, ob eine existiert. Verwende memoisiertes DFS auf `dp[i]`.
- **Concatenated Words** — finde alle Wörter im Wörterbuch, die selbst aus anderen Wörtern des Wörterbuchs zusammengesetzt sind. Wende Word Break auf jedes Wort an.
- **Trie-basierte Suche** — für große Wörterbücher: speichere alle Wörter in einem Trie und durchlaufe den String in insgesamt $O(n)$ Zeit pro `i` (amortisiert $O(n²)$ für den gesamten Algorithmus).
- **Längenbeschränktes Wörterbuch** — berechne `min_len` und `max_len` vorab; überspringe `j`, wenn `i - j` außerhalb des Bereichs liegt.
- **Word Break mit einem Wildcard** — `'*'` entspricht einem beliebigen einzelnen Zeichen. Etwas komplexeres DP.

## Anwendungen in der Praxis

- **Natürliche Sprachverarbeitung** — Tokenisierung, Zerlegung eines Satzes in Wörter.
- **Code-Parsing** — Aufteilen eines Bezeichners in camelCase-Teilwörter.
- **URL-Slug-Generierung** — Aufteilen einer langen URL in aussagekräftige Pfadsegmente.
- **DNA-Sequenz-Segmentierung** — Finden bekannter Gen-Teilsequenzen in einem langen DNA-String.
- **Compiler-Symbolauflösung** — Aufteilen eines zusammengesetzten Symbolnamens in Namespace-, Klassen- und Funktionsteile.

## Verwandte Algorithmen in cOde(n)

- **[dp_20 — Shortest Common Supersequence (Length)](dp_20_shortest-common-supersequence.md)** —
  ähnliche Struktur des Teilstring-DP. (d=5/10, r=9/10)
- **[dp_04 — LCS](dp_04_longest-common-subsequence.md)** — das
  klassische 2D-String-DP. (d=5/10, r=9/10)
- **[string_10 — Word Break (Strings)](string_10_word-break-strings.md)** —
  derselbe Algorithmus in der Kategorie Strings. (d=4/10, r=7/10)

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den enzyklopädischen Standardeintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*