from django.db import models
from django.urls import reverse
# Create your models here.


Discipline_Choices = ( ('power','POWER'), ('telecom','TELECOM'), ('common','COMMON'))
Student_Choices = ( ('power', 'POWER') , ('telecom', 'TELECOM'), ('did not decide yet', "DID NOT DECIDE YET") )

class Course(models.Model):
	def __str__(self):
		return self.Name
	Name = models.CharField(max_length=100, primary_key="True")
	Discipline = models.CharField(max_length=100, choices=Discipline_Choices,default="telecom")
	About = models.TextField(max_length=100000, null=False, blank=True, default="Nothing to show yet")

class Video(models.Model):
	def __str__(self):
		return str(self.Course) + " " + str(self.Lecture_Number)
	Youtube = models.CharField(max_length=300, default="https://youtube.com")
	Drive = models.CharField(max_length=300,null=True, blank=False)
	Date = models.DateTimeField('Date In', blank=False, null=True)
	Lecture_Number = models.FloatField(null=True, blank=False)
	Course = models.ForeignKey(Course, on_delete=models.CASCADE, default="Microprocessor II")

class Document(models.Model):
	def __str__(self):
		return str(self.Course) + "/" +self.Name
	Name = models.CharField(max_length=100, primary_key="True")
	Format = models.CharField(max_length=100,)
	Notes = models.CharField(max_length=100,)
	Drive = models.CharField(max_length=300,null=True, blank=False)
	Course = models.ForeignKey(Course, on_delete=models.CASCADE, default="Microprocessor II")

class VisitCount(models.Model):
    def __str__(self):
        return str(self.Count)
    Count = models.IntegerField(null=False, blank=False,default=0)

class News(models.Model):
    def __str__(self):
        return self.Content
    Content = models.TextField(max_length=1000, null=False, default="")
    Discipline = models.CharField(max_length=100, choices=Discipline_Choices,default="telecom")

class Student(models.Model):
    def __str__(self):
        return self.Name +" - "+self.Discipline
    def get_absolute_url(self):
        return reverse('student_details', args=[str(self.Id),])
    Id = models.IntegerField(primary_key="True")
    Name = models.CharField(max_length=100, blank=False)
    Gmail = models.CharField(max_length=200, blank=False)
    Email = models.CharField(max_length=200, blank=False)
    Discipline = models.CharField(max_length=100, choices=Student_Choices,default="telecom")
    LinuxGroup = models.CharField(max_length=1,default="A")

class Group(models.Model):
    def __str__(self):
        return self.Names + "/" + str(self.Week) + "/" + self.Method
    Names = models.CharField(max_length=500, blank=False)
    Week = models.CharField(max_length=20)
    Method = models.CharField(max_length=20)
    Description = models.CharField(max_length=10000)

class Viewer(models.Model):
    def __str__(self):
        return self.Username
    Username=models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Name = models.CharField(max_length=50,default="No name")
    file_id = models.IntegerField(default=0)
    data1 = models.IntegerField()
    data2 = models.IntegerField()
    data3 = models.IntegerField()
    data4 = models.CharField(max_length=200,null=True, default="unchosen")
    datamate = models.CharField(max_length=200, null=False, default="unchosen")
    bio1 = models.CharField(max_length=200,null=False, default="unchosen")
    biomate=models.CharField(max_length=200,null=False, default="unchosen")
    Schedule = models.CharField(max_length = 100, default="")
    Telecom = models.IntegerField(default=-1)
    Auto = models.IntegerField(default=-1)
    Micro = models.IntegerField(default=-1)
    Machine = models.IntegerField(default=-1)
    OS =models.IntegerField(default=-1)
    Synthesis =models.IntegerField(default=-1)
    Data_Analysis = models.IntegerField(default=-1)
    Instrumentation = models.IntegerField(default=-1)
    Miniproject = models.IntegerField(default=-1)
    Economy =models.IntegerField(default=-1)
    Lab4 =models.IntegerField(default=-1)
    Lab5 =models.IntegerField(default=-1)
    Total =models.IntegerField(default=-1)
    Rank=models.IntegerField(default=-1)

class Schedule(models.Model):
    def __str__(self):
        return self.Order
    Order = models.CharField(max_length = 100, default = "")
    Votes = models.IntegerField(default=0)
