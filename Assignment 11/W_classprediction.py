import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def CheckAccuracy(target_test,output):
	#step5 calculate accuracy	
	Accuracy=accuracy_score(target_test,output)
	return (Accuracy*100)	

def My_KNN(data_train,target_train,data_test,K_value):
	#step3 train data
	obj=KNeighborsClassifier(n_neighbors=K_value)
	obj.fit(data_train,target_train)
	#step4 test data
	output=obj.predict(data_test)
	return output	

def main():
	print("----wine class prediction application----")
	print("--K Nearest Neighbors ML Model--")
	#step1 Get data
	dataset=pd.read_csv("WinePredictor.csv")
	#print(dataset)
	
	#step2 clean prepare split it train,test
	data_feature=dataset.drop(columns=["Class"])
	data_target=dataset['Class']
	#print(data_feature)
	#print(data_target)
	data_train,data_test,target_train,target_test=train_test_split(data_feature,data_target,test_size=0.7)
	for i in range(1,4):
		predicted_data=My_KNN(data_train,target_train,data_test,i)
		print(f"Accuracy of our K_nearest ML Model on K_value {i} is:",CheckAccuracy(target_test,predicted_data))
if __name__=="__main__":
	main()
