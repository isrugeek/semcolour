
# An intelligent way to Colour Nanoscale Microscopy Images Using Machine Learning
[Project](https://github.com/isrugeek/semcolour) | [Arxiv](https://arxiv.org/abs/) | 
[Dataset](https://github.com/isrugeek/semcolour/datasets)

Keras implementation for learning a mapping from SEM gray images to colorful images, for example:

<img src="results_nst/AI-06.jpg" width="500px"/>

An intelligent way to Colour Nanoscale Microscopy Images Using Machine Learning
 [Israel Goytom](http://isrugeek.github.io), [Qin Wang](.),[Xinfei Zhou],Cong Liu,[Dong Dong Lin](www.dongdonglin.cn)
 Nature communication, 2019.


**Note**: Please check out our [Keras](https://github.com/isrugeek/semcolour) implementation for End2End ColorNet(End2End.ipynb) and CNN-NST(CnnNST.ipynb). 

## Setup

### Prerequisites
- Linux or OSX
- NVIDIA GPU + CUDA CuDNN (CPU mode and CUDA without CuDNN may work with minimal modification, but untested)
- Keras with tensorflow backend

### Getting Started
- Install keras with tensorflow backend and dependencies from https://keras.io/#installation
- Install python packages `jupyter-notebook` and `scikit-image`
```bash
pip install scikit-image
pip install jupyter
```
- Install [livelossplot](https://github.com/stared/livelossplot)(optional) - a live monitor during training. 

- Clone this repo:
```bash
git clone https://github.com/isrugeek/semcolour
cd semcolour
```
# End2End Training Network
## Train
Setting the right gpu configure.
ex:
```bash
os.environ["CUDA_VISIBLE_DEVICES"]="0,1,2"
```
Variable `iteration` means epochs, change these settings for your own conditions.
```bash
# global varibles
trainset_path = "datasets/trainset"
devset_path = "datasets/devset"
testset_path = "datasets/testset"
batch_size = 16
# epochs
iteration = 100

target_size = (256, 256)
```
## Test
Run the last cell in the `End2End.ipynb` file to test the datasets which in `devset_path` and save these to `results` directory. 

## Note
`flow_from_directory_regress.py` is rewrite the class `ImageDataGenerator`, adding `register_batch_process` method to make
our preprocess process more convenient, make sure u have this py file in your work directory.

## Datasets
We collected 800 colorful sem-images as `SEMCOLORFUL1.0` in the `datasets` directory split into `devset` and `trainset`.

## Models
The pre-trained models `pretrained_end2end_model.h5` can be loaded by running follow line.
```bash
model.load_weights('pretrained_end2end_model.h5')
```
after load the pretrained weights, you can test the model directly instead of training.

## Citation
If you use this code for your research, please cite our paper An intelligent way to Colour Nanoscale Microscopy Images Using Machine Learning <a href="https://arxiv.org/pdf/1611.07004v1.pdf">
</a>:

```
@article{pix2pix2017,
  title={An intelligent way to Colour Nanoscale Microscopy Images Using Machine Learning},
  author={Israel Goytom1, Qin Wang†, Xinfei Zhou, Cong Liu, Dong Dong Lin*},
  journal={Nature Communication},
  year={2019}
}
```
