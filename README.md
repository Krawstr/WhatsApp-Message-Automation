<h1 align="left">WhatsApp Message Automation</h1>

###

<h4>Descrição</h4>
<p>Este script automatiza o envio de mensagens via WhatsApp utilizando a API do Twilio. Ele lê números de telefone e nomes de um arquivo Excel 
  (telefones.xlsx)
  e envia mensagens em horários programados. O objetivo é facilitar o envio de mensagens periódicas e reduzir a necessidade de interação manual.</p>
  
  ###

<h3>Funcionalidades</h3>
<ul>
  <li>Envio automatizado de mensagens: Mensagens são enviadas para os contatos definidos no Excel.</li>
  <li>Controle de horários: As mensagens são enviadas em horários específicos (9:00 e 16:00, por exemplo).</li>
  <li>Fuso horário configurado: Adapta-se ao horário local do Brasil (America/Sao_Paulo).</li>
  <li>Log de envio: Registra os envios no console, exibindo o status e o SID de cada mensagem.</li>   
</ul>

###

<h3>Como usar</h3>
<ol>
  <li> <p>Pré-requisitos:</p></li>
  <ul>
      <li><p>instale as bibliotecas necessarias</p>
      ```bash
        pip install beautifulsoup4 requests
      ```</li>
  </ul>
  
</ol>
