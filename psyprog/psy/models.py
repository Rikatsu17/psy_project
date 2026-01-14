from django.db import models
# Create your models here.
class psy(models.Model):
    name = models.CharField(max_length=100, name='Name', verbose_name='Name')
    age = models.IntegerField(name='Age', verbose_name='Age')
    specialty = models.CharField(max_length=100, name='Specialty', verbose_name='Specialty')
    experience_years = models.IntegerField(name='Experience_Years', verbose_name='Experience Years')
    contact_email = models.EmailField(name='Contact_Email', verbose_name='Contact Email')
    bio = models.TextField(name='Bio', verbose_name='Bio')
    created_at = models.DateTimeField(auto_now_add=True, name='Created_At', verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, name='Updated_At', verbose_name='Updated At')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Psychologist'
        verbose_name_plural = 'Psychologists'

