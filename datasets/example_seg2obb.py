import time
from FRAPI.datasets import convert_to_obb,visualize_dataset_obb

if __name__=='__main__':

    image_dir = "/path/to/images"
    label_dir = "/path/to/labels"
    output_dir = "/path/to/train"

    # convert_to_obb_datasets(image_dir,label_dir,output_dir=None)


    image_dir = "/path/to/images"
    label_dir = "/path/to/labels"
    visualize_dataset_obb(image_dir, label_dir, output_dir=None, 
                         num_samples=None, save_images=False, 
                         show_plots=True, random_sample=False, 
                         seed=42, cols=3, figsize=(10, 8),
                         save_stats=True,wait_time=2)




