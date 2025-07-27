import pandas as pd
from io import StringIO
import re

vcf_file = "spWwcL2g3JV3V2xZ.vcf_"

# Paso 1: Leer encabezado y extraer nombres reales del campo CSQ
csq_header = ""
with open(vcf_file, 'r') as f:
    for line in f:
        if line.startswith("##INFO=<ID=CSQ"):
            csq_header = line
            break

match = re.search(r'Format: (.+?)">', csq_header)
if match:
    csq_cols = match.group(1).split('|')
    print(f"✔ Nombres de columnas CSQ detectadas: {len(csq_cols)} campos.")
else:
    raise ValueError("No se encontraron los nombres del campo CSQ en el encabezado del VCF.")

# Paso 2: Leer el archivo VCF ignorando las líneas que comienzan con ##
with open(vcf_file, 'r') as f:
    lines = [line for line in f if not line.startswith('##')]

vcf_df = pd.read_csv(StringIO(''.join(lines)), sep='\t')

# Paso 3: Extraer campo CSQ del campo INFO
def get_csq(info):
    for field in info.split(';'):
        if field.startswith('CSQ='):
            return field.replace('CSQ=', '')
    return None

vcf_df['CSQ'] = vcf_df['INFO'].apply(get_csq)

# Paso 4: Separar múltiples anotaciones por coma y expandir filas (con índice limpio)
vcf_df['CSQ_split'] = vcf_df['CSQ'].str.split(',')
exploded_df = vcf_df.reset_index(drop=True).explode('CSQ_split').reset_index(drop=True)

# Paso 5: Dividir anotaciones en columnas separadas
csq_split_df = exploded_df['CSQ_split'].str.split('|', expand=True)
csq_split_df.columns = csq_cols

# Paso 6: Combinar con columnas originales
result_df = pd.concat([exploded_df, csq_split_df], axis=1)

# Paso 7: Guardar resultados
result_df.to_csv("lins1_vep_anotado.csv", index=False)
print("✅ Archivo anotado guardado como lins1_vep_anotado.csv")