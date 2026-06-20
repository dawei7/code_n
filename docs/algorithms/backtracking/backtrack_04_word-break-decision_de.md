# Worttrennung II (Backtracking)

| | |
|---|---|
| **ID** | `backtrack_04` |
| **Kategorie** | Backtracking |
| **Komplexität (erforderlich)** | $O(N^2 + 2^N)$ Zeit, $O(N + 2^N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Word Break II](https://leetcode.com/problems/word-break-ii/) |

## Aufgabenstellung

Gegeben sei eine Zeichenkette `s` und ein Wörterbuch mit Zeichenketten `wordDict`. Füge Leerzeichen an den Stellen `s` ein, um einen Satz zu bilden, in dem jedes Wort ein gültiges Wort aus dem Wörterbuch ist. Gib alle möglichen Sätze in beliebiger Reihenfolge zurück.
Beachte, dass dasselbe Wort aus dem Wörterbuch bei der Segmentierung mehrfach verwendet werden darf.

**Eingabe:** Eine Zeichenkette `s` und eine Liste von Zeichenketten `wordDict`.
**Ausgabe:** Eine Liste von Zeichenketten, wobei jede Zeichenkette ein durch Leerzeichen getrennter gültiger Satz ist.

## Wann man es verwendet

- Um ALLE möglichen gültigen Segmentierungen oder Partitionen einer Sequenz auf der Grundlage einer deterministischen Validierungsregel zu finden.
- Es lässt sich perfekt mit der dynamischen Programmierung (`dp_15_word-break.md`) kombinieren, wobei die dynamische Programmierung die Frage „Ist es möglich?“ beantwortet und das Backtracking die Frage „Was sind alle exakten Pfade?“ beantwortet.

## Vorgehensweise

**1. Der Entscheidungsbaum:**
An jeder Stelle der Zeichenkette `s`, beginnend am Index `start`, schauen wir nach vorne, um zu prüfen, ob das Präfix `s[start...i]` in `wordDict` ein gültiges Wort bildet.
Ist dies der Fall, haben wir einen gültigen „Trennpunkt“ gefunden! Wir fügen dieses Wort unserem aktuellen Satz hinzu und verzweigen rekursiv, um den Rest der Zeichenkette ab Index `i + 1` zu verarbeiten.
Da wir JEDEN gültigen Schnittpunkt untersuchen müssen, wird eine Zeichenkette, die ausschließlich aus „a“ besteht und mit einem Wörterbuch von `["a", "aa", "aaa"]` abgeglichen wird, in $O(2^N)$ Verzweigungen explodieren!

**2. Der Backtracking-Zustand:**
`backtrack(start_index, current_sentence)`:
- `start_index`: Der Index in der Zeichenkette `s`, an dem die noch nicht analysierte verbleibende Teilzeichenkette beginnt.
- `current_sentence`: Eine Liste der Wörter, die wir bisher erfolgreich analysiert haben.

**3. Basisfall:**
Wenn `start_index == len(s)`, bedeutet dies, dass wir die GESAMTE Zeichenkette erfolgreich in gültige Wörter des Wörterbuchs zerlegt haben!
Wir fügen die Wörter in `current_sentence` mit einem Leerzeichen `" ".join(...)` zusammen und hängen sie an unsere globale Ergebnisliste an.

**4. Der rekursive Schritt:**
Schleife `i` von `start_index + 1` bis `len(s) + 1` (da das String-Slicing in Python am Ende exklusiv ist).
- Extrahiere die Teilzeichenfolge: `word = s[start_index : i]`.
- Wenn `word` in `wordDict` enthalten ist:
  - **Entscheidung treffen:** `word` an `current_sentence` anhängen.
  - **Rekursiv:** Rufe `backtrack(i, current_sentence)` auf.
  - **Backtrack:** Entferne `word` aus `current_sentence`, damit wir in der nächsten Schleifeniteration einen anderen, längeren Schnittpunkt ausprobieren können.

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

## Schritt-für-Schritt-Anleitung

`s = "catsanddog"`, `word_dict = ["cat", "cats", "and", "sand", "dog"]`.

1. `backtrack(0, [])`:
   - `i = 1, 2`: „c“, „ca“ nicht im Wörterbuch.
   - `i = 3`: „cat“ ist im Wörterbuch! Anfügen.
 - `backtrack(3, ["cat"])`:
 - `i = 4, 5, 6`: „s“, „sa“, „san“ nicht im Wörterbuch.
       - `i = 7`: „sand“ ist im Wörterbuch! Anfügen.
 - `backtrack(7, ["cat", "sand"])`:
 - `i = 8, 9`: „d“, „do“ nicht im Wörterbuch.
           - `i = 10`: „dog“ ist im Wörterbuch! Anfügen.
 - `backtrack(10, ["cat", "sand", "dog"])`: BASISFALL! `"cat sand dog"` an das Ergebnis anhängen.
           - Zurückgehen -> „dog“ entfernen.
 - Zurückgehen -> „sand“ entfernen.
   - `i = 4`: „cats“ ist im Wörterbuch! Anfügen.
 - `backtrack(4, ["cats"])`:
       - `i = 5, 6`: „a“, „an“ nicht im Wörterbuch.
 - `i = 7`: „and“ ist im Wörterbuch! Anfügen.
 - `backtrack(7, ["cats", "and"])`:
           - `i = 8, 9`: „d“, „do“ nicht im Wörterbuch.
 - `i = 10`: „dog“ ist im Wörterbuch! Anfügen.
 - `backtrack(10, ["cats", "and", "dog"])`: BASISFALL! `"cats and dog"` an das Ergebnis anhängen.
 - Rückverfolgung -> „dog“ entfernen.
 - Rückverfolgung -> „and“ entfernen.
   - `i = 5..10`: „catsa“ usw. nicht im Wörterbuch.

Ergebnis: `["cat sand dog", "cats and dog"]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(N^2)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(2^N)$ | $O(2^N)$ |
| **Schlechtester Fall** | $O(N^2 + 2^N)$ | $O(N + 2^N)$ |

*Dabei ist N die Länge der Zeichenkette.*
Im schlimmsten Fall (z. B. `s = "aaaaaa"`, `dict = ["a", "aa", "aaa"]`) ist jede einzelne Zeichengrenze ein gültiger Schnittpunkt. Dadurch entstehen genau 2^{N-1} gültige Sätze! Das Rekonstruieren und Zusammenfügen der Zeichenketten dauert $O(N)$, was zu einer Laufzeit von $O(N \cdot 2^N)$ führt.
Wenn die Zeichenkette überhaupt nicht segmentiert werden kann, dauert es $O(N^2)$, um Präfixe zu prüfen und die Aufgabe abzubrechen.
Die Platzkomplexität beträgt $O(N)$ für den Rekursionsstapel, zuzüglich des Speicherplatzes, der zum Speichern des $O(2^N)$ riesigen Ausgabe-Arrays benötigt wird.

## Varianten & Optimierungen

- **Memoisation (Hybrid aus DP und Backtracking):** Der reine Backtracking-Algorithmus führt zu einem TLE (Time Limit Exceeded), wenn die Zeichenkette sehr groß ist und viele ungültige Verzweigungen enthält! Wir können die rekursive Funktion memoisieren. Anstatt `current_sentence` nach unten zu übergeben und zu entfernen, lassen wir `backtrack(start_index)` eine Liste aller gültigen Suffix-Strings ab diesem Index RETURNEN! Wir speichern dieses Ergebnis in einem Wörterbuch `memo[start_index]`. Dadurch wird vollständig verhindert, dass dasselbe ungültige Suffix zweimal untersucht wird!

## Anwendungen in der Praxis

- **Verarbeitung natürlicher Sprache:** Rekonstruktion von Leerzeichen in gekürzten Hashtags, URLs oder Sprachen, die von Natur aus keine Leerzeichen verwenden (wie zusammenhängender chinesischer oder japanischer Text), um alle grammatikalisch gültigen Interpretationen des Textes zu finden.

## Verwandte Algorithmen in cOde(n)

- **[dp_15 – Worttrennung](../dynamic/dp_15_word-break.md)** — Die DP-Version, die nur einen booleschen Wert `True`/`False` zurückgibt, sofern dies möglich ist, und in streng $O(N^3)$- oder $O(N^2)$-Zeit läuft.
- **[backtrack_03 - Combination Sum](backtrack_03_combination-sum.md)** — Ein weiterer Algorithmus, bei dem sich die Anzahl der Auswahlmöglichkeiten dynamisch in Abhängigkeit von einer angestrebten Summe/Länge ändert.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
