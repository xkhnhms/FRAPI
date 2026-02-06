from FRAPI.cameras.capture_orbbecSDK_image import ImageCaptureSDK



if __name__ == '__main__':

    camera_ip = "169.254.4.153"
    root_dir = 'Data250826'
    
    capture = ImageCaptureSDK(camera_ip, root_dir,start_idx=0)
    capture.run()

