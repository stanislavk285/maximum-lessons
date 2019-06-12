person={
    "name":"Alex",
    "age":18,
    "gender": "male",
    }
print(person["age"])
cars=("bmw","renault","lada")
cars2=["kia", "mersedes"]
cars2.append("honda")
hours=17
if hours>5 and hours<=12:
    print("Утро")
elif hours>12 and hours<=18:
    print("День")
elif hours>18 and hours<=23:
    print("Вечер")
elif hours>23 or hours<5:
    print ("Ночь")
string= "арбуз, дыня, яблоко, апельсин, банан"
def fruits(fruits_str):
    list_fruits=string.split(", ")
    return list_fruits[0],list_fruits[-1]
fruit1, fruit2=fruits(string)
print(fruit2)

