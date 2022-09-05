from django.test import TestCase
from .models import Department, Employee

# Create your tests here.
class DepartmentsTest(TestCase):
    def setUp(TestCase):
        Department.objects.create(DepartmentName="IT")
    def test_department(self):
        department = Department.objects.get(DepartmentName="IT")
        self.assertEqual(department.DepartmentName, "IT")
        self.assertNotEqual(department.DepartmentName, "Support")

class EmployeesTest(TestCase):
    def setUp(TestCase):
        Employee.objects.create(EmployeeName="Name 1", Department="IT", DateOfJoining="2022-09-05", PhotoFileName="anonymous.png")
    def test_department(self):
        employee = Employee.objects.get(EmployeeName="Name 1")
        self.assertEqual(employee.Department, "IT")
        self.assertNotEqual(employee.Department, "Support")