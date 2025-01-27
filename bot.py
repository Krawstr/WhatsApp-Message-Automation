from datetime import datetime, date
import pytz
import openpyxl
from twilio.rest import Client
from time import sleep

ACCOUNT_SID = "ACCOUNT_SID"
AUTH_TOKEN = "AUTH_TOKEN"
FROM_WHATSAPP = "whatsapp:+numero twilio"  

def fuso_horario():
    tz = pytz.timezone('America/Sao_Paulo')
    timeNow = datetime.now(tz)
    return timeNow.strftime('%H:%M')

def sendMessage():

    workbook = openpyxl.load_workbook('telefones.xlsx')
    numerosSalvos = workbook['Planilha1']
    
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    for linha in numerosSalvos.iter_rows(min_row=2):
        name = linha[0].value
        telefone = linha[1].value
        
        mensagem = (
            f"mensagem"
            f"mensagem"
        )
        
        try:
            message = client.messages.create(
                body=mensagem,
                from_=FROM_WHATSAPP,
                to=f"whatsapp:{telefone}"
            )
            print(f"Mensagem enviada para {name} ({telefone}). SID: {message.sid}")
        except Exception as e:
            print(f"Erro ao enviar mensagem para {name} ({telefone}): {e}")

sendToday = set() 
currentDate = date.today()
while True:
    currentTime = fuso_horario()

    if currentDate != date.today():
        sendToday.clear()
        currentDate = date.today()

    if currentTime in ["9:00", "16:00"] and currentTime not in sendToday:
        sendMessage()
        sendToday.add(currentTime)
    sleep(30)