from sqlite3 import IntegrityError
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets

from .models.course_review import CourseReview
from .models.instructor_review import InstructorReview
from .serializers import *
from .models import *
from django.views.generic import ListView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest


# # instructor viewset
# @api_view(['GET', 'POST'])
# def instructor_list(request):
#     if request.method == 'GET':
#         instructors = Instructor.objects.all()
#         serializer = InstructorSerializer(instructors, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = InstructorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PATCH', 'DELETE'])
# def instructor_detail(request, instructor_id):
#     try:
#         instructor = Instructor.objects.get(instructor_id=instructor_id)
#     except Instructor.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = InstructorSerializer(instructor)
#         return Response(serializer.data)
#
#     elif request.method == 'PATCH':
#         serializer = InstructorSerializer(instructor, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         instructor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# # student viewset
# @api_view(['GET', 'POST'])
# def student_list(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PATCH', 'DELETE'])
# def student_detail(request, student_id):
#     try:
#         student = Student.objects.get(student_id=student_id)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#
#     elif request.method == 'PATCH':
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# # course viewset
# @api_view(['GET', 'POST'])
# def course_list(request):
#     if request.method == 'GET':
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PATCH', 'DELETE'])
# def course_detail(request, course_id):
#     try:
#         course = Course.objects.get(course_id=course_id)
#     except Course.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)
#
#     elif request.method == 'PATCH':
#         serializer = CourseSerializer(course, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# # enrollment viewset
# @api_view(['GET', 'POST'])
# def enrollment_list(request):
#     if request.method == 'GET':
#         enrollments = Enrollment.objects.all()
#         serializer = EnrollmentSerializer(enrollments, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = EnrollmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PATCH', 'DELETE'])
# def enrollment_detail(request, id):
#     try:
#         enrollment = Enrollment.objects.get(id=id)
#     except Enrollment.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = EnrollmentSerializer(enrollment)
#         return Response(serializer.data)
#
#     elif request.method == 'PATCH':
#         serializer = EnrollmentSerializer(enrollment, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         enrollment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# # schedule viewset
# @api_view(['GET', 'POST'])
# def schedule_list(request):
#     if request.method == 'GET':
#         schedules = Schedule.objects.all()
#         serializer = ScheduleSerializer(schedules, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ScheduleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PATCH', 'DELETE'])
# def schedule_detail(request, id):
#     try:
#         schedule = Schedule.objects.get(id=id)
#     except Schedule.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ScheduleSerializer(schedule)
#         return Response(serializer.data)
#
#     elif request.method == 'PATCH':
#         serializer = ScheduleSerializer(schedule, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         schedule.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# # wishlist viewset
# @api_view(['GET', 'POST'])
# def wishlist_list(request):
#     if request.method == 'GET':
#         wishlists = Wishlist.objects.all()
#         serializer = WishlistSerializer(wishlists, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = WishlistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PATCH', 'DELETE'])
# def wishlist_detail(request, id):
#     try:
#         wishlist = Wishlist.objects.get(id=id)
#     except Wishlist.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = WishlistSerializer(wishlist)
#         return Response(serializer.data)
#
#     elif request.method == 'PATCH':
#         serializer = WishlistSerializer(wishlist, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         wishlist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer





def header(request):
    return render(request, 'myapp/header.html')


def instructor_detail(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    return render(request, 'myapp/instructor.html', {'instructor': instructor})


@login_required
def details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    schedules = Schedule.objects.filter(course=course)
    topics_covered = course.topics_covered.split('\n')
    reviews = CourseReview.objects.filter(course=course)
    context = {
        'schedules': schedules,
        'course': course,
        'topics_covered': topics_covered,
        'reviews': reviews,
    }
    return render(request, 'myapp/details.html', context)


def CoursesListView(request):
    courses = Course.objects.all()
    wishlist_courses = []

    if request.user.is_authenticated:
        student = request.user.student
        wishlist_courses = Wishlist.objects.filter(student=student).values_list('course', flat=True)

    context = {
        'courses': courses,
        'wishlist_courses': wishlist_courses,
    }
    return render(request, 'myapp/course.html', context)


@login_required
def unenroll_course(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    enrollment = Enrollment.objects.filter(student=request.user.student, schedule__course=course).first()

    if enrollment:
        enrollment.delete()

    return redirect('enrollments')




@login_required
def enrollments(request):
    user = request.user
    student = get_object_or_404(Student, user=user)

    enrollments = Enrollment.objects.filter(student=student)
    enrolled_schedules = Enrollment.objects.filter(student=student).values_list('schedule', flat=True)
    enrolled_courses = Course.objects.filter(schedule__in=enrolled_schedules)

    reviewed_courses = CourseReview.objects.filter(student=user).values_list('course', flat=True)
    courses_to_review = enrolled_courses.exclude(course_id__in=reviewed_courses)

    # Fetch instructors for enrolled courses
    instructors_for_courses = {}
    for course in enrolled_courses:
        instructors_for_courses[course] = course.instructors.all()

    context = {
        'enrollments': enrollments,
        'courses_to_review': courses_to_review,
        'instructors_for_courses': instructors_for_courses,
    }

    if request.method == 'POST':
        course_id = request.POST.get('course')
        instructor_id = request.POST.get('instructor')
        rating = int(request.POST.get('rating'))
        comments = request.POST.get('comments')

        if course_id and rating and comments:
            # Handle course review
            if CourseReview.objects.filter(course_id=course_id, student=user).exists():
                messages.error(request, 'You have already reviewed this course.', extra_tags='course_review')
            else:
                course = get_object_or_404(Course, course_id=course_id)
                CourseReview.objects.create(
                    course=course,
                    student=user,
                    rating=rating,
                    comment=comments
                )
                messages.success(request, 'Your course review has been submitted successfully.',
                                 extra_tags='course_review')

        if instructor_id and rating and comments:
            # Handle instructor review
            instructor = get_object_or_404(Instructor, id=instructor_id)
            if CourseReview.objects.filter(course=instructor, student=user).exists():
                messages.error(request, 'You have already reviewed this instructor.', extra_tags='instructor_review')
            else:
                InstructorReview.objects.create(
                    instructor=instructor,
                    student=user,
                    rating=rating,
                    comment=comments
                )
                messages.success(request, 'Your instructor review has been submitted successfully.',
                                 extra_tags='instructor_review')

        if not (course_id or instructor_id) or not (rating and comments):
            messages.error(request, 'Please fill in all the required fields.', extra_tags='review')

        return redirect('home')

    return render(request, 'myapp/enrollments.html', context)


@login_required
def toggle_wishlist(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    wishlist_item = Wishlist.objects.filter(student=request.user.student, course=course).first()

    if wishlist_item:
        wishlist_item.delete()
        messages.success(request, f"'{course.course_name}' has been successfully removed from your wishlist.")
    else:
        Wishlist.objects.create(student=request.user.student, course=course)
        messages.success(request, f"'{course.course_name}' has been successfully added to your wishlist.")

    return redirect('course_view')


class WishlistView(ListView):
    model = Wishlist
    template_name = 'myapp/wishlist.html'
    context_object_name = 'wishlist_items'

    def get_queryset(self):
        return Wishlist.objects.filter(student=self.request.user.student)


class SignupStudent(CreateView):
    model = Student
    template_name = 'myapp/signup.html'
    fields = ['email', 'mobile_number', 'first_name', 'last_name']

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, self.template_name, {'form': self.get_form(),
                                                        'username_error': 'This username is already taken. Please choose a different one.',
                                                        'username': ''})

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, self.template_name, {'form': self.get_form(),
                                                        'email_error': 'This email is already taken. Please choose a different one.',
                                                        'email': ''})
        try:
            # Create the user
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            # Create the student instance
            Student.objects.create(
                user=user,
                email=email,
                mobile_number=request.POST['mobile_number'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name']
            )

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, '')
                return redirect('home')

        except IntegrityError:
            messages.error(request, 'An error occurred while creating the user. Please try again.')
            return render(request, self.template_name, {'form': self.get_form(),
                                                        'error': 'An error occurred while creating the user. Please try again.'})

        messages.error(request, 'An error occurred while logging in. Please try again.')
        return redirect('login')


class StudentLoginView(View):
    template_name = 'myapp/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)

            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                if hasattr(user, 'student'):
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "No student account associated with this email.")
            else:
                messages.error(request, "NO USER FOUND")
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")

        return render(request, self.template_name)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, '')
        return redirect('home')


@login_required
def enroll_schedules(request):
    if request.method == "POST":
        student = request.user.student
        selected_schedule_id = request.POST.get('schedule')

        if not selected_schedule_id:
            return JsonResponse({"message": "No schedule selected", "status": "error"})

        try:
            schedule = Schedule.objects.get(id=selected_schedule_id)

            # Check if the student is already enrolled in any schedule of this course
            if Enrollment.objects.filter(student=student, schedule__course=schedule.course).exists():
                return JsonResponse(
                    {"message": "You are already enrolled in a schedule for this course.", "status": "warning"})

            Enrollment.objects.create(student=student, schedule=schedule)
            return JsonResponse({"message": "Enrolled successfully!", "status": "success"})

        except Schedule.DoesNotExist:
            return JsonResponse({"message": "Schedule does not exist", "status": "error"})
        except IntegrityError:
            return JsonResponse({"message": "Error during enrollment", "status": "error"})

    return JsonResponse({"message": "Invalid request", "status": "error"})



def home(request):
    return render(request, 'myapp/home2.html')
