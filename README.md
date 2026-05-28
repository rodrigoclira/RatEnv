# Criação do RatEnv

Crie o ambiente `RatEnv` em um notebook utilizando Gymnasium as classes e funções da Gymnasium. 
No RatEnv, um rato (agente) precisa alcançar o objetivo, definido na posição (1,3) do grid e obter a recompensa máxima.

<img width="407" height="254" alt="image" src="https://github.com/user-attachments/assets/4c163ca7-b49d-41e1-b597-09f01aab7acc" />

Baseie-se nas informações abaixo: 

## Estados

Cada posição no grid é mapeada com um identificador único

```
Linha 0, coluna 0: 0 
Linha 0, coluna 1: 1
...
Linha 1, coluna 2: 5
```
## Ações 
A ação é definida na faixa {0, 3} indicando qual a direção que será tomada pelo agente (similar ao FrozenLake).

``` 
0: Mover para a esquerda
1: Mover para baixo
2: Mover para a direita
3: Mover para cima
```

## Recompensa
As recompensas são dadas de acordo com a seguinte tabela: 

```
R(0) = 0
R(1) = +1 
R(2) = 0 
R(3) = 0
R(4) = -10
R(5) = +10
```
## Truncated e estados terminais

- Os estados 5 e 4 são terminais no ambiente.
- Após a realização de 10 ações, o episódio será interrompido (truncated = True)

## Visão geral do ambiente 
<img width="618" height="111" alt="image" src="https://github.com/user-attachments/assets/d95398af-d6ff-48d6-ba48-ee2f0ef214c2" />


------

## O que é esperado? 

Um ambiente funcional com os métodos `step`, `reset`, `render` e `construtor` a ser definido no arquivo `RatEnv.ipynb`. 
Além desses, métodos auxiliares podem ser necessários. 

> Utilize emojis no método render https://www.invertexto.com/emojis-para-copiar


## Testando o ambiente:

- Valide a interface do ambiente utilizando o check_env da gymnasium 
```python
from gymnasium.utils.env_checker import check_env

check_env(ratEnv)
```
- Utilizando o código das funções `run_episode` e `make_scripted` do arquivo gym_util.py, valide os resultados das políticas abaixo.

> As funções `run_episode` e `make_scripted` foram usadas na aula sobre wrappers. 

```python
WORST_PATH = [1, 2] # recompensa total acumulada -10
OPTIMAL_PATH  = [2, 2, 1] # recompensa total acumulada +11
SUB_OPTIMAL_PATH = [2, 1] # recompensa total acumulada -9
```

