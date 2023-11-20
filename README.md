                                                PROJETO - Aplicação Cliente/Servidor com boot no Telegram

● Esse repositório foi criado com a perspectiva de mostrar o desenvolvimento do projeto para a disciplina Programação para Redes, do curso superior Tecnologia em Redes de 
Computadores. O projeto em si visa o desenvolvimento de uma aplicação cliente/servidor com a utilização de um boot no Telegram.

Qual tipo de Protocolo:
● TCP
Qual o motivo de escolha deste protocolo?
● O protocolo foi escolhido com o intuito de ter uma melhor experiência com o
desenvolvimento do projeto. Pois o mesmo, fornece algumas características e
funcionalidades mais relevantes do que o protocolo UDP, dentre elas, a confiabilidade 
que o protocolo entrega seus pacotes de dados, o controle de fluxo, gerenciamento
de conexões e a certeza de integridade dos dados. Além disso, por ser um protocolo
no Python que depende da conexão pré-estabelecida para funcionar, garante que
todas as funcionalidades do protocolo sejam utilizadas nos clientes e no servidor.

Quais os comandos que o boot irá interpretar?
● U -> Lista os usuários conectados ao servidor
● C -> Lista as configurações dos usuários conectados (CPU, Memória, Disco, ...)
● i ip:______ -> Traz os aplicativos instalados nos clientes especificados pelo IP
● N t:______ -> Histórico de navegação da aplicação especificada
● u ip:______ -> Traz informações detalhadas sobre o usuário especificado
● off -c ip:_____ -> Desconecta de maneira manual o cliente especificado (que está conectado em segundo plano)
● off -s -> Desconecta de maneira manual o servidor (que está rodando em segundo plano)
