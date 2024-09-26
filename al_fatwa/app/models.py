from django.db import models

# Create your models here.


class Lecture(models.Model):
    '''Model definition for Lecture.'''
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    img = models.FileField(upload_to='img', max_length = 100)


    def __str__(self):
        return self.title
    
    
class Episodes(models.Model):
    '''Model definition for episodes.'''
    video = models.FileField(upload_to='video', max_length = 100, null=True, blank=True )
    audio = models.FileField(upload_to='audio', max_length = 100, null=True, blank=True)
    
    title = models.CharField(max_length = 150)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=False)


    def __str__(self):
        return f"{self.title} - {self.lecture.title} "
    
    
class Questions(models.Model):
    '''Model definition for Questions.'''
    details = models.CharField(max_length = 150)

    episode = models.ForeignKey(Episodes, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.details