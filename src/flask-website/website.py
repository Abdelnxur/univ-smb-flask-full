from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Adresse de l'API
API = "http://127.0.0.1:5000"

# Page d'accueil
@app.route("/")
def start():
    return render_template('start.html')

# Liste tous les webservers
@app.route("/webserver")
def webservers():
    liste = requests.get(f"{API}/webserver").json()
    return render_template('webserver_list.html', webservers=liste)

# Affiche le détail d'un webserver
@app.route("/webserver/<int:id>")
def webserver_detail(id):
    item = requests.get(f"{API}/webserver/{id}").json()
    return render_template('webserver_detail.html', webserver=item)

# Ajoute un webserver
@app.route("/webserver/add", methods=['GET', 'POST'])
def webserver_add():
    if request.method == 'POST':
        nouveau = {
            "name": request.form['name'],
            "ip_bind": request.form['ip_bind'],
            "port": int(request.form['port']),
            "root": request.form['root']
        }
        requests.post(f"{API}/webserver", json=nouveau)
        return redirect(url_for('webservers'))
    return render_template('webserver_add.html')

# Supprime un webserver
@app.route("/webserver/delete/<int:id>")
def webserver_delete(id):
    requests.delete(f"{API}/webserver/{id}")
    return redirect(url_for('webservers'))

# Liste tous les reverse proxies
@app.route("/reverseproxie")
def reverseproxies():
    liste = requests.get(f"{API}/reverseproxie").json()
    return render_template('reverseproxie_list.html', reverseproxies=liste)

# Affiche le détail d'un reverse proxy
@app.route("/reverseproxie/<int:id>")
def reverseproxie_detail(id):
    item = requests.get(f"{API}/reverseproxie/{id}").json()
    return render_template('reverseproxie_detail.html', reverseproxie=item)

# Ajoute un reverse proxy
@app.route("/reverseproxie/add", methods=['GET', 'POST'])
def reverseproxie_add():
    if request.method == 'POST':
        nouveau = {
            "name": request.form['name'],
            "ip_bind": request.form['ip_bind'],
            "pass": request.form['pass']
        }
        requests.post(f"{API}/reverseproxie", json=nouveau)
        return redirect(url_for('reverseproxies'))
    return render_template('reverseproxie_add.html')

# Supprime un reverse proxy
@app.route("/reverseproxie/delete/<int:id>")
def reverseproxie_delete(id):
    requests.delete(f"{API}/reverseproxie/{id}")
    return redirect(url_for('reverseproxies'))

# Liste tous les load balancers
@app.route("/loadbalancer")
def loadbalancers():
    liste = requests.get(f"{API}/loadbalancer").json()
    return render_template('loadbalancer_list.html', loadbalancers=liste)

# Affiche le détail d'un load balancer
@app.route("/loadbalancer/<int:id>")
def loadbalancer_detail(id):
    item = requests.get(f"{API}/loadbalancer/{id}").json()
    return render_template('loadbalancer_detail.html', loadbalancer=item)

# Ajoute un load balancer
@app.route("/loadbalancer/add", methods=['GET', 'POST'])
def loadbalancer_add():
    if request.method == 'POST':
        nouveau = {
            "name": request.form['name'],
            "ip_bind": request.form['ip_bind'],
            "pass": request.form['pass']
        }
        requests.post(f"{API}/loadbalancer", json=nouveau)
        return redirect(url_for('loadbalancers'))
    return render_template('loadbalancer_add.html')

# Supprime un load balancer
@app.route("/loadbalancer/delete/<int:id>")
def loadbalancer_delete(id):
    requests.delete(f"{API}/loadbalancer/{id}")
    return redirect(url_for('loadbalancers'))