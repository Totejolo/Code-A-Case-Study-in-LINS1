import pandas as pd
from io import StringIO

# Nombre del archivo VCF
vcf_file = "spWwcL2g3JV3V2xZ.vcf_"

# Leer el archivo ignorando los encabezados que empiezan con '##'
with open(vcf_file, 'r') as f:
    lines = [line for line in f if not line.startswith('##')]

# Convertir las líneas en un DataFrame
vcf_df = pd.read_csv(StringIO(''.join(lines)), sep='\t')

# Verificar las primeras filas
print(vcf_df.head())