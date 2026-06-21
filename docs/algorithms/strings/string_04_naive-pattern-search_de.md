# Naive Pattern Search

| | |
|---|---|
| **ID** | `string_04` |
| **Kategorie** | strings |
| **Komplexität (erforderlich)** | $O(N * M)$ |
| **Schwierigkeit** | 1/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **LeetCode-Äquivalent** | [Implement strStr()](https://leetcode.com/problems/implement-strstr/) |

## Problemstellung

Gegeben sind zwei Strings: ein `text` der Länge `N` und ein `pattern` der Länge `M`.
Finde alle Startindizes im `text`, an denen das `pattern` als zusammenhängender Teilstring existiert.

**Eingabe:** Zwei Strings `text` und `pattern`.
**Ausgabe:** Eine Liste von Integern, die die Startindizes der Übereinstimmungen repräsentieren.

**Beispiel:**
`text = "AABAACAADAABAABA"`, `pattern = "AABA"`
Ausgabe: `[0, 9, 12]`.

## Wann sollte man es verwenden?

- Wenn das `pattern` sehr kurz ist (z. B. M \le 5) oder der `text` sehr kurz ist, wodurch der Overhead für den Aufbau komplexer Hilfsdatenstrukturen (wie das LPS-Array bei KMP) unnötig wird.
- Als Brute-Force-Basisalgorithmus, um das exakte Problem zu verstehen, das KMP und Rabin-Karp zu lösen versuchen.

## Ansatz

Wir richten das `pattern` einfach am `text` beginnend bei Index 0 aus. Wir prüfen Zeichen für Zeichen.
- Wenn alle Zeichen übereinstimmen, notieren wir den Startindex.
- Wenn an irgendeiner Stelle eine Nichtübereinstimmung auftritt, brechen wir den aktuellen Vergleich vollständig ab, verschieben das `pattern` um genau 1 Stelle nach rechts und beginnen den Vergleich erneut ab dem ersten Zeichen des `pattern`.

Wir wiederholen diesen Prozess bis zum Ende des `text`. Die letzte gültige Startposition für das `pattern` ist der Index `N - M`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_04: Naive Pattern Search.

Slide the pattern across the text, compare character-by-character.
"""


def solve(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i
    return -1
```

</details>

## Durchlauf

`text = "ABCA"`, `pattern = "BC"`.
`N = 4, M = 2`. Schleife `i` von `0` bis `4 - 2 = 2`.

**i = 0:**
- Vergleiche `text[0]` ('A') mit `pattern[0]` ('B').
- Nichtübereinstimmung! Abbruch.

**i = 1:**
- Vergleiche `text[1]` ('B') mit `pattern[0]` ('B'). Übereinstimmung!
- Vergleiche `text[2]` ('C') mit `pattern[1]` ('C'). Übereinstimmung!
- Schleife beendet. `match_found = True`. Füge `1` zum Ergebnis hinzu.

**i = 2:**
- Vergleiche `text[2]` ('C') mit `pattern[0]` ('B').
- Nichtübereinstimmung! Abbruch.

Ausgabe: `[1]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N * M)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N * M)$ | $O(1)$ |

Die äußere Schleife läuft N - M + 1 Mal.
Die innere Schleife läuft bis zu M Mal.
Im schlechtesten Fall (z. B. `text = "AAAAAAAAAB"`, `pattern = "AAAB"`) prüft die innere Schleife fast das gesamte `pattern` erfolgreich, bevor sie beim allerletzten Zeichen fehlschlägt, was zu exakt $O(N \times M)$ Vergleichen führt.
Die Platzkomplexität beträgt $O(1)$ (abgesehen vom Speicherplatz für die zurückgegebene Liste der gefundenen Indizes).

## Varianten & Optimierungen

- **Sprachinterne Funktionen:** In fast allen Hochsprachen sind die eingebauten String-Suchfunktionen (z. B. `text.find(pattern)` in Python oder `text.indexOf(pattern)` in Java) hochgradig optimiert. Während sie bei kleinen Strings konzeptionell auf eine naive Suche zurückgreifen könnten, verwenden sie unter der Haube SIMD-Instruktionen oder Varianten des Boyer-Moore-Algorithmus. Für Coding-Interviews sollten Sie die eingebauten Funktionen verwenden, es sei denn, Sie werden explizit aufgefordert, einen Pattern-Matching-Algorithmus von Grund auf zu implementieren.

## Anwendungen in der Praxis

- **Kleine Textausschnitte:** Da Algorithmen wie KMP und Rabin-Karp einen Overhead haben (Speicherallokation für Arrays oder aufwendige Modulo-Arithmetik), ist die naive Suche in der Praxis bei der Suche nach sehr kurzen Strings tatsächlich die strikt schnellere und optimalere Wahl.

## Verwandte Algorithmen in cOde(n)

- **[string_03 - KMP String Matching](string_03_kmp-string-matching.md)** — Die optimierte $O(N+M)$-Version, die redundante Prüfungen überspringt.
- **[string_06 - Rabin-Karp](string_06_rabin-karp.md)** — Eine optimierte Version, die Rolling Hashes verwendet, um die Prüfungen der inneren Schleife zu überspringen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*