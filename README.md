# Multi-omics Insights into the Role of Host Innate Immunity in Shaping SARS-CoV-2 Mutational Patterns

This repository provides the necessary resources to reproduce the analysis presented in our study. 

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Data Download](#data-download)
- [Environment Setup](#environment-setup)
- [Running the Analysis](#running-the-analysis)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Overview
The project employs a multi-omics approach, leveraging publicly available genomics, bulk transcriptomics, and single-cell transcriptomics datasets to identify mutational patterns in SARS-CoV-2 and uncover their underlying causes.

## Prerequisites
- Anaconda

## Data Download
To reproduce the analysis, follow the data preparation steps below:

1. **Download SARS-CoV-2 Genome Sequences:**
   - Download complete genomes and metadata from [NCBI Virus](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=Severe%20acute%20respiratory%20syndrome%20coronavirus%202,%20taxid:2697049&QualNum_i=0&Completeness_s=complete&HostLineage_ss=Homo%20sapiens%20(human),%20taxid:9606)
   - Save them as:
     - `Sequence_Data/sequences.fasta`
     - `Sequence_Data/sequences.csv`

2. **Download and Extract Bulk Transcriptomics Data:**
   ```bash
   mkdir Bulk-Transcriptomics
   wget -O Bulk-Transcriptomics/GSE205099.tar "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE205099&format=file"
   mkdir Bulk-Transcriptomics/GSE205099_RAW
   tar -xvf Bulk-Transcriptomics/GSE205099.tar -C Bulk-Transcriptomics/GSE205099_RAW/
   gunzip Bulk-Transcriptomics/GSE205099_RAW/*.gz
   ```

3. **Download and Extract Single-Cell Transcriptomics Data:**
   ```bash
   mkdir Single-Cell-Transcriptomics
   wget -O Single-Cell-Transcriptomics/GSE171524_RAW.tar "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE171524&format=file"
   mkdir Single-Cell-Transcriptomics/GSE171524_RAW/
   tar -xvf Single-Cell-Transcriptomics/GSE171524_RAW.tar -C Single-Cell-Transcriptomics/GSE171524_RAW/
   gunzip Single-Cell-Transcriptomics/GSE171524_RAW/*.gz
   wget -O Single-Cell-Transcriptomics/GSE171524_lung_metaData.txt.gz "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE171nnn/GSE171524/suppl/GSE171524%5Flung%5FmetaData%2Etxt%2Egz"
   gunzip Single-Cell-Transcriptomics/GSE171524_lung_metaData.txt.gz
   ```

4. **Download the Oxidative Damage Response Gene Set:**
   ```bash
   wget -O WP_OXIDATIVE_DAMAGE_RESPONSE.gmt "https://www.gsea-msigdb.org/gsea/msigdb/human/download_geneset.jsp?geneSetName=WP_OXIDATIVE_DAMAGE_RESPONSE&fileType=gmt"
   ```

## Environment Setup
Create a Conda environment and install necessary packages:
```bash
conda create -n mutatioanalysis python=3.12 -y
conda activate mutatioanalysis
conda config --add channels conda-forge
conda config --add channels bioconda
conda install -y -c conda-forge -c bioconda pandas==2.2.3 numpy==1.26.4 matplotlib==3.10.1 seaborn==0.13.2 \
               scikit-learn biopython==1.85 pydeseq2==0.4.12 mygene==3.1.0 numba==0.60.0 \
               gseapy==1.1.5 adjustText==1.2.0 scanpy==1.10.4 dask=2025.2.0 jupyterlab==4.3.5 logomaker==0.8.6 ipykernel==6.29.5
pip install decoupler==1.8.0
conda install mafft=7.525
conda install iqtree=2.3.6
```

## Running the Analysis
Run the analysis using the provided Bash script:
```bash
bash run_analysis.bash
```

## License
This project is licensed under the MIT License.

## Citation
To be added
