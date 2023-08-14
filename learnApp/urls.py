from django.urls import path


from . import views

urlpatterns = [
    path('',views.hello,name="home"),
    path('signup',views.signup,name="signup"),
    path('InstructorSignup',views.signupInstructor,name="InstructorSignup"),
    path('signin',views.signin,name="signin"),
    path('logout',views.logout_view,name="logout"),
    path('home',views.homepage,name="homepage"),
    path('question',views.QuestionsPage,name="QuestionPage"),
    path('answer',views.AnswerPage,name="answerPage"),
    path('profile',views.profile,name="profiles"),
    path('lectprofile/<str:id>/',views.lectProfile,name="lectprofile"),
    path('profile/<str:id>/',views.ProfileDetail,name="profileDetail"),


]