from FRAPI.cameras.capture_mecheye_image_input import Capture2DStreamInput

if __name__ == '__main__':
    streamer = Capture2DStreamInput(save_directory = "./images",use_idx=False)
    streamer.main()
