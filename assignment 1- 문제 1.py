import csv


def read_iris(file_name): #iris 파일 읽어오는 함수
    with open(file_name,'r') as f1:
        next(f1) # 맨 앞줄에 이름이 있어서 float로 가져올 때 오류 발생하여 한 줄 건너 뜀
        data_list = [] # iris.csv안에 있는 정보들을 저장하는 리스트
        print("====================== iris data ======================")

        for item in f1:
    
            sepal_length, sepal_width, petal_length, petal_width, name = item.split(',')
            data = [float(sepal_length), float(sepal_width), float(petal_length),float(petal_width),name]
            data_list.append(data)
            
            print(data)
        print("=======================================================")

    return data_list

def iris_calculateAvg(data_list): #평균
    iris_avg = iris_mean(data_list) #iris 전체 평균 계산 함수 호출
    setosa_avg = setosa_mean(data_list) #setosa 평균 계산 함수 호출
    versicolor_avg = versicolor_mean(data_list) #versicolor 평균 계산 함수 호출
    virginica_avg = virginica_mean(data_list) #virginica 평균 계산 함수 호출

    return iris_avg, setosa_avg, versicolor_avg, virginica_avg
    
        
def iris_mean(data_list):
    iris_mean = []

    sum_sepal_length = 0
    sum_sepal_width = 0
    sum_petal_length = 0
    sum_petal_width = 0

    for i in range(150):
        sum_sepal_length += data_list[i][0]
        sum_sepal_width += data_list[i][1]
        sum_petal_length += data_list[i][2]
        sum_petal_width += data_list[i][3]


    mean_sepal_length = sum_sepal_length / 150
    mean_sepal_width = sum_sepal_width / 150
    mean_petal_length = sum_petal_length / 150
    mean_petal_width = sum_petal_width / 150

    iris_mean.append(mean_sepal_length)
    iris_mean.append(mean_sepal_width)
    iris_mean.append(mean_petal_length)
    iris_mean.append(mean_petal_width)
    print("====================== iris_mean ======================")
    print("mean_iris_sepal_length =" ,iris_mean[0])
    print("mean_iris_sepal_width =", iris_mean[1])
    print("mean_iris_petal_length =", iris_mean[2])
    print("mean_iris_petal_width =", iris_mean[3])
    print("=======================================================")
    
    return iris_mean

def setosa_mean(data_list):
    sepal_length_sum = 0
    sepal_width_sum = 0
    petal_length_sum = 0
    petal_width_sum = 0
    
    for i in range(150):

        if(data_list[i][4].strip().lower() == '"setosa"'):
        
            sepal_length_sum += data_list[i][0]
            sepal_width_sum += data_list[i][1]
            petal_length_sum += data_list[i][2]
            petal_width_sum += data_list[i][3]
    
    sepal_length_mean = sepal_length_sum/50
    sepal_width_mean = sepal_width_sum/50
    petal_length_mean = petal_length_sum/50
    petal_width_mean = petal_width_sum/50
    
    setosa_mean = []
    setosa_mean.append(sepal_length_mean)
    setosa_mean.append(sepal_width_mean)
    setosa_mean.append(petal_length_mean)
    setosa_mean.append(petal_width_mean)
    print("=====================setosa_mean=======================")
    print("setosa_sepal_length =",setosa_mean[0])
    print("setosa_sepal_width =",setosa_mean[1])
    print("setosa_petal_length =",setosa_mean[2])
    print("setosa_petal_width =", setosa_mean[3])
    print("=======================================================")
    return setosa_mean

def versicolor_mean(data_list):
    sepal_length_sum = 0
    sepal_width_sum = 0
    petal_length_sum = 0
    petal_width_sum = 0
    
    for i in range(150):

        if(data_list[i][4].strip().lower() == '"versicolor"'):
        
            sepal_length_sum += data_list[i][0]
            sepal_width_sum += data_list[i][1]
            petal_length_sum += data_list[i][2]
            petal_width_sum += data_list[i][3]
    
    sepal_length_mean = sepal_length_sum/50
    sepal_width_mean = sepal_width_sum/50
    petal_length_mean = petal_length_sum/50
    petal_width_mean = petal_width_sum/50
    
    versicolor_mean = []
    versicolor_mean.append(sepal_length_mean)
    versicolor_mean.append(sepal_width_mean)
    versicolor_mean.append(petal_length_mean)
    versicolor_mean.append(petal_width_mean)
    print("==================versicolor_mean======================")
    print("versicolor_sepal_length =",versicolor_mean[0])
    print("versicolor_sepal_width =",versicolor_mean[1])
    print("versicolor_petal_length =",versicolor_mean[2])
    print("versicolor_petal_width =", versicolor_mean[3])
    print("=======================================================")
    return versicolor_mean

def virginica_mean(data_list):
    sepal_length_sum = 0
    sepal_width_sum = 0
    petal_length_sum = 0
    petal_width_sum = 0
    
    for i in range(150):

        if(data_list[i][4].strip().lower() == '"virginica"'):
        
            sepal_length_sum += data_list[i][0]
            sepal_width_sum += data_list[i][1]
            petal_length_sum += data_list[i][2]
            petal_width_sum += data_list[i][3]
    
    sepal_length_mean = sepal_length_sum/50
    sepal_width_mean = sepal_width_sum/50
    petal_length_mean = petal_length_sum/50
    petal_width_mean = petal_width_sum/50
    
    virginica_mean = []
    virginica_mean.append(sepal_length_mean)
    virginica_mean.append(sepal_width_mean)
    virginica_mean.append(petal_length_mean)
    virginica_mean.append(petal_width_mean)
    print("===================virginica_mean======================")
    print("virginica_sepal_length =",virginica_mean[0])
    print("virginica_sepal_width =",virginica_mean[1])
    print("virginica_petal_length =",virginica_mean[2])
    print("virginica_petal_width =", virginica_mean[3])
    print("=======================================================")
    return virginica_mean

def result_csv(data_list, iris_avg, setosa_avg, versicolor_avg, virginica_avg):
    with open("result.csv",'w') as f2:
        f2.write("Iris_sepal_length,Iris_sepal_width,Iris_petal_length,Iris_petal_width\n")

        for data in data_list:
            f2.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}")
        f2.write("\n")
        f2.write("Iris_sepal_length_mean,Iris_sepal_width_mean,Iris_petal_length_mean,Iris_petal_width_mean\n")
        f2.write(f"{iris_avg[0]:.2f},{iris_avg[1]:.2f},{iris_avg[2]:.2f},{iris_avg[3]:.2f}\n")

        f2.write("Setosa_sepal_length_mean,Setosa_sepal_width_mean,Setosa_petal_length_mean,Setosa_petal_width_mean\n")
        f2.write(f"{setosa_avg[0]:.2f}, {setosa_avg[1]:.2f}, {setosa_avg[2]:.2f},{setosa_avg[3]:.2f}\n")

        f2.write("Versicolor_sepal_length_mean,Versicolor_sepal_width_mean,Versicolor_petal_length_mean,Versicolor_petal_width_mean\n")
        f2.write(f"{versicolor_avg[0]:.2f}, {versicolor_avg[1]:.2f}, {versicolor_avg[2]:.2f}, {versicolor_avg[3]:.2f}\n")

        f2.write("Virginica_sepal_length_mean,Virginica_sepal_width_mean,Virginica_petal_length_mean,Virginica_petal_width_mean\n")
        f2.write(f"{virginica_avg[0]:.2f}, {virginica_avg[1]:.2f}, {virginica_avg[2]:.2f}, {virginica_avg[3]:.2f}\n")
        

def main(file_name):
    
        data_list = read_iris(file_name)

        iris_avg, setosa_avg, versicolor_avg, virginica_avg = iris_calculateAvg(data_list)
        result_csv(data_list,iris_avg, setosa_avg, versicolor_avg, virginica_avg)

        
main('iris.csv')