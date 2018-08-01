from django.urls import path
from . import views


app_name = 'billing'

urlpatterns = [
    # ex: api/billing/list/
    path('list/', views.ShowBillView.as_view(), name='Show-Bill-Item'),
    # ex: api/billing/add/
    path('add/', views.AddBillingHeaderView.as_view(), name='Add-Bill-Item'),
    # ex: api/instamojo/
    path('instamojo/', views.Instamojo, name='InstaMojo'),
]
