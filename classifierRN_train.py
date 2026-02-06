import cv2
from FRAPI.network.classifierRN_model import train_classifierRN,test_classifierRN,infer_classifierRN



if __name__ == '__main__':

    # # for train
    train_path = 'train'
    test_path = 'train'
    classifier_names =["0", "1"]                     
    
    train_classifierRN(
        train_path,
        test_path,

        classifier_names,

        results_dir='results',

        batch_size=16, # 8
        epochs=200,
        num_workers=4,

        img_size=224,
        lr=1e-3,
        model_name='classifierRN',
    )

    # for test
    img_path = 'val'
    model_path = 'best.pth'
    classifier_names = ["3_1", "3_2"]                
    results_output = test_classifierRN(
        img_path,
        model_path,
        classifier_names,
        img_size=224,
    )

    for file_name, result,perc in results_output:
        print('file_name:', file_name)
        print('predicted:', result)
        print('perc:', perc)
        break
        

    print('----------------')

    # for infer 
    img=cv2.imread('region.png')
    
    infer_classifier = infer_classifierRN(model_path,classifier_names,img_size=224)
    pred_label,perc = infer_classifier.infer(img)
    print('pred_label,perc: ',pred_label,perc)








