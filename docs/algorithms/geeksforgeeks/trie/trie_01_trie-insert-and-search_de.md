# Trie Insert and Search

| | |
|---|---|
| **ID** | `trie_01` |
| **Kategorie** | trie |
| **Komplexität (erforderlich)** | $O(M)$ Zeit, $O(M)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) |

## Problemstellung

Ein Trie (ausgesprochen wie „try“) oder Präfixbaum ist eine Baumdatenstruktur, die verwendet wird, um Schlüssel in einem Datensatz von Strings effizient zu speichern und abzurufen.
Implementieren Sie die `Trie`-Klasse:
- `insert(word)`: Fügt den String `word` in den Trie ein.
- `search(word)`: Gibt `true` zurück, wenn der String `word` im Trie vorhanden ist (d. h. zuvor eingefügt wurde), und andernfalls `false`.
- `startsWith(prefix)`: Gibt `true` zurück, wenn ein zuvor eingefügter String `word` existiert, der das Präfix `prefix` hat, und andernfalls `false`.

**Eingabe:** Sequenzen von Methodenaufrufen mit Strings.
**Ausgabe:** Boolesche Werte für Suchoperationen.

## Wann man es verwendet

- Um extrem schnelle Wörterbuchabfragen und Präfix-Abgleiche durchzuführen.
- Er ist deutlich schneller als eine Hash Table bei der Arbeit mit Strings, die gemeinsame Präfixe teilen, da er keine Hashes berechnet und massiv Speicherplatz spart.

## Ansatz

**1. Die Knotenstruktur:**
Im Gegensatz zu einem Binary Tree, der einen `left`- und `right`-Pointer besitzt, kann ein Trie-Knoten bis zu 26 Kinder haben (eines für jeden Buchstaben des englischen Alphabets).
Jeder Knoten enthält:
- `children`: Eine Hash Map oder ein Array der Größe 26, das Zeichen auf untergeordnete `TrieNode`s abbildet.
- `is_end_of_word`: Ein boolesches Flag. Nur weil ein Knoten existiert, bedeutet das nicht, dass es ein Wort ist! Wenn wir `"apple"` einfügen, existiert der Knoten für `'p'`, aber `"app"` ist kein Wort in unserem Wörterbuch, bis wir es explizit einfügen!

**2. Einfügen:**
Starten Sie an der Wurzel. Für jedes Zeichen im Wort:
- Wenn das Zeichen nicht in den `children` des aktuellen Knotens existiert, erstellen Sie einen neuen `TrieNode` dafür.
- Bewegen Sie den aktuellen Pointer auf diesen Kindknoten.
Wenn das Wort endet, markieren Sie den letzten Knoten, auf dem wir gelandet sind, als `is_end_of_word = True`.

**3. Suche nach einem Wort:**
Starten Sie an der Wurzel. Für jedes Zeichen im Wort:
- Wenn das Zeichen nicht in `children` existiert, ist das Wort nicht im Wörterbuch! Geben Sie `False` zurück.
- Bewegen Sie den Pointer nach unten.
Wenn das Wort endet, prüfen wir den Knoten, auf dem wir gelandet sind. Geben wir einfach `True` zurück? NEIN!
Was, wenn wir `"apple"` eingefügt haben und nach `"app"` suchen? Wir durchlaufen den Baum erfolgreich, aber `"app"` ist kein gültiges Wort!
Wir müssen `curr.is_end_of_word` zurückgeben!

**4. Suche nach einem Präfix:**
Identisch zur Suche nach einem Wort. Wenn das Präfix jedoch endet, ist es uns egal, ob es das Ende eines Wortes ist! Die Tatsache, dass der Pfad überhaupt existierte, bedeutet, dass das Präfix gültig ist! Geben Sie `True` zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for trie_01: Trie Insert and Search.

Build a trie from the words, then return True iff target is in it.
"""


def solve(words, n, target):
    children = []
    is_end = []

    def new_node():
        children.append({})
        is_end.append(False)
        return len(children) - 1

    root = new_node()
    for w in words:
        cur = root
        for ch in w:
            nxt = children[cur].get(ch)
            if nxt is None:
                nxt = new_node()
                children[cur][ch] = nxt
            cur = nxt
        is_end[cur] = True
    cur = root
    for ch in target:
        if ch not in children[cur]:
            return False
        cur = children[cur][ch]
    return is_end[cur]
```

</details>

## Durchlauf

`insert("apple")`
- Die Wurzel hat kein 'a'. Füge `TrieNode` bei 'a' hinzu. Gehe zu 'a'.
- 'a' hat kein 'p'. Füge `TrieNode` bei 'p' hinzu. Gehe zu 'p'.
...
- Markiere den 'e'-Knoten als `is_end_of_word = True`.

`search("apple")`
- Verfolge 'a' -> 'p' -> 'p' -> 'l' -> 'e'.
- Pfad existiert. `curr.is_end_of_word` ist True. Gibt `True` zurück. ✓

`search("app")`
- Verfolge 'a' -> 'p' -> 'p'.
- Pfad existiert. `curr.is_end_of_word` ist False. Gibt `False` zurück. ✓

`startsWith("app")`
- Verfolge 'a' -> 'p' -> 'p'.
- Pfad existiert. Gibt `True` zurück. ✓

`insert("app")`
- Verfolge 'a' -> 'p' -> 'p' (Knoten existieren bereits, wir traversieren nur).
- Markiere den 'p'-Knoten als `is_end_of_word = True`.

`search("app")`
- Verfolge 'a' -> 'p' -> 'p'.
- Pfad existiert. `curr.is_end_of_word` ist True! Gibt `True` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(M)$ | $O(M)$ |
| **Schlechtester Fall** | $O(M)$ | $O(M)$ |

Wobei M die Länge des Strings ist, der eingefügt oder gesucht wird.
Jede Operation (insert, search, startsWith) erfordert das Durchlaufen von genau M Knoten. Das Nachschlagen eines Zeichens in der `children` Hash Map benötigt $O(1)$ konstante Zeit.
Die gesamte Zeitkomplexität ist strikt $O(M)$. Dies ist schneller als bei Binary Search Trees mit $O(M log N)$ und vergleichbar mit Hash Tables, jedoch ohne Hash-Kollisionen!
Die Platzkomplexität für das Einfügen ist $O(M)$, wenn kein Teil des Wortes ein Präfix mit existierenden Wörtern teilt (wir müssen M neue Knoten erstellen). Für Suchoperationen ist der Platzbedarf $O(1)$.

## Varianten & Optimierungen

- **Array vs Hash Map (`children[26]`):** Wenn Sie nur mit englischen Kleinbuchstaben arbeiten, ist die Verwendung eines Arrays `children = [None] * 26` mathematisch schneller, da die Berechnung eines Array-Index `ord(char) - ord('a')` schneller ist als das Hashen eines String-Schlüssels. Es verbraucht jedoch drastisch mehr Speicher, da jeder Knoten 26 leere Plätze reserviert, selbst wenn er nur 1 Kind hat.

## Anwendungen in der Praxis

- **Auto-Vervollständigung in Suchmaschinen:** Wenn Sie "algo" bei Google eingeben, verwendet es `startsWith("algo")` auf einem massiv verteilten Trie, findet den `"o"`-Knoten und führt eine BFS aus, um die 10 populärsten Teilbäume (Wörter) zurückzugeben, die darunter angehängt sind!
- **Rechtschreibprüfung:** Die wellenförmigen roten Unterstreichungen in Microsoft Word werden berechnet, indem Ihr getipptes Wort durch einen Trie eines englischen Wörterbuchs verfolgt wird.

## Verwandte Algorithmen in cOde(n)

- **[trie_02 - Word Count with Prefix](trie_02_word-count-with-prefix.md)** — Eine kleine Modifikation, um die Knoten mit Zählervariablen zu erweitern.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*