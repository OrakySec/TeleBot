import random
import time
import telebot
from datetime import datetime

# substitua <SEU_TOKEN> pelo token do seu bot criado no BotFather
bot = telebot.TeleBot('6241855745:AAEK-cYBCwaLprRpvJqv-Ru4pYWqp7LqL_s')

chat_id = "-1001941781910"

# sequência de Fibonacci
fibonacci = [0, 2, 4, 7]

# inicializando o índice da sequência de Fibonacci
i = 0

while True:
    try:
        # obtendo o horário atual
        now = datetime.now()

        # verificando se o último dígito do minuto atual é um número da sequência de Fibonacci
        if now.minute % 10 in fibonacci:
            # gerando número aleatório para o número de jogadas
            jogadas = random.randint(5, 13)

            # gerando número aleatório para a validade (em segundos)
            validade = random.randint(1, 5)

            # construindo a mensagem com o link na palavra 'link'
            mensagem = f'<b>🟢 Oportunidade Identificada 🟢</b>\n' \
                       f'\n' \
                       f'🐯 Fortune Tiger 🐯\n' \
                       f'🔥 Nº de Jogadas: <b>{jogadas}</b>\n' \
                       f'🕓 Validade: <b>{validade}</b> minutos\n' \
                       f'⚜ Bot Fibonacci\n\n\n' \
                       f'<b>🔰 Conheça a BetFiery 🔰</b>\n\n' \
                       f'A mais conviável casa\n' \
                       f'de apostas online\n' \
                       f'Cadastre-se pelo nosso link\n' \
                       f'E receba um bônus de <b>100%</b>\n' \
                       f'Do valor da primeira recarga\n\n' \
                       f'<a href="https://tinyurl.com/app-betfiery?referralcode=643c7815822c6de5ce2dd54f">' \
                       f'<b>👉 CADASTRE-SE 👈</b></a>'
                       

            # enviando a mensagem com parse_mode = 'HTML' para suportar o link
            bot.send_message(chat_id, mensagem, parse_mode='HTML')

            # atualizando o índice da sequência de Fibonacci
            i += 1
            if i >= len(fibonacci):
                i = 0

            # tempo de espera definido pela sequência de Fibonacci
            tempo_espera = fibonacci[i]
            time.sleep(tempo_espera * 60)

        else:
            # aguardando 1 minuto para verificar novamente
            time.sleep(60)

    except Exception as e:
        print("Ocorreu um erro:", e)
        # Pode-se fazer algo com o erro, como registrar em um log ou enviar uma notificação
        # Neste exemplo, o programa irá continuar a execução na próxima iteração do loop
