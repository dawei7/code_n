# Einzelzahl III

| | |
|---|---|
| **ID** | `bit_05` |
| **Kategorie** | Bitmanipulation |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Single Number III](https://leetcode.com/problems/single-number-iii/) |

## Aufgabenstellung

Gegeben ist ein Array von Ganzzahlen `nums`, in dem genau **zwei** Elemente nur einmal und alle anderen Elemente genau zweimal vorkommen. Finde die beiden Elemente, die nur einmal vorkommen. Du kannst die Antwort in beliebiger Reihenfolge zurückgeben.
Du musst einen Algorithmus schreiben, der in linearer Laufzeitkomplexität läuft und nur konstanten zusätzlichen Speicherplatz benötigt.

**Eingabe:** Ein Array von ganzen Zahlen `nums`.
**Ausgabe:** Ein Array aus zwei ganzen Zahlen, das die eindeutigen Zahlen darstellt.

## Wann man diese Aufgabe nutzen sollte

- Um die absolute Beherrschung der XOR-Eigenschaften und der Bit-Isolation zu demonstrieren.
- Dies ist eine Kombination aus zwei bekannten Bit-Tricks: dem XOR-Array-Collapse (`bit_03`) UND Brian Kernighans Isolation des niedrigsten gesetzten Bits (`bit_01`).

## Vorgehensweise

**1. Der anfängliche XOR-Collapse:**
Wenn wir jede Zahl im Array miteinander XOR-verknüpfen (genau wie bei „Single Number I“), heben sich alle gepaarten Zahlen zu `0` auf.
Was bleibt übrig? Seien die beiden eindeutigen Zahlen A und B.
Das Endergebnis ist `xor_sum = A ^ B`.
Da A und B eindeutige Zahlen sind, gilt A ≠ B. Das bedeutet, dass `xor_sum` NICHT 0 sein kann. Es MUSS mindestens ein Bit in `xor_sum` gesetzt sein, das auf `1` steht!

**2. Die Bedeutung eines „1“-Bits bei XOR:**
Was bedeutet ein `1`-Bit in einem XOR-Ergebnis? Es bedeutet, dass A und B an dieser bestimmten Bitposition UNTERSCHIEDLICHE Werte hatten! (Eines von beiden hatte ein `1`, das andere ein `0`).
Wenn wir *beliebiges* `1`-Bit aus `xor_sum` isolieren können, haben wir ein Unterscheidungsmerkmal zwischen A und B gefunden.

**3. Isolieren des Bits (Brian Kernighans Variante):**
Um das absolut niedrigste (ganz rechts stehende) `1`-Bit einer beliebigen Zahl zu isolieren, wenden wir folgenden „Zaubertrick“ an:
`diff_bit = xor_sum & -xor_sum`
(Anmerkung: In der Zweierkomplement-Arithmetik ist `-n` gleichbedeutend mit `~n + 1`. Durch eine UND-Verknüpfung werden alle Bits auf Null gesetzt, außer dem niedrigsten gesetzten Bit).

**4. Aufteilen des Arrays:**
Nun haben wir ein `diff_bit` (z. B. `00100`). Wir wissen mit Sicherheit, dass A an dieser Position ein `1` hat und B an dieser Position ein `0` hat (oder umgekehrt).
Wir können das ursprüngliche Array erneut durchlaufen und die Zahlen in zwei völlig getrennte Gruppen aufteilen:
- Gruppe 1: Zahlen, die an der Position `diff_bit` ein `1` aufweisen (`(num & diff_bit) != 0`).
- Gruppe 2: Zahlen, die an der Position `diff_bit` ein `0` aufweisen (`(num & diff_bit) == 0`).

**5. Die abschließende Eliminierung:**
A wird vollständig in Gruppe 1 eingeordnet. B wird vollständig in Gruppe 2 fallen.
Was ist mit den Zahlenpaaren? Da Zahlenpaare identisch sind, haben sie IMMER identische Bits! Daher fallen die Paare ENTWEDER BEIDE in Gruppe 1 oder BEIDE in Gruppe 2!
Nun enthält Gruppe 1 A, umgeben von Paaren. Fach 2 enthält B, umgeben von Paaren.
Wir wenden einfach unabhängig voneinander den Standardtrick „Einzelzahl I XOR“ auf beide Fächer an, um A und B zu ermitteln!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_05: Single Number III.

Every element in the input array appears exactly
"""


def solve(arr):
    """Return the two elements that appear exactly once (sorted)."""
    xor_all = 0
    for v in arr:
        xor_all ^= v
    diff_bit = xor_all & -xor_all
    a, b = 0, 0
    for v in arr:
        if v & diff_bit:
            a ^= v
        else:
            b ^= v
    return sorted([a, b])
```

</details>

## Schritt-für-Schritt-Anleitung

`nums = [1, 2, 1, 3, 2, 5]`. (Die eindeutigen Zahlen sind 3 und 5).

1. **Schritt 1 (XOR-Reduktion):**
   - `xor_sum = 1^2^1^3^2^5`
   - `1` heben sich auf. `2` heben sich auf.
   - `xor_sum = 3 ^ 5`. (`011 ^ 101 = 110`). `xor_sum = 6`.
2. **Schritt 2 (Bit isolieren):**
   - `diff_bit = 6 & -6`.
   - `6` ist `0110`. `-6` ist `...11111010`.
   - `0110 & 1010 = 0010`. `diff_bit = 2`.
   - (Dies beweist, dass das zweite Bit von rechts bei 3 und 5 UNTERSCHIEDLICH ist).
3. **Schritt 3 (Aufteilen & XOR):**
   - `a = 0`, `b = 0` initialisieren.
   - `num = 1 (001)`: `1 & 2 == 0`. Bucket B. `b = 0 ^ 1 = 1`.
   - `num = 2 (010)`: `2 & 2 != 0`. Bucket A. `a = 0 ^ 2 = 2`.
   - `num = 1 (001)`: `1 & 2 == 0`. Bucket B. `b = 1 ^ 1 = 0`. (Paar gelöscht!).
   - `num = 3 (011)`: `3 & 2 != 0`. Gruppe A. `a = 2 ^ 3 = 1`.
   - `num = 2 (010)`: `2 & 2 != 0`. Bucket A. `a = 1 ^ 2 = 3`. (Paar gestrichen!).
   - `num = 5 (101)`: `5 & 2 == 0`. Bucket B. `b = 0 ^ 5 = 5`.

Ergebnis `a = 3`, `b = 5`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Das Array wird genau zweimal durchlaufen. Die bitweisen Operationen sind $O(1)$. Die Gesamtzeit beträgt streng $O(N)$.
Die Platzkomplexität beträgt $O(1)$, da wir nur ganzzahlige Variablen `xor_sum`, `diff_bit`, `a` und `b` verwenden.

## Varianten & Optimierungen

- **Vermeidung von Ganzzahlüberlauf:** In Sprachen mit strengen 32-Bit-Ganzzahlen mit Vorzeichen (wie Java/C++) führt die Anwendung von `-xor_sum` bei `xor_sum == Integer.MIN_VALUE` zu einem Überlauffehler! Man muss vor der Isolierung explizit auf `MIN_VALUE` prüfen oder in eine 64-Bit-Ganzzahl umwandeln. (Python skaliert die Ganzzahlgenauigkeit dynamisch und vermeidet so dieses Problem).

## Praktische Anwendungen

- **Verteilte Netzwerke (Gossip-Protokolle):** Abgleich von Synchronisationszuständen zwischen zwei riesigen Datenbanken. Durch den Austausch von XOR-Signaturen von Datensätzen kann ein Server genau ermitteln, welche beiden Datensätze nicht synchron sind, ohne den gesamten mehrere Gigabyte großen Datensatz über das Netzwerk umschichten zu müssen!

## Verwandte Algorithmen in cOde(n)

- **[bit_03 – Einzelne Zahl (XOR)](bit_03_single-number-xor.md)** — Der grundlegende Vorbedingungenalgorithmus.
- **[bit_01 – Count Set Bits](bit_01_count-set-bits.md)** — Erläutert die Funktionsweise hinter der Bit-Isolationstechnik aus `n & -n`.

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
