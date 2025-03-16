from django.contrib import admin
from .models import Student,Instructor,Course,Schedule,Enrollment,Wishlist
from .models.course_review import CourseReview


class InstructorInline(admin.TabularInline):
    model = Course.instructors.through
    extra = 1
class CourseInline(admin.TabularInline):
    model = Course.instructors.through
    extra = 1
class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1
class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1
class WishlistInline(admin.TabularInline):
    model = Wishlist
    extra = 1

class StudentInline(admin.TabularInline):
    model = Student
    extra = 1

# Customize the Course admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'credit_hours')
    list_filter = ('credit_hours', 'course_name', 'course_code')
    search_fields = ('course_code', 'course_name')
    ordering = ('course_code',)
    inlines = [ScheduleInline]

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('course', 'created_on', 'updated_date')
    list_filter = ('course', 'created_on','updated_date')
    search_fields = ('course__course_name',)
    ordering = ('-created_on',)
    date_hierarchy = 'created_on'
    fields = ('course', 'created_on', 'updated_date')
    list_editable = ('updated_date',)
    inlines = [EnrollmentInline]


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'credit_hours')
    list_filter = ('credit_hours','course_name', 'course_code','instructors','course_id')
    search_fields = ('course_code', 'course_name')
    ordering = ('course_code',)
    inlines = [ScheduleInline]

class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'rating','comment')
    list_filter = ('course', 'student', 'rating')
    search_fields = ('course__course_name',)
    ordering = ('rating',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile_number')
    list_filter = ('student_id','first_name','last_name','mobile_number','email','user')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')
    # raw_id_fields = ('user',)
    inlines = [EnrollmentInline,WishlistInline]

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile_number')
    list_filter = ('instructor_id','first_name','last_name','mobile_number','email','user')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')
    # raw_id_fields = ('user',)
    inlines = [CourseInline]

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('student', 'course','enroll_date')
    list_filter = ('enroll_date', 'course','student')
    search_fields = ('student__first_name', 'course__course_name')
    ordering = ('student', 'course')
    date_hierarchy = 'enroll_date'

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'schedule', 'enroll_date')
    list_filter = ('student','schedule', 'enroll_date')
    search_fields = ('student__first_name', 'course__course_name')
    ordering = ('enroll_date',)
    date_hierarchy = 'enroll_date'

admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(CourseReview,CourseReviewAdmin)





