#%%
import pandas
import numpy
#%%
def confusion_matrix_genarator(model, test_data:numpy.ndarray, test_label:numpy.ndarray, classes_name=None):
    '''
    케라스 전용 혼동행렬함수
    model: 케라스 모델
    test_data: 테스트 입력값
    test_label: 테스트 라벨
    classes_name:분류할 클래스 이름
    '''
    n_classes = test_label.shape[1]
    confusion_matrix = numpy.zeros((n_classes,n_classes),dtype=int)
    pred = model.predict(test_data)
    for idx in range(len(test_data)):
        pred_class = pred[idx].argmax()
        actual_class = test_label[idx].argmax()
        confusion_matrix[actual_class][pred_class]+=1
    
    confusion_matrix = pandas.DataFrame(confusion_matrix)
    if classes_name:
        classes_name_list = list(classes_name)
        col_name_list = ['(pred) '+str(string) for string in classes_name_list]
        index_name_list = ['(actual) '+str(string) for string in classes_name_list]
        confusion_matrix.columns = col_name_list
        confusion_matrix.index = index_name_list
    accuracy = (pred.argmax(-1)==test_label.argmax()).sum()/len(test_label)*100
    print(f'ACCURACY:{round(accuracy,2)} %')
    return confusion_matrix
