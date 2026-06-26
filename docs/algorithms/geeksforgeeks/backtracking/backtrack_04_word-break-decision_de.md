# Word Break II (Backtracking)

| | |
|---|---|
| **ID** | `backtrack_04` |
| **Kategorie** | Backtracking |
| **Komplexität (erforderlich)** | $O(N^2 + 2^N)$ Zeit, $O(N + 2^N)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Word Break II](https://leetcode.com/problems/word-break-ii/) |

## Problemstellung

Gegeben ist ein String `s` und ein Wörterbuch `wordDict`. Fügen Sie Leerzeichen in `s` ein, um einen Satz zu bilden, bei dem jedes Wort ein gültiges Wort aus dem Wörterbuch ist. Geben Sie alle möglichen Sätze in beliebiger Reihenfolge zurück.
Beachten Sie, dass dasselbe Wort aus dem Wörterbuch mehrfach in der Segmentierung verwendet werden darf.

**Eingabe:** Ein String `s` und eine Liste von Strings `wordDict`.
**Ausgabe:** Eine Liste von Strings, wobei jeder String ein durch Leerzeichen getrennter, gültiger Satz ist.

## Wann man es verwendet

- Um ALLE möglichen gültigen Segmentierungen oder Partitionen einer Sequenz basierend auf einer deterministischen Validierungsregel zu finden.
- Es lässt sich hervorragend mit Dynamischer Programmierung (`dp_15_word-break.md`) kombinieren, wobei DP die Frage "Ist es möglich?" beantwortet und Backtracking die Frage "Was sind alle exakten Pfade?".

## Ansatz

**1. Der Entscheidungsbaum:**
An jedem Punkt im String `s`, beginnend bei Index `start`, schauen wir voraus, ob das Präfix `s[start...i]` ein gültiges Wort in `wordDict` bildet.
Wenn dies der Fall ist, haben wir einen gültigen "Schnittpunkt" gefunden! Wir fügen dieses Wort unserem aktuellen Satz hinzu und verzweigen rekursiv, um den Rest des Strings ab Index `i + 1` zu verarbeiten.
Da wir JEDEN gültigen Schnitt untersuchen müssen, explodiert ein String aus lauter "a"s bei einem Wörterbuch von `["a", "aa", "aaa"]` in $O(2^N)$ Zweige!

**2. Der Backtracking-Zustand:**
`backtrack(start_index, current_sentence)`:
- `start_index`: Der Index im String `s`, an dem der noch nicht geparste verbleibende Teilstring beginnt.
- `current_sentence`: Eine Liste von Wörtern, die wir bisher erfolgreich geparst haben.

**3. Basisfall:**
Wenn `start_index == len(s)`, bedeutet dies, dass wir den GESAMTEN String erfolgreich in gültige Wörterbuchwörter zerlegt haben!
Wir verbinden die Wörter in `current_sentence` mit einem Leerzeichen `" ".join(...)` und fügen das Ergebnis unserer globalen Ergebnisliste hinzu.

**4. Der rekursive Schritt:**
Schleife `i` von `start_index + 1` bis `len(s) + 1` (da Python-String-Slicing am Ende exklusiv ist).
- Extrahiere den Teilstring: `word = s[start_index : i]`.
- Wenn `word` im `wordDict` enthalten ist:
  - **Wahl treffen:** Füge `word` zu `current_sentence` hinzu.
  - **Rekursion:** Rufe `backtrack(i, current_sentence)` auf.
  - **Backtrack:** Entferne `word` mittels `pop` aus `current_sentence`, damit wir im nächsten Schleifendurchlauf einen anderen, längeren Schnittpunkt ausprobieren können.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for backtrack_04: Word Break.

Given a string s and a list of dictionary words, return True
iff s can be segmented into a sequence of one or more dict
words. Backtracking: at each step, try each dict word as a
prefix; recurse on the remaining suffix.
"""


def solve(s, dictionary, n):
    if n == 0:
        return True

    def helper(remaining):
        if not remaining:
            return True
        for word in dictionary:
            if remaining.startswith(word) and helper(remaining[len(word):]):
                return True
        return False

    return helper(s)
```

</details>

## Durchlauf

`s = "catsanddog"`, `word_dict = ["cat", "cats", "and", "sand", "dog"]`.

1. `backtrack(0, [])`:
   - `i = 1, 2`: "c", "ca" nicht im Wörterbuch.
   - `i = 3`: "cat" ist im Wörterbuch! Hinzufügen.
     - `backtrack(3, ["cat"])`:
       - `i = 4, 5, 6`: "s", "sa", "san" nicht im Wörterbuch.
       - `i = 7`: "sand" ist im Wörterbuch! Hinzufügen.
         - `backtrack(7, ["cat", "sand"])`:
           - `i = 8, 9`: "d", "do" nicht im Wörterbuch.
           - `i = 10`: "dog" ist im Wörterbuch! Hinzufügen.
             - `backtrack(10, ["cat", "sand", "dog"])`: BASISFALL! Füge `"cat sand dog"` zum Ergebnis hinzu.
           - Backtrack -> `pop` "dog".
       - Backtrack -> `pop` "sand".
   - `i = 4`: "cats" ist im Wörterbuch! Hinzufügen.
     - `backtrack(4, ["cats"])`:
       - `i = 5, 6`: "a", "an" nicht im Wörterbuch.
       - `i = 7`: "and" ist im Wörterbuch! Hinzufügen.
         - `backtrack(7, ["cats", "and"])`:
           - `i = 8, 9`: "d", "do" nicht im Wörterbuch.
           - `i = 10`: "dog" ist im Wörterbuch! Hinzufügen.
             - `backtrack(10, ["cats", "and", "dog"])`: BASISFALL! Füge `"cats and dog"` zum Ergebnis hinzu.
           - Backtrack -> `pop` "dog".
       - Backtrack -> `pop` "and".
   - `i = 5..10`: "catsa", etc. nicht im Wörterbuch.

Ergebnis: `["cat sand dog", "cats and dog"]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^2)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(2^N)$ | $O(2^N)$ |
| **Schlechtester Fall** | $O(N^2 + 2^N)$ | $O(N + 2^N)$ |

*Wobei N die Länge des Strings ist.*
Im schlechtesten Fall (z. B. `s = "aaaaaa"`, `dict = ["a", "aa", "aaa"]`) ist jede einzelne Zeichengrenze ein gültiger Schnitt. Dies erzeugt genau $2^{N-1}$ gültige Sätze! Das Rekonstruieren und Verbinden der Strings benötigt $O(N)$, was zu einer Zeitkomplexität von $O(N \cdot 2^N)$ führt.
Wenn der String überhaupt nicht segmentiert werden kann, dauert es $O(N^2)$, um die Präfixe zu prüfen und fehlzuschlagen.
Die Platzkomplexität beträgt $O(N)$ für den Rekursions-Stack, zuzüglich des Platzes, der zum Speichern des massiven $O(2^N)$ Ausgabe-Arrays erforderlich ist.

## Varianten & Optimierungen

- **Memoization (DP + Backtracking Hybrid):** Der reine Backtracking-Algorithmus führt zu einem TLE (Time Limit Exceeded), wenn der String sehr groß ist und viele ungültige Zweige enthält! Wir können die rekursive Funktion mit Memoization versehen. Anstatt `current_sentence` nach unten zu reichen und `pop` zu verwenden, lassen wir `backtrack(start_index)` eine Liste aller gültigen Suffix-Strings ab diesem Index ZURÜCKGEBEN! Wir speichern dieses Ergebnis in einem Dictionary `memo[start_index]`. Dies verhindert vollständig, dass derselbe ungültige Suffix mehrfach untersucht wird!

## Anwendungen in der Praxis

- **Natural Language Processing:** Wiederherstellen von Leerzeichen in zusammenhängenden Hashtags, URLs oder Sprachen, die natürlicherweise keine Leerzeichen verwenden (wie kontinuierlicher chinesischer/japanischer Text), um alle grammatikalisch gültigen Interpretationen des Textes zu finden.

## Verwandte Algorithmen in cOde(n)

- **[dp_15 - Word Break](../dynamic/dp_15_word-break.md)** — Die DP-Version, die nur einen booleschen Wert `True`/`False` zurückgibt, ob es möglich ist, und in strikter $O(N^3)$ oder $O(N^2)$ Zeit läuft.
- **[backtrack_03 - Combination Sum](backtrack_03_combination-sum.md)** — Ein weiterer Algorithmus, bei dem sich die Größe der Auswahlmöglichkeiten dynamisch basierend auf einer Zielsumme/-länge ändert.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*