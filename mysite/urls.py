from django.urls import path

from mysite.core import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('manual-form/', views.ManualFormView.as_view(), name='manual'),
    path('xdsoft-datetimepicker/', views.XDSoftDateTimePickerView.as_view(), name='xdsoft'),
    path('bootstrap-datetimepicker/', views.BootstrapDateTimePickerView.as_view(), name='bootstrap'),
    path('fengyuanchen-datepicker/', views.FengyuanChenDatePickerView.as_view(), name='fengyuanchen'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
]
