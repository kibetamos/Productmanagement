from django.urls import path
from students.views import (
    student_create_view,
    student_list_view,
    student_detail_view,
    student_update_view,
)

app_name = 'students'
urlpatterns = [
    path('', student_list_view, name='student-list'),
    path('create/', student_create_view, name='student-list'),
    path('<int:id>/', student_detail_view, name='student-detail'),
    path('<int:id>/update/', student_update_view, name='student-update'),
    # path('<int:id>/delete/', product_delete_view, name='product-delete'),
]
