from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('roommate/<str:obj1>/<str:obj2>',views.roommate,name="roommate"),
    path('vacanthouse',views.vacanthouse,name="vacanthouse"),
    path('sellroom',views.sellroom,name="sellroom"),
    path('logout',views.logout,name="logout"),
    path('final',views.final,name="final"),
    path('done/<str:obj1>/<str:obj2>/<str:obj3>',views.done,name="done"),
    path('more/<str:obj1>/<str:obj2>/<str:obj3>',views.more,name="more"),
    path('search',views.search,name="search"),
    path('profile',views.profile,name="profile"),
    path('accept/<str:obj1>/<str:obj2>/<str:obj3>/<str:obj4>',views.accept,name="accept"),
    path('delete/<str:obj1>/<str:obj2>/<str:obj3>/<str:obj4>',views.delete,name="delete")


]


if settings.DEBUG :
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
