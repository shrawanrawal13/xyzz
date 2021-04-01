from django.urls import path
from .views import *

app_name = 'posapp'



urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/',HomeView.as_view(),name = 'home'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    #supplier
    path('supplier/list/', SupplierListView.as_view(), name='supplierlist'),
    path('admin/student/create', SupplierCreateView.as_view(), name='studentcreate'),
    path('supplier/update/<int:pk>/',
         SupplierUpdateView.as_view(), name='supplierupdate'),
#     path('supplier/delete/<int:pk>/',
#          SupplierdeleteView.as_view(), name='supplierdelete'),
    

    
    







]