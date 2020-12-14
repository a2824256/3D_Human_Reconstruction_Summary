# 单图人体三维重建资料汇总
## 文献调研
### 现状分析：
大多数现存的工作都在使用深度网络进行3D 数据采用体积网格或图像集合。
### 1. DeepHuman: 3D Human Reconstruction from a Single Image(ICCV 2019)
| [code](https://github.com/ZhengZerong/DeepHuman) | [paper](http://www.liuyebin.com/deephuman/assets/DeepHuman.pdf) |
**网络结构:**
![img.png](img/img.png)

模块说明：图像特征编码（橙色），立体到立体转换网络（蓝色&绿色），正向投影网络（黄色）<br>
训练输入：三维人体模型、RGB图片 <br>
预测输入：RGB图片 <br>
网络输出：3D网格模型<br>



### 2. PIFuHD: Multi-Level Pixel-Aligned Implicit Function for High-Resolution 3D Human Digitization(CVPR 2020)
- 说明 <br>
分两个版本PIFu(ICCV 2019)与PIFuhd(CVPR 2020) <br>
  | 左对齐标题 | 右对齐标题 | 居中对齐标题 |
| :------:| :------: | :------: |
| 短文本 | 中等文本 | 稍微长一点的文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |
  
- code <br>
https://github.com/facebookresearch/pifuhd <br> 
https://github.com/shunsukesaito/PIFu <br>
- paper <br>
PIFuhd：https://arxiv.org/pdf/2004.00452.pdf <br>
PIFu：https://arxiv.org/pdf/1905.05172.pdf <br>
- PIFu网络结构
![网络结构](img/img_1.png)

- 使用的数据集 <br>
[RenderPeople(Linux Only)](https://renderpeople.com/sample/free/rp_dennis_posed_004_OBJ.zip)

### 3. Convolutional Mesh Regression for Single-Image Human Shape Reconstruction
| [code](https://github.com/nkolot/GraphCMR/) | [paper](https://arxiv.org/abs/1905.03244) |
| :------:| :------: | :------: |



## 开源数据集
* DeepHuman使用:<br>
THUman:https://github.com/ZhengZerong/DeepHuman/tree/master/THUmanDataset
* PIFu使用：<br>
RenderPeople(分收费和免费模型): https://renderpeople.com/free-3d-people/ <br>
* 3.使用：<br>
Mosh: http://mosh.is.tue.mpg.de/

## 数据集制作方法


## 关键词解释
SMPL(Skinned Multi-Person Linear model)
