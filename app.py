from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
FICHIER_STOCK = "stock.json"

# Charger les produits
def charger_stock():
    if os.path.exists(FICHIER_STOCK):
        with open(FICHIER_STOCK, 'r') as f:
            return json.load(f)
    return {}

# Sauvegarder les produits
def sauvegarder_stock(stock):
    with open(FICHIER_STOCK, 'w') as f:
        json.dump(stock, f, indent=2)

# Page d'accueil - Voir tous les produits
@app.route('/')
def index():
    stock = charger_stock()
    return render_template('index.html', stock=stock)

# Ajouter un produit
@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        designation = request.form['designation'].strip()
        reference = request.form['reference'].strip()
        quantite = int(request.form['quantite'])
        
        stock = charger_stock()
        
        if reference in stock:
            return "Erreur : Référence existe déjà !"
        
        stock[reference] = {
            "designation": designation,
            "quantite": quantite
        }
        sauvegarder_stock(stock)
        return redirect('/')
    
    return render_template('ajouter.html')

# Modifier la quantité
@app.route('/ajouter_quantite/<reference>', methods=['POST'])
def ajouter_quantite(reference):
    stock = charger_stock()
    if reference in stock:
        stock[reference]["quantite"] += 1
        sauvegarder_stock(stock)
    return redirect('/')

@app.route('/retirer_quantite/<reference>', methods=['POST'])
def retirer_quantite(reference):
    stock = charger_stock()
    if reference in stock and stock[reference]["quantite"] > 0:
        stock[reference]["quantite"] -= 1
        sauvegarder_stock(stock)
    return redirect('/')

# Supprimer un produit
@app.route('/supprimer/<reference>', methods=['GET','POST'])
def supprimer(reference):
    stock = charger_stock()
    
    if reference in stock:
        del stock[reference]
        sauvegarder_stock(stock)
    
    return redirect('/')

# Lancer l'app
if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)