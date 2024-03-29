# 最精简代码学习GAN的生成图像示例
<img src = "809325722_cover.jpg" width= "80%">

## **前言**
- 数据集已上传百度网盘，如有需要请自取~[百度网盘链接](https://pan.baidu.com/s/15yfpZ9_q4cYBkdv1ua6omg?pwd=0203)
提取码：0203


- [B站讲解链接](https://www.bilibili.com/video/BV1934y1r7jc)

- **该教程较为基础，适合NN，CV等初学者。** 

## **配环境**

打开cmd， git clone该demo的地址
```
git clone git@github.com:752413464/GAN.git
cd GAN
```
首先起一个虚拟环境，需要配置torch，torchvision等库（**以下命令需要先安装好Anaconda**）
```
conda create -n GAN_demo python=3.7
conda activate GAN_demo
conda install pytorch=1.7.0 torchvision=0.8.1 cudatoolkit=11.0 -c pytorch
```
配置好torch等框架，安装一些常用的cv视觉库。
```
pip install matplotlib scikit-image opencv-python tqdm 
```
或者可以直接安装requirements.txt
```
pip install -r requirements.txt
``` 
## **开始训练**

将下载的数据集放在Gan_.py同级目录下
```
python GAN_.py
```
## **推理**
将保存的weights加载进来推理
```
python inference.py
```

