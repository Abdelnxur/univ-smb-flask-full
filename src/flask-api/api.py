from flask import Flask, jsonify, request
import json, os

app = Flask(__name__)

# Lire un fichier JSON
def lire(fichier):
    with open(os.path.join('data', fichier)) as f:
        return json.load(f)

# Ecrire dans un fichier JSON
def ecrire(fichier, data):
    with open(os.path.join('data', fichier), 'w') as f:
        json.dump(data, f, indent=4)

# Retourne la liste des webservers
@app.route('/webserver')
def liste_webservers():
    return jsonify(lire('webserver.json'))

# Retourne un webserver par son id
@app.route('/webserver/<int:id>')
def detail_webserver(id):
    liste = lire('webserver.json')
    item = next((x for x in liste if x['id'] == id), None)
    if item is None:
        return jsonify({'erreur': 'introuvable'}), 404
    return jsonify(item)

# Ajoute un webserver
@app.route('/webserver', methods=['POST'])
def ajouter_webserver():
    liste = lire('webserver.json')
    nouveau = request.json
    nouveau['id'] = max([x['id'] for x in liste], default=0) + 1
    liste.append(nouveau)
    ecrire('webserver.json', liste)
    return jsonify(nouveau), 201

# Supprime un webserver
@app.route('/webserver/<int:id>', methods=['DELETE'])
def supprimer_webserver(id):
    liste = lire('webserver.json')
    liste = [x for x in liste if x['id'] != id]
    ecrire('webserver.json', liste)
    return jsonify({'message': 'supprimé'})

# Retourne la liste des reverse proxies
@app.route('/reverseproxie')
def liste_reverseproxies():
    return jsonify(lire('reverseproxie.json'))

# Retourne un reverse proxy par son id
@app.route('/reverseproxie/<int:id>')
def detail_reverseproxie(id):
    liste = lire('reverseproxie.json')
    item = next((x for x in liste if x['id'] == id), None)
    if item is None:
        return jsonify({'erreur': 'introuvable'}), 404
    return jsonify(item)

# Ajoute un reverse proxy
@app.route('/reverseproxie', methods=['POST'])
def ajouter_reverseproxie():
    liste = lire('reverseproxie.json')
    nouveau = request.json
    nouveau['id'] = max([x['id'] for x in liste], default=0) + 1
    liste.append(nouveau)
    ecrire('reverseproxie.json', liste)
    return jsonify(nouveau), 201

# Supprime un reverse proxy
@app.route('/reverseproxie/<int:id>', methods=['DELETE'])
def supprimer_reverseproxie(id):
    liste = lire('reverseproxie.json')
    liste = [x for x in liste if x['id'] != id]
    ecrire('reverseproxie.json', liste)
    return jsonify({'message': 'supprimé'})

# Retourne la liste des load balancers
@app.route('/loadbalancer')
def liste_loadbalancers():
    return jsonify(lire('loadbalancer.json'))

# Retourne un load balancer par son id
@app.route('/loadbalancer/<int:id>')
def detail_loadbalancer(id):
    liste = lire('loadbalancer.json')
    item = next((x for x in liste if x['id'] == id), None)
    if item is None:
        return jsonify({'erreur': 'introuvable'}), 404
    return jsonify(item)

# Ajoute un load balancer
@app.route('/loadbalancer', methods=['POST'])
def ajouter_loadbalancer():
    liste = lire('loadbalancer.json')
    nouveau = request.json
    nouveau['id'] = max([x['id'] for x in liste], default=0) + 1
    liste.append(nouveau)
    ecrire('loadbalancer.json', liste)
    return jsonify(nouveau), 201

# Supprime un load balancer
@app.route('/loadbalancer/<int:id>', methods=['DELETE'])
def supprimer_loadbalancer(id):
    liste = lire('loadbalancer.json')
    liste = [x for x in liste if x['id'] != id]
    ecrire('loadbalancer.json', liste)
    return jsonify({'message': 'supprimé'})