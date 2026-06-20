# App de gestion de stock - Mugen Odyssey
import json
import os

FICHIER_STOCK = "stock.json"

# Charger les produits depuis le fichier
def charger_stock():
    if os.path.exists(FICHIER_STOCK):
        with open(FICHIER_STOCK, 'r') as f:
            return json.load(f)
    return {}

# Sauvegarder les produits dans le fichier
def sauvegarder_stock(stock):
    with open(FICHIER_STOCK, 'w') as f:
        json.dump(stock, f, indent=2)

# Ajouter un produit
def ajouter_produit(stock, designation, reference, quantite):
    if reference in stock:
        print(f"❌ Erreur : Référence {reference} existe déjà !")
        return
    stock[reference] = {
        "designation": designation,
        "quantite": quantite
    }
    sauvegarder_stock(stock)
    print(f"✅ {designation} ({reference}) ajouté(e) : {quantite} pièce(s)")

# Voir tous les produits
# Voir tous les produits OU chercher par référence
def voir_stock(stock, reference=None):
    if not stock:
        print("📭 Aucun produit en stock")
        return
    
    if reference:
        # Chercher un produit spécifique
        if reference not in stock:
            print(f"❌ Référence {reference} introuvable !")
            return
        info = stock[reference]
        print(f"\n📊 {info['designation']} ({reference}) : {info['quantite']} pièce(s)\n")
    else:
        # Afficher tous les produits
        print("\n📊 === TON STOCK ===")
        for ref, info in stock.items():
            print(f"  {info['designation']} ({ref}) : {info['quantite']} pièce(s)")
        print()
def modifier_quantite(stock, reference, quantite_change):
    if reference not in stock:
        print(f"❌ Erreur : Référence {reference} introuvable !")
        return
    
    nouvelle_quantite = stock[reference]["quantite"] + quantite_change
    
    if nouvelle_quantite < 0:
        print(f"❌ Erreur : Quantité ne peut pas être négative !")
        return
    
    stock[reference]["quantite"] = nouvelle_quantite
    sauvegarder_stock(stock)
    designation = stock[reference]["designation"]
    print(f"✅ {designation} : {nouvelle_quantite} pièce(s)")

# Supprimer un produit
def supprimer_produit(stock, reference):
    if reference not in stock:
        print(f"❌ Erreur : Référence {reference} introuvable !")
        return
    
    designation = stock[reference]["designation"]
    del stock[reference]
    sauvegarder_stock(stock)
    print(f"✅ {designation} ({reference}) supprimé(e)")

# Menu principal
def menu():
    stock = charger_stock()
    
    while True:
        print("\n🛒 === APP DE GESTION DE STOCK ===")
        print("1️⃣  Ajouter un produit")
        print("2️⃣  Voir le stock")
        print("3️⃣  Ajouter des pièces")
        print("4️⃣  Retirer des pièces")
        print("5️⃣  Supprimer un produit")
        print("6️⃣  Chercher un produit par référence")
        print("7️⃣  Quitter")
        
        choix = input("\nChoisis une option (1-7) : ").strip()
        
        if choix == "1":
            designation = input("Désignation du produit : ").strip()
            reference = input("Référence : ").strip()
            try:
                quantite = int(input("Quantité : ").strip())
                ajouter_produit(stock, designation, reference, quantite)
            except ValueError:
                print("❌ La quantité doit être un nombre !")
        
        elif choix == "2":
            voir_stock(stock)
        
        elif choix == "3":
            reference = input("Référence du produit : ").strip()
            try:
                quantite = int(input("Nombre de pièces à ajouter : ").strip())
                modifier_quantite(stock, reference, quantite)
            except ValueError:
                print("❌ La quantité doit être un nombre !")
        
        elif choix == "4":
            reference = input("Référence du produit : ").strip()
            try:
                quantite = int(input("Nombre de pièces à retirer : ").strip())
                modifier_quantite(stock, reference, -quantite)
            except ValueError:
                print("❌ La quantité doit être un nombre !")
        
        elif choix == "5":
            reference = input("Référence du produit à supprimer : ").strip()
            supprimer_produit(stock, reference)
        elif choix == "6":
            reference = input("Référence du produit à chercher : ").strip()
            voir_stock(stock, reference)
        
        elif choix == "7":
            print("👋 À bientôt !")
            break
        
        elif choix == "6":
            print("👋 À bientôt !")
            break
        
        else:
            print("❌ Option invalide, réessaie !")

# Lancer l'app
if __name__ == "__main__":
    menu()