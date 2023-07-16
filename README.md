# Resolvendo o mesmo algoritmo com o GitHub Copilot, ChatGPT e o BARD

Este projeto tem como objetivo comparar o desempenho e as respostas geradas pelo GitHub Copilot, ChatGPT e BARD ao resolverem o mesmo algoritmo, o repeatedString.

O algoritmo repeatedString é um desafio que envolve a manipulação de strings e a contagem de ocorrências de um caractere específico em uma sequência de strings repetidas infinitamente. Durante o processo de resolução, foi fornecido um prompt padrão para as três ferramentas de inteligência artificial.

Foram estabelecidas as seguintes premissas para o experimento:

* Tempo limite de 15 minutos para trabalhar em cada solução.
* O código gerado pelas AIs não poderia ser alterado diretamente, apenas copiado e colado.
* As respostas geradas pelas AIs foram comparadas em termos de precisão e desempenho.

O repositório contém os seguintes arquivos:

* `copilot_algorithm.py`: Implementação do algoritmo gerado pelo GitHub Copilot.
* `chatgpt_algorithm.py`: Implementação do algoritmo gerado pelo ChatGPT.
* `bard_algorithm.py`: Implementação do algoritmo gerado pelo BARD.
* `benchmark.py`: Conjunto de casos de teste para avaliar as soluções.

Resultados obtidos:

* GitHub Copilot: 3 acertos de 25 testes. Tempo de execução excedeu o limite.
* ChatGPT: 8 acertos de 25 testes. Tempo de execução dentro do limite.
* BARD: 19 acertos de 25 testes. Tempo de execução dentro do limite.

Conclusão: O BARD se destacou em relação ao GitHub Copilot e ao ChatGPT, apresentando uma maior precisão nas respostas e um tempo de execução satisfatório. O ChatGPT obteve um tempo de execução aceitável, mas com uma precisão menor. Já o GitHub Copilot teve dificuldades em fornecer respostas corretas dentro do tempo limite estabelecido.

Este projeto serve como um experimento para explorar as capacidades das AIs em resolver problemas algorítmicos e comparar seu desempenho. As informações aqui apresentadas podem auxiliar no entendimento das diferenças entre essas ferramentas de inteligência artificial.

## Como executar os algoritmos

1. Certifique-se de ter Python instalado em seu ambiente.
2. Execute cada arquivo de implementação do algoritmo (`copilot_algorithm.py`, `chatgpt_algorithm.py`, `bard_algorithm.py`) utilizando um interpretador Python.
3. Os resultados serão exibidos no console.

Sinta-se à vontade para explorar os códigos e os testes realizados. Contribuições e melhorias são bem-vindas.

**Observação**: Este projeto não tem como objetivo promover ou denegrir qualquer uma das ferramentas utilizadas. Ele foi realizado com fins experimentais e educacionais, buscando apenas avaliar o desempenho das AIs em resolver o mesmo problema específico.