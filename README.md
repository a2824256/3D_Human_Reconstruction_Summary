# 单图人体三维重建资料汇总
## 一、文献调研
### 1. DeepHuman: 3D Human Reconstruction from a Single Image(ICCV 2019)
| [code](https://github.com/ZhengZerong/DeepHuman) | [paper](https://arxiv.org/pdf/1903.06473.pdf) |
|  ----  | ---- |
#### 贡献
1. 建立了一个基于真实世界的3D真人身体模型数据库-THUman，其中包含7000个模型。
2. 设计了一个通过输入单张真人图片输出3D预测模型的SOTA方法。

#### 摘要
作者们提出了一种image-guided volume-to-volume translation进行单图真人三维重建的CNN算法。<br>
为了减少表面重建的模糊噪声，作者提出通过SMPL模型生成的密集语义作为输入。<br>
（即神经网络的输入为图片与无背景的二维人体语义图）<br>
这个网络的一个关键特征就是，通过空间特征变换，将不同尺寸的图像特征融合到3D空间中，有助于恢复平面几何的精确度。<br>
(图像搭配语义图，由于语义图具有一定的梯度性，能够将3D模型表面恢复得更光滑平整，指网络结构图中橙+蓝+绿部分)<br>
可视的平面细节通过一般精炼网络(Normal Refinement Network)进一步精炼, 可以与容积生成网络(Volume Generation Network)使用连接(concat)操作，使用我们提出的容积一般投影层(Volumetric Normal Projection Layer)。



#### 网络结构
![img.png](img/img.png)
**Tips** <br>
紫色箭头就是文章中描述的volume-to-normal部分



### 2. PIFu

| Version | Code | Paper | 
|  ----  | ----  | ---- | 
| PIFu(ICCV 2019) | [code](https://github.com/shunsukesaito/PIFu) | [PIFu: Pixel-Aligned Implicit Function for High-Resolution Clothed Human Digitization ](https://arxiv.org/pdf/1905.05172.pdf) | 
| PIFuhd(CVPR 2020) | [code](https://github.com/facebookresearch/pifuhd) | [Multi-Level Pixel-Aligned Implicit Function for High-Resolution 3D Human Digitization](https://arxiv.org/pdf/2004.00452.pdf) | 

- PIFu网络结构
![网络结构](img/img_1.png)

### 3. Convolutional Mesh Regression for Single-Image Human Shape Reconstruction
| [code](https://github.com/nkolot/GraphCMR/) | [paper](https://arxiv.org/abs/1905.03244) | 
|  ----  | ----  | 
- GraphCMR网络结构
![网络结构](img/img_2.png)

## 二、开源数据集

| Dataset | Method |
|  ----  | ----  |
| [THUman](https://github.com/ZhengZerong/DeepHuman/tree/master/THUmanDataset) | DeepHuman | 
| [RenderPeople](https://renderpeople.com/free-3d-people/) | PIFu | 
| [BUFF](http://buff.is.tue.mpg.de/) | PIFu | 
| [Human3.6M](http://vision.imar.ro/human3.6m/description.php) | GraphCMR | 
| [Mosh](http://mosh.is.tue.mpg.de/) | GraphCMR | 
| [UP-3D](http://files.is.tuebingen.mpg.de/classner/up/) | GraphCMR | 
| [DensePose COCO](https://github.com/facebookresearch/DensePose) |  |
| [3DPW](http://virtualhumans.mpi-inf.mpg.de/3DPW/) |  |



## 三、常用数据集模型制作方法
1. 制作3D人偶模型
2. 多角度图片合成

## 四、Comparison
- BodyNet在上述三种方法中均被提及到，可视为baseline进行比较;
- DeepHuman与GraphCMR在论文中均表示自己比HMR和BodyNet两种方法效果好,由于两篇论文评价指标不一样所以两个算法之间无法比较;
- DeepHuman评价指标 Averaged 3D IoU, 测试数据集为THuman;
- GraphCMR评价指标 MPJPE与Reconst. Error, 测试数据集为Human3.6M;
- PIFu在论文中表示在RenderPeople和Buff数据集上比BodyNet等多种方法效果好(不含DeepHuman与GraphCMR),比较指标与上面两种方法也不一样;
- 速度对比没有提及。

## 五、深度学习框架
| Method | DL Framework |
| ---- | ---- |
| DeepHuman | TensorFlow |
| PIFu | PyTorch |
| GraphCMR | PyTorch |

## 关键词
| Word | Detail |
| ---- | ---- |
| SMPL | Skinned Multi-Person Linear model, 一种参数化人体模型。 该方法中β和θ是其中的输入参数，其中β代表是个人体高矮胖瘦、头身比等比例的10个参数，θ是代表人体整体运动位姿和24个关节相对角度的75个参数。 |
| MPJPE | Mean Per Joint Postion Error 3D姿态估计常用评价指标，预测关键点和groundtruth之间的平均欧式距离 |
| Reconst. Error | 重建误差 |