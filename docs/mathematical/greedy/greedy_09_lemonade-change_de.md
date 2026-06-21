# Formale mathematische Spezifikation: Lemonade Change

## 1. Definitionen und Notation

Sei $B = (b_1, b_2, \dots, b_n)$ eine Sequenz von Geldscheinen, die die Queue der Kunden repräsentiert, wobei jeder $b_i \in \{5, 10, 20\}$ gilt.
Seien $c_5^{(i)}$ und $c_{10}^{(i)}$ die Anzahl der 5-Einheiten- und 10-Einheiten-Scheine in der Kasse nach der Bearbeitung des $i$-ten Kunden, mit dem Anfangszustand $c_5^{(0)} = 0$ und $c_{10}^{(0)} = 0$.

Der Zustand der Kasse zum Schritt $i$ ist definiert durch das Tupel $\mathcal{S}_i = (c_5^{(i)}, c_{10}^{(i)}) \in \mathbb{N}_0^2$.
Das Ziel ist es zu bestimmen, ob eine Sequenz von Übergängen existiert, sodass für alle $i \in \{1, \dots, n\}$ das erforderliche Wechselgeld $r_i = b_i - 5$ durch den aktuellen Kassenstand $\mathcal{S}_{i-1}$ gedeckt werden kann.

## 2. Algebraische Charakterisierung

Der Algorithmus verarbeitet jeden Schein $b_i$ und aktualisiert den Zustand $\mathcal{S}_i$ basierend auf der folgenden Übergangsfunktion $f: (\mathcal{S}_{i-1}, b_i) \to \mathcal{S}_i \cup \{\perp\}$, wobei $\perp$ einen ungültigen Zustand (Fehler) bezeichnet:

1. **Fall $b_i = 5$:**
   $c_5^{(i)} = c_5^{(i-1)} + 1, \quad c_{10}^{(i)} = c_{10}^{(i-1)}$

2. **Fall $b_i = 10$:**
   Falls $c_5^{(i-1)} \geq 1$:
   $c_5^{(i)} = c_5^{(i-1)} - 1, \quad c_{10}^{(i)} = c_{10}^{(i-1)} + 1$
   Sonst: $\perp$

3. **Fall $b_i = 20$:**
   Wir benötigen Wechselgeld $r_i = 15$. Die gierige Wahl (Greedy-Strategie) ist durch die Priorität definiert, einen 10-Einheiten-Schein zu verwenden:
   - Falls $c_{10}^{(i-1)} \geq 1$ und $c_5^{(i-1)} \geq 1$:
     $c_5^{(i)} = c_5^{(i-1)} - 1, \quad c_{10}^{(i)} = c_{10}^{(i-1)} - 1$
   - Sonst, falls $c_5^{(i-1)} \geq 3$:
     $c_5^{(i)} = c_5^{(i-1)} - 3, \quad c_{10}^{(i)} = c_{10}^{(i-1)}$
   - Sonst: $\perp$

**Schleifeninvariante:**
Zu jedem Schritt $k$ ist der Kassenstand $\mathcal{S}_k$ der eindeutige Zustand, der das Potenzial maximiert, zukünftige Anfragen $b_j$ ($j > k$) zu erfüllen. Da $c_5$ sowohl für 10-Einheiten- als auch für 20-Einheiten-Wechselgeld benötigt wird, während $c_{10}$ nur für 20-Einheiten-Wechselgeld erforderlich ist, bewahrt die gierige Strategie, $c_{10}$ vor $c_5$ zu verbrauchen, wenn $b_i=20$ gilt, den maximal möglichen Wert von $c_5$, welcher das "liquideste" Gut im System darstellt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus iteriert genau einmal durch die Eingabesequenz $B$. Für jedes Element $b_i$ führt die Übergangsfunktion $f$ eine konstante Anzahl an arithmetischen Operationen und Vergleichen aus, bezeichnet als $T_{step} = O(1)$.
Die gesamte Zeitkomplexität $T(n)$ ergibt sich aus der Summation:
$$T(n) = \sum_{i=1}^{n} T_{step} = \sum_{i=1}^{n} O(1) = O(n)$$
Somit ist der Algorithmus linear in Bezug auf die Anzahl der Kunden $n$.

### Platzkomplexität
Der Algorithmus verwaltet lediglich zwei skalare Variablen, $c_5$ und $c_{10}$, um den Zustand $\mathcal{S}_i$ abzubilden. Der benötigte Speicher ist unabhängig von der Eingabegröße $n$.
$$S(n) = O(1)$$
Der zusätzliche Speicherbedarf ist konstant, da keine weiteren Datenstrukturen (wie Arrays oder Hash Maps) erforderlich sind, um die Historie der Transaktionen oder den Kassenstand zu speichern.