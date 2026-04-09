import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import os
from FRAPI.point_cloud_utils.vis_tool import visualize_image

# Usage example
if __name__ == "__main__":
    # Example 1: Read image from file path
    # img_path = './tmp_imgs/1772757924.023581_rgb.png'
    # img_path = './local_mech_imgs/1774253737.560197_rgb.png'
    # img_path = './local_mech_imgs/1774316330.953421_rgb.png' 

    from FRAPI.cameras.mechEyeCamera import mechCamera
    camera_mech = mechCamera()
    camera_mech.ConnectToCameraByDefault()
    img_path = camera_mech.capture_2d_image()

    try:
        result_img = visualize_image(img_path, title="Image read from path")
        
        
    except Exception as e:
        print(f"Error occurred while processing image: {e}")
