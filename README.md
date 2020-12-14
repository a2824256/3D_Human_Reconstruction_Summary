# 单图人体三维重建资料汇总
## 文献调研
### 现状分析：
大多数现存的工作都在使用深度网络进行3D 数据采用体积网格或图像集合。
### 1. DeepHuman: 3D Human Reconstruction from a Single Image(ICCV 2019)
| [code](https://github.com/ZhengZerong/DeepHuman) | [paper](http://www.liuyebin.com/deephuman/assets/DeepHuman.pdf) | by TensorFlow |
|  ----  | ----  | ---- |

**网络结构:**
![img.png](img/img.png)

| Item | Content |
|  ----  | ----  |
| 模块说明 | 图像特征编码（橙色），立体到立体转换网络（蓝色&绿色），正向投影网络（黄色）|
| 训练输入 | 三维人体模型、RGB图片|
| 预测输入 | RGB图片 |
| 网络输出 | 3D网格模型 |



### 2. PIFu

| version | code | paper | framework |
|  ----  | ----  | ---- | ---- |
| PIFu(ICCV 2019) | [code](https://github.com/shunsukesaito/PIFu) | [PIFu: Pixel-AlignedImplicitFunctionfor High-Resolution Clothed Human Digitization ](https://arxiv.org/pdf/1905.05172.pdf) | PyTorch |
| PIFuhd(CVPR 2020) | [code](https://github.com/facebookresearch/pifuhd) | [Multi-Level Pixel-Aligned Implicit Function for High-Resolution 3D Human Digitization](https://arxiv.org/pdf/2004.00452.pdf) | PyTorch |

- PIFu网络结构
![网络结构](img/img_1.png)

### 3. Convolutional Mesh Regression for Single-Image Human Shape Reconstruction
| [code](https://github.com/nkolot/GraphCMR/) | [paper](https://arxiv.org/abs/1905.03244) | by PyTorch |
|  ----  | ----  | ---- |



## 开源数据集

| algorithm | dataset |
|  ----  | ----  |
| DeepHuman | [THUman](https://github.com/ZhengZerong/DeepHuman/tree/master/THUmanDataset) |
| PIFu | [RenderPeople](https://renderpeople.com/free-3d-people/)|
| GraphCMR | [Mosh](http://mosh.is.tue.mpg.de/) |


## 数据集制作方法


## 关键词
SMPL(Skinned Multi-Person Linear model)
