from django.contrib import admin
from django.urls import path, include  # include quan trọng!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('list_exam.urls')),  # Gắn toàn bộ url của app `list_exam`
]
