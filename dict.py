from json import dumps

dic = {}
values = [1,2,3,4,5]

# collect info about multiple entries that share the same attributes
for idx, value in enumerate(values, start = 1):
    dic[f"Entry{idx}"] = {
        "Id": "N/A",
        "Name": "N/A",
        "Created": "N/A"        
    }

print(dumps(dic,indent=4))  