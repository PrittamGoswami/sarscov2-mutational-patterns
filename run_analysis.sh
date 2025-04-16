#!/bin/bash

# GENOME SAMPLING
echo "===================="
echo "1. GENOME SAMPLING"
echo "===================="
# Run the script to sample the genome sets
jupyter nbconvert --to notebook --execute --inplace Scripts/1.genome_sampling.ipynb
echo " Generated Samples stored in the Samples directory."
echo " Genome Sampling Completed successfully!"


# Multiple sequence alignment and Tree Construction
echo "====================================================="
echo "2. MULTIPLE SEQUENCE ALIGNMENT AND TREE CONSTRUCTION"
echo "====================================================="
# Run the script to perform multiple sequence alignment and tree construction
stdbuf -oL python -u Scripts/2.msa_and_tree_construction.py #--threads n (if needed)
echo " Generated MSA and Tree files stored in the Sample sub-directories."
echo " Multiple sequence alignment and Tree Construction Completed successfully!"


# MUTATION DETECTION AND OVERALL MUTATION PROFILE ANALYSIS
echo "====================================================="
echo "3. MUTATION DETECTION AND OVERALL MUTATION PROFILE ANALYSIS"
echo "====================================================="
# Run the script to perform overall mutation profile analysis
jupyter nbconvert --to notebook --execute --inplace Scripts/3.mutation_detection_and_overall_mutation_profile_analysis.ipynb
echo " Detected mutations saved as pickle files in the Sample sub-directories."
echo " Generated Plots saved in the Results directory."
echo " Mutation Detection and Overall Mutation Profile Analysis Completed successfully!"


# TEMPORAL MUTATION PROFILE ANALYSIS
echo "====================================================="
echo "4. TEMPORAL MUTATION PROFILE ANALYSIS"
echo "====================================================="
# Run the script to perform temporal mutation profile analysis
jupyter nbconvert --to notebook --execute --inplace Scripts/4.temporal_mutation_profile_analysis.ipynb
echo " Generated Plots saved to Results directory."
echo " Temporal Mutation Profile Analysis Completed successfully!"


# Bulk Transcriptomics Analysis
echo "====================================================="
echo "5. BULK TRANSCRIPTOMICS ANALYSIS"
echo "====================================================="
# Run the script to perform bulk transcriptomics analysis
jupyter nbconvert --to notebook --execute --inplace Scripts/5.bulk_transcriptomic_analysis.ipynb
echo " Combined count matrix saved to Bulk-Transcriptomics directory."
echo " Generated Plots and tables saved to Results directory."
echo " Bulk Transcriptomics Analysis Completed successfully!"


# Single Cell Transcriptomics Analysis
echo "====================================================="
echo "6. SINGLE CELL TRANSCRIPTOMICS ANALYSIS"
echo "====================================================="
# Run the script to perform single cell transcriptomics analysis
jupyter nbconvert --to notebook --execute --inplace Scripts/6.single_cell_transcriptomic_analysis.ipynb
echo " Generated Plots and tables saved to Results directory."
echo " Single Cell Transcriptomics Analysis Completed successfully!"


# All analyses completed
echo "====================================================="
echo "All analyses completed successfully!"
echo "====================================================="
echo "Please check the Results directory and the .ipynb files for the results."
echo "====================================================="

