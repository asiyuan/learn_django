from django.conf.urls import url, include
from .views import (
    OrgView,
    AddUserAskView,
    OrgHomeView,
    OrgCourseView,
    OrgDescView,
    OrgTeacherView,
    AddFavView,
    TeacherListView,
    TeacherDetailView,
)

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url('add_ask/', AddUserAskView.as_view(), name='add_ask'),
    url('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name='org_home'),
    url('course/(?P<org_id>\d+)/', OrgCourseView.as_view(), name='org_course'),
    url('desc/(?P<org_id>\d+)/', OrgDescView.as_view(), name='org_desc'),
    url(r'^org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),

    url('add_fav/', AddFavView.as_view(), name='add_fav'),

    # 讲师列表页
    url('teacher/list/', TeacherListView.as_view(), name='teacher_list'),
    url('teacher/detail/(?P<teacher_id>\d+)/', TeacherDetailView.as_view(), name='teacher_detail')
]
