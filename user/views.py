from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class UserAdd(TemplateView):
    template_name = "useradd.html"

    """
      if request.method == "POST":
            useraddform = UserAddForm(request.POST)
            if useraddform.is_valid():

                useradded = useraddform.save(commit=False)

                password = useraddform.cleaned_data["password"]
                useradded.set_password(useradded.password)
                useradded.save()
                """
                fname = useraddform.cleaned_data["name"]
                faddress = useraddform.cleaned_data["address"]
                femail = useraddform.cleaned_data["email"]
                fpassword = useraddform.cleaned_data["password"]
                useradd = User(
                    name=fname, address=faddress, email=femail, password=fpassword
                )
                useradd.save()
                """
            else:
                print("invalid form")
        else:
            useraddform = UserAddForm()
    else:
        return HttpResponseRedirect("../login/")

    return render(request, "useradd.html", {"form": useraddform})

"""

class UserView(TemplateView):
    template_name = "userread.html"
