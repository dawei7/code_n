# Einzelne Zahl (XOR)

| | |
|---|---|
| **ID** | `bit_03` |
| **Kategorie** | Bitmanipulation |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Single Number](https://leetcode.com/problems/single-number/) |

## Aufgabenstellung

Gegeben ist ein nichtleeres Array von ganzen Zahlen `nums`, in dem jedes Element *zweimal* vorkommt, bis auf eines. Finde dieses eine Element.
Sie müssen eine Lösung mit linearer Laufzeitkomplexität implementieren und dürfen nur konstanten zusätzlichen Speicherplatz verwenden.

**Eingabe:** Ein Array aus ganzen Zahlen `nums`.
**Ausgabe:** Eine ganze Zahl, die das einzige Element darstellt.

## Wann man es verwenden sollte

- Um die magischen, kommutativen Eigenschaften des bitweisen XOR-Operators (`^`) zu veranschaulichen.
- Der grundlegende „Ausgleichstrick“, mit dem sich eine ganze Familie von Problemen mit gepaarten Arrays lösen lässt.

## Vorgehensweise

**1. Der Fehler der Standardansätze:**
- **Hash-Map:** Zähle die Häufigkeiten jeder Zahl und durchlaufe anschließend die Map, um die Häufigkeit von 1 zu finden. Dies benötigt $O(N)$ Zeit, aber $O(N)$ Speicherplatz, was gegen die Aufgabenbeschränkung verstößt!
- **Sortieren:** Sortiere das Array und durchlaufe es anschließend in 2er-Schritten. Wenn `nums[i] != nums[i+1]`, hast du das Ziel gefunden. Dies benötigt $O(1)$ Speicherplatz, aber das Sortieren dauert $O(N \log N)$ Zeit, was gegen die lineare Zeitbeschränkung verstößt!

**2. Die Magie von XOR:**
Der bitweise XOR-Operator (`^`) vergleicht zwei Binärzahlen Bit für Bit. Sind die Bits gleich, gibt er `0` aus. Sind sie unterschiedlich, gibt er `1` aus.
Dies führt zu zwei unglaublichen mathematischen Axiomen:
1. **Selbstaufhebung:** Jede Zahl, die mit sich selbst XOR-verknüpft wird, ergibt 0! `A ^ A = 0`.
2. **Identität:** Jede Zahl, die mit 0 XOR-verknüpft wird, ergibt sich selbst! `A ^ 0 = A`.

**3. Die Kommutativität:**
XOR ist kommutativ und assoziativ. Das bedeutet, dass `A ^ B ^ A` mathematisch identisch mit `(A ^ A) ^ B` ist.
Da `A ^ A = 0` gilt, vereinfacht sich die Gleichung zu `0 ^ B`, was `B` entspricht!
Beachte, dass die Reihenfolge der Zahlen im Array KEINE Rolle spielt.
Wenn wir eine Variable `result = 0` initialisieren und sie mit jeder einzelnen Zahl im Array XOR-verknüpfen, heben sich alle Zahlen, die zweimal vorkommen, vollständig gegenseitig auf (und ergeben `0`), ganz gleich, wie weit sie voneinander entfernt sind!
Die einzige Zahl, die in `result` übrig bleibt, ist die einzelne Zahl!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_03: Single Number (XOR).

Every element in the input array appears exactly
"""


def solve(arr):
    """Return the element that appears exactly once (others appear twice)."""
    result = 0
    for v in arr:
        result ^= v
    return result
```

</details>

## Schritt-für-Schritt-Anleitung

`nums = [4, 1, 2, 1, 2]`. `result = 0`.

1. **num = 4:**
   - `result = 0 ^ 4 = 4`(`000 ^ 100 = 100`)
2. **num = 1:**
   - `result = 4 ^ 1 = 5`(`100 ^ 001 = 101`)
3. **num = 2:**
   - `result = 5 ^ 2 = 7`(`101 ^ 010 = 111`)
4. **num = 1:**
   - `result = 7 ^ 1 = 6`(`111 ^ 001 = 110`)
   - *(Beachten Sie, dass das „1“-Bit aus dem ersten `1` aufgehoben wurde!)*
5. **num = 2:**
   - `result = 6 ^ 2 = 4`(`110 ^ 010 = 100`)
   - *(Beachten Sie, dass das „1“-Bit aus dem ersten `2` aufgehoben wurde!)*

Das endgültige `result` ist 4. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Das Array wird genau einmal durchlaufen, wobei bei jedem Schritt eine einzige $O(1)$ XOR-Operation durchgeführt wird. Die Zeitkomplexität beträgt streng $O(N)$.
Wir verwenden nur eine einzige ganzzahlige Variable `result`, wodurch die Platzkomplexität streng $O(1)$ beträgt.

## Varianten & Optimierungen

- **Fehlende Zahl (1 bis N):** Gegeben ist ein Array mit N verschiedenen Zahlen aus dem Bereich von 0 bis N. Eine Zahl fehlt. Finde sie.
  Du kannst dies mit XOR lösen! Im Array fehlt genau EINE gepaarte Zahl. Wenn du alle Indizes `0...N` mit XOR verknüpfst und anschließend alle Werte im Array `nums` mit XOR verknüpfst, werden sich alle Zahlen paarweise aufheben *außer* dem fehlenden Index!
- **Einzelne Zahl II (Jedes Element kommt dreimal vor):** Der XOR-Trick funktioniert nicht, weil `A ^ A ^ A = A`, nicht `0`. Du musst eine Zustandsmaschine mit zwei Variablen (`ones`, `twos`) verwenden, um die Bits modulo 3 zu verfolgen.
- **Einzelzahl III (Zwei Elemente kommen einmal vor):** Wenn zwei Zahlen eindeutig sind, lautet das endgültige XOR-Ergebnis `A ^ B`. Man muss Brian Kernighans Trick (`result & -result`) anwenden, um ein unterscheidendes Bit zu isolieren, dann das Array in zwei Buckets aufteilen und den XOR-Trick erneut auf beide Buckets anwenden! (`bit_05`)

## Praktische Anwendungen

- **RAID-Speichersysteme:** RAID-4- und RAID-5-Arrays verteilen Daten auf mehrere Festplatten und verwenden eine zusätzliche „Paritätsfestplatte“. Die Paritätsfestplatte ist buchstäblich nur das bitweise XOR aller anderen Festplatten! Fällt eine einzelne Festplatte aus, können die genauen Daten der fehlenden Festplatte wiederhergestellt werden, indem die intakten Festplatten mit der Paritätsfestplatte XOR-verknüpft werden.

## Verwandte Algorithmen in cOde(n)

- **[bit_05 – Einzelne Zahl III](bit_05_single-number-iii.md)** — Die wesentlich schwierigere Variante, bei der genau ZWEI Zahlen einmal vorkommen.
- **[bit_10 – Fehlende Zahl](bit_10_missing-number.md)** — Die Variante, bei der man mit einer bekannten, erwarteten Folge XOR-operieren muss.

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
