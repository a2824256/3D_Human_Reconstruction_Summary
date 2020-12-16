# 单图人体三维重建资料汇总
## 一、文献调研
### 1. DeepHuman: 3D Human Reconstruction from a Single Image(ICCV 2019)
| [code](https://github.com/ZhengZerong/DeepHuman) | [paper](https://arxiv.org/pdf/1903.06473.pdf) |
|  ----  | ---- |

#### 贡献
1. 建立了一个基于真实世界的3D真人模型数据库-THUman，其中包含7000个模型。
2. 设计了一个通过输入单张真人图片输出3D预测模型的SOTA方法。

#### 摘要
作者们提出了一种image-guided volume-to-volume translation进行单图真人三维重建的CNN算法。
为了减少表面重建的模糊噪声（包含不可见区域重建，指相机视角看不见的地方），作者提出通过SMPL模型生成的密集语义作为输入。（即神经网络的输入为图片、无背景的二维人体语义图和语义volume）。
这个网络的一个关键特征就是，通过空间特征变换，将不同尺寸的图像特征融合到3D空间中，有助于恢复平面几何的精确度。(图像搭配语义图，由于语义图具有一定的梯度性，能够将3D模型表面恢复得更光滑平整，指网络结构图中橙+蓝+绿部分)。
可视的平面(相机视角)细节通过一般细化网络(Normal Refinement Network,黄色部分)进一步细化,
使用我们提出的容积法向投影层(Volumetric Normal Projection Layer, 结尾最后交汇的箭头),与容积生成网络(Volume Generation Network, 指图中的蓝色和绿色的volume-to-volume translation network)使用连接(concat)操作，用于支持end-to-end的训练。
还有贡献了一个三维基于真实世界的3D真人模型数据集-THUman。由于作者网络架构的设计与数据集的多样性，只需要给出单张图片，就能优于现在大多数的单图人体三维重建方法。

#### 网络结构
![img.png](img/img.png)
**Tips** <br>
紫色箭头就是文章中描述的volume-to-normal部分，三维投影到二维，然后与input的原图和语义map一起进入normal refinement network进行处理。

#### 总结
将三维人体重建任务分解为三个子任务： <br>
a）从输入图像进行参数化人体估计 <br>
b）从图像和估计的身体进行表面重建 <br>
c）根据图像进行可见表面细节细化 <br>


### 2. PIFu
#### PIFu贡献
1. 目前唯一支持表面材料预测的深度学习方法

#### PIFu摘要
作者们介绍了Pixel-aligned Implicit Function (PIFu), 一种2D图片与其对应3D物体的全局信息进行局部像素对其的隐式表达方法。
PIFu是一种能够从单图或多图预测目标3D表面和材质的针对数字化高细节化穿着人体的end-to-end的深度学习方法。
高度复杂的形状，例如：头发、衣服，以及他们的变化和形变都可以统一数字化。对比现在已有的深度学习方法，PIFu可以产生大量的高分辨率的表面(包含如人的背部等看不到区域)。
尤其是不同于那种体积元素(内存密集型)表示的，它是内存高效的，能够掌控任意的拓扑，和结果表面是空间对齐输入的图片。
此外, 以前的算法是用来处理单个或者多个视觉的，PIFu可以自然地拓扑到多个视觉。PIFu在公共基准上达到了SOTA的性能，已经优于先前单一穿着人体图像数字化的工作。


| Version | Code | Paper | 
|  ----  | ----  | ---- | 
| PIFu(ICCV 2019) | [code](https://github.com/shunsukesaito/PIFu) | [PIFu: Pixel-Aligned Implicit Function for High-Resolution Clothed Human Digitization ](https://arxiv.org/pdf/1905.05172.pdf) | 
| PIFuhd(CVPR 2020) | [code](https://github.com/facebookresearch/pifuhd) | [Multi-Level Pixel-Aligned Implicit Function for High-Resolution 3D Human Digitization](https://arxiv.org/pdf/2004.00452.pdf) | 

#### PIFu-摘要


#### PIFuhd-摘要

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
2. 多角度关键点对应图片合成

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

## 测试汇总
### PIFu - [colab](https://colab.research.google.com/drive/1GFSsqP2BWz4gtq0e-nki00ZHSirXwFyY#scrollTo=5995t2PnQTmG)
- 工具

| [在线photoshop](https://www.tuyitu.com/photoshop/) | [在线去人像背景](https://www.remove.bg/zh/) | [自制无背景png转8位mask图python脚本](tools/png2mask.py) |
| ---- | ---- | ---- |

- 输入要求
1. 512x512输入尺寸，没有自带resize
2. 需要无背景或者黑色背景原图(32位) + 白色黑底mask图片(8位)

- 测试效果

| 体姿 | 原图 | 测试效果 | 结果 |
| ---- | ---- | ---- | ---- |
| 正面 | ![原图](img/PIFu/img2.png) | ![官方测试效果](img/PIFu/img.png)| 模型完整 |
| 平躺（脚下方视角带一点倾斜角度） | ![原图2](img/PIFu/img4.png) | ![失败1](img/PIFu/失败1mesh.png) | 头部缺失，是否数据集问题？待测试 |
| 平躺（侧面） | ![原图3](img/PIFu/img5.png) | ![失败2](img/PIFu/失败2mesh.png) | 侧面缺失，是否数据集问题？待测试 |

## 问题汇总
1. DeepHuman暂时无法测试,需要修改服务器gcc和g++版本低于8.0,服务器当前版本9.3.0

