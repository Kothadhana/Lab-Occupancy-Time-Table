from django.urls import path
from Labtt2 import views
from django.contrib.auth import views as t

#from django.contrib.auth import views as t

urlpatterns = [
		path("",views.home,name="hme"),
		path("central/",views.central,name="cntrl"),
		path("add/",views.add_new,name="add"),
		path("select/<int:id>",views.view_select,name='slct'),
		path("update/<int:id>",views.update,name='update'),
		path("delete/<int:id>",views.delete,name='delete'),
		path('login/', t.LoginView.as_view(template_name="demo/login.html"), name='lg'),
		path("logout/",t.LogoutView.as_view(template_name="demo/logout.html"),name="lgo"),
		path('reg/',views.usrg,name="ug"),
		path('regd/',views.regd,name='reg'),
]
