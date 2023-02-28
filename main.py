# Definição do vetor de faturamento diário da distribuidora
faturamento_diario = [1500, 2000, 1200, 3000, 1800, 2500, 1900, 0, 1700, 2300, 2800, 2600, 3100, 0, 2200, 2400, 1800, 2000, 2700, 2200, 2400, 1900, 2100, 0, 2600, 2000, 2200, 2500, 1900, 2000, 2800]

# Cálculo do menor e do maior valor de faturamento diário
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

# Cálculo da média mensal de faturamento diário, ignorando os dias sem faturamento
faturamento_valido = [faturamento for faturamento in faturamento_diario if faturamento != 0]
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

# Contagem do número de dias no mês em que o faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for faturamento in faturamento_valido if faturamento > media_mensal)

# Impressão dos resultados
print("O menor valor de faturamento diário ocorrido no mês foi: R$", menor_faturamento)
print("O maior valor de faturamento diário ocorrido no mês foi: R$", maior_faturamento)
print("O número de dias no mês em que o faturamento diário foi superior à média mensal foi:", dias_acima_da_media)
