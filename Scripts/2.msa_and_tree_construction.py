import os
import subprocess
import argparse
import multiprocessing

def run_mafft(input_fasta, output_fasta, threads):
    """
    Runs MAFFT alignment on a given multifasta file  
    with a specified number of threads.

    Parameters:
        - input_fasta (str): Path to the input multifasta file.
        - output_fasta (str): Path where the aligned output will be saved.
        - threads (int): Number of threads to use (default is 3).
    """
    # MAFFT command with specified number of threads
    command = ["mafft", "--thread", str(threads), input_fasta]

    try:
        # Open the output file and run the MAFFT command
        with open(output_fasta, "w") as output_file:
            subprocess.run(command, stdout=output_file, check=True)
        print(f"MAFFT alignment completed successfully. Output saved to {output_fasta}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during MAFFT alignment: {e}")


def run_model_selection(aligned_fasta, threads):
    """
    Runs IQ-TREE model selection and returns the best-fit substitution model.
    
    Parameters:
        aligned_fasta (str): Path to the input MSA FASTA file.
        threads (int): Number of threads to use for IQ-TREE.
        
    Returns:
        str: Best-fit substitution model according to BIC. otherwise return None.
    """
    os.makedirs("model_selector", exist_ok=True)
    prefix = os.path.join(output_dir, "model_selection")

    # Construct the IQ-TREE command
    command = [
        "iqtree2",
        "-s", aligned_fasta,
        "-m", "TESTONLY",
        "-nt", str(threads),
        "-pre", prefix
    ]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print("Model selection completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during model selection:\n{e.stderr}")
        return None

    # Parse the best-fit model from the .log file
    log_file_path = f"{prefix}.log"
    try:
        with open(log_file_path, "r") as log_file:
            for line in log_file:
                if "Best-fit model:" in line:
                    return line.split(" ")[2].strip() #Extract the model name
    except FileNotFoundError:
        print("Log file not found. Please ensure IQ-TREE ran successfully.")

    return None



def create_phylogenetic_tree(alignment_file, outgroup_sequence, sample, threads):
    """
    Create a phylogenetic tree using IQ-TREE by specifying the first sequence in the alignment as the outgroup.

    Parameters:
        - alignment_file (str): Path to the input alignment file.
        - outgroup_sequence (str): Identifier of the outgroup sequence in the alignment.
        - sample (str): Depicts the Sample number to which the alignment file belongs.
        - threads (int): Number of threads to use for running the IQTREE.
    """
    # Define the IQ-TREE command with the outgroup specified
    iqtree_cmd = [
        "iqtree2",
        "-s", alignment_file,
        "-o", outgroup_sequence,  # the outgroup sequence
        "-m", best_fit_model,  # Substitution model
        "-nt", str(threads),  # Number of threads to use
        "-redo",  # Redo the analysis from scratch if it already exists
        "-fast",  # Use the fasttree algorithm for tree construction
        "-asr",  # Ancestral state reconstruction
        "-pre", f"Samples/{sample}/{sample}", # Location to save the generated files
        "-seed", "21" #Specifying a seed number for reproducibility
    ]

    # Execute the IQ-TREE command
    try:
        subprocess.run(iqtree_cmd, check=True)
        print("IQ-TREE analysis completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error running IQ-TREE:", e)



def construct_msa_and_phylogenetic_tree(folder_path, outgroup_sequence, sample_size, threads_to_be_used):
    """
    Construct the Multiple Sequence Alignment and the Phylogenetic tree for all the sampled genome sets

    Parameters:
        - folder_path (str): The path to the folder containing all the sampled genomesets sub-directories
        - outgroup_sequence (str): Identifier of the outgroup sequence.
        - sample_size (str): Number of Sampled genomes in each Genome set
        - threads_to_be_used (int): Number of threads to use for running the IQTREE.
    """
    
    
    # Iterate over all samples in the directory in ascending order
    for sample in  sorted(os.listdir(folder_path), key=lambda x: int(x.split("_")[1])):
        print(sample)
        # Designate the full path for each multifasta file corresponding to each sampled genomeset
        input_fasta = os.path.join(folder_path, sample, f"SARS-CoV-2_{sample}_{sample_size}+1.fasta")
        # construct MSA output file path
        msa_output_fasta = os.path.join(folder_path, sample, f"SARS-CoV-2_{sample}_{sample_size}+1_msa.fasta")
        # run mafft
        run_mafft(input_fasta, msa_output_fasta, threads=threads_to_be_used)
        # run model selection if it is the first sampled genome set
        if(sample == "Sample_1"):
            global best_fit_model 
            best_fit_model = run_model_selection(msa_output_fasta, threads=threads_to_be_used)
            print(f"Best-fit model from Sample_1: {best_fit_model}")
            
        # construct phylogenetic tree        
        create_phylogenetic_tree(msa_output_fasta, outgroup_sequence, sample, threads_to_be_used)


def main():
    cpu_count = multiprocessing.cpu_count()

    parser = argparse.ArgumentParser(description="Run MSA and Phylogenetic Tree construction.")
    parser.add_argument(
        "--threads",
        type=int,
        default=cpu_count,
        help=f"Number of CPU threads to use. Default: number of available cores ({cpu_count})"
    )
    args = parser.parse_args()

    construct_msa_and_phylogenetic_tree(
        folder_path="Samples/",
        outgroup_sequence="NC_045512.2",
        sample_size=5250,
        threads_to_be_used=args.threads
    )

if __name__ == "__main__":
    main()
