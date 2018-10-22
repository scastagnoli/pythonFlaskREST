import flask
import json
import urllib.request

'''
#Sorgente dati = file JSON locale
with open('C:\\Users\\Stefano\\OneDrive\\lavori\\scuola\\appunti\\ebooks\\fileFreemind\\src\\REST\\dati.json', 'r') as f:
    toys = json.load(f)
'''
#Sorgente dati = risorsa JSON remota
'''
with urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts') as data:
    toys = data.read()
    toys = json.loads(toys.decode())
'''

with open('C:\\Users\\Stefano\\OneDrive\\lavori\\scuola\\appunti\\ebooks\\fileFreemind\\src\\REST\\dati.json', 'r') as f:
    persone = json.load(f)

app = flask.Flask(__name__)

@app.route('/api/visualizzaTutti/', methods=['GET'])
def getPersone():
    return flask.jsonify({'persone': persone})

@app.route('/api/visualizzaNome/<string:nomePersona>', methods=['GET'])
def getPersona(nomePersona):
    persona = [p for p in persone if p['first_name'] == nomePersona]
    if len(persona) == 0:
        return("Errore 404")
    return flask.jsonify({'persona': persona})   

@app.route('/api/visualizzaNominativo', methods=['GET'])
def cercaNominativo():
    nome = flask.request.get_json()['first_name']
    cognome = flask.request.get_json()['last_name']
    persona = [p for p in persone if p['first_name'] == nome and p['last_name'] == cognome]
    return flask.jsonify({'persona': persona}), 201

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')

    