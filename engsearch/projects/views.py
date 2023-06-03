from django.shortcuts import render

# Create your views here.
from .models import SeatMetrixDb

def projects(request):
    return render(request,'projects/projects.html')

def check_number_range(dictionary, number):
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    # Sort the values and keys together
    sorted_items = sorted(zip(values, keys))

    # Iterate through the sorted items
    for i in range(len(sorted_items) - 1):
        # Check if the number falls between two keys
        if sorted_items[i][0] <= number <= sorted_items[i + 1][0]:
            print(sorted_items[i + 1][1])
            return sorted_items[i + 1][1]

    return ""

def getClgInfo(rank) :
    db = SeatMetrixDb.objects.all()
    clg_dict ={}
    for clg_db in db :
        clg_dict = clg_db.info

    output = check_number_range(clg_dict,rank)
    if not output :
        return {}

    output_split = output.split('-')
    return {"name":output_split[0],"branch":output_split[1]}

def search(request):
    def getResults(query) :
        try:
            rank = int(query)
        except ValueError:
            return {}
        if rank :
            return getClgInfo(rank)
        else:
            return {}
    query = request.GET.get('q')
    if query:
        results = getResults(query)
    else:
        results = {}
    return render(request, 'search/search.html', {'results': results})
