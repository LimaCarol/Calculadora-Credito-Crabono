# Calculadora de emissão de carbono
def calcular_emissoes(consumo_de_combustivel, distancia, tipo_combustivel):

# Fator de emissão (aproximado) de CO2 em kg/l para os combustiveis 
    fatores_emissao = {
        1: 2.80, #1 = gasolina
        2: 2.60, #2 = diesel
        3: 0.56  #3 = alcool
        }
    
    cilindradas_padrao = {
        1: 1600, #Cilindradas em Centimetros Cubicos para gasolina
        2: 2000, #Cilindradas em Centimetros Cubicos para diesel 
        3: 1400  #Cilindradas em Centimetros Cubicos para alcool
    }

    if tipo_combustivel not in fatores_emissao or tipo_combustivel not in cilindradas_padrao :
        print("Selecione um tipo de combustível válido")

        return None
    
    fator_emissao = fatores_emissao[tipo_combustivel]
    cilindradas_padrao = cilindradas_padrao[tipo_combustivel]
    fator_emissao_cilindradas = fator_emissao * (cilindradas_padrao / cilindradas_padrao)
    emissoes = consumo_de_combustivel*fator_emissao_cilindradas*distancia

    return emissoes

# Coletando dados do usuario
def coletor_dados():
    print("-"*127)
    print("Bem vindo! Antes, algumas informações:")
    print("")
    print("Cada tonelada métrica de CO2 equivalente (tCO2e) reduzida gera um credito de carbono. 1 Credito de carbono equivale a U$37.")
    print("")
    print("Consideramos também as cilindradas em centimetros cubicos padrão para cada combustivel")
    print("Gasolina: 1600 Cilindradas em Centimetros Cubicos")
    print("Diesel: 2000 Cilindradas em Centimetros Cubicos")
    print("Alcool: 1400 Cilindradas em Centimetros Cubicos")
    print("-"*127)
    print("")

    consumo_de_combustivel = float(input("Digite o consumo de combustivel em litros:"))
    distancia = float(input("Digite a distância percorrida em KM:"))
    tipo_combustivel = int(input("Digite o tipo de combustivel (1 = gasolina; 2 = diesel; 3 = alcool):"))
    if tipo_combustivel not in [1,2,3]:
        print("Selecione um tipo de combustível válido (1 = gasolina; 2 = diesel; 3 = alcool)")

        return None
    
    return consumo_de_combustivel, distancia, tipo_combustivel

# Calculo do valor aproximado de CO2 absorvido por uma árvore por ano
def arvores_para_compensacao(emissoes_totais):
    kg_co2_por_arvore_ano = 20
    arvores_necessarias = emissoes_totais/kg_co2_por_arvore_ano
    return arvores_necessarias

# Calculo de crédito de carbono gerado
def calcular_credito_carbono(emissoes, preco_credito_carbono):
    preco_credito_carbono = 37.0 # Preço médio em US credito carbono 
    toneladas_carbono = emissoes / 1000 # Conversão de kg para toneladas
    credito_carbono = toneladas_carbono * preco_credito_carbono

    return credito_carbono

# Resultados
def resultados(emissoes, arvores_necessarias, credito_carbono):
    if emissoes is not None:
        print("")
        print("-"*37)
        print("Resultado das emissões de carbono")
        print("-"*37)
        print("")
        print(f"Emissões de CO2: {emissoes:.2f} kg C02")
        print(f"Credito de carbono gerado: {credito_carbono:.2f}")
        print("")
        print(f"Você tera que plantar {arvores_necessarias:.2f} árvores para compensar as emissões de CO2 (valor aproximado).")
        print("")
    else:
        print("Tipo de combustivel invalido ou não suportado.")

def main():
    consumo_de_combustivel, distancia, tipo_combustivel = coletor_dados()
    emissoes = calcular_emissoes(consumo_de_combustivel, distancia, tipo_combustivel)

    if emissoes is not None:
        preco_credito_carbono = 37.0 # Preço médio em US credito carbono 
        credito_carbono = calcular_credito_carbono(emissoes, preco_credito_carbono)
        arvores_necessarias = arvores_para_compensacao(emissoes)
        resultados(emissoes, arvores_necessarias, credito_carbono)

main()