import requests

tl_bot_token = ''
tl_bot_chatID = ''

def telegram_bot_sendtext(bot_message, prefix=''):
    """
    :param bot_message: Mensaje que publicará el bot.
    :param prefix: Prefijo con que se identificará el mensaje (opcional).
    :return: Resultado de la petición.
    """
    bot_token = tl_bot_token
    bot_chatID = tl_bot_chatID
    
    if prefix != '':
        bot_message = '[{}]: {}'.format(prefix,bot_message)
        
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&text=' + bot_message

    response = requests.get(send_text)

    return response.json()['ok']