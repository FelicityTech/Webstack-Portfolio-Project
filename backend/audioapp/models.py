from django.db import models
import datetime

# Create your models here.
class TextAudio(models.Model):
    language_choice = (
        ('en-us', 'English-United States'),
        ('af', 'Afrikaans'),
        ('sq', 'Albanian'),
        ('ar', 'Arabic'), 
        ('hy', 'Armenian'),
        ('bn', 'Bengali'),
        ('bn', 'Bengali'),
        ('ca', 'Catalan'),
        ('bn', 'Bengali'),
        ('zh', 'Chinese'),
        ('bn', 'Bengali'),
        ('zh-cn', 'Chinese'),
        ('zh-tw', 'Taiwan'),
        ('zh-yue', 'Cantonese'),
        ('hr', 'Croatian'),
        ('cs', 'Czech'),
        ('da', 'Danish'), 
        ('nl', 'Dutch'),
        ('en', 'English'),
        ('en-au', 'English-Australia'),
        ('en-uk', 'English-United Kingdom'),
        ('eo', 'Esperanto'),
        ('fi', 'Finnish'), 
        ('fr', 'French'),
        ('de', 'German'),
        ('hu', 'Hungarian'),
        ('el', 'Greek'),
        ('hi', 'Hindi'), 
        ('is', 'Icelandic'),
        ('id', 'Indonesian'),
        ('it', 'Italian'),
        ('ja', 'Japanese'),
        ('km', 'Cambodian'),
        ('ko', 'Korean'),
        ('la', 'Latin'), 
        ('lv', 'Latvian'), 
        ('mk', 'Macedonian'),
        ('no', 'Norwegian'), 
        ('pl', 'Polish'), 
        ('pt','Portuguese'),
        ('ro', 'Romanian'), 
        ('ru', 'Russian'), 
        ('sr','Serbian'),
        ('si', 'Sinhala'), 
        ('sk','Slovak'),
        ('es', 'Spanish'),
        ('es-es', 'Spanish-Spain'),
        ('es-us', 'Spanish-USA'),
        ('sw', 'Swahili'),
        ('sv', 'Swedish'), 
        ('ta',  'Tamil'),
        ('th', 'Thai'),
        ('tr', 'Turkish'),
        ('uk', 'Ukrainian'),
        ('vi', 'Vietnamese'),
        ('cy', 'Welsh'),
    )
    text_name = models.CharField(max_length=20)
    info = models.TextField()
    lang= models.CharField(max_length=10, choices=language_choice, default='English - United States')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.text_name, self.date_created)
