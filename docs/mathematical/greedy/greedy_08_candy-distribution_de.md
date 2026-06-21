# Formale mathematische Spezifikation: Candy Distribution Problem

## 1. Definitionen und Notation

Sei $R = \langle r_0, r_1, \dots, r_{n-1} \rangle$ eine Sequenz von Bewertungen, wobei $r_i \in \mathbb{Z}^+$ die Bewertung des $i$-ten Kindes repräsentiert. Die Menge der Kinder ist durch $I = \{0, 1, \dots, n-1\}$ indiziert.

Wir definieren eine Verteilungsfunktion $C: I \to \mathbb{Z}^+$, wobei $C(i)$ die Anzahl der an Kind $i$ vergebenen Süßigkeiten bezeichnet. Das Ziel ist es, eine Funktion $C$ zu finden, welche die Gesamtsumme $S = \sum_{i=0}^{n-1} C(i)$ unter den folgenden Nebenbedingungen minimiert:

1. **Positivitätsbedingung:** $\forall i \in I, C(i) \geq 1$.
2. **Lokale Monotoniebedingung:** 
   - Wenn $r_i > r_{i-1}$, dann $C(i) > C(i-1)$ für $i \in \{1, \dots, n-1\}$.
   - Wenn $r_i > r_{i+1}$, dann $C(i) > C(i+1)$ für $i \in \{0, \dots, n-2\}$.

Der Zustandsraum $\mathcal{S}$ ist die Menge aller Vektoren $\mathbf{c} \in (\mathbb{Z}^+)^n$, die die obigen Bedingungen erfüllen. Wir suchen $\mathbf{c}^* = \arg \min_{\mathbf{c} \in \mathcal{S}} \sum_{i=0}^{n-1} c_i$.

## 2. Algebraische Charakterisierung

Um $\mathbf{c}^*$ zu bestimmen, zerlegen wir die Bedingungen in zwei unabhängige gerichtete Durchläufe. Sei $L_i$ die minimale Anzahl an Süßigkeiten, die erforderlich ist, um die Bedingung für den linken Nachbarn zu erfüllen, und $R_i$ die minimale Anzahl, um die Bedingung für den rechten Nachbarn zu erfüllen.

### Durchlauf 1: Links-nach-rechts-Sweep
Wir definieren die Sequenz $L = \langle L_0, L_1, \dots, L_{n-1} \rangle$ über die Rekurrenz:
$$L_0 = 1$$
$$L_i = \begin{cases} L_{i-1} + 1 & \text{wenn } r_i > r_{i-1} \\ 1 & \text{sonst} \end{cases} \quad \text{für } i = 1, \dots, n-1$$

### Durchlauf 2: Rechts-nach-links-Sweep
Wir definieren die Sequenz $R = \langle R_0, R_1, \dots, R_{n-1} \rangle$ über die Rekurrenz:
$$R_{n-1} = 1$$
$$R_i = \begin{cases} R_{i+1} + 1 & \text{wenn } r_i > r_{i+1} \\ 1 & \text{sonst} \end{cases} \quad \text{für } i = n-2, \dots, 0$$

### Optimale Lösung
Die minimale Süßigkeitenverteilung $C^*(i)$ ergibt sich aus dem punktweisen Maximum der beiden gerichteten Bedingungen:
$$C^*(i) = \max(L_i, R_i)$$
Die minimale Gesamtzahl an Süßigkeiten $S^*$ ist:
$$S^* = \sum_{i=0}^{n-1} \max(L_i, R_i)$$

**Korrektheitsinvariante:** Für jedes $i$ ist $C^*(i)$ die kleinste ganze Zahl, die sowohl $C^*(i) > C^*(i-1)$ (falls $r_i > r_{i-1}$) als auch $C^*(i) > C^*(i+1)$ (falls $r_i > r_{i+1}$) erfüllt. Da $L_i$ und $R_i$ die engsten unteren Schranken für ihre jeweiligen Richtungen darstellen, ist ihr Maximum die engste untere Schranke für die Schnittmenge beider Bedingungen.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt drei separate lineare Durchläufe über das Eingabe-Array der Größe $n$ aus:
1. Der Vorwärtsdurchlauf berechnet $L_i$ in $O(n)$ Zeit, da jeder Schritt $i$ eine konstante Anzahl an Operationen umfasst: $T_1 = \sum_{i=1}^{n-1} \Theta(1) = \Theta(n)$.
2. Der Rückwärtsdurchlauf berechnet $R_i$ und die laufende Summe $S^*$ in $O(n)$ Zeit: $T_2 = \sum_{i=n-2}^{0} \Theta(1) = \Theta(n)$.
3. Die gesamte Zeitkomplexität beträgt $T(n) = T_1 + T_2 = \Theta(n)$.

### Platzkomplexität
Der Algorithmus erfordert die Allokation eines zusätzlichen Arrays `candies` der Größe $n$, um die Werte von $L_i$ zu speichern und diese anschließend zu $C^*(i)$ zu aktualisieren.
- Der benötigte Speicherplatz ist $S(n) = \text{sizeof}(\text{int}) \times n$.
- Somit beträgt die zusätzliche Platzkomplexität $O(n)$. 
- Die gesamte Platzkomplexität, einschließlich der Speicherung der Eingabe, beträgt $O(n)$.