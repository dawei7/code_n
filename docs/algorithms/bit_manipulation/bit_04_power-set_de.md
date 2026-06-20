# Potenzmenge (bitweise Optimierung)

| | |
|---|---|
| **ID** | `bit_04` |
| **Kategorie** | Bitmanipulation |
| **Komplexität (erforderlich)** | $O(N * 2^N)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Teilmengen](https://leetcode.com/problems/subsets/) |

## Aufgabenstellung

Gegeben ist ein Ganzzahl-Array `nums` mit **eindeutigen** Elementen. Gib alle möglichen Teilmengen (die Potenzmenge) zurück.
Die Lösungsmenge darf keine doppelten Teilmengen enthalten. Geben Sie die Lösung in beliebiger Reihenfolge zurück.
*Einschränkung:* Sie müssen diese Aufgabe vollständig iterativ lösen, ohne Rekursion oder Backtracking zu verwenden.

**Eingabe:** Ein Array von Ganzzahlen `nums`.
**Ausgabe:** Eine Liste von Listen, wobei jede innere Liste eine gültige Teilmenge ist.

## Wann man es verwendet

- Um Kombinationen blitzschnell in einer Wettbewerbsumgebung für Programmierer zu generieren, in der der Overhead durch Rekursion zu „Time Limit Exceeded“ (TLE)-Fehlern führt.
- Es belegt dein Verständnis dafür, wie Binärzahlen von Natur aus auf Auswahlzustände abgebildet werden.

## Vorgehensweise

**1. Die binäre Abbildung:**
Beim Backtracking-Ansatz (`backtrack_01`) haben wir für jedes einzelne Element eine Entscheidung zum „Einbeziehen“ oder „Ausschließen“ getroffen. Das sind 2 Auswahlmöglichkeiten pro Element.
Beachte, dass eine Binärzahl ebenfalls genau 2 Zustände pro Bit hat: `1` (Einbeziehen) und `0` (Ausschließen)!
Wenn ein Array N = 3 Elemente hat, gibt es genau 2^3 = 8 Teilmengen.
Zählen wir von `0` bis `7` im Binärsystem:
- `0` = `000` -> Alle ausschließen -> `[]`
- `1` = `001` -> 3. einbeziehen -> `[nums[2]]`
- `2` = `010` -> 2. einbeziehen -> `[nums[1]]`
- `3` = `011` -> 2. und 3. einbeziehen -> `[nums[1], nums[2]]`
- `4` = `100` -> 1. einbeziehen -> `[nums[0]]`
- `5` = `101` -> 1. und 3. einbeziehen -> `[nums[0], nums[2]]`
- `6` = `110` -> 1. und 2. einbeziehen -> `[nums[0], nums[1]]`
- `7` = `111` -> Alle einbeziehen -> `[nums[0], nums[1], nums[2]]`

Jede einzelne Zahl von 0 bis 2^N - 1 stellt perfekt eine eindeutige, gültige Teilmenge dar!

**2. Die Bitmasken-Strategie:**
1. Berechne die Gesamtzahl der Teilmengen: `total = 1 << n`. (Diese beträgt 2^N).
2. Durchlaufen Sie die Variable `mask` von `0` bis `total - 1`.
3. Für einen bestimmten `mask` müssen wir herausfinden, welche Bits auf `1` gesetzt sind.
   Wir durchlaufen einen Index `i` von `0` bis `n - 1`.
   Um zu prüfen, ob das i-te Bit von `mask` ein `1` ist, verschieben wir ein `1` um `i` Positionen nach links (`1 << i`), und führen eine bitweise UND-Verknüpfung durch!
   Wenn `(mask & (1 << i)) != 0`, nehmen wir `nums[i]` in unsere aktuelle Teilmenge auf!

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

## Schritt-für-Schritt-Anleitung

`nums = [A, B, C]`. N=3.
`total_subsets = 1 << 3 = 8`.

1. **mask = 0 (`000`):**
   - i=0: `000 & 001 == 0`. Überspringen.
   - i=1: `000 & 010 == 0`. Überspringen.
   - i=2: `000 & 100 == 0`. Überspringen.
   - Ergebnis wird angehängt: `[]`.
2. **mask = 3 (`011`):**
   - i=0: `011 & 001 == 1`. Einbeziehen von `nums[0] (A)`.
   - i=1: `011 & 010 == 2`. Einbeziehen von `nums[1] (B)`.
   - i=2: `011 & 100 == 0`. Überspringen.
   - Ergebnis wird angehängt: `[A, B]`.
3. **mask = 5 (`101`):**
   - i=0: `101 & 001 == 1`. `A` einfügen.
   - i=1: `101 & 010 == 0`. Überspringen.
   - i=2: `101 & 100 == 4`. `C` einbeziehen.
   - Ergebnis wird angehängt: `[A, C]`.
4. ... wiederholt sich bis `mask = 7`.

Ergebnis: `[[], [A], [B], [A,B], [C], [A,C], [B,C], [A,B,C]]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N * 2^N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N * 2^N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N * 2^N)$ | $O(1)$ |

Die äußere Schleife läuft genau 2^N Mal. Die innere Schleife läuft genau N Mal. Die bitweisen Prüfungen sind $O(1)$. Die Gesamtzeit ist perfekt auf $O(N x 2^N)$ begrenzt. Dies ist in der Praxis wesentlich schneller als Rekursion, da der Overhead durch den Funktionsaufruf-Stack vermieden wird.
Die Platzkomplexität beträgt $O(1)$ Hilfsspeicher! (Das Ausgabe-Array, das $O(N x 2^N)$ Speicherplatz beansprucht, wird nicht mitgezählt.) Die rekursive Backtracking-Lösung benötigt $O(N)$ Hilfsstapelplatz.

## Varianten & Optimierungen

- **Kombinationen einer bestimmten Größe K (Gosper’s Hack):** Wenn man nur Teilmengen der exakten Größe K (z. B. 3 Elemente) möchte, ist eine vollständige 2^N-Schleife extrem verschwenderisch! Gosper's Hack ist eine bitweise Zauberformel, die eine Bitmaske mit K Einsen nimmt und die *lexikografisch nächste* Bitmaske mit genau K Einsen in streng $O(1)$ Zeit berechnet! Man initialisiert einfach `mask = (1 << k) - 1` und führt dann `mask = gospers_hack(mask)` so lange in einer Schleife aus, bis der Wert 2^N überschreitet.

## Anwendungen in der Praxis

- **Zustandskomprimierung:** Bei hochkomplexen DP-Problemen (wie dem Handlungsreisenden-Problem) wird ein Array besuchter Städte `[True, False, True]` zu einer einzigen Ganzzahl `5` komprimiert (`101`). Dadurch kann der Zustand direkt als Array-Index (`dp[5]`) verwendet werden, was einen blitzschnellen Speicherzugriff ermöglicht.

## Verwandte Algorithmen in cOde(n)

- **[backtrack_01 – Teilmengen](../backtracking/backtrack_01_subset-sum-decision.md)** — Die rekursive Lösung für genau dasselbe Problem.
- **[bit_01 – Count Set Bits](bit_01_count-set-bits.md)** — Grundlegende Konzepte der Bitmaskierung.

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen
Enzyklopädieeintrag finden Sie unter dem Wikipedia-Link oben auf der Seite.
Quell-Repository:
<https://github.com/dawei7/code_n>.*
