import pandas as pd

# Cargar el archivo anotado
result_df = pd.read_csv("lins1_vep_anotado.csv")

# Definir impactos y tipos de variante de interés
impactos_interes = ['MODERATE', 'HIGH']
tipos_interes = ['missense_variant', 'stop_gained', 'splice_acceptor_variant', 'splice_donor_variant', 'frameshift_variant']

# Filtrar por impacto
filtro_impacto = result_df['IMPACT'].isin(impactos_interes)

# Filtrar por tipo variante
filtro_tipo = result_df['Consequence'].apply(
    lambda x: any(t in x for t in tipos_interes) if isinstance(x, str) else False
)

# Aplicar filtros
variantes_filtradas = result_df[filtro_impacto & filtro_tipo].copy()

# Guardar resultado
variantes_filtradas.to_csv("lins1_variantes_filtradas.csv", index=False)

print(f"Variantes filtradas: {len(variantes_filtradas)}")
print("Archivo guardado como lins1_variantes_filtradas.csv")