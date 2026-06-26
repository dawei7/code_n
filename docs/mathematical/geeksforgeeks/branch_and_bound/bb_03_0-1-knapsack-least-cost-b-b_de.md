# Formale mathematische Spezifikation: 0-1 Knapsack (Least Cost Branch & Bound)

## 1. Definitionen und Notation

Sei das 0-1 Knapsack-Problem definiert durch eine Menge von $n$ Objekten, $I = \{1, 2, \dots, n\}$. Jedes Objekt $i \in I$ ist durch ein Gewicht $w_i \in \mathbb{R}^+$ und einen Wert $v_i \in \mathbb{R}^+$ charakterisiert. Gegeben eine Gesamtkapazität $W \in \mathbb{R}^+$, suchen wir einen binären Vektor $\mathbf{x} = (x_1, x_2, \dots, x_n) \in \{0, 1\}^n$, der die Zielfunktion maximiert:
$$f(\mathbf{x}) = \sum_{i=1}^n v_i x_i$$
unter der Nebenbedingung:
$$\sum_{i=1}^n w_i x_i \le W$$

**Zustandsraum:** Der Algorithmus durchsucht einen Binärbaum $\mathcal{T}$ der Tiefe $n$. Ein Knoten $u$ auf der Tiefe $k$ repräsentiert eine Teillösung $\mathbf{x}^{(k)} = (x_1, \dots, x_k, ?, \dots, ?)$. 
- Sei $V_u = \sum_{i=1}^k v_i x_i$ der akkumulierte Wert am Knoten $u$.
- Sei $W_u = \sum_{i=1}^k w_i x_i$ das akkumulierte Gewicht am Knoten $u$.

**Schrankenfunktionen:** Wir definieren zwei Funktionen, um den Suchraum zu beschneiden:
1. **Obere Schranke ($UB$):** Sei $UB(u)$ der maximal mögliche Wert, der von Knoten $u$ aus erreicht werden kann, wenn eine fraktionale Auswahl der verbleibenden Objekte erlaubt ist (die Relaxation zum Fractional Knapsack). Wenn $W_u > W$, ist $UB(u) = -\infty$.
2. **Untere Schranke ($LB$):** Sei $LB(u)$ der Wert einer zulässigen Lösung, die durch einen Greedy-Ansatz von Knoten $u$ aus gefunden wurde.

## 2. Algebraische Charakterisierung

Der Algorithmus verwendet eine Priority Queue $\mathcal{Q}$, um aktive Knoten zu speichern, sortiert nach ihren $UB$-Werten. Der Zustandsübergang wird durch die Verzweigungsregel definiert:
Für einen Knoten $u$ auf der Ebene $k$ generieren wir zwei Kinder:
- **Linkes Kind (Einschluss):** $x_{k+1} = 1$, gültig falls $W_u + w_{k+1} \le W$.
- **Rechtes Kind (Ausschluss):** $x_{k+1} = 0$.

**Optimalitätsbedingung:**
Sei $f^*$ der bisher gefundene globale Maximalwert (der aktuelle beste $LB$). Der Algorithmus hält die Invariante aufrecht, dass für jeden Knoten $u \in \mathcal{Q}$ gilt: Wenn $UB(u) \le f^*$, dann kann der Teilbaum mit Wurzel $u$ keine optimale Lösung enthalten.

**Abbruchkriterium:**
Der Algorithmus terminiert, wenn $\mathcal{Q} = \emptyset$ oder wenn $\max_{u \in \mathcal{Q}} \{UB(u)\} \le f^*$. Da $UB(u)$ eine zulässige Heuristik ist (sie liefert eine obere Schranke für den optimalen Wert des Teilbaums), garantiert die Bedingung $UB(u) \le f^*$, dass kein Knoten in der Queue einen Wert liefern kann, der größer ist als das aktuelle Optimum, was die globale Optimalität sicherstellt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität im schlechtesten Fall ist $O(2^n)$. 
- **Herleitung:** Im schlechtesten Fall gelingt es der Schrankenfunktion $UB(u)$ nicht, Zweige zu beschneiden (z. B. wenn alle Objekte identische Wert-zu-Gewicht-Verhältnisse haben oder die Kapazität hinreichend groß ist). Der Algorithmus führt dann eine vollständige Traversierung des Binärbaums $\mathcal{T}$ durch, welcher $2^{n+1}-1$ Knoten enthält.
- **Aufwand pro Knoten:** An jedem Knoten berechnen wir $UB$ und $LB$, was $O(n)$ Zeit erfordert. Mit vorberechneten Suffix-Summen kann dies jedoch nach einer initialen $O(n \log n)$ Sortierphase auf $O(1)$ reduziert werden.
- **Gesamt:** $T(n) = O(n \log n) + \sum_{i=0}^n 2^i \cdot O(1) = O(2^n)$.

### Platzkomplexität
Die Platzkomplexität ist $O(2^n)$ im schlechtesten Fall, wenngleich sie in der Praxis meist deutlich niedriger ausfällt.
- **Hilfsspeicher:** Die Priority Queue $\mathcal{Q}$ speichert die Front des Suchbaums. Im schlechtesten Fall ist die Anzahl der Knoten in der Queue proportional zur Anzahl der Blätter, $O(2^n)$.
- **Gesamtspeicher:** $S(n) = O(2^n)$. 
- **Hinweis:** Während der theoretische schlechteste Fall exponentiell ist, beschneidet die "Least Cost"-Heuristik den Suchbaum in der Praxis signifikant, was oft zu einer Platzkomplexität führt, die näher bei $O(n \cdot d)$ liegt, wobei $d$ die effektive Tiefe der Suche vor dem Eintreten der Beschneidung ist.