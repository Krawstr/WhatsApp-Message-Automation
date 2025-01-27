  <h1>WhatsApp Message Automation</h1>
    <hr>
    <h2>Descrição</h2>
    <p>
        Este script automatiza o envio de mensagens via WhatsApp utilizando a API do Twilio. Ele lê números de telefone e nomes de um arquivo Excel (<code>telefones.xlsx</code>) e envia mensagens em horários programados. O objetivo é facilitar o envio de mensagens periódicas e reduzir a necessidade de interação manual.
    </p>
    <h2>Funcionalidades</h2>
    <ul>
        <li><b>Envio automatizado de mensagens</b>: Mensagens são enviadas para os contatos definidos no Excel.</li>
        <li><b>Controle de horários</b>: As mensagens são enviadas em horários específicos (9:00 e 16:00, por exemplo).</li>
        <li><b>Fuso horário configurado</b>: Adapta-se ao horário local do Brasil (<code>America/Sao_Paulo</code>).</li>
        <li><b>Log de envio</b>: Registra os envios no console, exibindo o status e o SID de cada mensagem.</li>
    </ul>
    <h2>Como usar</h2>
    <ol>
        <li><b>Pré-requisitos</b>:
            <ul>
                <li>Instale as bibliotecas necessárias:
                    <pre><code>pip install pytz openpyxl twilio</code></pre>
                </li>
                <li>Crie uma conta no <a href="https://www.twilio.com/" target="_blank">Twilio</a> e obtenha:
                    <ul>
                        <li><code>ACCOUNT_SID</code></li>
                        <li><code>AUTH_TOKEN</code></li>
                    </ul>
                </li>
                <li>Configure um número WhatsApp no Twilio para envio.</li>
            </ul>
        </li>
        <li><b>Configuração</b>:
            <ul>
                <li>Substitua as variáveis <code>ACCOUNT_SID</code>, <code>AUTH_TOKEN</code> e <code>FROM_WHATSAPP</code> no código com as informações da sua conta Twilio.</li>
                <li>Crie um arquivo Excel chamado <code>telefones.xlsx</code> com a seguinte estrutura:
                    <table border="1">
                        <thead>
                            <tr>
                                <th>Nome</th>
                                <th>Telefone</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>João Silva</td>
                                <td>+55ddnumero</td>
                            </tr>
                        </tbody>
                    </table>
                </li>
            </ul>
        </li>
        <li><b>Execução</b>:
            <ul>
                <li>Execute o script Python:
                    <pre><code>python script.py</code></pre>
                </li>
                <li>O script ficará em execução contínua, verificando os horários configurados para envio.</li>
            </ul>
        </li>
    </ol>
    <h2>Estrutura do Código</h2>
    <ul>
        <li><code>fuso_horario</code>: Obtém o horário atual no fuso de São Paulo.</li>
        <li><code>sendMessage</code>: Lê os números do arquivo Excel e envia mensagens para os contatos.</li>
        <li><b>Controle do loop</b>:
            <ul>
                <li>Monitora o horário atual.</li>
                <li>Garante que as mensagens sejam enviadas apenas uma vez por dia nos horários configurados.</li>
                <li>Atualiza o controle diariamente.</li>
            </ul>
        </li>
    </ul>
    <h2>Personalização</h2>
    <ul>
        <li><b>Horários de envio</b>:<br>
            Altere os horários no trecho:
            <pre><code>
if currentTime in ["9:00", "16:00"] and currentTime not in sendToday:
            </code></pre>
            Adicione ou remova horários conforme necessário.
        </li>
        <li><b>Mensagem personalizada</b>:<br>
            Substitua o conteúdo da variável <code>mensagem</code> para adaptar o texto ao seu caso de uso.
        </li>
    </ul>
    <h2>Avisos</h2>
    <ul>
        <li>Certifique-se de não violar as políticas de uso do Twilio e as leis de privacidade e spam locais.</li>
        <li>Teste com números próprios antes de enviar mensagens para terceiros.</li>
    </ul>
    <h2>Requisitos do Sistema</h2>
    <ul>
        <li>Python 3.8+</li>
        <li>Conexão com a internet</li>
        <li>Conta Twilio configurada</li>
    </ul>
 <br>
    <p>
        obrigador por me ler <3.
    </p>
