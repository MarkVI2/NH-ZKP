# NH-ZKP
Neural Hash based zero knowledge proof (NH-ZKP) is an authentication scheme that utilises neural network generated binary hashes in contrast with regular hashing schemes. The authentication scheme is proved to be faster than using the conventional hashing methods while used in a zero knowledge proof.

## Prerequisites 
Linux or OSX
NVIDIA GPU + CUDA (may CuDNN) and corresponding PyTorch framework (v2.1.0.dev)
Python v3.10.9

For ARM/Apple Silicon chips-
Use MPS else if a GPU is available define the gpu under the variable "mps_device" in the ``src/test.py`` and ``src/train.py``

## Datasets
I used NUS WIDE image dataset used in HashNet the link for their google drive can be found here [link](https://drive.google.com/drive/folders/0B7IzDz-4yH_HOXdoaDU4dk40RFE?usp=sharing). 
It is suggested to train the model on COCO and Imagenet dataset as well to get better results.

Before training the model you would have to move the downloaded images to [/data/nus_wide] and extract the images folder over there
```
mv nus_wide.tar.gz ./data/nus_wide
cd ./data/nus_wide
tar -zxvf nus_wide.tar.gz
```

You can also modify the list file(txt format) in ./data as you like. Each line in the list file follows the following format:
```
<image path><space><one hot label representation>
```

Refer to HashNet's github for more instructions.

## Training
First, you can manually download the PyTorch pre-trained model introduced in `torchvision' library or if you have connected to the Internet, you can automatically downloaded them.
Then, you can train the model for each dataset using the followling command.
```
cd src
python train.py --gpu_id 0 --dataset coco --prefix resnet50_hashnet --hash_bit 48 --net ResNet50 --lr 0.0003 --class_num 1.0
```
You can set the command parameters to switch between different experiments. 
- "gpu_id" is the GPU ID to run experiments.
- "hash_bit" parameter is the number of bits of the hash codes.
- "dataset" is the dataset selection. In our experiments, it can be "imagenet", "nus_wide" or "coco".
- "prefix" is the path to output model snapshot and log file in "snapshot" directory.
- "net" sets the base network. For details of setting, you can see network.py.
    - For AlexNet, "net" is AlexNet.    
    - For VGG Net, "net" is like VGG16. Detail names are in network.py.
    - For ResNet, "net" is like ResNet50. Detail names are in network.py.
- "lr" is the learning rate.
- "class_num" is the positive and negative pairs balance weight.

## Testing
You can evaluate the Mean Average Precision(mAP) result on each dataset using the followling command.
```
cd src
python test.py --gpu_id 0 --dataset nus_wide --prefix resnet50_hashnet --hash_bit 16 --snapshot iter_00900
```
You can set the command parameters to switch between different experiments. 
- "gpu_id" is the GPU ID to run experiments.
- "hash_bit" parameter is the number of bits of the hash codes.
- "dataset" is the dataset selection. In our experiments, it can be "imagenet", "nus_wide" or "coco".
- "prefix" is the path to output model snapshot and log file in "snapshot" directory.
- "snapshot" is the snapshot model name. "iter_09000" means the model snapshoted at iteration 9000.

## Authentication
Run the binary.py file
```
cd src
python binary.py
```
The function ``x_generator`` requires three inputs :-
- bitNum: In case of neural hash, the bitNum accepts 16, 32, 48 as the parameter. In all other cases this should be 0
- hashType: This is the type of hashing method you want to test. Valid inputs consist of "nh", "neuralhash", "md5", "sha256"
- imageNum: This is the index number from the image list in the defined path list(imageDataset).

