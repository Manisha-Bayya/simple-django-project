from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup$', views.signup, name="signup"),
    url(r"^signup/validate$", views.signup_validate, name="signup_validate"),
    url(r'^login$', views.c_login, name="login"),
    url(r'^login/send_otp$', views.send_otp, name="send_otp"),
    url(r"^login/validate$", views.login_validate, name="login_validate"),
    url(r'^search$', views.search, name="search"),
    url(r'country/(?P<country_name>[\w|\W]+)$', views.get_country_details, name="country_page"),
    url(r'^logout$', views.c_logout, name="logout"),
]
