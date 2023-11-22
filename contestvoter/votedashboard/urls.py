from django.urls import path
from .views import video_page
from .views import vote
app_name = "votedashboard"
urlpatterns = [
    # Otras rutas de tu aplicación pueden ir aquí
    path('video/', video_page, name='video_page'),
    path('vote/<int:video_id>/', vote, name='vote'),

]