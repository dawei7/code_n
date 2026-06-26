# Potenzmenge (Bitweise Optimierung)

| | |
|---|---|
| **ID** | `bit_04` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(N * 2^N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Subsets](https://leetcode.com/problems/subsets/) |

## Problemstellung

Gegeben ist ein Array `nums` mit **eindeutigen** Elementen. Geben Sie alle möglichen Teilmengen (die Potenzmenge) zurück.
Die Lösungsmenge darf keine doppelten Teilmengen enthalten. Die Reihenfolge der Rückgabe ist beliebig.
*Einschränkung:* Sie müssen das Problem vollständig iterativ lösen, ohne Rekursion oder Backtracking zu verwenden.

**Eingabe:** Ein Array `nums`.
**Ausgabe:** Eine Liste von Listen, wobei jede innere Liste eine gültige Teilmenge darstellt.

## Wann man diesen Ansatz verwendet

- Um Kombinationen in einer Competitive-Programming-Umgebung extrem schnell zu generieren, wo rekursiver Overhead zu Time Limit Exceeded (TLE)-Fehlern führt.
- Er beweist Ihr Verständnis dafür, wie Binärzahlen inhärent auf Auswahlzustände abgebildet werden.

## Ansatz

**1. Die binäre Abbildung:**
Beim Backtracking-Ansatz (`backtrack_01`) haben wir für jedes einzelne Element eine "Einschließen"- oder "Ausschließen"-Entscheidung getroffen. Das sind 2 Möglichkeiten pro Element.
Beachten Sie, dass eine Binärzahl ebenfalls genau 2 Zustände pro Bit hat: `1` (Einschließen) und `0` (Ausschließen)!
Wenn ein Array N=3 Elemente hat, gibt es genau 2^3 = 8 Teilmengen.
Zählen wir von `0` bis `7` im Binärsystem:
- `0` = `000` -> Alles ausschließen -> `[]`
- `1` = `001` -> 3. Element einschließen -> `[nums[2]]`
- `2` = `010` -> 2. Element einschließen -> `[nums[1]]`
- `3` = `011` -> 2. und 3. Element einschließen -> `[nums[1], nums[2]]`
- `4` = `100` -> 1. Element einschließen -> `[nums[0]]`
- `5` = `101` -> 1. und 3. Element einschließen -> `[nums[0], nums[2]]`
- `6` = `110` -> 1. und 2. Element einschließen -> `[nums[0], nums[1]]`
- `7` = `111` -> Alles einschließen -> `[nums[0], nums[1], nums[2]]`

Jede einzelne Zahl von 0 bis 2^N - 1 repräsentiert perfekt eine eindeutige, gültige Teilmenge!

**2. Die Bitmasken-Strategie:**
1. Berechnen Sie die Gesamtzahl der Teilmengen: `total = 1 << n`. (Dies entspricht 2^N).
2. Iterieren Sie mit einer Variablen `mask` von `0` bis `total - 1`.
3. Für eine bestimmte `mask` müssen wir herausfinden, welche Bits auf `1` gesetzt sind.
   Wir iterieren mit einem Index `i` von `0` bis `n - 1`.
   Um zu prüfen, ob das i-te Bit von `mask` eine `1` ist, verschieben wir eine `1` um `i` Positionen nach links (`1 << i`) und führen ein bitweises AND aus!
   Wenn `(mask & (1 << i)) != 0`, schließen wir `nums[i]` in unsere aktuelle Teilmenge ein!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_04: Power Set.

Return every subset of the input list as a list
"""


def solve(arr, n):
    """Return every subset of arr as a list of lists."""
    result = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        result.append(subset)
    return result
```

</details>

## Durchlauf

`nums = [A, B, C]`. N=3.
`total_subsets = 1 << 3 = 8`.

1. **mask = 0 (`000`):**
   - i=0: `000 & 001 == 0`. Überspringen.
   - i=1: `000 & 010 == 0`. Überspringen.
   - i=2: `000 & 100 == 0`. Überspringen.
   - Ergebnis fügt hinzu: `[]`.
2. **mask = 3 (`011`):**
   - i=0: `011 & 001 == 1`. Einschließen `nums[0] (A)`.
   - i=1: `011 & 010 == 2`. Einschließen `nums[1] (B)`.
   - i=2: `011 & 100 == 0`. Überspringen.
   - Ergebnis fügt hinzu: `[A, B]`.
3. **mask = 5 (`101`):**
   - i=0: `101 & 001 == 1`. Einschließen `A`.
   - i=1: `101 & 010 == 0`. Überspringen.
   - i=2: `101 & 100 == 4`. Einschließen `C`.
   - Ergebnis fügt hinzu: `[A, C]`.
4. ... Wiederholung bis `mask = 7`.

Ergebnis: `[[], [A], [B], [A,B], [C], [A,C], [B,C], [A,B,C]]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N * 2^N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N * 2^N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N * 2^N)$ | $O(1)$ |

Die äußere Schleife läuft genau 2^N Mal. Die innere Schleife läuft genau N Mal. Die bitweisen Prüfungen sind $O(1)$. Die Gesamtlaufzeit ist perfekt auf $O(N * 2^N)$ begrenzt. Dies ist in der Praxis wesentlich schneller als Rekursion, da der Overhead durch den Funktionsaufruf-Stack vermieden wird.
Die Platzkomplexität beträgt $O(1)$ an zusätzlichem Speicher! (Wir zählen das Ausgabe-Array, das $O(N * 2^N)$ Platz benötigt, nicht mit). Die rekursive Backtracking-Lösung erfordert $O(N)$ zusätzlichen Stack-Speicher.

## Varianten & Optimierungen

- **Kombinationen einer bestimmten Größe K (Gosper's Hack):** Wenn Sie nur Teilmengen der exakten Größe K (z. B. 3 Elemente) benötigen, ist eine vollständige 2^N-Schleife extrem verschwenderisch! Gosper's Hack ist eine bitweise Zauberformel, die eine Bitmaske mit K Einsen nimmt und die *lexikographisch nächste* Bitmaske mit genau K Einsen in strikt $O(1)$ Zeit berechnet! Sie initialisieren einfach `mask = (1 << k) - 1` und führen dann `mask = gospers_hack(mask)` aus, bis der Wert 2^N überschreitet.

## Anwendungen in der Praxis

- **Zustandskomprimierung:** In hochkomplexen DP-Problemen (wie dem Problem des Handlungsreisenden) wird ein Array von besuchten Städten `[True, False, True]` in eine einzelne Ganzzahl `5` (`101`) komprimiert. Dies ermöglicht es, den Zustand direkt als Array-Index (`dp[5]`) für blitzschnellen Speicherzugriff zu verwenden.

## Verwandte Algorithmen in cOde(n)

- **[backtrack_01 - Subsets](../backtracking/backtrack_01_subset-sum-decision.md)** — Die rekursive Lösung für exakt dasselbe Problem.
- **[bit_01 - Count Set Bits](bit_01_count-set-bits.md)** — Grundlegende Konzepte der Bitmaskierung.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Competitive Programming verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*