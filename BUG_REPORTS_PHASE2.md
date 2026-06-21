# Bug Reports - Phase 2 (Flask Web Interface)

## Bug #1 : HTML Form Structure Issue
**Titre :** Boutons ➕/➖ ne soumettent pas le formulaire
**Sévérité :** Critical
**Statut :** Fixed ✅

**Préconditions :**
- App Flask running
- Produit en stock

**Étapes pour reproduire :**
1. Cliquer sur bouton ➕ ou ➖
2. Observer si le formulaire se soumet

**Résultat attendu :**
- Quantité augmente/diminue

**Résultat observé :**
- Rien ne se passe (formulaire n'était pas soumis)

**Cause :**
- Tags `</form>` mal placés (ferment avant le bouton)
- Les boutons étaient en DEHORS du formulaire

**Fix appliqué :**
- Restructuré le HTML : `<form>` → `<button>` → `</form>`

---

## Bug #2 : Menu Message Incorrect
**Titre :** Menu affiche "(1-6)" au lieu de "(1-7)"
**Sévérité :** Low
**Statut :** Fixed ✅

**Résultat observé :**
- Message disait "Choisis une option (1-6)" mais 7 options existaient

**Fix appliqué :**
- Changé le message en "(1-7)"

---

## Bug #3 : Negative Quantity Issue
**Titre :** Impossible de réduire quantité avec la route Flask
**Sévérité :** High
**Statut :** Fixed ✅

**Préconditions :**
- Produit avec quantité > 0

**Étapes :**
1. Cliquer bouton ➖

**Résultat observé :**
- Erreur 404 (route `/modifier` ne trouvait pas les nombres négatifs)

**Cause :**
- Le convertisseur Flask `<int:quantite>` n'acceptait pas les nombres négatifs

**Fix appliqué :**
- Créé deux routes séparées : `/ajouter_quantite/` et `/retirer_quantite/`