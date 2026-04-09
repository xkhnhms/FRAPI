import os
import cv2
from FRAPI.point_cloud_utils.vis_tool import YOLOSegmentVisualizer


if __name__ == "__main__":
    # --- 配置区 ---
    # 请在这里修改你的类别名称
    # 例如：class_names = ['crossbeam', 'gear', 'bolt']
    exam_vis = YOLOSegmentVisualizer(class_names=['crossbeam']) 

    exam_vis.visualize_directory('/path/to/Datasets/')

    '''
    /path/to/Datasets/
        - images
        - labels
    '''
