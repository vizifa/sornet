## Setup
- Install dependencies by `conda env create -f environment.yml`.
- Activate virtual environment by `conda activate sornet`.
- Download data ([clevr](https://drive.google.com/drive/folders/1Shgm4IjBYyupu7376uzcs9X7rArm10ui) and [leonardo](https://drive.google.com/drive/folders/1YsYkvSTM8rqkyPAmEnbmwu6J6_R4qq2V)) and copy or sym link to `data/`.
- Download [pre-trained models](https://drive.google.com/drive/folders/1kXPBnQI46VxQfAEqoaCeFLZfRn8HH3at) and copy or sym link to `models/`.


## Json File

Set the following values to true to implement the corresponding augumentations:
- rotation : Rotate patch by a random angle from 0-90,
- scaling : Scale patch by a random factor resulting in an image of size 32
- mirroring : randomly mirror the patch with a probability of 0.5
- reflection : randomly reflect the patch with a probability of 0.5
- hsv : randomly change the hue and saturation of the patch with a probability of 0.5

## To train the model:
```
python train_clevr.py --data data/clevr_cogent --log log/clevr
```