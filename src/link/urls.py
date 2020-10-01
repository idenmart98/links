from django.urls import path
from .views import cut_link, all_link, redirect_old

app_name = 'link'

urlpatterns = [
   path('history', all_link, name='history'),
   path('', cut_link, name='cut'),
   path('redirect/<int:link_id>', redirect_old, name='redirect_old') 
]