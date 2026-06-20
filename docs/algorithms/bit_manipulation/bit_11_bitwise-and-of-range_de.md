# Bitweises UND von Zahlen eines Bereichs

| | |
|---|---|
| **ID** | `bit_11` |
| **Kategorie** | Bitmanipulation |
| **Komplexität (erforderlich)** | $O(1)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Bitweises UND eines Zahlenbereichs](https://leetcode.com/problems/bitwise-and-of-numbers-range/) |

## Aufgabenstellung

Gegeben sind zwei Ganzzahlen `left` und `right`, die den Bereich `[left, right]` darstellen. Gib das bitweise UND aller Zahlen in diesem Bereich einschließlich der Endpunkte zurück.

**Eingabe:** Zwei ganze Zahlen `left` und `right` (0 \le \text{links} \le \text{rechts} \le 2^{31} - 1).
**Ausgabe:** Eine ganze Zahl, die das bitweise UND des Bereichs darstellt.

## Anwendungsfälle

- Zur Veranschaulichung fortgeschrittener binärer Mustererkennung.
- Wenn Sie einen riesigen zusammenhängenden Zahlenbereich sofort und ohne Schleifen zusammenfassen oder maskieren müssen.

## Vorgehensweise

**1. Der Nachteil von Schleifen:**
Der naive Ansatz besteht darin, eine `for`-Schleife von `left` bis `right` auszuführen und dabei jeweils eine `AND`-Operation durchzuführen.
Wenn `left = 0` und `right = 2147483647`, wird die Schleife 2 Milliarden Mal ausgeführt und einen „Time Limit Exceeded“ (TLE)-Fehler auslösen! Wir benötigen eine $O(1)$ mathematische Lösung.

**2. Das binäre Muster:**
Betrachten wir den Bereich von `9` bis `12`:
`09` = `0000 1001`
`10` = `0000 1010`
`11` = `0000 1011`
`12` = `0000 1100`

Was passiert, wenn wir all diese Zahlen bitweise mit „AND“ verknüpfen?
Jede Spalte, die auch nur EIN `0` enthält, wird im Endergebnis zu `0` zusammengefasst!
Beachten Sie die Bits ganz rechts. Mit steigenden Zahlen wechseln die unteren Bits unglaublich schnell ihre Wertigkeit. Zwischen `9` und `12` haben die drei Bits ganz rechts jeweils mindestens ein `0` und ein `1` durchlaufen. Daher werden sie ALLE zu `0`!
Betrachten Sie nun die höheren Bits. Die Bits `0000 1...` haben sich NIEMALS geändert! Sie sind über alle Zahlen im Bereich hinweg vollkommen identisch!

**3. Die Strategie (gemeinsames Präfix):**
Das bitweise UND einer zusammenhängenden Zahlenreihe ist einfach das **längste gemeinsame Präfix** der binären Darstellungen von `left` und `right`, wobei die restlichen Bits mit `0`s aufgefüllt werden!
Wie isolieren wir das gemeinsame Präfix?
Wir verschieben einfach sowohl `left` als auch `right` gleichzeitig nach rechts (`>>`), bis sie vollkommen gleich sind! Wir halten in einem Zähler `shifts` fest, wie oft wir sie verschoben haben.
Sobald sie gleich sind, haben wir das gemeinsame Präfix gefunden! Anschließend verschieben wir das Präfix (`<<`) um `shifts` nach links zurück, um seine ursprüngliche Größe wiederherzustellen, wodurch die unteren Bits natürlich mit `0`s gefüllt werden!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_11: Bitwise AND of Range.

Given two non-negative integers left and right
"""


def solve(left, right):
    """Return AND of all integers in [left, right] (the common prefix)."""
    shift = 0
    # While left and right differ, shift them both right by 1
    # (and count the shifts) to find the common prefix.
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift
```

</details>

## Schritt-für-Schritt-Anleitung

`left = 9`(`1001`), `right = 12`(`1100`). `shifts = 0`.

1. **Schleife 1:** `9 < 12`.
   - `left = 9 >> 1 = 4`(`100`)
   - `right = 12 >> 1 = 6`(`110`)
   - `shifts = 1`
2. **Schleife 2:** `4 < 6`.
   - `left = 4 >> 1 = 2`(`10`)
   - `right = 6 >> 1 = 3`(`11`)
   - `shifts = 2`
3. **Schleife 3:** `2 < 3`.
   - `left = 2 >> 1 = 1`(`1`)
   - `right = 3 >> 1 = 1`(`1`)
   - `shifts = 3`
4. **Schleife 4:** `1 < 1` FALSE. Die Schleife wird beendet.

**Letzter Schritt:**
- Rückgabe `left << shifts` -> `1 << 3` = `8`(`1000`).

Das Ergebnis ist `8`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(1)$ |
| **Schlechtester Fall** | $O(1)$ | $O(1)$ |

Die `while`-Schleife wird genau so oft ausgeführt, wie es unterschiedliche Bits in den Binärzeichenfolgen gibt. Bei einer 32-Bit-Ganzzahl läuft diese Schleife höchstens 32 Mal.
Da 32 Operationen eine konstante Obergrenze darstellen, unabhängig von der tatsächlichen numerischen Differenz zwischen `left` und `right` (selbst wenn die Differenz 2 Milliarden beträgt), beträgt die Zeitkomplexität streng $O(1)$.
Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Brian Kernighans Variante:** Anstelle einer Rechtsverschiebung können wir den Trick anwenden, bei dem das niedrigste gesetzte Bit gelöscht wird! Während `left < right`, führen wir einfach `right = right & (right - 1)` aus. Dadurch werden die schwankenden unteren Bits von `right` drastisch abgeschnitten, bis der Wert so weit nach unten gepusht wird, dass er perfekt mit `left` übereinstimmt (oder sogar darunter fällt und dem gemeinsamen Präfix entspricht). Dadurch entfällt die Notwendigkeit eines `shifts`-Zählers vollständig! `return right`.

## Praktische Anwendungen

- **Subnetzmaskierung (CIDR-Notation):** In IP-Netzwerken entspricht die Bestimmung der Netzwerkadresse, zu der ein Bereich von IP-Adressen gehört, mathematisch gesehen der Ermittlung des längsten gemeinsamen binären Präfixes der niedrigsten und höchsten IP-Adressen in diesem Bereich. Das Ergebnis der bitweisen UND-Verknüpfung *ist* die Subnetzmaske!

## Verwandte Algorithmen in cOde(n)

- **[bit_01 – Count Set Bits](bit_01_count-set-bits.md)** — Erläutert den in der optimierten Variante verwendeten `n & (n - 1)`-Trick.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
