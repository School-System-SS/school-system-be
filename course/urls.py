from django.urls import path
from .views import GetAllAssignments, GetAssignment, CreateAssignment, EditAssignmnet, DeleteAssignment, GetAllCourses, GetCourse, CreateCourse, EditCourse, DeleteCourse, GetAllStudents, GetStudent, CreateStudent, EditStudent, DeleteStudent, GetAllTeachers, GetTeacher, CreateTeacher, EditTeacher, DeleteTeacher, GetAllStudentAssignments, GetStudentAssignment, CreateStudentAssignment, EditStudentAssignmnet, GetAllCoursesStudent, CourseStudents, AssignmentStudentAssignment, StudentCourseAssignment

urlpatterns = [
    path('assignment/get-all/', GetAllAssignments.as_view()),
    path('assignment/get-one/<int:pk>', GetAssignment.as_view()),
    path('assignment/create/', CreateAssignment.as_view()),
    path('assignment/update/<int:pk>', EditAssignmnet.as_view()),
    path('assignment/delete/<int:pk>', DeleteAssignment.as_view()),

    path('course/get-all/', GetAllCourses.as_view()),
    path('course/students/get-all/', GetAllCoursesStudent.as_view()),
    path('course/get-one/<int:pk>', GetCourse.as_view()),
    path('course/create/', CreateCourse.as_view()),
    path('course/update/<int:pk>', EditCourse.as_view()),
    path('course/delete/<int:pk>', DeleteCourse.as_view()),

    path('student/get-all/', GetAllStudents.as_view()),
    path('student/course/get-all/<int:pk>', CourseStudents.as_view()),
    path('student/get-one/<int:pk>', GetStudent.as_view()),
    path('student/create/', CreateStudent.as_view()),
    path('student/update/<int:pk>', EditStudent.as_view()),
    path('student/delete/<int:pk>', DeleteStudent.as_view()),

    path('teacher/get-all/', GetAllTeachers.as_view()),
    path('teacher/get-one/<int:pk>', GetTeacher.as_view()),
    path('teacher/create/', CreateTeacher.as_view()),
    path('teacher/update/<int:pk>', EditTeacher.as_view()),
    path('teacher/delete/<int:pk>', DeleteTeacher.as_view()),
    
    path('studentAssignment/get-all/', GetAllStudentAssignments.as_view()),
    path('studentAssignment/assignment/get-all/<int:pk>', AssignmentStudentAssignment.as_view()),
    path('studentAssignment/course/get-all/<int:pk>', StudentCourseAssignment.as_view()),
    path('studentAssignment/get-one/<int:pk>', GetStudentAssignment.as_view()),
    path('studentAssignment/create/', CreateStudentAssignment.as_view()),
    path('studentAssignment/update/<int:pk>', EditStudentAssignmnet.as_view()), 
]