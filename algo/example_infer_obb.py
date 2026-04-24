import cv2
import sys
import os
from FRAPI.algo.infer_obb import Solve_6D_Pose_OBB


if __name__=='__main__':


    local_rgb_path = './imgs/1776673886.6853254_rgb.png' 
    local_depth_path =  './imgs/1776673886.6853254_depth.png'

    # local_rgb_path = None
    # local_depth_path = None
   
        
    solve_pose = Solve_6D_Pose_OBB(
                local_rgb_path = None, 
                local_depth_path = None,
            )
    
    solve_pose.start_detect_main(local_rgb_path,local_depth_path,is_show=True)

    # while True:
    #     print("请输入指令： k[args]:继续 [k],  a:结束")
    #     cmd = input()
    #     if cmd == 'k':
            
    #         time1=time.time()
    #         solve_pose.start_detect_main(local_rgb_path,local_depth_path,is_show=True)
    #         time2=time.time()
    #         print(f'all process cost: {time2-time1}s')

    #     elif cmd=='a':
    #         solve_pose.close_hw()
    #         break

    # while True:
    #     solve_pose.move_home()
    #     time.sleep(0.5)
        
    #     time1=time.time()
    #     solve_pose.start_main()
    #     time2=time.time()
    #     print(f'all process cost: {time2-time1}s')
