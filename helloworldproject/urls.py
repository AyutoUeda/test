from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
# from .views import helloworldfunc
# from .views import HelloWorldClass

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('helloworldurl/', helloworldfunc),
    # path('helloworldurl2/', HelloWorldClass.as_view()),
    path('', include('helloworldapp.urls'))
]

# path('  ', 実行内容)
#       ↑空欄ならどんな文字列でrequestを送られてきても実行内容を実施