Quantum Computing Programming Tutorial
======================================

Setup
-----

 - Install [miniforge](https://github.com/conda-forge/miniforge) to set up an environment for the Python installation. Alternative: Anaconda or Miniconda.
 - Create new conda environment
    
    conda create -n qc-programming-tutorial python=3.10  

 - Activate the new environment

    conda activate qc-programming-tutorial

 - Clone this repository and enter the directory

    git clone https://github.com/FZJ-PGI-12/qc-programming-tutorial.git
    cd qc-programming-tutorial

 - Install the dependencies

    pip install -r requirements.txt

 - Start the notebook

    jupyter notebook

Display Presentation
--------------------

Install [rise extension for jupyter notebook](https://rise.readthedocs.io/en/stable/index.html)

    conda activate qc-programming-tutorial
    conda install -c conda-forge rise

