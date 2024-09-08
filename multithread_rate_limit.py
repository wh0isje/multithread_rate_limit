import threading
import requests

# Função que será executada por cada thread
def send_request(url, thread_id, timeout):
    try:
        # Adicionando timeout à requisição
        response = requests.get(url, timeout=timeout)
        print(f'Thread {thread_id}: {response.status_code}')
    except requests.Timeout:
        print(f'Thread {thread_id}: Timeout - o servidor demorou a responder')
    except requests.RequestException as e:
        print(f'Thread {thread_id}: Erro ao fazer a requisição - {e}')

# Função para iniciar múltiplas threads
def test_rate_limit(url, num_threads, timeout):
    threads = []

    # Criando as threads
    for i in range(num_threads):
        thread = threading.Thread(target=send_request, args=(url, i, timeout))
        threads.append(thread)
    
    # Iniciando todas as threads
    for thread in threads:
        thread.start()

    # Aguardando todas as threads terminarem
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    url = "https://exemplo.com/api/teste"  # Altere para a URL que você quer testar
    num_threads = 20  # Número de threads (ou requisições simultâneas)
    timeout = 5  # Timeout em segundos para cada requisição (ajuste conforme necessário)
    
    test_rate_limit(url, num_threads, timeout)
