import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

def MY_PlayPredictor(data_feature,data_target,test_f,test_t):
	#step2
	obj=LabelEncoder()
	WetherX=obj.fit_transform(data_feature["Wether"]) #fit_transform method takes input series and return updated encoded series
	#print("Encoded Wether is=",WetherX)
	TemperatureX=obj.fit_transform(data_feature["Temperature"])
	#print("Encoded Temperature is=",TemperatureX)
	LabelX=obj.fit_transform(data_target)
	#print("Encoded Play_Label is=",LabelX)

	features=list(zip(WetherX,TemperatureX))
	#print(features)
	
	#step3
	Kobj=KNeighborsClassifier(n_neighbors=3)
	Kobj.fit(features,LabelX)
	#step4
	output=Kobj.predict([[test_f,test_t]])
	return output

def main():
	print("--------IPL Play Prediction Application--------")
	try:
		print("Enter file name from we need to fetch data:-")
		file_name=input()
		#step1	
		dataset=pd.read_csv(file_name)
		data_feature=dataset.drop(columns=['Play','NO'])
		data_target=dataset['Play']
	except Exception as obj:
		print("Sorry,file does'nt exits",obj)
		return


	#print(data_feature)
	#print(data_target)
	print("Wether Dashboard\n#.Sunny\n#.Overcast\n#.Rainy")
	print("Temperature Dashborad\n#.Hot\n#.Cold\n#.Mild")
	Test_feature=input("Enter Todays Wether :")
	if Test_feature.lower()=="sunny":
		Test_feature=2
	elif Test_feature.lower()=="overcast":
		Test_feature=0
	elif Test_feature.lower()=="rainy":
		Test_feature=1
	else:
		print("Invalid input")

	Test_target=input("Enter Todays Temperature :")
	if Test_target.lower()=="hot":
		Test_target=1
	elif Test_target.lower()=="cold":
		Test_target=0
	elif Test_target.lower()=="mild":
		Test_target=2
	else:
		print("Invalid input")
	output=MY_PlayPredictor(data_feature,data_target,Test_feature,Test_target)
	
	if output==1:
		print("---You can play---")
	else:
		print("---Wether is Bad,You can't play---")

if __name__=="__main__":
	main()
	
#pandas concepts(panel data)

#one dimensional is series
#two dimensional is dataframe
#multiple dataframes collection is panel
