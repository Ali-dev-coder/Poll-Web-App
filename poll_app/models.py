from django.db import models

# Create your models here.
class pollmodel(models.Model):
    poll_question = models.TextField()
    poll_option_one = models.CharField(max_length=30)
    poll_option_two = models.CharField(max_length=30)
    poll_option_three = models.CharField(max_length=30)
    poll_option_one_count = models.IntegerField(default=0)
    poll_option_two_count = models.IntegerField(default=0)
    poll_option_three_count = models.IntegerField(default=0)
    
    def total(self):
        return self.poll_option_one_count+self.poll_option_two_count+self.poll_option_three_count

