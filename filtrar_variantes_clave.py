import pandas as pd

# Cargar datos anotados y filtrados
df = pd.read_csv("lins1_vep_anotado.csv")

# Ejemplo de filtrado
# 1. Impacto alto o moderado
impact_filter = df['IMPACT'].isin(['HIGH', 'MODERATE'])

# 2. Tipo de variante interesante
variant_types = ['missense_variant', 'stop_gained', 'frameshift_variant']
variant_filter = df['Consequence'].isin(variant_types)

# 3. Frecuencia alélica baja (opcional, si tienes columna AF o similar)
if 'AF' in df.columns:
    freq_filter = df['AF'] < 0.01  # menos del 1%
else:
    freq_filter = True  # si no hay frecuencia, no filtrar por esto

# Combinar filtros
final_filter = impact_filter & variant_filter & freq_filter

variantes_clave = df[final_filter]

# Guardar resultado
variantes_clave.to_csv("lins1_variantes_clave.csv", index=False)
print(f"✅ Guardadas {len(variantes_clave)} variantes clave en lins1_variantes_clave.csv")
