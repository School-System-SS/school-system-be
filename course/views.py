from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser 
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.db.models import Count, Subquery, OuterRef
from .models import Student
from .models import Teacher
from .models import CourseModel
from .models import Assignment
from .models import StudentAssignment
from .serializers import AssignmentSerializer
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from .serializers import CourseSerializer
from .serializers import StudentAssignmentSerializer


# ----- Student Views ----- #

class GetAllStudents(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

class GetStudent(APIView):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, context={'request': request}, many=False)
        return Response(serializer.data)

class CourseStudents(APIView):
    def get(self, request, pk):
        course = CourseModel.objects.get(pk=pk)
        students = course.student.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

class CreateStudent(APIView):
    def post(self, request):
        user = request.user.pk 
        data = request.data
        data["user"] = user 
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditStudent(APIView):
    def put(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            owner = request.user.id
            updated = JSONParser().parse(request) 
            print(updated)
            updated["owner"] = owner
            serializer = StudentSerializer(student, data=updated)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteStudent(APIView):
    def delete(self, request, pk):
        try:
            data = Student.objects.get(pk=pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ----- Teacher Views ----- #

class GetAllTeachers(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

class GetTeacher(APIView): 
    def get(self, request, pk):
        data = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)

class CreateTeacher(APIView):
    def post(self, request):
        # user = request.user.pk 
        data = request.data
        # data["user"] = user
        serializer = TeacherSerializer(data=data)
        print(data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditTeacher(APIView):
    def put(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
            owner = request.user.id
            updated = JSONParser().parse(request) 
            print(updated)
            updated["owner"] = owner
            serializer = TeacherSerializer(teacher, data=updated)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteTeacher(APIView):
    def delete(self, request, pk):
        try:
            data = Teacher.objects.get(pk=pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Teacher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ---- Course Views ---- #

class GetAllCourses(APIView):
    def get(self, request):
        courses = CourseModel.objects.all()
        cleaned_data = [i for i in courses if request.user.id == i.teacher.type.id]
        serializer = CourseSerializer(cleaned_data, many=True)
        return Response(serializer.data)

class GetAllCoursesAdmin(APIView):
    def get(self, request):
        courses = CourseModel.objects.all()
        # cleaned_data = [i for i in courses if request.user.id == i.teacher.type.id]
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class GetAllCoursesStudent(APIView):
    def get(self, request):
        student = Student.objects.get(type=request.user)
        courses = student.coursemodel_set.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class GetCourse(APIView):
    def get(self, request, pk):
        data = CourseModel.objects.get(pk=pk)
        serializer = CourseSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)

class CreateCourse(APIView):
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditCourse(APIView):
    def put(self, request, pk):
        try:
            course = CourseModel.objects.get(id=pk)
            serializer = CourseSerializer(course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CourseModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteCourse(APIView):
    def delete(self, request, pk):
        try:
            data = CourseModel.objects.get(pk=pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CourseModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ----- Assignment Views ----- #

class GetAllAssignments(APIView):
    def get(self, request):
        assignmnets = Assignment.objects.all()
        cleaned_data = [i for i in assignmnets if request.user.id == i.teacher.type.id]
        serializer = AssignmentSerializer(cleaned_data, many=True)
        return Response(serializer.data)

class GetAssignment(APIView):
    def get(self, request, pk):
        data = Assignment.objects.get(pk=pk)
        serializer = AssignmentSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)

class CreateAssignment(APIView):
    def post(self, request):
        courses = CourseModel.objects.all()
        data = request.data
        for i in courses:
            if request.user.id == i.teacher.type.id:
                data["teacher"] = i.teacher.id
        serializer = AssignmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditAssignmnet(APIView):
    def put(self, request, pk):
        try:
            assignment = Assignment.objects.get(pk=pk)
            serializer = AssignmentSerializer(assignment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
        except Assignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteAssignment(APIView):
    def delete(self, request, pk):
        try:
            data = Assignment.objects.get(pk=pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Assignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

# ----- StudentAssignment Views ----- #

class GetAllStudentAssignments(APIView):
    def get(self, request):
        assignmnets = StudentAssignment.objects.all()
        serializer = StudentAssignmentSerializer(assignmnets, many=True)
        return Response(serializer.data)

class AssignmentStudentAssignment(APIView):
    def get(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        student_assignments = assignment.studentassignment_set.all()
        serializer = StudentAssignmentSerializer(student_assignments, many=True)
        return Response(serializer.data)

class StudentCourseAssignment(APIView):

    def get(self, request, pk):
        course = get_object_or_404(CourseModel, pk=pk)
        student = Student.objects.get(type=request.user.id)
        student_assignments = StudentAssignment.objects.filter(course=course, student=student)
        serializer = StudentAssignmentSerializer(student_assignments, many=True)
        return Response(serializer.data)

class GetStudentAssignment(APIView):
    def get(self, request, pk):
        data = StudentAssignment.objects.get(pk=pk)
        serializer = StudentAssignmentSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)

class CreateStudentAssignment(APIView):
    def post(self, request):
        try:
            course = CourseModel.objects.get(id=request.data["course"])
            students = course.student.all()
            print(course.teacher.id)
            for student in students:
                
                serializer = StudentAssignmentSerializer(data={
                                                              **request.data,
                                                              'student': student.id,
                                                              })
                if serializer.is_valid():
                    print(serializer)
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_201_CREATED)
        except CourseModel.DoesNotExist:
            return Response(f'Course with id {course.id} does not exist', status=status.HTTP_400_BAD_REQUEST)

class EditStudentAssignmnet(APIView):
    def put(self, request, pk):
        try:
            student_assignment = StudentAssignment.objects.get(pk=pk)
            student = request.user.id
            print(student)
            serializer = StudentAssignmentSerializer(student_assignment, data={
                                                              **request.data,
                                                              "is_submitted": True
                                                              }, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StudentAssignment.DoesNotExist:
            return Response(f'StudentAssignment with id {pk} does not exist', status=status.HTTP_404_NOT_FOUND)

# class DeleteStudentAssignment(APIView):
#     def delete(self, request, pk):
#         try:
#             data = StudentAssignment.objects.get(pk=pk)
#             data.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Assignment.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)