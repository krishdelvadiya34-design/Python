dict=[
    {"id":101,"name":"krish","score":89},
    {"id":102,"name":"vedang","score":78},
    {"id":103,"name":"dhyey","score":69}
]

for i in dict:
        print(i["name"])





new_data={"id":104,"name":"bhavy","score":70}
dict.update(new_data)

print(dict)