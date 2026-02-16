[[preprocessing]]
[[gradient-descent]]
O **`StandardScaler`** é uma ferramenta de pré-processamento de dados da biblioteca **scikit-learn** usada para **padronizar** (ou seja, normalizar em termos estatísticos) as características (features) de um conjunto de dados. Essa padronização transforma os dados de forma que cada feature passe a ter **média zero (0)** e **desvio padrão um (1)**.

Essa técnica é especialmente útil em algoritmos de aprendizado de máquina que são sensíveis à escala dos dados, como regressão linear, SVM e PCA.

A fórmula usada pelo `StandardScaler` para transformar cada valor é:
$$ z = \frac{x - \mu}{\sigma} $$
Onde:

- **x** é o valor original da feature
- **μ (mu)** é a média dos valores da feature
- **σ (sigma)** é o desvio padrão da feature
- **z** é o valor padronizado (resultado da transformação)
---
## Parâmetros

### - `copy`: _bool_, default=True

Se `False`, o escalonamento pode ser feito "in-place", ou seja, sem criar uma cópia dos dados de entrada. No entanto, isso só é possível em certas condições, como quando os dados são arrays NumPy ou matrizes `scipy.sparse` em formatos compatíveis. Caso contrário, uma cópia dos dados ainda poderá ser gerada.

### - `with_mean`: _bool_, default=True

Se `True`, o scaler irá subtrair a média de cada feature antes de aplicar a escala. Isso implica centralizar os dados em torno de zero.

> **Nota:** Não é compatível com matrizes esparsas (`sparse`) porque a centralização tornaria a matriz densa, o que pode ser inviável em termos de uso de memória.

### - `with_std`: _bool_, default=True

Se `True`, o scaler irá dividir os dados pelo desvio padrão de cada feature, garantindo variância unitária.

---

## Atributos

### - `mean_`: _array de shape (n_features,)_
Média calculada para cada feature durante o ajuste (`fit`). Usada para centralização se `with_mean=True`.

### - `scale_`: _array de shape (n_features,)_
Desvio padrão calculado para cada feature. Usado para escalonamento se `with_std=True`.

### - `var_`: _array de shape (n_features,)_
Variância calculada para cada feature no conjunto de treino.

### - `n_samples_seen_`: _int_
Número de amostras usadas para calcular as estatísticas internas (média e desvio padrão).

---
## Métodos Principais

- `fit(X)`: Calcula a média e o desvio padrão de cada feature com base nos dados `X`    
- `transform(X)`: Aplica a padronização aos dados com base nas estatísticas aprendidas durante o `fit`.
- `fit_transform(X)`: Combina `fit` e `transform` em uma única etapa.
- `inverse_transform(X_scaled)`: Reverte os dados padronizados para o formato original (antes da transformação).