# Formale mathematische Spezifikation: TSP via MST (2-Approximation)

## 1. Definitionen und Notation

Sei $G = (V, E, w)$ ein vollständiger, ungerichteter, gewichteter Graph, der das Netzwerk von Städten und die Distanzen zwischen ihnen repräsentiert, wobei:
*   $V = \{v_0, v_1, \dots, v_{n-1}\}$ die Menge der Knoten (Städte) ist, mit der Kardinalität $|V| = n \ge 2$.
*   $E = \{\{u, v\} \mid u, v \in V, u \neq v\}$ die Menge der ungerichteten Kanten ist. Da $G$ vollständig ist, beträgt die Anzahl der Kanten $|E| = \frac{n(n-1)}{2}$.
*   $w: E \to \mathbb{R}^+$ eine Gewichtsfunktion ist, die jede Kante auf eine positive reelle Zahl abbildet, welche die Distanz zwischen den Knoten repräsentiert.

### Annahmen zum metrischen Raum
Es wird angenommen, dass die Gewichtsfunktion $w$ einen metrischen Raum über $V$ definiert. Insbesondere erfüllt sie für alle $u, v, x \in V$ die folgenden Eigenschaften:
1.  **Nicht-Negativität**: $w(u, v) \ge 0$, mit $w(u, v) = 0 \iff u = v$.
2.  **Symmetrie**: $w(u, v) = w(v, u)$.
3.  **Dreiecksungleichung**: 
    $$w(u, v) \le w(u, x) + w(x, v)$$

### Spannbäume und minimale Spannbäume (MST)
*   Ein **Spannbaum** von $G$ ist ein azyklischer Teilgraph $T = (V, E_T)$, wobei $E_T \subseteq E$ und $|E_T| = n - 1$.
*   Das Gewicht eines Spannbaums $T$ ist die Summe seiner Kantengewichte:
    $$w(T) = \sum_{e \in E_T} w(e)$$
*   Ein **Minimaler Spannbaum (MST)**, bezeichnet als $T^* = (V, E_{T^*})$, ist ein Spannbaum, der dieses Gesamtgewicht minimiert:
    $$T^* = \arg\min_{T \in \mathcal{T}} w(T)$$
    wobei $\mathcal{T}$ die Menge aller Spannbäume von $G$ ist.

### Hamilton-Zyklen und das Problem des Handlungsreisenden (TSP)
*   Ein **Hamilton-Zyklus** (oder TSP-Tour) in $G$ ist ein geschlossener Pfad, der jeden Knoten in $V$ genau einmal besucht und zum Startknoten zurückkehrt. Formal kann er als Permutation $\pi$ der Knotenindizes $\{0, 1, \dots, n-1\}$ dargestellt werden, die den Zyklus definiert:
    $$H = (v_{\pi(0)}, v_{\pi(1)}, \dots, v_{\pi(n-1)}, v_{\pi(0)})$$
*   Das Gewicht eines Hamilton-Zyklus $H$ ist:
    $$w(H) = \sum_{i=0}^{n-2} w(v_{\pi(i)}, v_{\pi(i+1)}) + w(v_{\pi(n-1)}, v_{\pi(0)})$$
*   Die **optimale TSP-Tour**, bezeichnet als $H^*$, ist ein Hamilton-Zyklus mit minimalem Gewicht:
    $$H^* = \arg\min_{H \in \mathcal{H}} w(H)$$
    wobei $\mathcal{H}$ die Menge aller Hamilton-Zyklen in $G$ ist.

---

## 2. Algebraische Charakterisierung und Korrektheitsbeweis

Der 2-Approximationsalgorithmus konstruiert eine approximative TSP-Tour $H_{approx}$ durch drei sequentielle algebraische Phasen: Konstruktion des minimalen Spannbaums, Erzeugung eines Euler-Multigraphen und Abkürzung mittels Preorder-Traversierung.

### Phase 1: Konstruktion des minimalen Spannbaums (Prim-Algorithmus)
Sei $S_k \subset V$ die Menge der bereits besuchten Knoten zum Schritt $k$, und $E_{T, k}$ die Menge der bis Schritt $k$ ausgewählten Kanten.
*   **Initialisierung ($k=0$)**:
    $$S_0 = \{v_0\}, \quad E_{T, 0} = \emptyset$$
*   **Induktionsschritt ($k \in \{1, \dots, n-1\}$)**:
    Wähle eine Kante $e_k = \{u_k, v_k\}$, die das Schnittgewicht zwischen $S_{k-1}$ und $V \setminus S_{k-1}$ minimiert:
    $$e_k = \arg\min \{ w(u, v) \mid u \in S_{k-1}, v \in V \setminus S_{k-1} \}$$
    Aktualisiere den Zustand:
    $$S_k = S_{k-1} \cup \{v_k\}, \quad E_{T, k} = E_{T, k-1} \cup \{e_k\}$$
*   **Terminierung**: Der resultierende Graph $T^* = (V, E_{T, n-1})$ ist ein MST von $G$.

### Phase 2: Verdopplung der Kanten und der Euler-Kreis
Sei $2T^*$ der gerichtete Multigraph, der durch Ersetzen jeder ungerichteten Kante $\{u, v\} \in E_{T^*}$ durch zwei gerichtete Kanten $(u, v)$ und $(v, u)$ entsteht. 
*   Für jeden Knoten $v \in V$ sind der Eingangsgrad $\deg^-(v)$ und der Ausgangsgrad $\deg^+(v)$ in $2T^*$ gleich dem Grad von $v$ in $T^*$:
    $$\deg^-(v) = \deg^+(v) = \deg_{T^*}(v)$$
*   Da $2T^*$ zusammenhängend ist und jeder Knoten einen gleichen Eingangs- und Ausgangsgrad besitzt, ist $2T^*$ ein Euler-Graph. Er enthält einen Euler-Kreis $U = (u_0, u_1, \dots, u_{2n-2}, u_0)$ mit dem Gesamtgewicht:
    $$w(U) = \sum_{i=0}^{2n-2} w(u_i, u_{i+1}) = 2 \cdot w(T^*)$$
    wobei $u_{2n-1} = u_0$.

### Phase 3: Preorder-Traversierung und Abkürzung
Sei $\text{DFS}(T^*, v_0)$ die Sequenz der Knoten, die während einer Tiefensuche (DFS) auf $T^*$ beginnend bei der Wurzel $v_0$ besucht werden. Wir definieren den Abkürzungsoperator $\mathcal{S}$, der den Euler-Pfad $U$ auf einen Hamilton-Zyklus $H_{approx}$ abbildet, indem nur das erste Auftreten jedes Knotens beibehalten wird.

Sei $H_{approx} = (v_{\sigma(0)}, v_{\sigma(1)}, \dots, v_{\sigma(n-1)}, v_{\sigma(0)})$ die Sequenz der eindeutigen Knoten in der Reihenfolge ihrer Entdeckung in $\text{DFS}(T^*, v_0)$, wobei $\sigma(0) = 0$.

### Mathematischer Beweis der Approximationsschranke

Um zu beweisen, dass der Algorithmus eine 2-Approximation garantiert, stellen wir zwei fundamentale Lemmata auf.

#### Lemma 1: Untere Schranke des MST
Das Gewicht des minimalen Spannbaums $T^*$ ist strikt kleiner als das Gewicht der optimalen TSP-Tour $H^*$:
$$w(T^*) < w(H^*)$$

*Beweis:* Sei $H^*$ der optimale Hamilton-Zyklus. Das Entfernen einer beliebigen Kante $e \in H^*$ ergibt einen Spannpfad $P$. Da $w(e) > 0$:
$$w(P) = w(H^*) - w(e) < w(H^*)$$
Da $P$ ein Spannbaum von $G$ ist und $T^*$ der *minimale* Spannbaum von $G$ ist, gilt per Definition:
$$w(T^*) \le w(P)$$
Die Kombination dieser Ungleichungen ergibt:
$$w(T^*) \le w(H^*) - w(e) < w(H^*)$$
$\blacksquare$

#### Lemma 2: Dreiecksungleichung und Abkürzung
Das Gewicht der abgekürzten Tour $H_{approx}$ ist höchstens so groß wie das Gewicht des Euler-Kreises $U$:
$$w(H_{approx}) \le w(U)$$

*Beweis:* Die Sequenz $H_{approx}$ wird konstruiert, indem Teilpfade in $U$ der Form $(x, y_1, y_2, \dots, y_k, z)$ — wobei $y_1, \dots, y_k$ bereits besuchte Knoten sind — durch eine direkte Kante $(x, z)$ ersetzt werden.
Durch induktive Anwendung der Dreiecksungleichung gilt:
$$w(x, z) \le w(x, y_1) + w(y_1, y_2) + \dots + w(y_k, z)$$
Summiert man diese Ungleichung über alle Abkürzungen, die zur Konstruktion von $H_{approx}$ aus $U$ vorgenommen wurden, erhält man:
$$w(H_{approx}) \le w(U)$$
$\blacksquare$

#### Theorem: 2-Approximationsgarantie
Die Gesamtkosten der vom Algorithmus generierten Tour betragen höchstens das Doppelte der Kosten der optimalen Tour:
$$w(H_{approx}) \le 2 \cdot w(H^*)$$

*Beweis:* Durch Kombination der Ergebnisse aus Lemma 1 und Lemma 2:
$$w(H_{approx}) \le w(U) = 2 \cdot w(T^*) < 2 \cdot w(H^*)$$
Somit erfüllt das Approximationsverhältnis $\alpha$:
$$\alpha = \frac{w(H_{approx})}{w(H^*)} \le 2$$
$\blacksquare$

---

## 3. Komplexitätsanalyse

### Zeitkomplexitätsanalyse

Die Rechenkomplexität des Algorithmus wird durch drei verschiedene Phasen bestimmt: MST-Konstruktion, Baumrepräsentation und Tiefensuche.

```
  [Input: Cost Matrix]
           │
           ▼
┌──────────────────────┐
│ Phase 1: Prim's MST  │  ◄─── O(V^2) using array-based min-set
└───────┬──────────────┘       or O(E log V) = O(V^2 log V) with Heap
        │
        ▼
┌──────────────────────┐
│ Phase 2: Tree Rep.   │  ◄─── O(V) to construct adjacency list
└───────┬──────────────┘
        │
        ▼
┌──────────────────────┐
│ Phase 3: DFS Walk    │  ◄─── O(V) to generate preorder tour
└──────────────────────┘
```

#### 1. MST-Konstruktion (Prim-Algorithmus)
Sei $V$ die Menge der Knoten und $E$ die Menge der Kanten. In einem vollständigen Graphen gilt $|E| = \Theta(V^2)$.
*   **Naive Implementierung (wie im Python-Code gezeigt)**:
    Die äußere Schleife läuft $V-1$ Mal. Innerhalb wird eine verschachtelte Suche über alle Paare $(u, v) \in V \times V$ durchgeführt, um die Kante mit dem minimalen Gewicht zu finden, die den Schnitt kreuzt. Der Arbeitsaufwand beträgt:
    $$T_{\text{naive}}(V) = \sum_{k=1}^{V-1} \sum_{u=1}^{V} \sum_{v=1}^{V} \mathcal{O}(1) = \sum_{k=1}^{V-1} \mathcal{O}(V^2) = \Theta(V^3)$$
*   **Standard-Array-basierter Prim-Algorithmus**:
    Durch die Pflege eines `key`-Arrays, das das minimale Gewicht von einem beliebigen Knoten im MST zu einem Knoten außerhalb des MST speichert, können wir den minimalen Knoten in $O(V)$ finden und die Keys in $O(V)$ aktualisieren.
    $$T_{\text{array}}(V) = \sum_{k=1}^{V} \left( \mathcal{O}(V) + \mathcal{O}(V) \right) = \Theta(V^2)$$
*   **Binärer Heap-basierter Prim-Algorithmus**:
    Unter Verwendung eines binären Heaps zum Extrahieren der Kante mit dem minimalen Gewicht dauert das Extrahieren des Minimums $O(\log V)$ und das Aktualisieren der Keys $O(\log V)$ pro Kante.
    $$T_{\text{heap}}(V) = \mathcal{O}(V \log V + E \log V)$$
    Da der Graph vollständig ist ($E = \Theta(V^2)$):
    $$T_{\text{heap}}(V) = \mathcal{O}(V^2 \log V)$$

#### 2. Baumrepräsentation
Die Umwandlung der Eltern-Array-Repräsentation des MST in eine Adjazenzliste der Kinder erfordert das Iterieren über das Eltern-Array der Größe $V$:
$$T_{\text{tree}}(V) = \Theta(V)$$

#### 3. Tiefensuche (DFS)
Die DFS besucht jeden Knoten genau einmal und traversiert jede Kante des Baums $T^*$ genau zweimal (einmal abwärts, einmal aufwärts). Da $T^*$ $V-1$ Kanten hat:
$$T_{\text{dfs}}(V) = \Theta(V + (V-1)) = \Theta(V)$$

#### 4. Akkumulation der Tourkosten
Das Summieren der Gewichte der Kanten im finalen Hamilton-Zyklus der Länge $V$ dauert:
$$T_{\text{cost}}(V) = \Theta(V)$$

#### Gesamte Zeitkomplexität
Die gesamte Zeitkomplexität wird von der Phase der MST-Konstruktion dominiert. Abhängig von der Implementierung des Prim-Algorithmus:
*   **Naive Implementierung**: $\Theta(V^3)$
*   **Binäre Heap-Implementierung**: $\Theta(V^2 \log V)$
*   **Array-basierte Implementierung (Optimal für dichte Graphen)**: $\Theta(V^2)$

---

### Platzkomplexitätsanalyse

Die Platzkomplexität wird hinsichtlich des Hilfsspeichers (vom Algorithmus belegter Speicher exklusive der Eingabe) und des Gesamtspeichers analysiert.

#### 1. Hilfsspeicher
Der Hilfsspeicher wird von folgenden Datenstrukturen verbraucht:
*   `in_mst`: Ein boolesches Tracking-Array der Größe $V \implies \Theta(V)$ Bits.
*   `parent`: Ein Integer-Array der Größe $V$, das die MST-Struktur speichert $\implies \Theta(V)$ Wörter.
*   `children`: Eine Adjazenzliste, die den gerichteten Baum repräsentiert, enthaltend $V$ Listenköpfe und insgesamt $V-1$ Knoten $\implies \Theta(V)$ Wörter.
*   `tour`: Ein Array, das die Preorder-Traversierungssequenz der Größe $V$ speichert $\implies \Theta(V)$ Wörter.
*   **Rekursions-Stack**: Der Ausführungs-Stack während der DFS-Traversierung hat eine maximale Tiefe, die der Höhe des Baums $T^*$ entspricht. Im Schlechtesten Fall (ein degenerierter Linien-Graph) beträgt die Tiefe $V$, was $\Theta(V)$ Stack-Frames erfordert.

Summiert man diese Komponenten:
$$\text{Space}_{\text{auxiliary}}(V) = \Theta(V) + \Theta(V) + \Theta(V) + \Theta(V) + \mathcal{O}(V) = \Theta(V)$$

#### 2. Gesamtspeicher
Die gesamte Platzkomplexität beinhaltet die Eingaberepräsentation. Die Eingabe ist eine Adjazenzmatrix der Größe $V \times V$, die den vollständigen Graphen repräsentiert:
$$\text{Space}_{\text{input}}(V) = \Theta(V^2)$$
Somit ist die gesamte Platzkomplexität:
$$\text{Space}_{\text{total}}(V) = \text{Space}_{\text{input}}(V) + \text{Space}_{\text{auxiliary}}(V) = \Theta(V^2)$$