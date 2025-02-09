from django.urls import path
from .views import suppliers_list,SupplierAdd,SupplierDelete,SupplierUpdate

urlpatterns = [
    path('list/',suppliers_list,name="suppliers_list"),
    path('add/',SupplierAdd.as_view(),name="suppliers_add"),
    path('update/<int:pk>/',SupplierUpdate.as_view(),name = "suppliers_update"),
    path('delete/<int:pk>',SupplierDelete.as_view(),name ="suppliers_delete" )
]