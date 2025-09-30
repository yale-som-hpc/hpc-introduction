#!/bin/bash
#SBATCH --job-name=fibonacci
#SBATCH --output=fibonacci_%j.log
#SBATCH --error=fibonacci_%j.err
#SBATCH --time=00:10:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G

# Print job information
echo "Job started at: $(date)"
echo "Running on node: $(hostname)"
echo "Job ID: $SLURM_JOB_ID"
echo "=========================================="

# Load Python from Spack
spack load python

# Run the Python script
# You can change the argument to compute more Fibonacci numbers
python fibonacci.py 30

echo "=========================================="
echo "Job finished at: $(date)"