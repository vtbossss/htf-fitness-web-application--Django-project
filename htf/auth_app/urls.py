from django.urls import path
from auth_app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('login',views.dologin,name='dologin'),
    path('logout',views.dologout,name='dologout'),
    path('bmicalculator',views.bcalc,name='bcalc'),
    path('caloriecalculator',views.ccalc),
    path('macrocalculator',views.mcalc),
    path('workout',views.work),
    path('nutrition',views.nutrition),
    path('profile',views.profile),
]