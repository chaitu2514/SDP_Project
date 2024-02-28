from django.contrib import admin
from django.urls import path
from .views import*
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello/',hello1,name='hello'),
    path('',NewHomePage,name='NewHomePage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print_to_console/',print_to_console,name='print_to_console'),
    path('print1/',print1,name='print1'),
    path('randomcall/',randomcall,name='randomcall'),
    path('randomlogic/',randomlogic,name='randomlogic'),
    path('getdate1/',getdate1,name='getdate1'),
    path('get_date/',get_date,name='datetime'),
    path('register1/',register1,name='register1'),
    path('registerloginfunction/',registerloginfunction,name='registerloginfunction'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('rent/',rent,name='rent'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('weatherpagecall/',weatherpagecall,name='weatherpagecall'),
    path('feedback/',feedback,name='feedback'),
    path('feedbackfunction/',feedbackfunction,name='feedbackfunction'),
    path('login/',login,name='login'),
    path('login1/',login1,name='login1'),
    path('logout/',logout,name='logout'),
    path('signup/', signup, name='signup'),
    path('signup1/', signup1, name='signup1')

]