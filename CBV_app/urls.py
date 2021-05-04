from django.conf.urls import url
from CBV_app import views

app_name='CBV_app'

urlpatterns=[
    url(r'^$',views.SchoolListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.StudentsDetailView.as_view(),name='detail'),
    url(r'^create/$',views.SchoolCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteViews.as_view(),name='delete'),

]
