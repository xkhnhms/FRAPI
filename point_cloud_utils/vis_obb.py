import os
import cv2
from FRAPI.point_cloud_utils.vis_tool import YOLOOBBVisualizer

if __name__ == "__main__":
    # main()

    exam_vis = YOLOOBBVisualizer(class_names='crossbeam')
    img_path = '/path/to/Datasets/images/rgb_20260112_163014_518.png'
    label_path = '/path/to/Datasets/labels/rgb_20260112_163014_518.txt'

    exam_vis.visualize_single(img_path,label_path)

    exam_vis.visualize_directory('/path/to/Datasets/', img_extensions=['.jpg', '.jpeg', '.png', '.bmp'])

    '''
    /path/to/Datasets/
        - images
        - labels
    '''