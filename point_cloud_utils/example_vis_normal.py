import open3d as o3d
import numpy as np
from FRAPI.point_cloud_utils.time_log import TimeLogger
from FRAPI.point_cloud_utils.sample_points_tool import compute_and_visualize_normals

def load_ply(ply_file_path, return_np=False):
    pcd = o3d.io.read_point_cloud(ply_file_path, remove_nan_points=False)
    return pcd
    

def vis_points_o3d(pcd):

    # 2将点云坐标转换为NumPy数组
    points = np.asarray(pcd.points)

    # 过滤掉包含NaN的行
    # np.isnan(points).any(axis=1) 会为每个点创建一个布尔值，True表示该点坐标中有NaN
    valid_points = points[~np.isnan(points).any(axis=1)]

    # 创建新的点云对象，并赋值为过滤后的点
    filtered_pcd = o3d.geometry.PointCloud()
    filtered_pcd.points = o3d.utility.Vector3dVector(valid_points)

    # 如果原有点云有颜色信息，也需要按相同索引进行过滤
    if pcd.has_colors():
        colors = np.asarray(pcd.colors)
        valid_colors = colors[~np.isnan(points).any(axis=1)]
        filtered_pcd.colors = o3d.utility.Vector3dVector(valid_colors)

    # 可视化过滤后的点云
    o3d.visualization.draw_geometries([filtered_pcd], window_name="Filtered Point Cloud", width=800, height=600)



if __name__=='__main__':

    timer = TimeLogger()
    

    ply_file_path = '../local_mech_imgs/region_cloud_0.ply'
    pcd = load_ply(ply_file_path)
    # vis_points_o3d(pcd)

    timer.start("extract mask points")
    compute_and_visualize_normals(pcd, voxel_size=0.0, radius=0.02, max_nn=30, is_vis=True)
    timer.end("extract mask points")

    timer.summary()
    








