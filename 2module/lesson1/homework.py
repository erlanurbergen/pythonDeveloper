import json

with open("sample-data.json", "r") as simpleFile:
    data = json.load(simpleFile)

print("Interface status ")
print("=========================================================")
print("DN                                   Description              Speed         MTU")
for i in data["imdata"]:
    data1 = i["l1PhysIf"]["attributes"]["dn"]
    data2 = i["l1PhysIf"]["attributes"]["descr"]
    data3 = i["l1PhysIf"]["attributes"]["speed"]
    data4 = i["l1PhysIf"]["attributes"]["mtu"]
    print("{}{}                   {},       {}".format(data1, data2, data3, data4))