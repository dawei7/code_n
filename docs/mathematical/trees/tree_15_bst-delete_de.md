# Formale mathematische Spezifikation: BST-Löschung

## 1. Definitionen und Notation
Sei $T$ ein Binärer Suchbaum (Binary Search Tree, BST) und $k$ der zu löschende Schlüssel.

## 2. Algebraische Charakterisierung
Löschfunktion $\mathcal{D}(T, k) \to T'$:
1. Suchphase identisch mit $\mathcal{S}(T, k)$.
2. Wenn $T = \emptyset$, gib $\emptyset$ zurück.
3. Sei $x$ der Knoten, bei dem $x.val = k$.
   - **Fall 1 (Blatt):** Wenn $x_L = \emptyset \land x_R = \emptyset$, gib $\emptyset$ zurück.
   - **Fall 2 (Ein Kind):** Wenn $x_L = \emptyset$, gib $x_R$ zurück. Wenn $x_R = \emptyset$, gib $x_L$ zurück.
   - **Fall 3 (Zwei Kinder):** Finde den Inorder-Nachfolger $y$ (minimaler Knoten in $x_R$). Ersetze $x.val \leftarrow y.val$. Wende $\mathcal{D}(x_R, y.val)$ rekursiv an.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Der Pfad zu $x$ ist $O(\mathcal{H}(T))$. Das Finden des Inorder-Nachfolgers $y$ erfordert ein weiteres Absteigen, aber der gesamte Abstieg überschreitet niemals $\mathcal{H}(T)$. Die Gesamtzeit ist mathematisch durch $O(\mathcal{H}(T))$ begrenzt.
- **Platzkomplexität:** $O(\mathcal{H}(T))$ für Rekursion, $O(1)$ für iterative Implementierung.