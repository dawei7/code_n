# Bits umkehren

| | |
|---|---|
| **ID** | `bit_12` |
| **Kategorie** | Bitmanipulation |
| **Komplexität (erforderlich)** | $O(1)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) |

## Aufgabenstellung

Kehren Sie die Bits einer gegebenen vorzeichenlosen 32-Bit-Ganzzahl um.

**Eingabe:** Eine vorzeichenlose 32-Bit-Ganzzahl `n`.
**Ausgabe:** Eine Ganzzahl, die den bitweise umgekehrten Wert darstellt.

## Wann man diese Aufgabe nutzen sollte

- Eine grundlegende Übung zum Bit-Shuffling, die beweist, dass du weißt, wie man Binärzahlen von Grund auf aufbaut.

## Lösungsansatz

**1. Der Baustein-Ansatz:**
Stell dir vor, du nimmst einen Kartensatz und baust einen brandneuen, umgekehrten Stack auf.
Du nimmst die oberste Karte vom ursprünglichen Stack und legst sie ganz unten auf den neuen Stack.
Das wiederholst du, bis der ursprüngliche Stack leer ist.
Genau das können wir auch mit Bits machen!

1. Erstelle eine Variable `result`, die auf `0` initialisiert ist.
2. Führe genau 32 Schleifen durch (da die Aufgabe eine 32-Bit-Ganzzahl garantiert).
3. **Extrahiere** das Bit ganz rechts von `n` mithilfe von `n & 1`.
4. **Setze** dieses Bit in unsere `result`! Aber wohin kommt es? Da es das Bit ganz rechts der ursprünglichen Zahl ist, muss es das Bit ganz links der umgekehrten Zahl werden!
   Eigentlich ist es einfacher, es einfach an die rechte Seite von `result` anzuhängen und dann sofort *`result` nach links zu verschieben*! Dadurch werden die früheren Bits im Verlauf der Schleife natürlich immer weiter nach links verschoben.
5. **Verschiebe** `n` nach rechts (`n >> 1`), um das nächste Bit freizulegen.

*Wichtiges Detail:* Du MUSST `result` nach links verschieben, BEVOR du das extrahierte Bit hinzufügst, sonst wird dein allererstes Bit am Ende der 32 Schleifen um 1 Position zu weit verschoben!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_12: Reverse Bits.

Reverse the bits of a 32-bit unsigned integer n.
"""


def solve(n):
    """Reverse the bits of the 32-bit unsigned integer n."""
    result = 0
    for i in range(32):
        # Take bit i of n, place it at bit (31 - i) of result.
        if n & (1 << i):
            result |= 1 << (31 - i)
    return result
```

</details>

## Schritt-für-Schritt-Anleitung

Führen wir aus Platzgründen eine 4-Bit-Simulation durch: `n = 13`(`1101`). Wir wollen `1011`(`11`). `result = 0`.

1. **Schleife 1 (i=0):**
   - `result = 0 << 1 = 0`(`0000`)
   - `bit = 1101 & 1 = 1`
   - `result = 0000 | 1 = 0001`(`1`)
   - `n = 1101 >> 1 = 110`(`6`)
2. **Schleife 2 (i=1):**
   - `result = 0001 << 1 = 0010`(`2`)
   - `bit = 110 & 1 = 0`
   - `result = 0010 | 0 = 0010`(`2`)
   - `n = 110 >> 1 = 11`(`3`)
3. **Schleife 3 (i=2):**
   - `result = 0010 << 1 = 0100`(`4`)
   - `bit = 11 & 1 = 1`
   - `result = 0100 | 1 = 0101`(`5`)
   - `n = 11 >> 1 = 1`(`1`)
4. **Schleife 4 (i=3):**
   - `result = 0101 << 1 = 1010`(`10`)
   - `bit = 1 & 1 = 1`
   - `result = 1010 | 1 = 1011`(`11`)
   - `n = 1 >> 1 = 0`

Das Ergebnis ist `11`(`1011`). ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(1)$ |
| **Schlechtester Fall** | $O(1)$ | $O(1)$ |

Die Schleife läuft genau 32 Mal mit konstant $O(1)$ Operationen im Inneren. Die Zeitkomplexität beträgt streng $O(1)$.
Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Teile-und-herrsche-Blocktausch:** Wenn man Bits millionenfach pro Sekunde umkehren muss, ist eine Schleife mit 32 Verschiebungen tatsächlich zu langsam! Man kann die gesamte 32-Bit-Zeichenkette mit nur 5 $O(1)$ Operationen umkehren!
  1. Benachbarte 1-Bit-Paare vertauschen: `n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)`
  2. Benachbarte 2-Bit-Blöcke vertauschen: `n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)`
  3. Benachbarte 4-Bit-Blöcke vertauschen: `n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)`
  4. Benachbarte 8-Bit-Blöcke vertauschen: `n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)`
  5. Benachbarte 16-Bit-Blöcke vertauschen: `n = (n >> 16) | (n << 16)`
  Die Bits werden ohne Schleifen perfekt umgekehrt!

## Praktische Anwendungen

- **Digitale Signalverarbeitung (FFT):** Der Cooley-Tukey-Algorithmus für die schnelle Fourier-Transformation erfordert, dass auf Array-Elemente in „bitumgekehrter Reihenfolge“ zugegriffen wird. Diese physikalische Bitumkehr auf Hardwareebene stellt sicher, dass die rekursive Signalaufteilung linear im Speicher erfolgt.

## Verwandte Algorithmen in cOde(n)

- **[bit_07 – Ungerade und gerade Bits vertauschen](bit_07_swap-odd-and-even-bits.md)** — Die grundlegende logische Voraussetzung für die Blockvertauschungsvariante $O(1)$.
- **[math_01 – Ganzzahl umkehren](../math/math_01_reverse-integer.md)** — Umkehrung von Ziffern im Dezimalsystem (Basis 10) mithilfe von `% 10` und `/ 10`, was die Extraktion von Bits im Binärsystem (Basis 2) mithilfe von `& 1` und `>> 1` perfekt widerspiegelt!

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
