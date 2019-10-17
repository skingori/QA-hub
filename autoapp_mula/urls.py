from django.conf.urls import url
from django.urls import path, re_path, include
from . import views
from django.http import Http404
from django.views.decorators.cache import never_cache

app_name = "qa_app"

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('accounts/login/', views.Login.as_view(), name='login'),
    path('login/', views.MakeLogin.as_view(), name='logged'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('tests/', views.DisplayTests.as_view(), name='tests'),
    path('user_keys', views.CreateKeyView.as_view(), name='user_keys'),
    path('new_test/', views.TestCreate.as_view(), name='new_test'),
    path('simulate/', views.SimulateTest.as_view(), name='simulate'),
    path('simulatePay/', views.SimulatePay.as_view(), name='simulatePay'),
    path('payments/', views.AllPayments.as_view(), name='payments'),
    # url(r'^refunds/(?P<checkout_id>\w+)/(?P<merchant_id>[\w-]+)/(?P<amount>[\w-]+)/$', views.Refunds.as_view(),
    #     name='refunds'),
    path('refunds/<str:checkout_id>/<str:merchant_id>/<str:amount>/', views.Refunds.as_view(), name='refunds'),
    path('post_refunds/', views.Refunds.as_view(), name='post_refunds'),
    path('cancel_request/<str:checkout_id>/<str:merchant_id>/', views.CancelRequest.as_view(), name='cancel_request'),
    path('initiate_cancel/', views.CancelRequest.as_view(), name='initiate_cancel'),
    path('open/', views.OpenAPI.as_view(), name='open'),
    path('call/', views.APICallBack.as_view(), name='call'),
    path('simulate_json/', views.SimulateJson.as_view(), name='simulate_json'),
    path('status_codes/', views.GetStatusCodes.as_view(), name='status_codes'),
    path('endpoints/', views.GetEndpointsList.as_view(), name='endpoints'),
    re_path(r'^code/(?P<pk>[\w-]+)/$', views.SetDefaultCode.as_view(), name='set_code'),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('signup/', views.SignUp.as_view(), name='signup'),

]
