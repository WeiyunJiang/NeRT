# NeRT: Implicit Neural Representations for General Unsupervised Turbulence Mitigation
Weiyun Jiang, Vivek Boominathan, Ashok Veeraraghavan
## Set up environment

```
conda env create -f implicit_turbu.yml
conda activate implicit_turbu
```
## Dataset
* Put the desired dataset under ```data/Ablation_data/```
* Download the precomputed p2s model parameters from here: https://drive.google.com/drive/folders/1LHc5g7qPDuqmdbAwTdW0HtEYsHhj04jA?usp=sharing
* Unzip ```p2s_data.zip``` under ```data/p2s_data```
## High-Level structure
The code is organized as follows:
* ```networks/``` contains some basic neural network building blocks.
* ```utils/``` contains utility functions, most promintently related to reading images.
* ```NeRT.ipynb``` contains demo codes. 

## Reproducing experiments
Run the NeRT.ipynb using jupyter notebook
