# Algoritmo de Viabilidade Urbana para Novas Empresas
import pandas as pd

# 1. Base de dados dos bairros (Sub-scores de 0 a 10)
dados_bairros = {
    'Bairro': ['Centro', 'Floresta', 'Buritis', 'Savassi', 'Castelo'],
    'Concorrencia': [3.0, 6.5, 5.0, 2.5, 8.5],
    'Seguranca': [5.0, 7.0, 8.0, 9.0, 8.5],
    'Onibus': [10.0, 8.0, 5.5, 10.0, 6.0],
    'Apps': [10.0, 8.5, 6.0, 10.0, 6.5]
}

df = pd.DataFrame(dados_bairros)

# 2. Definição dos pesos estatísticos (Soma = 1.0)
w_C, w_S, w_T, w_A = 0.40, 0.30, 0.15, 0.15

# 3. Função para calcular a Nota Final de Viabilidade com Fator de Penalidade
def calcular_nv(row):
    # Cálculo da média ponderada das notas do bairro
    nota_base = (w_C * row['Concorrencia'] + 
                 w_S * row['Seguranca'] + 
                 w_T * row['Onibus'] + 
                 w_A * row['Apps'])
    
    # Aplicação da Penalidade automática de 30% se a Segurança for crítica (< 4.0)
    fator_p = 0.7 if row['Seguranca'] < 4.0 else 1.0
    
    return round(nota_base * fator_p, 2)

# Execução do modelo analítico na base de dados
df['Nota_Final_Viabilidade'] = df.apply(calcular_nv, axis=1)

# Ordenação e geração do ranking de viabilidade comercial
ranking = df.sort_values(by='Nota_Final_Viabilidade', ascending=False)
print(ranking[['Bairro', 'Nota_Final_Viabilidade']])
