from django.urls import path
from tba_app import views
from django.views.generic import TemplateView

urlpatterns=[
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('memberlist',TemplateView.as_view(template_name='member.html'),name='member'),
    path('loginpage',TemplateView.as_view(template_name='login.html'),name='login'),
    path('registerpage',TemplateView.as_view(template_name='reg.html'),name='reg'),
    path('homeadmin',TemplateView.as_view(template_name='adminhome.html'),name='adminhome'),
    path('lawhome',TemplateView.as_view(template_name='lawyerhome.html'),name='lawyerhome'),
    path('lawprof',TemplateView.as_view(template_name='lawyerprofile.html'),name='lawyerprofile'),
    path('lawprofed',TemplateView.as_view(template_name='lawyerprofedit.html'),name='lawyerprofedit'),
    path('admsg',TemplateView.as_view(template_name='adminmsg.html'),name='adminmsg'),


    
    
   
    path('registerdetails/',views.regview,name='adminhome1'),
    path('reg',views.register,name='register'),
    path('approval',views.approval,name='approv'),
    path('auth',views.authentication,name='submitt'),
    path('details',views.lawyerdetails,name='member'),
    path('sout',views.logout_view,name='logout'),
    path('lawdetails',views.viewlawprof,name='lawyerprofile'),
    path('lawdetail',views.viewlawprofedit,name='lawyerprofedit'),
    path('lawedd',views.lawyerdetailsedit,name='lawyeredit'),
    path('mss',views.submitmsg,name='msgsub'),
    path('admsgg',views.viewmsg,name='adminmsg'),
    path('rmsg',views.readmsg,name='readmessage'),
    
    

  
]