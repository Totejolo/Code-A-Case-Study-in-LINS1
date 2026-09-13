# LINS1 — variant discovery in an orphan gene

Code for the preprint *Discovery of Functional Genomic Variants in Orphan Genes Associated with Rare Diseases: A Case Study in LINS1* (https://doi.org/10.6084/m9.figshare.29651720).

LINS1 is an orphan gene associated with rare disease. This pipeline retrieves every known variant in the gene from Ensembl, annotates them with VEP, keeps the ones most likely to affect protein function, and plots the result.

## Pipeline

Run the scripts in this order.

**1. `ensembl_variants.py`** — queries the Ensembl REST API: resolves the LINS1 gene ID, looks up its genomic coordinates, and retrieves every variation overlapping that region. Writes `lins1_variants.csv` (id, start, end, strand, consequence_type).

**2. `comprobacion.py`** — inspects that table and extracts the dbSNP identifiers (ids starting with `rs`) into `lins1_rsids.txt`, the input list for VEP.

**3. VEP (external step)** — annotate `lins1_rsids.txt` with Ensembl VEP, through the web interface or the CLI, and download the annotated VCF.

**4. `leer_vcf_a_dataframe.py`** — reads the annotated VCF into a pandas DataFrame, skipping the `##` header lines. Quick sanity check on the file.

**5. `anotar_vcf_con_vep.py`** — parses the `CSQ` field: reads the field names from the `##INFO=<ID=CSQ` header, splits the multiple annotations per variant into one row each, and expands them into columns. Writes `lins1_vep_anotado.csv`.

**6. `filtrar_variantes.py`** — keeps variants with `IMPACT` HIGH or MODERATE whose `Consequence` includes missense_variant, stop_gained, splice_acceptor_variant, splice_donor_variant or frameshift_variant. Writes `lins1_variantes_filtradas.csv`.

**7. `filtrar_variantes_clave.py`** — stricter pass over the annotated table: same impact filter, a narrower consequence list (missense_variant, stop_gained, frameshift_variant) and allele frequency below 1% when an `AF` column is available. Writes `lins1_variantes_clave.csv`.

**8. `visualizar_variantes.py`** — plots variant counts by impact, the ten most frequent consequence types, and the allele-frequency distribution.

## Requirements

Python 3.9+

```
pip install pandas requests matplotlib seaborn
```

## Before running

The VCF filename is hard-coded at the top of `leer_vcf_a_dataframe.py` and `anotar_vcf_con_vep.py`. Change the `vcf_file` variable to your own VEP output before running those two scripts. The VCF itself is not included in this repository.

## Data

All variant data comes from public sources: the Ensembl REST API and Ensembl VEP. No patient data is used.
