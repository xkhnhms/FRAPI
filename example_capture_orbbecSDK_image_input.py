from FRAPI.cameras.capture_orbbecSDK_image_input import ImageCaptureSDKInput

if __name__ == '__main__':

    camera_ip = "169.254.4.153"
    root_dir = 'images'
    
    capture = ImageCaptureSDKInput(camera_ip, root_dir, use_idx=False)
    capture.run()