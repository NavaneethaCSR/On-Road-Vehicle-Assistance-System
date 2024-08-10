
from django.urls import path

from . import views

urlpatterns = [
  path('Home', views.Homefun, name='Home'),
  path('Userlogout', views.UserLogoutfun, name='Userlogout'),
  path('UserSignup', views.UserSignupfun, name='UserSignup'),
  path('MechanicSignup', views.MechanicSignupfun, name='MechanicSignup'),
  path('UserSignin', views.UserSigninfun, name='UserSignin'),
  path('MechanicSignin', views.MechanicSigninfun, name='MechanicSignin'),
   path('Mechaniclogout', views.MechanicLogoutfun, name='Mechaniclogout'),
  path('applyrequest', views.applyrequestfun, name='applyrequest'),
  path('USER', views.USERfun, name='USER'),
  path('review', views.reviewfun, name='review'),
  path('reviewstatus', views.reviewstatusfun, name='reviewstatus'),
  path('approval', views.approvalfun, name='approval'),

  path('approval_for_mechanic/<int:k_id>', views.user_approve_request, name='approval_for_mechanic'),
  path('approvall_for_mechanic/<int:k_id>',
       views.user_disapprove_request, name='approvall_for_mechanic'),
path('status', views.user_request_view, name='status'),
path('call', views.callfun, name='call'),
path('callstatus', views.callstatusfun, name='callstatus'),

]