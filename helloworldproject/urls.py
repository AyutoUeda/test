from django.contrib import admin
from django.urls import path
from .views import helloworldfunc
from .views import HelloWorldClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworldurl/', helloworldfunc),
    path('helloworldurl2/', HelloWorldClass.as_view()),
]

# path('  ', 実行内容)