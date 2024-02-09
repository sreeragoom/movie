from django.urls import path

from movie_app import views
app_name='movie_app'
urlpatterns = [
    path('add/', views.add_movie, name='add'),
    path('',views.index,name='index'),

    path('details/<int:id>/',views.detail,name='detail'),
    path('<slug:c_slug>/', views.index, name='movies_by_category'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    # path('<slug:c_slug>/<slug:movie_slug>/<int:id>/',views.proDetail,name='detail')
]