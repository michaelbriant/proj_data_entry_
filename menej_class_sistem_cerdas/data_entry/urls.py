from django.urls import path
from . import views

app_name = 'data_entry'

urlpatterns = [
    path('', views.set_pengguna, name='set_pengguna'),
    path('data_entry/', views.set_data_entry, name='set_data_entry'),
    path('pengguna/', views.set_pengguna, name='set_pengguna'),
    path('pengguna/update/<int:id>/', views.update_pengguna, name='update_pengguna'),
    path('pengguna/delete/<int:id>/', views.delete_pengguna, name='delete_pengguna'),
    path('pengguna/view/<int:id>/', views.view_pengguna, name='view_pengguna'),
    path('api/pengguna/<int:user_id>/', views.get_pengguna_detail_api, name='get_pengguna_detail_api'),
    path('content/', views.set_content, name='set_content'),
    path('pengguna/listpenggunabystate', views.search_pengguna_by_state, name='search_pengguna_by_state'),
]
