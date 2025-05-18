# Brief-Glitch-Data
# 📊 Analyse des ventes avec Python et Plotly

Ce projet Python génère des graphiques interactifs (camemberts) à partir de données de ventes, en utilisant les bibliothèques `pandas` et `plotly.express`.

## 📁 Données utilisées

Les données sont chargées depuis une feuille Google Sheets au format CSV, contenant :

- `produit` : nom du produit
- `qte` : quantités vendues
- `prix` : prix unitaire
- `region` : région de vente

## 📈 Graphiques générés

1. **Camembert des ventes par produit (quantités)**
2. **Camembert du chiffre d'affaires par produit**
3. **Camembert du chiffre d'affaires par région**

Chaque graphique est sauvegardé au format `.html` pour être consulté dans un navigateur.

## 📦 Librairies utilisées

- [pandas](https://pandas.pydata.org/)
- [plotly](https://plotly.com/python/)

Installe-les avec :

```bash
pip install pandas plotly
