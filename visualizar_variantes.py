import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar variantes filtradas
df = pd.read_csv("lins1_variantes_filtradas.csv")

# Configuración estética seaborn
sns.set(style="whitegrid")

# 1. Conteo de variantes por IMPACT
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='IMPACT', order=df['IMPACT'].value_counts().index)
plt.title("Distribución de variantes por impacto")
plt.xlabel("Impacto")
plt.ylabel("Número de variantes")
plt.tight_layout()
plt.show()

# 2. Conteo de variantes por tipo de Consequence (los 10 más comunes)
top_conseq = df['Consequence'].value_counts().nlargest(10).index
plt.figure(figsize=(10,6))
sns.countplot(data=df[df['Consequence'].isin(top_conseq)], y='Consequence', order=top_conseq)
plt.title("Top 10 tipos de variantes Consequence")
plt.xlabel("Número de variantes")
plt.ylabel("Tipo de variante")
plt.tight_layout()
plt.show()

# 3. (Opcional) Histograma de frecuencia alélica si existe la columna, ejemplo 'AF' o similar
if 'AF' in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df['AF'].dropna(), bins=30, kde=True)
    plt.title("Distribución de frecuencia alélica (AF)")
    plt.xlabel("Frecuencia alélica")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.show()
else:
    print("No se encontró columna de frecuencia alélica para graficar.")
