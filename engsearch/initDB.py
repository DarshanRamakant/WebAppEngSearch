import os



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'engsearch.settings')
import django
django.setup()
from projects.models import SeatMetrixDb

clg_data = [{
        "name" : "University of Visvesvaraya College of Engineering Bangalore",
        "AI": 4202,
        "CE": 46143,
        "CS": 1969,
        "EC": 6666,
        "EE": 15937,
        "IE": 3103,
        "ME": 57138
    },
    {
        "name" : "S K S J T Institute of Engineering. Bangalore",
        "CE":79785,
        "CS":10946,
        "EC":23106,
        "ST":67508,
        "TX":100000000
    },
    {
        "name" : "B M S College of Engineering Basavanagudi,Bangalore",
        "CE":45354,
        "EC":1898,
        "EE":10376,
        "IM":43625,
        "ME":28283
    },
    {
        "name" : "Ambedkar Institute Of Technology Bangalore",
        "CE":89354,
        "CS":7278,
        "EC":17921,
        "EE":36725,
        "EI":53334,
        "ET":42943,
        "IM":68060,
        "ME":94026
    },
    {
        "name" : "R. V. College of Engineering Bangalore",
        "AI":336,
        "BT":491,
        "CE":206,
        "CH":972,
        "CS":158,
        "CY":368,
        "DS":287,
        "EC":776,
        "EE":209,
        "EI":434,
        "ET":279,
        "IE":268,
        "IM":222,
        "ME":732,
        "SE":215
    },
    {
        "name" : "M S Ramaiah Institute of Technology Bangalore",
        "AD":2233,
        "AI":2124,
        "BT":9284,
        "CA":1223,
        "CE":39775,
        "CH":23930,
        "CS":827,
        "CY":1840,
        "EC":3020,
        "EE":8465,
        "EI":11470,
        "ET":7449,
        "IE":1534,
        "IM":42492,
        "MD":18041,
        "ME":29510
    }    
]

def flatten_dict(original_dict) :
    new_dict = {}
    prefix = original_dict["name"] + " - "

    for key, value in original_dict.items():
        if key != "name":
            new_key = prefix + key
            new_dict[new_key] = value
    return new_dict

def flatten_keys(dictionary, parent_key='', sep='.'):
    flattened_dict = {}
    for key, value in dictionary.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_keys(value, new_key, sep=sep))
        else:
            flattened_dict[new_key] = value
    return flattened_dict


def create_one_dict(orig_dict) :
    appended_dict = {}

    for data in orig_dict:
        for key, value in data.items():
            if key in appended_dict:
                appended_dict[key].append(value)
            else:
                appended_dict[key] = value
    return appended_dict

flatten_clg_data = []
for index,clg in enumerate(clg_data) :
    flatten_clg_data.append(flatten_dict(clg))

the_dict = create_one_dict(flatten_clg_data)

#print(the_dict)

SeatMetrixDb.objects.all().delete()

"""
db = {}
for index, clg in enumerate(the_dict) :
    db[index] = SeatMetrixDb(info=clg)
    db[index].save()
"""

db = SeatMetrixDb(info=the_dict)
db.save()

fulldb = SeatMetrixDb.objects.all()

for a in fulldb :
    print(a.info)

