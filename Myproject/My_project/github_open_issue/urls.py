from django.conf.urls import include , url
from . import views
app_name='github_open_issue'
urlpatterns = [

    url(r'^$',views.index ,name = 'index'),
    url(r'^claculate_github_result/(?P<url>.+)', views.showResult,name ='showResult'),
]