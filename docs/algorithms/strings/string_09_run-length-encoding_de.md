# Run Length Encoding

| | |
|---|---|
| **ID** | `string_09` |
| **Kategorie** | strings |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **GeeksForGeeks Äquivalent** | [Run Length Encoding](https://www.geeksforgeeks.org/run-length-encoding/) |

## Problemstellung

Gegeben sei ein String `s`, führe ein **Run Length Encoding** (RLE) darauf aus.
RLE ist eine einfache Form der Datenkompression, bei der Läufe von Daten (Sequenzen, in denen derselbe Datenwert in vielen aufeinanderfolgenden Datenelementen vorkommt) als ein einzelner Datenwert und eine Anzahl gespeichert werden.
Zum Beispiel sollte aus `"wwwwaaadexxxxxx"` der String `"w4a3d1e1x6"` werden.

**Eingabe:** Ein String `s`.
**Ausgabe:** Ein komprimierter String.

## Wann man es verwendet

- Zur starken Komprimierung von Strings oder Arrays, die massive, zusammenhängende Blöcke wiederholter identischer Werte enthalten.
- Als grundlegende algorithmische Aufwärmübung in Vorstellungsgesprächen für Einsteiger.

## Ansatz

**1. Der Zähler für zusammenhängende Blöcke:**
Wir müssen den String durchlaufen und zählen, wie oft ein Zeichen nacheinander wiederholt wird.
Wir können einen Pointer `i` verwenden, der von `0` bis `N-1` iteriert.
Wir führen einen Zähler `count` ein, der mit `1` initialisiert wird.
Bei jedem Zeichen `s[i]` schauen wir auf das nächste Zeichen `s[i+1]`.
- Wenn `s[i] == s[i+1]`, ist es Teil desselben Laufs! Wir erhöhen `count` und bewegen `i` vorwärts.
- Wenn `s[i] != s[i+1]`, ist der Lauf mathematisch beendet! Wir nehmen das Zeichen `s[i]`, konvertieren `count` in einen String, hängen beides an unseren Ausgabe-String an und setzen `count` sicher wieder auf `1` für den Lauf des nächsten Zeichens zurück!

**2. Der Randfall am Ende des Strings:**
Wenn `i` das allerletzte Zeichen (`N-1`) erreicht, gibt es kein `s[i+1]`, das überprüft werden könnte! Der Versuch, darauf zuzugreifen, würde das Programm mit einem `IndexOutOfBounds`-Fehler zum Absturz bringen.
Um dies zu beheben, sollte unsere `for`-Schleife nur bis `N-2` (das vorletzte Zeichen) laufen.
Moment, wenn die Schleife bei `N-2` stoppt, wie wird dann der letzte Lauf hinzugefügt? Wir können einfach das letzte Zeichen `s[N-1]` und den verbleibenden `count` direkt nach Beendigung der Schleife anhängen!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_09: Run-Length Encoding.

Walk the string, counting consecutive equal chars.
"""


def solve(s):
    if not s:
        return ""
    out = []
    cur = s[0]
    count = 1
    for c in s[1:]:
        if c == cur:
            count += 1
        else:
            out.append(cur + str(count))
            cur = c
            count = 1
    out.append(cur + str(count))
    return "".join(out)
```

</details>

## Durchlauf

`s = "AABCCC"`
`n = 6`. Array `[]`. `count = 1`.

1. `i = 0`: `s[0] = 'A'`, `s[1] = 'A'`. Treffer!
   - `count = 2`.
2. `i = 1`: `s[1] = 'A'`, `s[2] = 'B'`. Kein Treffer!
   - Hänge `'A'` und `"2"` an. Ausgabe `["A", "2"]`.
   - `count = 1`.
3. `i = 2`: `s[2] = 'B'`, `s[3] = 'C'`. Kein Treffer!
   - Hänge `'B'` und `"1"` an. Ausgabe `["A", "2", "B", "1"]`.
   - `count = 1`.
4. `i = 3`: `s[3] = 'C'`, `s[4] = 'C'`. Treffer!
   - `count = 2`.
5. `i = 4`: `s[4] = 'C'`, `s[5] = 'C'`. Treffer!
   - `count = 3`.
6. Schleife endet (erreicht `n - 2`).
7. Führe das Anhängen nach der Schleife aus:
   - Hänge `s[5]` (`'C'`) und `count` (`"3"`) an.
   - Ausgabe `["A", "2", "B", "1", "C", "3"]`.

Finaler String: `"A2B1C3"`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Das Array wird genau einmal durchlaufen. Vergleiche und das Anhängen an das Array benötigen $O(1)$ konstante Zeit. Das Zusammenfügen des Strings am Ende benötigt $O(N)$ Zeit.
Die Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität ist $O(N)$, da Strings in den meisten Sprachen (Python, Java, C#) unveränderlich sind. Daher muss ein zusätzliches `encoded_chars`-Array der Größe bis zu 2N erstellt werden, um das Zwischenergebnis zu speichern, bevor es in den finalen Rückgabe-String zusammengefügt wird.

## Varianten & Optimierungen

- **In-Place Modifikation:** Wenn die Sprache veränderbare Strings verwendet (wie C++ `std::string` oder ein vorallokiertes `char[]`), kann man dies technisch mit $O(1)$ Platz unter Verwendung von zwei Pointern (einem Lese-Pointer und einem Schreib-Pointer) erreichen, vorausgesetzt, der komprimierte String ist garantiert kürzer als der ursprüngliche String.
- **Dekodierung (String Compression II):** Die Umkehroperation. Gegeben `"A2B1C3"`, generiere `"AABCCC"`. Man iteriert, liest das Zeichen, parst die folgende Ganzzahl und führt eine `for`-Schleife aus, um das Zeichen entsprechend oft anzuhängen.

## Anwendungen in der Praxis

- **Faxgeräte / Bitmaps:** Die standardmäßige Schwarz-Weiß-Faxübertragung verwendet RLE. Anstatt 1000 weiße Pixel einzeln zu senden, sendet es `[White, 1000]`. Dies reduziert massive Bilddateien während der Übertragung um 99%!
- **JPEG-Kodierung:** Nach der Quantisierung mittels diskreter Kosinustransformation enthalten Bilddaten massive Blöcke aufeinanderfolgender Nullen. RLE wird vor der Huffman-Kodierung angewendet, um die Nullen sofort zu eliminieren.

## Verwandte Algorithmen in cOde(n)

- **[two_pointers_05 - Remove Duplicates from Sorted Array](../two_pointers/two_pointers_05_remove-duplicates.md)** — Ein funktional identischer Algorithmus, aber anstatt den Lauf zu zählen, überschreibt man einfach das Array, um den Lauf vollständig zu löschen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*