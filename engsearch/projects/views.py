from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
from .models import SeatMetrixDb


def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
    
def loginPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        if is_valid_email(email):
            return redirect('search')
        else:
            print("Invalid email")
            messages.error(request, 'Invalid email entered.')
    return render(request, 'login_page.html')

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
    results = {}
    if query:
        results = getResults(query)

    error_msg = {}
    if not results:
        error_msg = "Invalid Input"
    return render(request, 'search/search.html', {'results': results,'error':error_msg,'query':query})
