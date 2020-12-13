from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.contrib.auth.models import User


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        username = "Minurasam"
        email = "minura.samaranayake@gmail.com"
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            username = username,
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))





# class TasksTest(TestCase):
#     def test_create_courses(self):
#         """
#         Tests to create courses
#         """

#         current_semester = SemesterFactory.create(end = datetime.now().date() - timedelta(days = 1))

#         self.assertEquals(current_semester, get_yesterday_semester())
    
#     def test_delete_courses(self):
#         """
#         Tests to delete courses
#         """

#         faculty = FacultyFactory.create()
#         current_semester = SemesterFactory.create(end = datetime.now().date() - timedelta(days = 1))
#         next_semester = SemesterFactory.create(start = datetime.now().date() + timedelta(days = 60) ,end = datetime.now().date() + timedelta(days = 90))

#         current_course = CourseFactory.create(semester = current_semester)
#         next_course = CourseFactory.create(semester = next_semester)

#         current_course.faculty.add(faculty)

#         disable_faculty()
        

#         faculty = User.objects.get(username = faculty.username)
#         self.assertEquals(faculty.is_active, False)