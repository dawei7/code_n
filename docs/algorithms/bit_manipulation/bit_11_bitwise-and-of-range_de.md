# Bitwise AND of Numbers Range

| | |
|---|---|
| **ID** | `bit_11` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(1)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) |

## Problemstellung

Gegeben sind zwei Ganzzahlen `left` und `right`, die den Bereich `[left, right]` repräsentieren. Geben Sie das bitweise AND aller Zahlen in diesem Bereich (einschließlich der Grenzen) zurück.

**Eingabe:** Zwei Ganzzahlen `left` und `right` (0 \le \text{left} \le \text{right} \le 2^{31} - 1).
**Ausgabe:** Eine Ganzzahl, die das bitweise AND des Bereichs darstellt.

## Wann man es verwendet

- Um fortgeschrittene binäre Mustererkennung zu demonstrieren.
- Wenn Sie einen massiven, zusammenhängenden Bereich von Zahlen sofort zusammenfassen oder maskieren müssen, ohne eine Schleife zu verwenden.

## Ansatz

**1. Der Fehler bei der Verwendung von Schleifen:**
Der naive Ansatz besteht darin, eine `for`-Schleife von `left` bis `right` laufen zu lassen und eine fortlaufende `AND`-Operation durchzuführen.
Wenn `left = 0` und `right = 2147483647` ist, würde die Schleife 2 Milliarden Mal ausgeführt werden und einen Time Limit Exceeded (TLE)-Fehler verursachen! Wir benötigen eine mathematische Lösung mit $O(1)$.

**2. Das binäre Muster:**
Betrachten wir den Bereich von `9` bis `12`:
`09` = `0000 1001`
`10` = `0000 1010`
`11` = `0000 1011`
`12` = `0000 1100`

Was passiert, wenn wir alle diese Zahlen bitweise AND-verknüpfen?
Jede Spalte, die auch nur eine einzige `0` enthält, wird im Endergebnis zu `0`!
Beachten Sie die Bits auf der rechten Seite. Während die Zahlen inkrementieren, ändern sich die niederwertigen Bits extrem schnell. Zwischen `9` und `12` haben die 3 rechtesten Bits alle mindestens eine `0` und eine `1` gesehen. Daher werden sie ALLE zu `0`!
Betrachten Sie nun die höherwertigen Bits. Die Bits `0000 1...` haben sich NIE geändert! Sie sind über alle Zahlen im Bereich hinweg vollkommen identisch.

**3. Die Strategie (Längster gemeinsamer Präfix):**
Das bitweise AND eines kontinuierlichen Zahlenbereichs ist einfach der **längste gemeinsame Präfix** der binären Repräsentationen von `left` und `right`, wobei die restlichen Bits mit `0`en aufgefüllt werden!
Wie isolieren wir den gemeinsamen Präfix?
Wir verschieben einfach sowohl `left` als auch `right` gleichzeitig nach rechts (`>>`), bis sie exakt gleich sind! Wir protokollieren die Anzahl der Verschiebungen in einem Zähler namens `shifts`.
Sobald sie gleich sind, haben wir den gemeinsamen Präfix gefunden! Wir verschieben den Präfix dann wieder um `shifts` nach links (`<<`), um seine ursprüngliche Größenordnung wiederherzustellen, was die niederwertigen Bits auf natürliche Weise mit `0`en auffüllt!

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

## Durchlauf

`left = 9` (`1001`), `right = 12` (`1100`). `shifts = 0`.

1. **Schleife 1:** `9 < 12`.
   - `left = 9 >> 1 = 4` (`100`)
   - `right = 12 >> 1 = 6` (`110`)
   - `shifts = 1`
2. **Schleife 2:** `4 < 6`.
   - `left = 4 >> 1 = 2` (`10`)
   - `right = 6 >> 1 = 3` (`11`)
   - `shifts = 2`
3. **Schleife 3:** `2 < 3`.
   - `left = 2 >> 1 = 1` (`1`)
   - `right = 3 >> 1 = 1` (`1`)
   - `shifts = 3`
4. **Schleife 4:** `1 < 1` FALSCH. Schleife terminiert.

**Letzter Schritt:**
- Rückgabe `left << shifts` -> `1 << 3` = `8` (`1000`).

Das Ergebnis ist `8`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(1)$ |
| **Schlechtester Fall** | $O(1)$ | $O(1)$ |

Die `while`-Schleife wird exakt so oft ausgeführt, wie es unterschiedliche Bits in den binären Strings gibt. Für eine 32-Bit-Ganzzahl läuft diese Schleife maximal 32 Mal.
Da 32 Operationen eine konstante Obergrenze darstellen, unabhängig von der tatsächlichen numerischen Differenz zwischen `left` und `right` (selbst wenn die Differenz 2 Milliarden beträgt), ist die Zeitkomplexität strikt $O(1)$.
Die Platzkomplexität ist $O(1)$.

## Varianten & Optimierungen

- **Brian Kernighans Variante:** Anstatt nach rechts zu verschieben, können wir den Trick verwenden, der das niedrigste gesetzte Bit löscht! Solange `left < right`, führen wir einfach `right = right & (right - 1)` aus. Dies entfernt gewaltsam die fluktuierenden niederwertigen Bits von `right`, bis es gezwungen ist, exakt mit `left` übereinzustimmen (oder darunter zu fallen, was dem gemeinsamen Präfix entspricht). Dies macht einen `shifts`-Zähler komplett überflüssig! `return right`.

## Anwendungen in der Praxis

- **Subnetzmaskierung (CIDR-Notation):** In der IP-Netzwerktechnik ist die Bestimmung der Netzwerkadresse, zu der ein Bereich von IP-Adressen gehört, mathematisch identisch mit der Suche nach dem längsten gemeinsamen binären Präfix der niedrigsten und höchsten IP im Bereich. Das resultierende bitweise AND *ist* die Subnetzmaske!

## Verwandte Algorithmen in cOde(n)

- **[bit_01 - Count Set Bits](bit_01_count-set-bits.md)** — Erklärt den `n & (n - 1)`-Trick, der in der optimierten Variante verwendet wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*