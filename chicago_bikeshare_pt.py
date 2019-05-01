# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)

print("Ok!")
 
# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for index in range(0,20):
    lines = list(zip(data_list[0],data_list[index+1]))
    print(lines)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for index, data_sample in enumerate(data_list):
    if index == 20:
         break
    print(f"{index+1} - {data_sample[6]}")  

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    '''
    Recebe uma lista de dados e um índice 
    Retorno uma lista de valores contidos no mesmo indíce das listas contidas na lista de dados

    [Parametros]
    data := lista contendo lista de dados 
    index := índice que se quer extrair os dados

    [Retorno]
    column_list := lista com valores dos dados extraídos

    [Exemplo]
    column_to_list(data_list, -3)
    >>>['', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', '', '', '', 'Female', '', 'Male', 'Male']
    '''
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for item in data:
        column_list.append(item[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
gender_list = column_to_list(data_list,-2)
male = len([gender for gender in gender_list if gender == 'Male'])
female = len([gender for gender in gender_list if gender == 'Female'])


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    '''
    Função para contar gêneros existentes e uma lista, considerando apenas "Male" e "Female"

    [Parametros]
    data_list := Uma lista de generos Ex: ['Male', 'Female', 'Male', 'Male', 'Male', 'Female']
    
    [Retorno]
    [male, female] := Lista contendo o número de ocorrências de Male e Female
    male := Quantidade de ocorrência do sexo masculino
    female := QUantidade de ocorrência do sexo feminino 
    '''
    male = len([gender for gender in column_to_list(data_list,-2) if gender == 'Male'])
    female = len([gender for gender in column_to_list(data_list,-2) if gender == 'Female'])
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    '''
    Função que verifica se a quantidede de pessoas do sexo masculino é maior, menor ou igual as do sexo feminino

    [Parametros]
    data_list := Uma lista de generos Ex: ['Male', 'Female', 'Male', 'Male', 'Male', 'Female']
    
    [Retorno]
    String := Uma string indicando qual gênero é mais frequente ou "Equal" caso ambos tenham o mesmo valor
    '''
    gender_count = count_gender(data_list)
    if gender_count[0] > gender_count[1]:
        return "Male"
    elif gender_count[0] < gender_count[1]:
        return "Female"
    else:
        return "Equal"


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_generic_type(samples_list):
    '''
    Função para extrair labels dos dados e contabilizar a quantidade de ocorrências

    [Parametros]
    samples_list := uma lista composta por valores de um tipo de dados

    [Retorno]
    type_labels := Um set de strings com o nome de cada tipo
    count_samples := Uma lista com a quantidade de ocorrencias 

    type_labels e count_samples possuem o mesmo tamanho e os 
    índices em ambos os objetos são correspondentes.

    [Exemplo]
    sample_list = column_to_list(data_list, -3) 
    count_generic_type(sample_list)
    >>>({'Customer', 'Dependent', 'Subscriber'}, [317162, 4, 1234339])

    '''

    types_labels = set(sample for sample in samples_list)
    count_samples = []
    for label in types_labels:
        counter = 0
        for sample in samples_list:
            if sample == label:
                counter += 1
        count_samples.append(counter)
    #print(types_labels, count_samples)
    return types_labels, count_samples

#types = ["Cliente", "Assinante"]
sample_list = column_to_list(data_list, -3)
types, quantity = count_generic_type(sample_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo')
plt.xticks(y_pos, types)
plt.title('Usuários por tipo')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Existem amostras onde o gênero está em branco, somar male + female não inclui essas amostras."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
def calculate_mean(values_list):
    '''
    Recebe uma lista de valores e retorna a média

    [Parametros]
    values_list := lista valores de inteiros ou decimais

    [Retorno]
    total_value/length := Valor da média 

    [Exemplo]
    data_list = [1,2,3,4,5,6]
    calculate_mean(data_list)
    >>>3.5
    '''
    length = 0
    total_value = 0
    for value in values_list:
        total_value += value
        length += 1
    return total_value/length

def calculate_median(values_list):
    '''
    Recebe uma lista de valores e retorna a mediana

    [Parametos]
    values_list := lista valores de inteiros ou decimais

    [Retorno]
    median := Valor da mediana 
    
    [Exemplo]
    values_list = [1, 3, 3, 6, 7, 8, 9]
    calculate_median(values_list)
    >>>6

    values_list = [3, 5, 7, 9]
    calculate_median(values_list)
    >>>6
    
    Cálculo como descrito em:
    https://pt.wikipedia.org/wiki/Mediana_(estatística)
    
    '''

    length = 0
    for item in values_list:
        length += 1
    
    if length % 2 == 0:
        position = int(length)/2  #length é par, dividir por 2 retonar um valor terminado em .0,  podendo ser desprezado.
        median =  (values_list[position] + values_list[position - 1])/2 # procura o valores centrais pelo indice e divide por 2 
    else:
        position = int((length + 1)/2) # length é impar, somado + 1 retorna um número par. Ao dividir por 2 podemos desprezar o decimal sem risco. 
        median = values_list[position - 1] # median -1 para retornar o índice
    
    return median 


trip_duration_list = [int(trip_duration) for trip_duration in column_to_list(data_list, 2)]
trip_duration_list.sort()
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
mean_trip = calculate_mean(trip_duration_list)
median_trip = calculate_median(trip_duration_list)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(station for station in column_to_list(data_list,3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#      """
#      Função de exemplo com anotações.
#      Argumentos:
#          param1: O primeiro parâmetro.
#          param2: O segundo parâmetro.
#      Retorna:
#          Uma lista de valores x.
#
#      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

# Havia feito uma função para isso na tarefa 7

def count_items(column_list):
    item_types , count_items = count_generic_type(column_list)
       
    return  item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
