from FRAPI.datasets.ch_datasets_labels import *

if __name__ == "__main__":

    # 示例1: 修改OBB标签
    obb_folder = r"/path/to/obb_labels"
    modify_yolo_obb_labels(obb_folder, target_class_id=0)
    
    # 示例2: 修改HBB标签
    hbb_folder = r"/path/to/hbb_labels"
    modify_yolo_hbb_labels(hbb_folder, target_class_id=0)
    
    # 示例3: 批量自动检测格式并修改
    labels_folder = r"/path/to/labels"
    modify_labels_batch(labels_folder, label_format='auto', target_class_id=0, dry_run=True)  # 先试运行
    # modify_labels_batch(labels_folder, label_format='auto', target_class_id=0, dry_run=False)  # 实际修改
    
    # 示例4: 指定格式修改
    modify_labels_batch(obb_folder, label_format='obb', target_class_id=1)
    modify_labels_batch(hbb_folder, label_format='hbb', target_class_id=1)