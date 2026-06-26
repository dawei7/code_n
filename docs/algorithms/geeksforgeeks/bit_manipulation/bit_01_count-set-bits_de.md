# Count Set Bits (Brian Kernighans Algorithmus)

| | |
|---|---|
| **ID** | `bit_01` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(K)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) |

## Problemstellung

Schreiben Sie eine Funktion, die eine vorzeichenlose Ganzzahl (unsigned integer) entgegennimmt und die Anzahl der '1'-Bits zurückgibt (auch bekannt als Hamming-Gewicht).

**Eingabe:** Eine vorzeichenlose Ganzzahl `n`.
**Ausgabe:** Eine Ganzzahl, die die Anzahl der '1'-Bits in `n` repräsentiert.

## Wann man es verwendet

- Um die gesetzten Bits (1en) einer Zahl optimal zu zählen.
- Es ist die absolute Grundlage für fast alle Probleme der Bitmanipulation.

## Ansatz

**1. Der naive Ansatz:**
Wir könnten wiederholt das niederwertigste Bit (Least Significant Bit, LSB) mittels `n & 1` prüfen und die Zahl `n` anschließend mittels `n >>= 1` nach rechts verschieben. Dies benötigt exakt 32 Iterationen für eine 32-Bit-Ganzzahl, unabhängig davon, ob sie ein `1`-Bit oder dreißig `1`-Bits enthält.

**2. Brian Kernighans Algorithmus:**
Können wir direkt von einem `1`-Bit zum nächsten springen und alle `0`en überspringen? Ja!
Betrachten wir die mathematische Operation `n - 1`. Was bewirkt die Subtraktion von 1 im Binärsystem?
Sie invertiert alle Bits beginnend vom rechtesten `1`-Bit bis zum Ende der Zahl!
Beispiel: Wenn `n = 12` (`1100` binär):
`n - 1 = 11` (`1011` binär).
Man beachte, dass die rechteste `1` in `n` (an der 2er-Stelle) zu einer `0` wurde und alle `0`en rechts davon zu `1`en wurden.

Wenn wir ein bitweises UND zwischen `n` und `n - 1` durchführen:
`n & (n - 1)`
`1100 & 1011 = 1000`.
Das rechteste `1`-Bit wurde vollständig gelöscht!

**3. Die Strategie:**
Wir führen einfach `n = n & (n - 1)` in einer Schleife aus. Jedes Mal, wenn wir diese Zeile ausführen, wird exakt ein `1`-Bit gelöscht. Wir erhöhen bei jedem Durchlauf einen Zähler.
Wenn `n` den Wert 0 erreicht, terminiert die Schleife!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_01: Count Set Bits.

Count the number of 1-bits in the binary
"""


def solve(n):
    """Count the 1-bits in n (Hamming weight)."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

</details>

## Schritt-für-Schritt-Durchlauf

`n = 14` (Binär: `1110`). `count = 0`.

1. **Schleife 1:**
   - `n != 0`. `count = 1`.
   - `n - 1` = `13` (`1101`).
   - `n = 1110 & 1101 = 1100` (`12`). (Die rechteste 1 wurde gelöscht!)
2. **Schleife 2:**
   - `n != 0`. `count = 2`.
   - `n - 1` = `11` (`1011`).
   - `n = 1100 & 1011 = 1000` (`8`).
3. **Schleife 3:**
   - `n != 0`. `count = 3`.
   - `n - 1` = `7` (`0111`).
   - `n = 1000 & 0111 = 0000` (`0`).
4. **Schleife 4:**
   - `n == 0`. Schleife terminiert.

Ergebnis: `count = 3`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(K)$ | $O(1)$ |
| **Schlechtester Fall** | $O(K)$ | $O(1)$ |

*Wobei K die Anzahl der '1'-Bits in der Ganzzahl ist.*
Im absoluten Schlechtesten Fall (eine Zahl wie `0xFFFFFFFF`) benötigt der Algorithmus 32 Iterationen für eine 32-Bit-Ganzzahl, was ihn technisch gesehen zu $O(1)$ in Bezug auf die Größe der Eingabezahl macht. Asymptotisch ist er jedoch strikt durch $O(K)$ Iterationen begrenzt, was ihn für dünn besetzte Bitmasken dem naiven $O(log n)$ Shift-Ansatz weit überlegen macht.
Die Platzkomplexität ist strikt $O(1)$.

## Varianten & Optimierungen

- **Integrierte Funktionen:** Die meisten modernen Sprachen verfügen über hardwarebeschleunigte Instruktionen hierfür. In Python verwenden Sie `n.bit_count()`. In C++ verwenden Sie `__builtin_popcount(n)`. In Java verwenden Sie `Integer.bitCount(n)`. Diese werden zu einer einzigen CPU-Instruktion (wie `POPCNT` auf x86) kompiliert und in buchstäblich 1 CPU-Zyklus ausgeführt.
- **Extrahieren des niederwertigsten gesetzten Bits:** Wenn Sie das niederwertigste gesetzte Bit nur *isolieren* möchten, anstatt es zu löschen, verwenden Sie `n & -n`. Für `n = 12` (`1100`) ergibt `n & -n` den Wert `4` (`0100`). Dies wird intensiv in Fenwick Trees (`fenwick_01`) verwendet!

## Anwendungen in der Praxis

- **Kryptographie / Hashing:** Berechnung der Hamming-Distanz zwischen zwei Hashes, um Bit-Fehler (Bit-Rot), Datenkorruption oder Bildähnlichkeit (z. B. Perceptual Hashing) zu erkennen.
- **Schach-Engines (Bitboards):** Sofortige Berechnung der Anzahl legaler Züge einer Figur durch Zählen der `1`en auf einer 64-Bit-Ganzzahl-Repräsentation des Spielfelds.

## Verwandte Algorithmen in cOde(n)

- **[bit_02 - Power of Two Check](bit_02_power-of-two-check.md)** — Verwendet denselben `n & (n - 1)`-Trick, wertet ihn jedoch ohne Schleife aus!
- **[fenwick_01 - Binary Indexed Tree](../fenwick/fenwick_01_binary-indexed-tree.md)** — Basiert auf der Extraktion des niederwertigsten gesetzten Bits (`n & -n`), um Array-Offsets im Baum zu berechnen.

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*