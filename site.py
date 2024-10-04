from flask import Flask, render_template, request, redirect

app = Flask(name)

# Lista para armazenar as mensagens (em memória)
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send_message():
    username = request.form['username']
    message = request.form['message']
    
    # Adiciona a mensagem à lista
    messages.append(f"{username}: {message}")
    
    # Redireciona para a página inicial para mostrar as mensagens
    return redirect('/')

# Arquivo HTML simples (chat.html) com um formulário de envio
# Salve este conteúdo em um arquivo 'templates/chat.html'
"""

"""

if name == 'main':
    app.run(debug=True)