# NeRT: Implicit Neural Representations for General Unsupervised Turbulence Mitigation
[Weiyun Jiang](https://weiyunjiang.github.io/), [Yuhao Liu](https://www.yuhaoliu.net/), [Vivek Boominathan](https://vivekboominathan.com/), [Ashok Veeraraghavan](https://profiles.rice.edu/faculty/ashok-veeraraghavan)

[Project Page](https://weiyunjiang.github.io/NeRT/)
## Set up environment

```
conda env create -f implicit_turbu.yml
conda activate implicit_turbu
```
## Dataset
* Put the desired dataset under ```data/Ablation_data/```
* Download the precomputed [p2s model](https://arxiv.org/abs/2107.11627) parameters from here: https://drive.google.com/drive/folders/1LHc5g7qPDuqmdbAwTdW0HtEYsHhj04jA?usp=sharing
* Unzip ```p2s_data.zip``` under ```data/p2s_data```
## High-Level structure
The code is organized as follows:
* ```networks/``` contains some basic neural network building blocks.
* ```utils/``` contains utility functions, most promintently related to reading images.
* ```NeRT.ipynb``` contains demo codes. 

## Reproducing experiments
Run the NeRT.ipynb using jupyter notebook

## Citation
```
@article{jiang2023nert_general,
    title={Nert: Implicit neural representations for general unsupervised 
           turbulence mitigation},
    author={Jiang, Weiyun and Liu, Yuhao and Boominathan, Vivek and 
            Veeraraghavan, Ashok},
    journal={arXiv preprint arXiv:2308.00622},
    year={2023}
}
```
```
@inproceedings{jiang2023nert,
    title={Nert: Implicit neural representations for unsupervised atmospheric 
           turbulence mitigation},
    author={Jiang, Weiyun and Boominathan, Vivek and Veeraraghavan, Ashok},
    booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and 
               Pattern Recognition Workshops},
    pages={4235--4242},
    year={2023}
}
```
