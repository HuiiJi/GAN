# 最精简代码学习GAN的生成图像示例

**前言**：
<hp />
- 数据集已上传百度网盘，如有需要请自取~
链接：[https://pan.baidu.com/s/1E6pjmurMYruPzKSdR-pORQ] 
提取码：0203

- [B站讲解链接](https://www.bilibili.com/video/BV1934y1r7jc)
<hp />

> **该教程较为基础，适合NN，CV等初学者。** 

**配环境**：

IAT is built in PyTorch 1.7.0 and tested on Ubuntu 16.04 environment (Python3.7, CUDA11.0).

For installing, follow these intructions
```
conda create -n IAT python=3.7
conda activate IAT
conda install pytorch=1.7.0 torchvision=0.8.1 cudatoolkit=11.0 -c pytorch
```
```
pip install matplotlib scikit-image opencv-python yacs joblib natsort h5py tqdm opencv-python timm warmup-lr torchsummary
```
or you can install these necessary toolkits by 
```
pip install -r requirements.txt
``` 
