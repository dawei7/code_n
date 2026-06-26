# Anagram Check

| | |
|---|---|
| **ID** | `string_01` |
| **Kategorie** | strings |
| **Komplexität (erforderlich)** | $O(N)$ |
| **Schwierigkeit** | 1/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) |

## Problemstellung

Gegeben sind zwei Strings `s` und `t`. Geben Sie `True` zurück, falls `t` ein Anagramm von `s` ist, andernfalls `False`.
Ein **Anagramm** ist ein Wort oder eine Phrase, die durch Umstellen der Buchstaben eines anderen Wortes oder einer anderen Phrase gebildet wird, wobei typischerweise alle ursprünglichen Buchstaben genau einmal verwendet werden.

**Eingabe:** Zwei Strings `s` und `t`.
**Ausgabe:** Ein boolescher Wert, der angibt, ob es sich um Anagramme handelt.

**Beispiel 1:**
`s = "anagram"`, `t = "nagaram"`
Ausgabe: `True`.

**Beispiel 2:**
`s = "rat"`, `t = "car"`
Ausgabe: `False`.

## Anwendung

- Um zu bestimmen, ob zwei Strings exakt dieselben Zeichenhäufigkeiten aufweisen.
- Dies ist das grundlegendste Einführungsproblem zum Verständnis von **Hash Maps** oder **Frequency Arrays** bei der String-Verarbeitung.

## Ansatz

Der naive Ansatz besteht darin, beide Strings zu sortieren und sie zu vergleichen: `return sort(s) == sort(t)`. Dies benötigt $O(N \log N)$ Zeit. Wir können das effizienter lösen!

Da ein Anagramm lediglich bedeutet, dass beide Strings für jeden Buchstaben die exakt gleiche Anzahl aufweisen, können wir die Häufigkeiten der Zeichen in $O(N)$ Zeit zählen.

1. **Längenprüfung:** Wenn `length(s) != length(t)`, können sie keine Anagramme sein. Geben Sie `False` zurück.
2. **Frequency Array:** Erstellen Sie ein Array (oder eine Hash Map) der Größe 26 (falls die Strings nur englische Kleinbuchstaben enthalten).
3. Iterieren Sie gleichzeitig durch beide Strings unter Verwendung eines Index `i`.
   - Erhöhen Sie den Zähler für das Zeichen `s[i]`.
   - Verringern Sie den Zähler für das Zeichen `t[i]`.
4. Iterieren Sie nach der Schleife durch das Frequency Array. Wenn ein Zähler nicht exakt `0` ist, weisen die Strings eine Diskrepanz in der Zeichenhäufigkeit auf. Geben Sie `False` zurück.
5. Wenn alle Zähler `0` sind, geben Sie `True` zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_01: Anagram Check.

Check whether two strings are anagrams (same character counts).
"""


def solve(s, t):
    return sorted(s) == sorted(t)
```

</details>

## Durchlauf

`s = "cat"`, `t = "act"`.
`counts = [0, 0, 0, ..., 0]` (Größe 26).

**i = 0:**
`s[0] = 'c'` (Index 2). `counts[2] += 1`.
`t[0] = 'a'` (Index 0). `counts[0] -= 1`.
Array-Zustand: `[-1, 0, 1, ...]`

**i = 1:**
`s[1] = 'a'` (Index 0). `counts[0] += 1`. (Wird 0).
`t[1] = 'c'` (Index 2). `counts[2] -= 1`. (Wird 0).
Array-Zustand: `[0, 0, 0, ...]`

**i = 2:**
`s[2] = 't'` (Index 19). `counts[19] += 1`.
`t[2] = 't'` (Index 19). `counts[19] -= 1`. (Wird 0).
Array-Zustand: `[0, 0, 0, ...]`

Die Schleife endet. Alle Werte in `counts` sind 0. Rückgabe `True`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Die Zeitkomplexität beträgt $O(N)$, wobei N die Länge des Strings ist. Wir durchlaufen die Strings einmal und das feste Array mit 26 Elementen einmal. (Der Bestfall ist $O(1)$, wenn sich die Längen unterscheiden).
Die Platzkomplexität ist $O(1)$, da die Größe des `char_counts`-Arrays immer 26 beträgt, unabhängig davon, wie groß N wird. *(Wenn die Strings beliebige Unicode-Zeichen enthalten, würde eine Hash Map $O(K)$ Platz benötigen, wobei K die Anzahl der eindeutigen Zeichen ist).*

## Varianten & Optimierungen

- **Group Anagrams:** Gegeben ein Array von Strings, gruppieren Sie die Anagramme. Anstatt eines Arrays von 26 Ganzzahlen konvertieren Sie das Frequency Array in einen String oder ein Tupel (z. B. `(1, 0, 1, 0...)`) und verwenden es als Schlüssel in einer Hash Map, die auf eine Liste von Strings verweist!
- **Find All Anagrams in a String:** Finden Sie alle Startindizes der Anagramme von `p` in `s`. Dies erfordert die Kombination des Frequency Arrays mit einem **Sliding Window** der Größe `length(p)`.

## Anwendungen in der Praxis

- **Kryptographie (Permutationschiffren):** Überprüfung, ob ein Geheimtext potenziell eine einfache Permutation (Anagramm) eines bekannten Klartextes sein könnte, indem deren Häufigkeitshistogramme verglichen werden.

## Verwandte Algorithmen in cOde(n)

- **[string_08 - Smallest Window](string_08_smallest-window.md)** — Basiert maßgeblich auf der Pflege und dem Vergleich von Zeichenhäufigkeits-Arrays.
- **[hashing_01 - Hash Map](../hashing/hashing_01_hash-map-chaining.md)** — Die Datenstruktur, die verwendet wird, wenn Zeichen nicht auf das englische Alphabet beschränkt sind.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*