from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_class_list, name='get_class_list'),
    path('<int:class_id>', views.get_assignment_list, name='get_assignment_list'),
    path('<int:class_id>/eng', views.get_assignment_list_eng, name='get_assignment_list_eng'),
    path('<int:class_id>/<int:assign_id>', views.get_assignment_info, name="get_assignment_info"),
    path('<int:class_id>/<int:assign_id>/eng', views.get_assignment_info_eng, name="get_assignment_info_eng"),
    path('<int:class_id>/<int:assign_id>/testcase', views.get_testcase_list, name="get_testcase_list"),
    path('<int:class_id>/<int:assign_id>/explain', views.get_explain, name="get_explain"),
    path('save',views.save_user_code, name="save_user_code"),
    path('save/<int:code_id>',views.get_user_code, name="get_user_code"),
    
]