Rate Limit Tester
Descrição
Este script tem como objetivo testar o limite de requisições simultâneas (rate-limit) de uma API ou site. Utilizando múltiplas threads, ele é capaz de enviar um grande número de requisições simultâneas para verificar se o servidor responde adequadamente ou se impõe limites de acesso.

O script é útil para realizar testes de estresse, detectar mecanismos de rate-limiting e garantir que um servidor web ou API esteja preparado para lidar com uma alta carga de requisições.

Funcionalidades
Requisições simultâneas: Envia um número configurável de requisições ao mesmo tempo usando threads.
Timeout configurável: Define um tempo limite para cada requisição, evitando que o script fique preso se o servidor não responder.
Tratamento de erros: Exibe mensagens em caso de falhas, como timeouts ou erros de conexão.
