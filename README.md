# Porjeto Py_Calc

Nesse projeto, o vetor de faturamento diário é definido logo no início do programa, incluindo alguns dias sem faturamento (representados pelo valor 0). Em seguida, utilizamos as funções min() e max() para encontrar, respectivamente, o menor e o maior valor de faturamento diário do mês.

Para calcular a média mensal, criamos um novo vetor chamado faturamento_valido utilizando uma expressão geradora (ou comprehension), que inclui apenas os valores de faturamento diferentes de zero. Em seguida, utilizamos esse vetor para calcular a média mensal da mesma forma que no exemplo anterior.

Por fim, utilizamos outra expressão geradora para contar o número de dias em que o faturamento diário foi superior à média mensal, mas desta vez utilizando o vetor faturamento_valido.

Os resultados são então impressos na tela utilizando a função print(). Note que utilizamos uma string formatada (ou f-string) para incluir os valores das variáveis nas mensagens de saída.
