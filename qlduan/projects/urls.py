from django.urls import path
from . import views

urlpatterns = [
    path("nhanviens", views.nhanvien_index, name="nhanvien_index"),
    path("nhanviens/search", views.nhanvien_search, name="nhanvien_search"),
    path("nhanviens/<str:id>", views.nhanvien_detail, name="nhanvien_detail"),
    path("duans", views.duan_index, name='duan_index'),
    path("duans/search", views.duan_search, name="duan_search"),
    path("duans/<str:id>", views.duan_detail, name='duan_detail'),
    path("teams", views.team_index, name='team_index'),
    path("teams/<str:id>", views.team_detail, name='team_detail'),
    path("chucvus", views.chucvu_index, name='chucvu_index'),
    path("chucvus/<str:id>", views.chucvu_detail, name='chucvu_detail')
]
