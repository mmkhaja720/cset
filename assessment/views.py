from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from .models.user import User
from django.views import View
from .models.assessment import Assessment
from .models.demography import Demography
# Create your views here.


def index(request):
    if request.session.get('user_email'):
        user = User.get_user_by_email(request.session.get('user_email'))
        print(user.fullname)
        return render(request, 'index.html', {'user': user})
    else:
        return redirect('/login')


def profile(request):
    if request.session.get('user_email'):
        user = User.get_user_by_email(request.session.get('user_email'))
        return render(request, 'profile.html', {'user': user})
    else:
        return redirect('/login')


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        fullName = postData.get('full_name')
        email = postData.get('email')
        user_name = postData.get('user_name')
        password = postData.get('user_password')

        user = User(
            fullname=fullName,
            useremail=email,
            username=user_name,
            userPassword=password,
        )
        isExists = user.isExist()
        if isExists:
            error_message = "Email already exists"
            return render(request, 'signup.html', {'error_message': error_message})
        else:

            user.userPassword = make_password(user.userPassword)
            user.register()
            return redirect('home')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.get_user_by_email(email)
        print(user)
        error_message = None
        if user:
            print(user.useremail)
            flag = check_password(password, user.userPassword)
            if flag:
                request.session['user_id'] = user.id
                request.session['user_email'] = user.useremail
                return redirect('home')
            else:
                error_message = "Email or Password invalid !!!"
        else:
            error_message = "Email or Password invalid !!!"
            return redirect('/login')
        return render(request, 'login.html', {'error_message': error_message})
class Newassessment(View):
    def get(self,request):
        return render(request,'newassessment.html')
    def post(self,request):
        postData=request.POST
        assessment=Assessment(assessmentname=postData.get('assessment_name'),assessmentdate=postData.get('assessment_date'),facilityname=postData.get('facility_name'),cityname=postData.get('city_name'),statename=postData.get('state_name'),assessment_options=postData.get('assessment_option'))
        assessment.register()
        return redirect('/demographics')
class Demographics(View):
    def get(self,request):
        return render(request,'demography.html')
    def post(self,request):
        postData=request.POST
        demography=Demography(
            sector=postData.get('sector'),
            industry=postData.get('industry'),
            asset_gross_value=postData.get('grossvalueofasset'),
            expected_effort=postData.get('expected_effort'),
            organization_name=postData.get('organisation_name'),
            business_unit=postData.get('business_unit'),
            organization_type=postData.get('organization_type'),
            facilitator=postData.get('facilator'),
            critical_service_point=postData.get('critical_service_point'),
            include_other_enterprise_business_units=postData.get('include_other_enterprise_business_units')
        )
        demography.register()
        return redirect('/thirdpage')

class Thirdpage(View):
    def get(self,request):
        return render(request,'third_page.html')

    