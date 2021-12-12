from django.contrib import admin
from .models import Student, Room, Hostel, Course, User, Warden,Feedback,Complaints,RoomClean


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'student_name',
        'father_name',
        'gender',
        'enrollment_no',
        'course',
        'dob',
        'room',
        'room_allotted']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['no', 'name', 'room_type', 'vacant', 'hostel']


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'room_type']


@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['is_warden']


@admin.register(Warden)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Complaints)
class ComplaintsAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'date_submit', 'Complaint_type','room_no')
    list_filter = ('date_submit',)
    search_fields = ('details',)

    class Meta:
        model = Feedback
        

@admin.register(RoomClean)
class RoomCleanAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'date_submit','room_no')
    list_filter = ('date_submit',)
    search_fields = ('details',)

    class Meta:
        model = Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'date', 'happy',)
    list_filter = ('date',)
    search_fields = ('details',)

    class Meta:
        model = Feedback
        
        
admin.site.register(Feedback, FeedbackAdmin)