from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from myapp import views
from myapp.views import CoursesListView

router_instructor = DefaultRouter()
router_instructor.register(r'', InstructorViewSet, basename='instructor')
router_student = DefaultRouter()
router_student.register(r'', views.StudentViewSet, basename='student')
router_course = DefaultRouter()
router_course.register(r'courses', views.CourseViewSet, basename='course')
router_enrollment = DefaultRouter()
router_enrollment.register(r'enrollments', views.EnrollmentViewSet, basename='enrollment')
router_schedule = DefaultRouter()
router_schedule.register(r'schedules', views.ScheduleViewSet, basename='schedule')
router_wishlist = DefaultRouter()
router_wishlist.register(r'wishlists', views.WishlistViewSet, basename='wishlist')

urlpatterns = [
    # path('instructor', views.instructor_list),
    # path('instructor/<int:instructor_id>', views.instructor_detail),
    # path('student', views.student_list),
    # path('student/<int:student_id>', views.student_detail),
    # path('course', views.course_list),
    # path('course/<int:course_id>', views.course_detail),
    # path('enrollment', views.enrollment_list),
    # path('enrollment/<int:id>', views.enrollment_detail),
    # path('schedule', views.schedule_list),
    # path('schedule/<int:id>', views.schedule_detail),
    # path('wishlist', views.wishlist_list),
    # path('wishlist/<int:id>', views.wishlist_detail),

    # ModelViewSets Urls
    path('instructor_c/', include(router_instructor.urls)),
    path('student_c/', include(router_student.urls)),
    path('course_c/', include(router_course.urls)),
    path('enrollment_c/', include(router_enrollment.urls)),
    path('schedule_c/', include(router_schedule.urls)),
    path('wishlist_c/', include(router_wishlist.urls)),
    path('', views.home, name='home'),
    path("course_view", CoursesListView, name="course_view"),
    path("signupStudent", SignupStudent.as_view(), name="signupStudent"),
    path("login", StudentLoginView.as_view(), name='login'),
    path("header", views.header, name='header'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('<int:course_id>', views.details, name='details'),
    path('enroll_schedules/', enroll_schedules, name='enroll_schedules'),
    path("enrollments", enrollments, name="enrollments"),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('wishlist/<int:course_id>/', toggle_wishlist, name='toggle_wishlist'),
    path('unenroll/<int:course_id>/', views.unenroll_course, name='unenroll'),
    path('instructor/<int:instructor_id>/', views.instructor_detail, name='instructor_detail'),

]
