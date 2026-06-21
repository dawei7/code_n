# Z-Algorithmus Mustersuche

| | |
|---|---|
| **ID** | `string_13` |
| **Kategorie** | Strings |
| **Komplexität (erforderlich)** | $O(N + M)$ Zeit, $O(N + M)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **GeeksForGeeks Äquivalent** | [Z algorithm (Linear time pattern searching Algorithm)](https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/) |

## Problemstellung

Gegeben ist ein `text`-String der Länge N und ein `pattern`-String der Länge M.
Finde alle Startindizes, an denen das `pattern` als zusammenhängender Teilstring innerhalb des `text` vorkommt.
Dies muss mathematisch garantiert in $O(N + M)$ Zeit unter Verwendung des Z-Algorithmus gelöst werden.

**Eingabe:** Zwei Strings `text` und `pattern`.
**Ausgabe:** Ein Array von Integern, die die Startindizes der Übereinstimmungen repräsentieren.

## Wann man ihn verwendet

- Bei der Mustersuche, wenn man den am einfachsten zu implementierenden Algorithmus mit mathematisch garantierter $O(N+M)$-Laufzeit sucht (im Vergleich zum mühsamen Implementieren des LPS-Arrays bei KMP).

## Ansatz

**1. Die magische Konkatenation:**
Der Z-Algorithmus berechnet ein Array, in dem `Z[i]` die Länge des längsten Teilstrings ist, der bei `S[i]` beginnt und exakt mit dem Präfix von `S` übereinstimmt.
Wenn unser Ziel darin besteht, `pattern` innerhalb von `text` zu finden, was wäre, wenn wir das `pattern` gewaltsam zum Präfix von `S` machen?
Wir erstellen einen neuen konkatenierten String: `S = pattern + "$" + text`.
(Das `$` ist ein spezielles Trennzeichen, das weder im `pattern` noch im `text` vorkommen darf).

**2. Die Trennzeichen-Barriere:**
Warum das `$`?
Ohne dieses Zeichen könnte eine Übereinstimmung im Text versehentlich "überlaufen" und Teile des Textes *hinter* dem Muster abgleichen. Durch das Platzieren von `$` direkt nach dem Muster garantieren wir, dass der maximal mögliche Z-Wert im gesamten String exakt M (die Länge des Musters) beträgt. Das `$` blockiert physisch, dass die Übereinstimmung weitergeht.

**3. Ausführung der Suche:**
1. Konkateniere `S = pattern + "$" + text`.
2. Führe den Standard $O(K)$ Z-Algorithmus auf `S` aus (wobei K = N + M + 1).
3. Iteriere durch das resultierende Z-Array. Wenn du einen Index `i` findest, an dem `Z[i] == M` (die Länge des Musters) gilt, bedeutet dies, dass du eine perfekte Übereinstimmung gefunden hast!
4. Berechne den ursprünglichen Index im `text`: `text_index = i - M - 1`. Füge diesen zu deinen Ergebnissen hinzu!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_13: Z-Algorithm (Pattern Search).

Build the Z-array of pattern + '$' + s, then collect
positions where Z[i] == |pattern| in the s region.
"""


def solve(s, n, pattern, m):
    if m == 0 or n == 0:
        return []
    combined = pattern + "$" + s
    L = len(combined)
    z = [0] * L
    left = 0
    right = 0
    for i in range(1, L):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < L and combined[z[i]] == combined[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    out = []
    for i in range(m + 1, L):
        if z[i] == m:
            out.append(i - m - 1)
    return out
```

</details>

## Durchlauf

`text = "aabzaa"`, `pattern = "aa"`. M = 2.
`S = "aaaabzaa"`.

1. Z-Algorithmus auf `S` ausführen:
   - `Z[0] = 9` (Länge des gesamten Strings).
   - `Z[1] = 1` (`"aaabzaa"` stimmt mit `"a"` überein).
   - `Z[2] = 0` (`"aabzaa"` stimmt mit nichts überein).
   - `Z[3] = 2` (`"aabzaa"` stimmt perfekt mit `"aa"` überein! Blockiert durch `b` vs `$`).
   - `Z[4] = 1` (`"abzaa"` stimmt mit `"a"` überein).
   - `Z[5] = 0` (`"bzaa"` stimmt mit nichts überein).
   - `Z[6] = 0` (`"zaa"` stimmt mit nichts überein).
   - `Z[7] = 2` (`"aa"` stimmt perfekt mit `"aa"` überein!).
   - `Z[8] = 1` (`"a"` stimmt mit `"a"` überein).
   Z-Array: `[9, 1, 0, 2, 1, 0, 0, 2, 1]`.
2. Z-Array ab Index M+1 = 3 scannen:
   - `Z[3] == 2` (M). Treffer! Ursprünglicher Index = 3 - 2 - 1 = 0. `matches = [0]`.
   - `Z[4] == 1`.
   - `Z[5] == 0`.
   - `Z[6] == 0`.
   - `Z[7] == 2` (M). Treffer! Ursprünglicher Index = 7 - 2 - 1 = 4. `matches = [0, 4]`.
   - `Z[8] == 1`.
3. Rückgabe `[0, 4]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N + M)$ | $O(N + M)$ |
| **Durchschnittlicher Fall** | $O(N + M)$ | $O(N + M)$ |
| **Schlechtester Fall** | $O(N + M)$ | $O(N + M)$ |

Das Erstellen des konkatenierten Strings benötigt $O(N + M)$ Zeit.
Die Ausführung des Z-Algorithmus benötigt strikt lineare Zeit proportional zur Länge des Strings: $O(N + M)$.
Das Scannen des resultierenden Arrays benötigt $O(N)$ Zeit.
Die gesamte Zeitkomplexität ist mathematisch garantiert $O(N + M)$, unabhängig von bösartigen Eingaben, im Gegensatz zu Rabin-Karp.
Die Platzkomplexität beträgt $O(N + M)$, um den physisch konkatenierten String und das resultierende Z-Array zu speichern. (KMP ist hier etwas effizienter, da sein Hilfsarray nur die Größe M hat).

## Varianten & Optimierungen

- **Rolling Z-Box ($O(M)$ Platz):** Man muss den String nicht tatsächlich physisch konkatenieren und ein massives Z-Array der Größe N+M aufbauen. Man kann zuerst das Z-Array für das Muster `Z_pat` berechnen. Dann schiebt man die Z-Box konzeptionell über den `text`, schlägt Werte aus `Z_pat` nach, wenn man sich innerhalb der Box befindet, und führt manuelle Vergleiche durch, wenn man außerhalb ist. Dies reduziert die Platzkomplexität auf strikt $O(M)$!

## Anwendungen in der Praxis

- **DNA-Subsequenz-Abgleich:** Finden aller Vorkommen einer spezifischen Gensequenz (das Muster) innerhalb einer riesigen Chromosomendatei (der Text).

## Verwandte Algorithmen in cOde(n)

- **[string_07 - Z Algorithm](string_07_z-algorithm.md)** — Die Engine, die diesen Suchalgorithmus antreibt.
- **[string_03 - KMP Pattern Matching](string_03_kmp-string-matching.md)** — Der andere $O(N+M)$-Suchalgorithmus, der auf dem "Longest Proper Prefix which is also Suffix"-Array basiert, anstatt auf direktem Abgleich.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*