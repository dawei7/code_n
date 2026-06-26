# Group Anagrams

| | |
|---|---|
| **ID** | `hash_04` |
| **Kategorie** | hashing |
| **Komplexität (erforderlich)** | $O(N * K)$ Zeit, $O(N * K)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) |

## Problemstellung

Gegeben ist ein Array von Strings `strs`. Gruppieren Sie die Anagramme zusammen. Sie können das Ergebnis in einer beliebigen Reihenfolge zurückgeben.
Ein Anagramm ist ein Wort oder eine Phrase, das bzw. die durch das Umstellen der Buchstaben eines anderen Wortes oder einer anderen Phrase gebildet wird, wobei typischerweise alle ursprünglichen Buchstaben genau einmal verwendet werden.

**Eingabe:** Ein Array von Strings `strs`.
**Ausgabe:** Ein 2D-Array von Strings, wobei jedes innere Array Strings enthält, die Anagramme voneinander sind.

## Wann man es verwendet

- Um Elemente basierend auf einem definierenden, permutationsinvarianten Merkmal zu gruppieren.
- Wenn das Sortieren von Strings zu lange dauert ($O(K log K)$ pro String) und Sie einen linearen $O(K)$-Weg benötigen, um eine eindeutige Signatur zu generieren.

## Ansatz

**1. Der kanonische Schlüssel:**
Eine Hash Map eignet sich hervorragend zum Gruppieren von Elementen. Der schwierige Teil besteht darin, herauszufinden, was der `key` sein sollte!
Für Anagramme müssen `"eat"`, `"tea"` und `"ate"` alle auf denselben Schlüssel abgebildet werden.
- *Methode 1 (Sortieren):* Wenn wir alle drei Strings alphabetisch sortieren, werden sie alle zu `"aet"`. Wir können `"aet"` als Dictionary-Schlüssel verwenden! Aber das Sortieren eines Strings der Länge K benötigt $O(K log K)$ Zeit.
- *Methode 2 (Zeichenzählung):* Anstatt zu sortieren, können wir einfach die Häufigkeiten der 26 englischen Kleinbuchstaben zählen. `"eat"` hat 1 'a', 1 'e' und 1 't'. Wir können dies als ein Tupel von 26 Ganzzahlen darstellen: `(1, 0, 0, 0, 1, 0..., 1, 0)`.

**2. Die Gruppierung mittels Hash Map:**
Wir initialisieren eine Hash Map, die ein `Tuple` auf eine `List of Strings` abbildet.
Wir iterieren durch jeden String im Array.
Wir generieren dessen Zeichenzählungs-Tupel in $O(K)$ Zeit.
Wir verwenden dieses Tupel als Schlüssel in der Hash Map und hängen den ursprünglichen String an die entsprechende Liste an.
Schließlich geben wir einfach alle `values` aus der Hash Map zurück!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for hash_04: Group Anagrams.

Two strings are anagrams iff their sorted characters are equal.
Use a dict keyed on the sorted-tuple; collect the original
strings into per-key lists. Sort each group's inner list and
the outer list of group keys so the verify can compare
directly. O(n * k log k) where k is the string length.
"""


def solve(strs, n):
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        groups.setdefault(key, []).append(s)
    out = []
    for key in groups:
        out.append(sorted(groups[key]))
    out.sort(key=lambda g: g[0])
    return out
```

</details>

## Durchlauf

`strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`

1. `s = "eat"`:
   - Zähl-Array: `a:1, e:1, t:1`. (Alle anderen 0).
   - `key = (1, 0, 0, 0, 1, ..., 1, 0)`.
   - `map[key] = ["eat"]`.
2. `s = "tea"`:
   - Zähl-Array: `a:1, e:1, t:1`.
   - `key = (1, 0, 0, 0, 1, ..., 1, 0)`. Stimmt exakt überein!
   - `map[key] = ["eat", "tea"]`.
3. `s = "tan"`:
   - Zähl-Array: `a:1, n:1, t:1`.
   - `key_2 = (1, 0, 0, ..., 1, ..., 1, 0)`.
   - `map[key_2] = ["tan"]`.
4. `s = "ate"`:
   - Stimmt mit `key` überein. `map[key] = ["eat", "tea", "ate"]`.
5. `s = "nat"`:
   - Stimmt mit `key_2` überein. `map[key_2] = ["tan", "nat"]`.
6. `s = "bat"`:
   - Zähl-Array: `a:1, b:1, t:1`.
   - `key_3 = (1, 1, 0, ..., 1, 0)`.
   - `map[key_3] = ["bat"]`.

Rückgabe der `values`: `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N * K)$ | $O(N * K)$ |
| **Durchschnittlicher Fall** | $O(N * K)$ | $O(N * K)$ |
| **Schlechtester Fall** | $O(N * K)$ | $O(N * K)$ |

Sei N die Anzahl der Strings und K die maximale Länge eines Strings.
Das Zählen der Zeichen für einen String benötigt $O(K)$ Zeit. Das Generieren des Tupels benötigt $O(26) = O(1)$ Zeit. Das Einfügen in die Hash Map benötigt $O(1)$ Zeit.
Wir führen dies N-mal durch. Die gesamte Zeitkomplexität beträgt strikt $O(N \cdot K)$.
*(Hinweis: Wenn wir die Sortiermethode verwenden würden, wäre die Zeitkomplexität $O(N \cdot K log K)$).*
Die Platzkomplexität beträgt $O(N \cdot K)$, um die Strings in der Hash Map und im Ausgabe-Array zu speichern.

## Varianten & Optimierungen

- **Primzahlmultiplikation:** Ein weiterer (mathematisch riskanter) Weg, einen $O(K)$-Schlüssel zu generieren, besteht darin, die 26 Buchstaben auf die ersten 26 Primzahlen abzubilden (`a=2, b=3, c=5...`). Das Produkt der Primzahlen der Zeichen ergibt eine eindeutige Ganzzahl, die garantiert für alle Anagramme gleich ist (aufgrund des Fundamentalsatzes der Arithmetik). Für Strings, die länger als ca. 15 Zeichen sind, übersteigt dieses Produkt jedoch schnell die Standard-Limits für 64-Bit-Ganzzahlen!

## Anwendungen in der Praxis

- **Kryptographie & Sicherheit:** Gruppierung von Variationen von Passwörtern oder Fuzzing-Eingaben, die identische Zeichenentropien aufweisen, um Schwachstellen bei Wörterbuchangriffen zu analysieren.

## Verwandte Algorithmen in cOde(n)

- **[hash_01 - Two Sum](hash_01_two-sum.md)** — Die grundlegende Einführung in die Verwendung von Hash Maps für $O(1)$-Lookups.
- **[string_02 - Valid Anagram](../string/string_02_valid-anagram.md)** — Die 1-zu-1-Vergleichsversion dieses Problems unter Verwendung exakt desselben Zeichenzählungs-Arrays.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*