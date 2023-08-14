from django.shortcuts import render,HttpResponse,redirect
from learnApp.models import materials,Questions,Answers,Profile
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def hello(request):
    profile = Profile.objects.all()[:3]

    return render(request,'index.html',{'profile':profile})

def signup(request):
    print(request.POST)
    User = get_user_model()
    if request.method == 'POST':
        data = request.POST
        print(data['firstname'])
        if request.POST['password'] == request.POST['Conf_password']:
            if User.objects.filter(email=request.POST['Email']).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(email=request.POST['Email'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],
                            userType= request.POST['userType'],phonenumber= request.POST['phonenumber'],password = request.POST['password'],subject = request.POST['subject'])
                print("user created")
                return redirect('signin')
            
        else:
            messages.info(request,'Password not matching')
            return redirect('signup')
    
    return render(request,'signup.html')

#instructor signup

def signupInstructor(request):
    print(request.POST)
    User = get_user_model()
    if request.method == 'POST':
        data = request.POST
        print(data['firstname'])
        if request.POST['password'] == request.POST['Conf_password']:
            if User.objects.filter(email=request.POST['Email']).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(email=request.POST['Email'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],
                            userType= request.POST['userType'],phonenumber= request.POST['phonenumber'],password = request.POST['password'],
                            subject = request.POST['subject'])
                print("user created")
                return redirect('signin')
            
        else:
            messages.info(request,'Password not matching')
            return redirect('signup')
    
    return render(request,'instructorSignup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email,password=password)
        
        """ new_var = None
        print(user) """
        if user is not None:
            print('login success')
            login(request,user)
            return redirect('homepage')
        else:
            messages.info(request,"invalid credential")
            print("invalid credential")
            return redirect('signin')
    return render(request,'signin.html')

@login_required(login_url="/signin")
def homepage(request):
    material = materials.objects.filter(subject=request.user.subject)
    print(request.user.subject)
    return render(request,'home.html',{'items':material})


def QuestionsPage(request):
    if request.method == "POST":
            print(request.POST)
            profile = Profile.objects.get(user__id=request.user.id)
            questions = Questions.objects.create(student=request.user,question=request.POST['textarea'],
                                                studentProfile=profile )
    return render(request,'questions.html')

def AnswerPage(request):
    questions = Questions.objects.all()
    ans = Answers.objects.all()
    profile = Profile.objects.all()
    print(ans)
    if request.method == "POST":
        print(request.POST)
        profile = Profile.objects.get(user__id=request.user.id)
        questionId = request.POST['id']
        question = Questions.objects.get(id=questionId)
        #print(question.author.bio)
        answer = Answers.objects.create(author=request.user,answer=request.POST['textarea'],
                                        rating=1,question=question,authorProfile=profile)
    return render(request,'answer.html',{'question':questions,'answers':ans,
                                         'profile':profile})


def profile(request):
    print(request.user)
    profile = Profile.objects.get(user=request.user)
    print(profile.bio)
    return render(request,'profile.html')

def ProfileDetail(request,id):
    #print(request.user)
    profile = Profile.objects.get(user__id=id)
    print(profile)
    print(profile.bio)
    return render(request,'profileDetail.html',{'profile':profile})

def logout_view(request):
    logout(request)
    return redirect('home')

def lectProfile(request,id):
    profile = Profile.objects.get(user__id=id)
    print(profile)
    return render(request,'dash.html',{'profile':profile})
