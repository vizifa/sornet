# import json
# json_file = "/home/ivlabs-0/sornet/augmentations.json"
# with open(json_file) as jsonfile:
#     print(jsonfile)
#     parent_dict = json.load(jsonfile)
#     aug_list = []
#     for c,report in enumerate(dict['report'].values()):
#     # print(c,report)
#         if report == "True":
#         aug_list.append(list(dict['report'].keys())[c])
def rotation(vaiab):
    print(vaiab)
def scaling(vaiab):
    print(vaiab)
def mirroring(vaiab):
    print(vaiab)

karthick=["rotation","scaling","mirroring"]
prices = []
for item in karthick:
    prices.append(globals()[item])
funct_dict = dict(zip(karthick,prices))
res = funct_dict["rotation"](1239123)
