from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    
    print(request.session.get("name", False))
    # request.session["name"] = "test"
    # request.session.flush()

    # request.session.set_test_cookie()
    # if request.session.test_cookie_worked():
    #     request.session.delete_test_cookie()
    #     return HttpResponse("You're logged in.")
    # else:
    #     return HttpResponse("Please enable cookies and try again.")
    # TODO add session in react
    return render(request, "index.html")