# Cas de Test - App de Gestion de Stock

## Test 1 : Ajouter un produit
**Préconditions :** App lancée, aucun produit en stock

**Étapes :**
1. Choisir option 1
2. Entrer "Assiettes" comme désignation
3. Entrer "REF-001" comme référence
4. Entrer "10" comme quantité

**Résultat attendu :** ✅ Assiettes (REF-001) ajouté(e) : 10 pièce(s)

---

## Test 2 : Voir tous les produits
**Préconditions :** Au moins 1 produit en stock

**Étapes :**
1. Choisir option 2

**Résultat attendu :** Affichage de tous les produits avec références et quantités

---

## Test 3 : Chercher un produit par référence
**Préconditions :** REF-001 existe en stock

**Étapes :**
1. Choisir option 6
2. Entrer "REF-001"

**Résultat attendu :** Affichage UNIQUEMENT du produit REF-001

---

## Test 4 : Ajouter des pièces
**Préconditions :** REF-001 en stock avec 10 pièces

**Étapes :**
1. Choisir option 3
2. Entrer "REF-001"
3. Entrer "5"

**Résultat attendu :** ✅ REF-001 : 15 pièce(s)

---

## Test 5 : Retirer des pièces
**Préconditions :** REF-001 en stock avec 15 pièces

**Étapes :**
1. Choisir option 4
2. Entrer "REF-001"
3. Entrer "3"

**Résultat attendu :** ✅ REF-001 : 12 pièce(s)

---

## Test 6 : Supprimer un produit
**Préconditions :** REF-001 existe en stock

**Étapes :**
1. Choisir option 5
2. Entrer "REF-001"

**Résultat attendu :** ✅ Assiettes (REF-001) supprimé(e)

---

## Test 7 : Chercher une référence inexistante
**Préconditions :** REF-001 supprimé

**Étapes :**
1. Choisir option 6
2. Entrer "REF-001"

**Résultat attendu :** ❌ Référence REF-001 introuvable !