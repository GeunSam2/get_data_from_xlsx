import random
import pandas as pd
import os

class_name = input("폴더이름을 입력하시오 : ")
path_dir = './'+class_name
file_list = os.listdir(path_dir)
file_list.sort()

data_set = {}

for file_name in file_list:
	print (file_name)
	tmp = []
	tmp.append(class_name)
	df_set1 = pd.read_excel(path_dir+"/"+file_name, skiprows=6, usecols="H,I", )
	birth = str(df_set1["Unnamed: 7"].loc[1])
	name = str(df_set1["Unnamed: 8"].loc[0])
	tmp.append(birth)
	data_set[name]=tmp

birth_data_f = open(class_name+" 생년월일 정보.txt", 'w')
for person in data_set:
	birth_data_f.write (person+"\t"+data_set[person][0]+"\t"+data_set[person][1]+"\n")
birth_data_f.close()



