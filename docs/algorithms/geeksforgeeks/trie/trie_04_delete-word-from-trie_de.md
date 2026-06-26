# Delete Word from Trie

| | |
|---|---|
| **ID** | `trie_04` |
| **Kategorie** | trie |
| **Komplexität (erforderlich)** | $O(M)$ Zeit, $O(M)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **GeeksForGeeks Äquivalent** | [Trie | (Delete)](https://www.geeksforgeeks.org/trie-delete/) |

## Problemstellung

Gegeben ist eine Standard-Trie-Datenstruktur und ein String `word`, der aktuell in ihr enthalten ist. Entfernen Sie den String vollständig aus dem Trie.
Sie müssen sicherstellen, dass das Entfernen dieses Wortes NICHT versehentlich die Präfixe anderer gültiger Wörter zerstört, die sich denselben Pfad teilen!
Wenn Knoten vollständig leer werden (keine Kinder und nicht das Ende eines anderen Wortes), müssen sie strukturell aus dem Speicher gelöscht werden, um Speicherlecks zu vermeiden.

**Eingabe:** Ein Trie `root`-Knoten und ein String `word`.
**Ausgabe:** Die modifizierte Trie-Struktur, aus der das Wort entfernt wurde.

## Wann man es verwendet

- Zur Pflege hochdynamischer Präfix-Wörterbücher, in denen Daten häufig ablaufen (wie z. B. Auto-Complete-Caches).
- Als rigoroser Test für Bottom-Up Post-Order DFS in Kombination mit sorgfältiger Pointer-Logik.

## Ansatz

**1. Die drei Löschszenarien:**
Wenn wir `"apple"` löschen wollen, traversieren wir bis zum `'e'`. Wir setzen dessen `is_end_of_word = False`. Das Wort ist nun offiziell aus dem Wörterbuch gelöscht!
Aber was ist mit den Knoten selbst?
1. **Der Knoten hat andere Kinder:** Wenn wir `"apple"` löschen, aber `"apples"` existiert, dürfen wir den `'e'`-Knoten NICHT physisch löschen! Er ist eine kritische Brücke für `"apples"`! Wir halten an.
2. **Der Knoten ist das Ende eines anderen Wortes:** Wenn wir `"apples"` löschen, verfolgen wir den Pfad zurück bis zum `'e'`. Das `'e'` hat keine anderen Kinder. Können wir es löschen? NEIN! Weil `"apple"` ein gültiges Wort ist, das bei `'e'` endet! Wir halten an.
3. **Der Knoten ist nutzlos (leer und kein Wort):** Wenn wir `"apple"` löschen und `"apples"` nicht existiert. `'e'` hat keine Kinder und ist nicht mehr das Ende eines Wortes. Wir löschen es physisch mittels `del` aus der Map seines Elternknotens! Wir gehen hoch zum `'l'`. Hat `'l'` andere Kinder? Nein. Ist es ein Wort? Nein. Wir führen `del` aus!

**2. Die Bottom-Up DFS-Löschung:**
Da wir Knoten vom UNTEREN Ende des Tries nach oben löschen müssen (wir können `'l'` erst löschen, nachdem wir `'e'` erfolgreich gelöscht haben), MÜSSEN wir eine rekursive Post-Order DFS verwenden!
Wir wandern rekursiv den String hinunter, bis wir das letzte Zeichen erreichen.
Während die Rekursion dann wieder nach OBEN zurückkehrt, wenden wir unsere drei Prüfungen an:
Wenn `len(node.children) == 0` UND `node.is_end_of_word == False`, geben wir `True` zurück (als Signal an den Elternknoten: "Hey, ich bin völlig nutzlos, lösche mich!").
Der Elternknoten empfängt dieses Signal und löscht das Kind explizit aus seiner Hash Map.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for trie_04: Delete Word from Trie.

Decrement per-node counts along the path. The word is
still present iff some other word shares the same path.
"""


def solve(words, n, target):
    children = []
    is_end = []
    count = []

    def new_node():
        children.append({})
        is_end.append(False)
        count.append(0)
        return len(children) - 1

    root = new_node()
    for w in words:
        cur = root
        count[cur] += 1
        for ch in w:
            nxt = children[cur].get(ch)
            if nxt is None:
                nxt = new_node()
                children[cur][ch] = nxt
            cur = nxt
            count[cur] += 1
        is_end[cur] = True
    cur = root
    count[cur] -= 1
    for ch in target:
        if ch not in children[cur]:
            return target in words
        cur = children[cur][ch]
        count[cur] -= 1
    cur = root
    for ch in target:
        if ch not in children[cur]:
            return False
        cur = children[cur][ch]
    return is_end[cur] and count[cur] > 0
```

</details>

## Walk-through

Der Trie enthält aktuell: `"apple"`, `"ape"`.
Lösche `"ape"`.

1. `dfs(root, depth=0)`. Folgt `'a'`.
2. `dfs('a', depth=1)`. Folgt `'p'`.
3. `dfs('p', depth=2)`. Folgt `'e'`.
4. `dfs('e', depth=3)`.
   - `depth == len("ape")` (3).
   - `node.is_end_of_word = False`.
   - Hat `'e'` Kinder? Nein. Gibt `True` zurück.
5. Zurück zu `dfs('p', depth=2)`:
   - `should_delete_child` ist `True`!
   - `del node.children['e']`.
   - Sind wir nutzlos? `len(children) == 1` (es hat noch `'p'` für "apple").
   - Gibt `False` zurück.
6. Zurück zu `dfs('a', depth=1)`:
   - `should_delete_child` ist `False`.
   - Tut nichts. Gibt `False` zurück.
7. Zurück zum `root`:
   - `should_delete_child` ist `False`. Tut nichts.

Ergebnis: `"ape"` ist weg. Der `'e'`-Knoten wurde aus dem Speicher gelöscht, um Platz zu sparen. `"apple"` bleibt vollständig intakt, da `'p'` die kaskadierende Löschung blockiert hat! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M)$ | $O(M)$ |
| **Durchschnittlicher Fall** | $O(M)$ | $O(M)$ |
| **Schlechtester Fall** | $O(M)$ | $O(M)$ |

Die DFS traversiert exakt M Knoten (die Länge des Wortes) nach unten und kehrt exakt M Schritte wieder nach oben zurück.
Hash-Map-Lookups und Löschungen `del dict[key]` benötigen $O(1)$ konstante Zeit.
Die gesamte Zeitkomplexität ist mathematisch strikt $O(M)$.
Die Platzkomplexität beträgt $O(M)$ für den rekursiven Aufruf-Stack der Tiefe M.

## Varianten & Optimierungen

- **Präfix-Zähler-Löschung ($O(M)$ iterativ):** Wenn Sie den erweiterten Trie (`trie_02`) verwenden, der `prefix_count` mitführt, wird das Löschen massiv einfacher und iterativ! Sie wandern einfach iterativ das Wort hinunter. An jedem Knoten dekrementieren Sie `curr.prefix_count -= 1`. Wenn `curr.prefix_count == 0` ist, führen Sie einfach ein `del` auf den Kind-Pointer aus und `return` sofort! Pythons Garbage Collector wird automatisch den gesamten abgetrennten Teilbaum bereinigen! Keine Rekursion erforderlich!

## Anwendungen in der Praxis

- **Netzwerk-Routing-Sicherheit:** Aktualisierung massiver Hardware-Access-Control-List (ACL) IP-Subnetze, wobei dynamisch auf der Blacklist stehende IP-Blöcke aus den Routing-Tabellen entfernt werden, indem ihre gemeinsamen Präfixe im Hardware-Trie gelöscht werden.

## Verwandte Algorithmen in cOde(n)

- **[trie_01 - Trie Insert/Search](trie_01_trie-insert-and-search.md)** — Die grundlegende Architektur.
- **[tree_15 - BST Delete](../trees/tree_15_bst-delete.md)** — Vergleichen Sie dies mit der Standard-Löschung in einem Binary Search Tree. Die Trie-Löschung ist weitaus eleganter, da Sie niemals Knoten umstrukturieren oder "rotieren" müssen, um Lücken zu füllen; Sie schneiden einfach tote Enden ab!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*