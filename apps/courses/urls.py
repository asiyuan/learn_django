from django.conf.urls import url
from .views import (
    CourseListView,
    CourseDetailView,
    CourseInfoView,
    CommentsView,
    AddCommentsView,
)


urlpatterns = [
    url('list/', CourseListView.as_view(), name='course_list'),
    url('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name='course_detail'),
    url('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name='course_info'),
    url('comment/(?P<course_id>\d+)/', CommentsView.as_view(), name='course_comments'),

    url('add_comment/', AddCommentsView.as_view(), name='add_comment')
]