import time
from FRAPI.datasets import augment_dataset_hbb

if __name__=='__main__':

    # 示例运行
   
    image_dir = "/path/to/images"
    label_dir = "/path/to/labels"
    output_dir = "/path/to/train"
    
    t1 = time.time()
    augment_dataset_hbb(image_dir, label_dir, output_dir, num_augmentations=4, cp_origin=True, # 5 
                    rotation_angle_range=(-20, 20),scale_range=(0.8, 1.1),translation_range=(-15, 15),
                    jitter_range=(1, 2),noise_range=(5, 9),blur_range=(0, 2),
                    bright_range=(0.5, 1.2),satura_range=(0.5, 1.2)) 
    t2 = time.time()
    print('time cost: ',t2-t1)





