import cv2
from FRAPI.network.classifierRN_model import train_classifierRN,test_classifierRN,infer_classifierRN



if __name__ == '__main__':

    # # for train
    # train_path = 'train'
    # test_path = 'train'
    # classifier_names =["0", "1"]                     
    
    # train_classifierRN(
    #     train_path,
    #     test_path,

    #     classifier_names,

    #     results_dir='results',

    #     batch_size=16, # 8
    #     epochs=200,
    #     num_workers=4,

    #     img_size=224,
    #     lr=1e-3,
    #     model_name='classifierRN',
    # )

    # # for test
    img_path = 'test'
    model_path = ''
    classifier_names = ["0", "1"]                
    results_output = test_classifierRN(
        img_path,
        model_path,
        classifier_names,
        img_size=224,
    )

    false_label=list()
    label = '0'
    nums_true_label=0
    for file_name, result,perc in results_output:
        print('file_name:', file_name)
        print('predicted:', result)
        print('perc:', perc)

        if result!=label:
            false_label.append(file_name)
        else:
            nums_true_label+=1
        # break
    
    print(f'acc: {nums_true_label/len(results_output)*100}%')
    print('false filename:',false_label)

    # print('----------------')

    # # for infer 
    # img=cv2.imread('gb_region.png')
    
    # infer_classifier = infer_classifierRN(model_path,classifier_names,img_size=224)
    # pred_label,perc = infer_classifier.infer(img)
    # print('pred_label,perc: ',pred_label,perc)







