import time
# from FRAPI.datasets.seg_aug import augment_dataset_seg
from FRAPI.datasets import augment_dataset_seg, visualize_dataset_seg

if __name__=='__main__':

    # 示例运行
    image_dir = "/path/to/images"
    label_dir = "/path/to/labels"
    output_dir = "/path/to/train"

    t1 = time.time()
    augment_dataset_seg(image_dir, label_dir, output_dir, num_augmentations=4, cp_origin=True, # 5 
                    rotation_angle_range=(-20, 20),scale_range=(0.8, 1.1),translation_range=(-15, 15),
                    jitter_range=(1, 2),noise_range=(5, 9),blur_range=(0, 2),
                    bright_range=(0.5, 1.2),satura_range=(0.5, 1.2)) 
    t2 = time.time()
    print('time cost: ',t2-t1)


    visualize_dataset_seg(
        images_dir=image_dir,
        labels_dir=label_dir,
        output_dir=None,
        num_samples=None,
        save_images=False,
        show_plots=True,
        random_sample=False,
        wait_time=1,
    )




