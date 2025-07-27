import pandas as pd

# Cargar el archivo .csv
df = pd.read_csv("lins1_variants.csv")

# Ver dimensiones
print("Dimensiones:", df.shape)

# Ver primeras filas
print(df.head())

# Ver columnas disponibles
print("Columnas:", df.columns.tolist())
# Filtrar solo variantes con id que empiecen por 'rs' y sin valores nulos
rs_variants = df[df['id'].str.startswith('rs', na=False)]

# Guardar solo los ids en un txt, sin índice ni encabezado
rs_variants['id'].to_csv("lins1_rsids.txt", index=False, header=False)

print(f"Archivo 'lins1_rsids.txt' creado con {len(rs_variants)} rsIDs para VEP.")
