import open3d as o3d
import numpy as np
from FRAPI.point_cloud_utils.sample_points_tool import compute_and_visualize_normals

# --- 使用示例 ---
if __name__ == '__main__':
    ply_file_path = './local_mech_imgs/region_cloud_o3d2.ply'
    raw_pcd = o3d.io.read_point_cloud(ply_file_path)
    
    # 调用函数
    compute_and_visualize_normals(raw_pcd, voxel_size=0.0)