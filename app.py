import plotly.express as px
import pandas as pd

# 1. Charger les données
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# 2. Camembert : Ventes par produit (en quantités)
figure_qte = px.pie(données, values='qte', names='produit',Ventes par produ title='it (quantités)')
figure_qte.write_html('ventes-par-produits.html')
print('✅ ventes-par-produits.html généré avec succès !')

# 3. Calcul du chiffre d'affaires (qte * prix)
données['ca'] = données['qte'] * données['prix']

# 4. Chiffre d'affaires total par produit
ca_par_produit = données.groupby('produit')['ca'].sum().reset_index()

# 5. Camembert : Chiffre d'affaires par produit
figure_ca = px.pie(ca_par_produit, values='ca', names='produit', title="Chiffre d'affaires par produit")
figure_ca.write_html('ca-par-produits.html')
print("✅ ca-par-produits.html généré avec succès !")

# 6. Chiffre d'affaire par regions
ca_par_region = données.groupby('region')['ca'].sum().reset_index()

# 7. Camenbert chiffre d'affaire par region
figure_re = px.pie(ca_par_region, values='ca', names='region', title="Chiffre d'affaire par regions")
figure_re.write_html ('ca-par-region.html')
print("✅ ca-par-region.html généré avec succès !")
