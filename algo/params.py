# dict of params
configs = {
        # 相机内参 []
        "CameraMatrix": [[2269.285674409311,0.0,1403.0955354112675],
                        [0.0,2269.9117832406714,901.2632669931866],
                        [0.0,0.0,1.0]],
        # 手眼标定外参变换矩阵
        "CalibMatrix": [[
            -0.9994108179217565,
            -0.03416965215472877,
            0.0032329386926765197,
            -51.02252260311724
        ],
        [
            0.0341849674856462,
            -0.999403963041904,
            0.004806938125445629,
            -67.94234255601359
        ],
        [
            0.003066760338056645,
            0.004914623867743125,
            0.9999832205858596,
            100.85604817712279
        ],
        [
            0.0,
            0.0,
            0.0,
            1.0
        ]],

        # 机械臂IP [可选参数，6D抓取姿态生成不需要]
        "robot_ip": "169.254.4.69",
        # 相机IP [可选参数，6D抓取姿态生成不需要]
        "mech_ip": "169.254.4.204", # {'WDM70252A510C004': '169.254.4.204', 'RUM3524BB500C004': '169.254.4.208'}


        # 起始拍照点时机械臂的位姿 [x,y,z,rx,ry,rz] unit: m, angle [可选参数，6D抓取姿态生成不需要]
        "homePose": [-0.154693, -0.438972, 0.743817, 179.034353, 0.164774, -179.987475],
        "homePoseJoint": [-48.289, -13.751, -49.452, -80.094, -11.001, 70.399, 34.521],

        # 放置点的机械臂位姿 [x,y,z,rx,ry,rz] unit: m, angle [可选参数，6D抓取姿态生成不需要]
        "placePose": [0.052413, -0.649648, 0.581572, -176.670808, 22.686928, 99.338504],
        "placePoseJoint": [-38.915, 15.619, -53.371, -89.41, 14.421, 121.524, 122.521],

        # 物体提起到的位置点 [x,y,z,rx,ry,rz] unit: m, angle [可选参数，6D抓取姿态生成不需要]
        "liftPose": [0.122588, 0.571193, 0.481236, 176.440032, -0.919864, -88.163794],
        "liftPoseJoint": [40.686, 6.331, 38.468, -104.416, -0.71, 107.71, 122.447],

        # 是否采用GPU
        "device": "cuda:3", # "cuda:1"

        # 2D像素坐标中有效工作区域范围[x,y],用于设定碰撞检测区域的点云 unit: pixel
        "top_left": [37, 45],
        "bottom_right": [2362, 1700],

        # 2D像素坐标中安全工作区域范围[x,y]，用于生成安全区域内的抓取姿态 unit: pixel
        "region_left": [600, 447],
        "region_right": [2070, 1360],

        # 抓取姿态的最大倾斜角度，高于该直被过滤掉
        "coneAngle": 30.0,
        "max_angle_deg": 40.0,
        "upper_ratio": 0.90,
        # 生成局部点云下采样的size
        "voxel_size": 0.001,
        # 碰撞检测的场景点云下采样的size
        "collision_voxel_size": 0.005, 

        # 碰撞检测的阈值，阈值越大生成的抓取姿态越多，但会导致更多的碰撞可能性
        "collision_thresh": 0.004,

        # 夹爪的长度 unit: mm [可选参数，6D抓取姿态生成不需要]
        "gripper_lens_list": [372,336.37,352.0, 235.0, 230.0, 225.0, 295.0],
        "gripper_lens": 310.0, # 相对深度； # 295.0, 固定深度
        # 安装在末端的夹爪与机械臂末端存在的旋转角度直，用于减少误差 [可选参数，6D抓取姿态生成不需要]
        "gripper_angle": 0,
        # 在抓取物体之前将机械臂末端沿着抓取方向后退的距离 unit: mm [可选参数，6D抓取姿态生成不需要]
        "gripper_forward_move": 60,

        # 相机深度的缩放因子
        "factor_depth": 1000.0,
        # 深度图预处理
        "use_depth_proce":False,
        "depth_radius": 3,

        # 检测阈值
        "detect_conf":0.25,
        # skip 检测个数
        "skip_detect_num":3,

        # checkpoint file path [需要修改为绝对路径]
        "obb_checkpoint": '/home/fs/fs/codes/grasp/yolo_grasp/crossbeam_6D_grasp/weights/yolov8s_obb_crossbeam.pt', # './weights/olov8s_obb_crossbeam.pt', 
        "seg_checkpoint": '/home/fs/fs/codes/grasp/yolo_grasp/crossbeam_6D_grasp/weights/yolov8s_seg_crossbeam.pt', # './weights/yolov8s_seg_crossbeam.pt', 
        "seg_checkpoint2": './weights/yolov8s_seg_crossbeam.pt', 

        # SAM model params [需要修改为绝对路径]
        "use_sam": False, 
        "sam_checkpoint": "weights/sam_vit_l_0b3195.pth", 
        "model_type": "vit_l", 

        # 将检测结果存放到指定的文件夹中 [需要修改为绝对路径]
        "root_dir": "./tmp_imgs",
        
        # mask file path [可选参数] [需要修改为绝对路径]
        "workspace_mask_path": "conf/workspace_mask.png",

        # collision params
        "approach_dist": 0.05,
        "collision_thresh": 0.002, # 0.0005 0.001
        "empty_thresh": 0.15, # 0.01  0.20
        "nms_t": 0.01,  # 0.03
        "nms_r": 30,  # 30
        "width_list": [0.012, 0.025, 0.032], # [0.015, 0.03, 0.038]  0.034 0.012 0.025
        "depth_list": [0.012, 0.015], # [0.01, 0.012, 0.015],  [0.008, 0.012]  [0.01, 0.015] 0.022  [0.012, 0.018]
        "point_sampler_nums": 350, # 200  150 300 350
        "gripper_height": 0.08, # 0.10

        "ratio_major": 0.85, # 0.75, # 0.65 0.75 0.60
        "ratio_minor": 0.70,  # 0.45, # 0.35 0.85 0.70

        # obb 可视化vis
        "IS_VIS_DEBUG":False, # for obb
        "verbose_obb_res": False,

        # 可视化
        "verbose_mask":False, 
        "verbose_alone_mask":False,
        "verbose_region_points":False,
        "verbose_normals":False,
    }
