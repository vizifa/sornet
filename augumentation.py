import numpy
import math
import json
from PIL import Image
from io import BytesIO
from torch.utils.data import Dataset
from torchvision import transforms
import h5py
import json
import numpy as np
import torch 

# define transform for dataset


class augumentations():
    
    def __init__(self, dict):
        self.dict= dict
        self.aug_list = []
        for c,report in enumerate(self.dict['report'].values()):
            # print(c,report)
            if report == "True":
                self.aug_list.append(list(self.dict['report'].keys())[c])
                
        self.local_dict  = {"rotation":self.rotation,"scaling":self.scaling,"mirroring":self.mirroring,"reflection":self.reflection,"hsv":self.hsv}
      
    # def get_transform(self):
    #     transforms_list = []
    #     transforms_list.append(globals()[item]() for item in self.aug_list)
    #     return transforms.Compose(transforms_list)

    def augment(self,patches):
        func_list = []
        for item in self.aug_list:
            func_list.append(self.local_dict[item])
        
        funct_dict = dict(zip(self.aug_list,func_list))
        #call the functions in the dict
        for key in funct_dict:
            patches = funct_dict[key](patches)
            
        return patches
    
    def rotation(self,patches):
        transform=transforms.RandomRotation((0,90))
        rot_image=transform(patches)
        return rot_image
        
    def scaling(self,patches):
        transform=transforms.RandomResizedCrop(32)
        scaled_image=transform(patches)
        return scaled_image
    
    def mirroring(self,patches):
        # random flip pytorch transforms
        transform = transforms.RandomHorizontalFlip(p=0.5)
        mirrored_image = transform(patches)
        return  mirrored_image
        
    def reflection(self,patches):
        # vertical flip
        transform = transforms.RandomVerticalFlip(p=0.5)
        reflected_image = transform(patches)
        return reflected_image

    def hsv(self, patches):
        # random hsv
        transform = transforms.ColorJitter(hue=.05, saturation=.05)
        hsv_image = transform(patches)
        return hsv_image
    
    