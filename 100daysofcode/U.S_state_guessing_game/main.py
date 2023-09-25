import pandas
data=pandas.read_csv('squirrel_data.csv')
gray_squrrels=len(data[data["Primary Fur Color"]=="Gray"])
Cinnamon_squrrels=len(data[data["Primary Fur Color"]=="Cinnamon"])
Black_squrrels=len(data[data["Primary Fur Color"]=="Black"])

data_dict={
    "Fur color":["Gray","Cinnamon","Black"],
    "Count":[gray_squrrels,Cinnamon_squrrels,Black_squrrels]
}
df=pandas.DataFrame(data_dict)
df.to_csv("squrrels_count.csv")
