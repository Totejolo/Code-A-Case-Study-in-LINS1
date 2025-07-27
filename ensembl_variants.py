import requests
import pandas as pd

# Nombre del gen
gene_name = "LINS1"
species = "human"

# Paso 1: Obtener el ID del gen en Ensembl
def get_ensembl_gene_id(gene_name, species="human"):
    url = f"https://rest.ensembl.org/xrefs/symbol/{species}/{gene_name}?content-type=application/json"
    response = requests.get(url)
    data = response.json()
    for item in data:
        if item['type'] == 'gene':
            return item['id']
    return None

ensembl_id = get_ensembl_gene_id(gene_name)
print(f"ID de Ensembl para {gene_name}: {ensembl_id}")
# Paso 2: Obtener la ubicación del gen
def get_gene_location(ensembl_id):
    url = f"https://rest.ensembl.org/lookup/id/{ensembl_id}?content-type=application/json"
    response = requests.get(url)
    data = response.json()
    return data['seq_region_name'], data['start'], data['end']

chrom, start, end = get_gene_location(ensembl_id)
print(f"{gene_name} está en chr{chrom}:{start}-{end}")
# Paso 3: Buscar variantes en esa región
def get_variants_in_region(chrom, start, end):
    region = f"{chrom}:{start}-{end}"
    url = f"https://rest.ensembl.org/overlap/region/human/{region}?feature=variation;content-type=application/json"
    response = requests.get(url)
    return response.json()

variants = get_variants_in_region(chrom, start, end)
print(f"Número de variantes encontradas: {len(variants)}")
#Paso 4: Convertir en DataFrame
df = pd.DataFrame(variants)
df_simple = df[['id', 'start', 'end', 'strand', 'consequence_type']]

# Guardamos para revisar más adelante
df_simple.to_csv("lins1_variants.csv", index=False)
df_simple.head()
