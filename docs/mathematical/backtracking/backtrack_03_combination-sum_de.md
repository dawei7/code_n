# Formale mathematische Spezifikation: Combination Sum

## 1. Definitionen und Notation

Um eine rigorose Grundlage für den **Combination Sum**-Algorithmus zu schaffen, definieren wir die Eingabeparameter, den Ausgaberaum und den Zustandsraum der Backtracking-Suche unter Verwendung der formalen Mengenlehre und algebraischer Strukturen.

### 1.1 Eingaberaum
Sei $C$ eine endliche Menge von $N$ verschiedenen positiven Ganzzahlen, die die Kandidaten repräsentieren:
$$C = \{c_1, c_2, \dots, c_N\} \subset \mathbb{Z}^+$$
Ohne Beschränkung der Allgemeinheit nehmen wir an, dass die Elemente von $C$ in streng aufsteigender Reihenfolge sortiert sind:
$$c_1 < c_2 < \dots < c_N$$
Sei $T \in \mathbb{Z}^+$ die Zielsumme.

### 1.2 Ausgaberaum (Die Lösungsmenge)
Eine gültige Kombination ist eine Multimenge von Elementen aus $C$, deren Summe $T$ ergibt. Um doppelte Repräsentationen zu vermeiden und Eindeutigkeit zu erzwingen, repräsentieren wir jede Kombination eindeutig als nicht-abnehmende Sequenz (oder Tupel) $P$.

Sei $P = (p_1, p_2, \dots, p_k)$ eine Sequenz der Länge $k \ge 1$. Wir definieren die Menge aller gültigen Kombinationen $\mathcal{P}(C, T)$ als:
$$\mathcal{P}(C, T) = \left\{ (p_1, p_2, \dots, p_k) \in C^k \;\middle|\; k \in \mathbb{Z}^+, \ \sum_{j=1}^k p_j = T, \text{ und } p_j \le p_{j+1} \ \forall j \in \{1, \dots, k-1\} \right\}$$

Alternativ können wir die Lösungsmenge durch einen Multiplizitätsvektor $x = (x_1, x_2, \dots, x_N) \in \mathbb{N}_0^N$ charakterisieren, wobei $x_i$ die Häufigkeit des Kandidaten $c_i$ in der Kombination angibt:
$$\mathcal{S}(C, T) = \left\{ (x_1, x_2, \dots, x_N) \in \mathbb{N}_0^N \;\middle|\; \sum_{i=1}^N x_i c_i = T \right\}$$
Es existiert eine Bijektion $\phi: \mathcal{P}(C, T) \to \mathcal{S}(C, T)$, die jede sortierte Sequenz auf ihren entsprechenden Multiplizitätsvektor abbildet.

### 1.3 Backtracking-Zustandsraum
Der Backtracking-Algorithmus exploriert systematisch einen Zustandsraum-Baum. Ein Suchzustand $u$ ist definiert als ein Tripel:
$$u = (i, R, P) \in \mathcal{X}$$
wobei:
*   $i \in \{1, \dots, N\}$ der **Startindex** ist, der die Auswahl auf das Suffix $\{c_i, \dots, c_N\}$ einschränkt, um doppelte Permutationen zu verhindern (z. B. das Generieren von sowohl $(2, 3)$ als auch $(3, 2)$).
*   $R \in \mathbb{Z}_{\ge 0}$ die **verbleibende Zielsumme** ist.
*   $P = (p_1, \dots, p_d)$ der **aktuelle Pfad** (die bisher getroffene Sequenz von Entscheidungen) der Tiefe $d \ge 0$ ist.

Der formale Zustandsraum $\mathcal{X}$ ist definiert als:
$$\mathcal{X} = \left\{ (i, R, P) \;\middle|\; 1 \le i \le N, \ 0 \le R \le T, \ P \in C^d, \ \sum_{y \in P} y = T - R \right\}$$

---

## 2. Algebraische Charakterisierung

Der Backtracking-Algorithmus kann als gerichteter Zustandsübergangsgraph $G = (\mathcal{X}, E)$ modelliert werden, wobei die Menge der gerichteten Kanten $E$ gültige Einzelschritt-Entscheidungen repräsentiert.

### 2.1 Zustandsübergangsrelation
Für jeden Zustand $u = (i, R, P) \in \mathcal{X}$ mit $R > 0$ existiert ein Übergang zu einem Folgezustand $u'$ für jeden Kandidaten $c_j$, der die Ordnung nicht verletzt oder die verbleibende Zielsumme nicht überschreitet:
$$(i, R, P) \xrightarrow{c_j} (j, R - c_j, P \parallel c_j)$$
wobei:
*   $j \in \{i, \dots, N\}$ (erzwingt eine nicht-abnehmende Reihenfolge der Elemente in $P$).
*   $c_j \le R$ (Pruning-Bedingung).
*   $P \parallel c_j$ die Konkatenation der Sequenz $P$ mit dem Element $c_j$ bezeichnet.

### 2.2 Rekursionsgleichung
Sei $f(i, R)$ eine mengenwertige Funktion, die alle gültigen, auf das Suffix eingeschränkten Sequenzen von Elementen aus $\{c_i, \dots, c_N\}$ zurückgibt, die sich zu $R$ summieren. Wir definieren $f(i, R)$ rekursiv als:

$$f(i, R) = \begin{cases} 
\{ () \} & \text{falls } R = 0 \\
\emptyset & \text{falls } R < 0 \text{ oder } i > N \\
\bigcup_{j=i}^{N} \left\{ (c_j) \parallel p \;\middle|\; p \in f(j, R - c_j) \right\} & \text{sonst}
\end{cases}$$

#### Sortieroptimierung und vorzeitiges Pruning
Da das Kandidaten-Array $C$ sortiert ist ($c_1 < c_2 < \dots < c_N$), gilt: Wenn $c_j > R$ für ein $j \ge i$, dann gilt für alle $k \ge j$ ebenfalls $c_k > R$. Dies erlaubt uns, die Vereinigung zu verkürzen:
$$f(i, R) = \bigcup_{\substack{j=i \\ c_j \le R}}^{N} \left\{ (c_j) \parallel p \;\middle|\; p \in f(j, R - c_j) \right\}$$
Diese algebraische Formulierung garantiert, dass der Suchraum sofort beschnitten wird, wenn ein Kandidat die verbleibende Zielsumme überschreitet, wodurch die Exploration redundanter Teilbäume verhindert wird.

### 2.3 Beweisskizze zur Korrektheit
Die Korrektheit des Algorithmus wird durch vollständige Induktion über die verbleibende Zielsumme $R$ etabliert.
*   **Induktionsanfang ($R = 0$):** Die leere Sequenz $()$ ist die eindeutige Sequenz, die sich zu $0$ summiert. $f(i, 0) = \{()\}$, was korrekt ist.
*   **Induktionsschritt:** Wir nehmen an, dass $f(j, R - c_j)$ korrekt alle gültigen nicht-abnehmenden Sequenzen berechnet, die sich zu $R - c_j$ summieren, unter Verwendung von Elementen aus $\{c_j, \dots, c_N\}$. Durch Voranstellen von $c_j$ vor jede Sequenz in $f(j, R - c_j)$ erhalten wir Sequenzen, die sich zu $c_j + (R - c_j) = R$ summieren. Da $j \ge i$, ist das vorangestellte Element $c_j$ kleiner oder gleich allen Elementen in den Sequenzen von $f(j, R - c_j)$, wodurch die nicht-abnehmende Reihenfolge gewahrt bleibt. Die Bildung der Vereinigung über alle gültigen $j \ge i$ ergibt exakt die Menge aller nicht-abnehmenden Sequenzen, die sich zu $R$ summieren und mit einem Element-Index $\ge i$ beginnen.

---

## 3. Komplexitätsanalyse

### 3.1 Zeitkomplexität

Sei $M = \min(C) = c_1$ der kleinste Kandidat in $C$. 

#### 3.1.1 Maximale Tiefe des Suchbaums
Die maximale Tiefe $D$ des Rekursionsbaums tritt auf, wenn wir wiederholt das kleinste Element $c_1$ wählen:
$$D = \left\lfloor \frac{T}{M} \right\rfloor$$

#### 3.1.2 Obere Schranke für die Anzahl der Zustände
An jedem Knoten im Suchbaum können wir bis zu $N$ Verzweigungen haben. Eine lose obere Schranke für die Gesamtzahl der Knoten im Suchbaum ist durch die Summe einer geometrischen Reihe gegeben:
$$\sum_{d=0}^{D} N^d = \frac{N^{D+1} - 1}{N - 1} = O\left(N^D\right) = O\left(N^{T/M}\right)$$

#### 3.1.3 Exakte kombinatorische Schranke
Da wir eine nicht-abnehmende Reihenfolge auf den Pfaden erzwingen ($j \ge i$), explorieren wir nicht alle Permutationen einer Kombination. Die Anzahl der eindeutigen nicht-abnehmenden Sequenzen der Länge höchstens $D$ unter Verwendung von $N$ Elementen entspricht der Anzahl der Kombinationen mit Wiederholung (Multikombinationen):
$$\left(\!\left( \begin{matrix} N \\ D \end{matrix} \right)\!\right) = \binom{N + D - 1}{D}$$

Summiert über alle möglichen Tiefen $d \le D$:
$$\sum_{d=0}^{D} \binom{N + d - 1}{d} = \binom{N + D}{D} = \binom{N + \lfloor T/M \rfloor}{\lfloor T/M \rfloor}$$

An jedem Blattknoten, der eine gültige Lösung repräsentiert, benötigt das Kopieren des Pfades der Länge höchstens $D$ in die Ausgabeliste $O(D) = O(T/M)$ Zeit. Somit ist die exakte asymptotische Zeitkomplexität beschränkt durch:
$$\mathcal{O}\left( \frac{T}{M} \cdot \binom{N + T/M}{T/M} \right)$$
Im Schlechtesten Fall, in dem $N \gg T/M$, ist dies lose durch $O\left( N^{T/M} \right)$ beschränkt.

---

### 3.2 Platzkomplexität

Die Platzkomplexität wird hinsichtlich des Hilfsspeichers analysiert (Speicher, der vom Algorithmus während der Ausführung verwendet wird, exklusive der Ausgabespeicherung).

#### 3.2.1 Rekursions-Stack-Speicher
Die maximale Tiefe des Call-Stacks entspricht der maximalen Höhe des Zustandsraum-Baums. Der tiefste Zweig wird exploriert, wenn der Algorithmus wiederholt das minimale Element $M = c_1$ auswählt. Die maximale Stack-Tiefe beträgt:
$$\text{Depth}_{\max} = \left\lfloor \frac{T}{M} \right\rfloor$$
Jeder Stack-Frame speichert eine konstante Anzahl von Variablen ($start$, $remaining$ und Schleifenindizes), was $O(1)$ Speicher pro Frame erfordert.

#### 3.2.2 Pfadspeicher
Der Algorithmus verwaltet ein dynamisches Array `path`, um die aktuelle Kombinationssequenz zu speichern. Die maximale Größe dieses Arrays ist durch die maximale Tiefe des Baums beschränkt:
$$\text{Size}_{\max}(\text{path}) = \left\lfloor \frac{T}{M} \right\rfloor$$

#### 3.2.3 Gesamter Hilfsspeicher
Kombiniert man den Rekursions-Stack und den Pfadspeicher, ergibt sich die Hilfsplatzkomplexität zu:
$$\mathcal{O}\left(\text{Depth}_{\max} + \text{Size}_{\max}(\text{path})\right) = \mathcal{O}\left(\frac{T}{M}\right)$$

Wenn der Speicherplatz für die endgültige Ausgabeliste einbezogen wird, beträgt die gesamte Platzkomplexität:
$$\mathcal{O}\left( \frac{T}{M} \cdot \left| \mathcal{P}(C, T) \right| + \frac{T}{M} \right)$$
wobei $\left| \mathcal{P}(C, T) \right|$ die Gesamtzahl der gültigen Kombinationen ist.