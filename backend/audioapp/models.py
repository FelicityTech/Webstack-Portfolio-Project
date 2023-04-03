from django.db import models
import datetime

# Create your models here.
class TextAudio(models.Model):
    language_choice = (('af', '1-Afrikaans'),('sq', '2-Albanian'),('ar', '3-Arabic'),('hy','4-Armenian'),('bn','5-Bengali'),('bn','6-Bengali'),('ca','7-Catalan'),('bn','8-Bengali'),('zh','9-Chinese'),('bn','10-Bengali'),('zh-cn','11-Chinese'),('zh-tw','12-Taiwan'),('zh-yue','13-Cantonese'),('hr','14-Croatian'),('cs','15-Czech'),('da','16-Danish'),('nl','17-Dutch'),('en','18-English'),('en-au','19-English-Australia'),('en-uk','20-English-United-Kingdom'),('en-us','21-English-United-states'),('eo','22-Esperanto'),('fi','23-Finnish'),('fr','24-French'),('de','25-German'),('hu','26-Hungarian'),('el','27-Greek'),('hi','28-Hindi'),('is','29-Icelandic'),('id', '30-Indonesian'),('it', '31-Italian'),('ja', '32-Japanese'),('km','33-Cambodian'),('ko','34-Korean'),('la','35-Latin'),('lv','36-Latvian'),('mk','37-Macedonian'),('no','38-Norwegian'),('pl','39-Polish'),('pt','40-Portuguese'),('ro','41-Romanian'),('ru','42-Russian'),('sr','43-Serbian'),('si','44-Sinhala'),('sk','45-Slovak'),('es','46-Spanish'),('es-es','47-Spanish-Spain'),('es-us','48-Spanish-USA'),('sw','49-Swahili'),('sv','50-Swedish'),('ta','51-Tamil'),('th','52-Thai'),('tr','53-Turkish'),('uk','54-Ukrainian'),('vi','55-Vietnamese'),('cy','56-Welsh'))
    text_name = models.CharField(max_length=20)
    info = models.TextField()
    lang= models.CharField(max_length=10, choices=language_choice, default='21-English-United-tates')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.text_name, self.date_created)
