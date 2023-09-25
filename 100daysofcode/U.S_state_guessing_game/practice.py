# # with open("weather-data.csv") as weather_data:
# #     data=weather_data.readlines()
# #     print(data)
# # import csv
# # with open("weather-data.csv") as data_file:
# #     data=csv.reader(data_file)
# #     temperature=[]
# #     for row in data:
# #         if row[1]!="temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
# import pandas
# data=pandas.read_csv("weather-data.csv")
# # print(data["temp"])
# # data_dict=data.to_dict()
# # temp_list=data["temp"].tolist()
# # total=0
# # for temp in temp_list:
# #     total=total+temp
# # average_temp=total/len(temp_list)
# # print(average_temp)
# # average_temp=sum(temp_list)/len(temp_list)
# # print(average_temp)
# # print(data["temp"].max())
# # row=data[data.day=="Monday"]
# # print(row)

# # print(data[data.temp==data.temp.max()])
# monday=data[data.day=="Monday"]
# temp_c=monday.temp
# temp_f=temp_c*(9/5)+32
# print(temp_f)
