# Cas de Test - Phase 2 (Interface Web Flask)

## Test 1 : Afficher la page d'accueil (index)
**Objectif :** Vérifier que la page affiche correctement le stock

**Préconditions :**
- Flask app en cours d'exécution
- Au moins 1 produit en stock

**Étapes :**
1. Ouvrir http://127.0.0.1:5000 dans le navigateur

**Résultat attendu :**
- ✅ Page se charge correctement
- ✅ Titre "🛒 Mugen Stock App" visible
- ✅ Bouton "➕ Ajouter un produit" présent
- ✅ Tableau avec colonnes : Désignation, Référence, Quantité, Actions
- ✅ Tous les produits affichés dans le tableau

---

## Test 2 : Ajouter un produit via formulaire
**Objectif :** Vérifier que le formulaire d'ajout fonctionne

**Préconditions :**
- Page d'accueil affichée

**Étapes :**
1. Cliquer sur le bouton "➕ Ajouter un produit"
2. Remplir le formulaire :
   - Désignation : "Bols Mugen"
   - Référence : "REF-002"
   - Quantité : "8"
3. Cliquer sur "Ajouter"

**Résultat attendu :**
- ✅ Redirection vers page d'accueil
- ✅ Nouveau produit "Bols Mugen (REF-002) : 8 pièces" visible en tableau
- ✅ Produit sauvegardé dans stock.json

---

## Test 3 : Augmenter la quantité avec le bouton ➕
**Objectif :** Vérifier que le bouton augmente correctement

**Préconditions :**
- "Assiettes Mugen (REF-001) : 10 pièces" en stock

**Étapes :**
1. Localiser la ligne "Assiettes Mugen (REF-001)"
2. Cliquer sur le bouton ➕ dans la colonne "Actions"

**Résultat attendu :**
- ✅ Page actualise
- ✅ Quantité passe de 10 à 11
- ✅ Modification sauvegardée dans stock.json
- ✅ POST request visible dans le terminal

---

## Test 4 : Réduire la quantité avec le bouton ➖
**Objectif :** Vérifier que le bouton réduit correctement

**Préconditions :**
- "Assiettes Mugen (REF-001) : 11 pièces" en stock

**Étapes :**
1. Localiser la ligne "Assiettes Mugen (REF-001)"
2. Cliquer sur le bouton ➖ dans la colonne "Actions"

**Résultat attendu :**
- ✅ Page actualise
- ✅ Quantité passe de 11 à 10
- ✅ Quantité ne peut pas être négative
- ✅ Modification sauvegardée dans stock.json

---

## Test 5 : Supprimer un produit avec le bouton 🗑️
**Objectif :** Vérifier que la suppression fonctionne

**Préconditions :**
- "Bols Mugen (REF-002) : 8 pièces" en stock

**Étapes :**
1. Localiser la ligne "Bols Mugen (REF-002)"
2. Cliquer sur le bouton 🗑️ dans la colonne "Actions"
3. Confirmer la suppression dans la pop-up

**Résultat attendu :**
- ✅ Pop-up "Supprimer ?" s'affiche
- ✅ Après confirmation, produit disparaît du tableau
- ✅ Produit supprimé de stock.json
- ✅ Page actualise correctement

---

## Test 6 : Refuser la suppression (Cancel)
**Objectif :** Vérifier que Cancel dans la pop-up ne supprime pas

**Préconditions :**
- Au moins 1 produit en stock

**Étapes :**
1. Cliquer sur le bouton 🗑️
2. Cliquer sur "Cancel" dans la pop-up

**Résultat attendu :**
- ✅ Pop-up se ferme
- ✅ Produit reste dans le tableau
- ✅ Aucune modification dans stock.json

---

## Test 7 : Vérifier la persistance (rechargement)
**Objectif :** Vérifier que les données sont bien sauvegardées

**Préconditions :**
- "Assiettes Mugen (REF-001) : 10 pièces" en stock

**Étapes :**
1. Augmenter la quantité à 15 avec le bouton ➕ (5 fois)
2. Fermer le navigateur complètement
3. Redémarrer l'app Flask
4. Rouvrir http://127.0.0.1:5000

**Résultat attendu :**
- ✅ Quantité toujours 15 (données persistées)
- ✅ stock.json contient bien 15

---

## Test 8 : Formulaire vide (validation)
**Objectif :** Vérifier que les champs requis sont validés

**Préconditions :**
- Page "Ajouter un produit" ouverte

**Étapes :**
1. Laisser un champ vide (ex: Désignation)
2. Cliquer sur "Ajouter"

**Résultat attendu :**
- ✅ Erreur HTML5 s'affiche (champ requis)
- ✅ Formulaire ne se soumet pas
- ✅ Aucun produit vide créé

---

## Test 9 : Référence dupliquée (erreur)
**Objectif :** Vérifier qu'on ne peut pas ajouter deux produits avec la même référence

**Préconditions :**
- "Assiettes Mugen (REF-001)" existe déjà

**Étapes :**
1. Aller sur "Ajouter un produit"
2. Entrer :
   - Désignation : "Verres"
   - Référence : "REF-001" (même que Assiettes)
   - Quantité : "5"
3. Cliquer sur "Ajouter"

**Résultat attendu :**
- ✅ Message d'erreur s'affiche : "Erreur : Référence REF-001 existe déjà !"
- ✅ Nouveau produit n'est pas créé

---

## Test 10 : CSS et responsive (visuel)
**Objectif :** Vérifier que le design est correct

**Préconditions :**
- Page affichée dans le navigateur

**Étapes :**
1. Observer le design de la page
2. Vérifier que le tableau est lisible
3. Vérifier que les boutons sont visibles et cliquables

**Résultat attendu :**
- ✅ Tableau bien formaté
- ✅ Boutons verts et visibles
- ✅ Texte lisible
- ✅ Pas d'erreur CSS dans console (F12)