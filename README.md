This repository is the official implementation of [NeRT: Implicit Neural Representations for Unsupervised Turbulence Mitigation](https://weiyunjiang.com/NeRT/).

> **[CVPRW 2023] NeRT: Implicit Neural Representations for Unsupervised Turbulence Mitigation** <br>
> [Weiyun Jiang](https://weiyunjiang.github.io/), [Vivek Boominathan](https://vivekboominathan.com/), [Ashok Veeraraghavan](https://profiles.rice.edu/faculty/ashok-veeraraghavan)<br>
[![CVPRW](https://img.shields.io/badge/CVPRW-2023-1e6eb5?style=for-the-badge)](https://ieeexplore.ieee.org/document/10208382)
[![Arxiv](https://img.shields.io/badge/arXiv-2509.21309-b31b1b.svg?style=for-the-badge&logo=arxiv)](https://arxiv.org/abs/2308.00622)
[![Project Page](https://img.shields.io/badge/Project-Page-green?style=for-the-badge)](https://weiyunjiang.github.io/NeRT/)

## Set up environment

```
conda env create -f implicit_turbu.yml
conda activate implicit_turbu
```
## Dataset
* Put the desired dataset under ```data/Ablation_data/```
* Download the precomputed [p2s model](https://arxiv.org/abs/2107.11627) parameters from [Google Drive](https://drive.google.com/file/d/10W7Y6hcGHRAsPXUSDqDfuE5z-z50jr1g/view?usp=drive_link)
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
