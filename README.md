# Unsupervised Non-Rigid Image Distortion Removal via Grid Deformation

Paper[https://openaccess.thecvf.com/content/ICCV2021/papers/Li_Unsupervised_Non-Rigid_Image_Distortion_Removal_via_Grid_Deformation_ICCV_2021_paper.pdf]

Many computer vision problems face difficulties when imaging through turbulent refractive media (e.g., air and water) due to the refraction and scattering of light. These effects cause geometric distortion that requires either handcrafted physical priors or supervised learning methods to remove. In this paper, we present a novel unsupervised network to recover the latent distortion-free image. The key idea is to model non-rigid distortions as deformable grids. Our network consists of a grid deformer that estimates the distortion field and an image generator that outputs the distortion-free image. By leveraging the positional encoding operator, we can simplify the network structure while maintaining fine spatial details in the recovered images. Our method doesn't need to be trained on labeled data and has good transferability across various turbulent image datasets with different types of distortions. Extensive experiments on both simulated and real-captured turbulent images demonstrate that our method can remove both air and water distortions without much customization. 

<!-- ![teaser](https://user-images.githubusercontent.com/22784070/129606461-13390c92-9e59-4f0f-8fad-e2111e7ada24.png){:height="20%" width="20%"} -->
<img src="https://user-images.githubusercontent.com/22784070/129606461-13390c92-9e59-4f0f-8fad-e2111e7ada24.png" width="70%" height="70%">



# Problem
![problems](https://user-images.githubusercontent.com/22784070/137428002-cb429c90-c8fa-462f-8837-55db60e187fd.gif)
