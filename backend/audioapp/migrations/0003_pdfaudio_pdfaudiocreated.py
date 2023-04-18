# Generated by Django 4.2 on 2023-04-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioapp', '0002_alter_textaudio_lang'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDFAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_name', models.CharField(max_length=30)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdffolder')),
                ('lang', models.CharField(choices=[('en-us', 'English-United States'), ('af', 'Afrikaans'), ('sq', 'Albanian'), ('ar', 'Arabic'), ('hy', 'Armenian'), ('bn', 'Bengali'), ('bn', 'Bengali'), ('ca', 'Catalan'), ('bn', 'Bengali'), ('zh', 'Chinese'), ('bn', 'Bengali'), ('zh-cn', 'Chinese'), ('zh-tw', 'Taiwan'), ('zh-yue', 'Cantonese'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('nl', 'Dutch'), ('en', 'English'), ('en-au', 'English-Australia'), ('en-uk', 'English-United Kingdom'), ('eo', 'Esperanto'), ('fi', 'Finnish'), ('fr', 'French'), ('de', 'German'), ('hu', 'Hungarian'), ('el', 'Greek'), ('hi', 'Hindi'), ('is', 'Icelandic'), ('id', 'Indonesian'), ('it', 'Italian'), ('ja', 'Japanese'), ('km', 'Cambodian'), ('ko', 'Korean'), ('la', 'Latin'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('no', 'Norwegian'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sr', 'Serbian'), ('si', 'Sinhala'), ('sk', 'Slovak'), ('es', 'Spanish'), ('es-es', 'Spanish-Spain'), ('es-us', 'Spanish-USA'), ('sw', 'Swahili'), ('sv', 'Swedish'), ('ta', 'Tamil'), ('th', 'Thai'), ('tr', 'Turkish'), ('uk', 'Ukrainian'), ('vi', 'Vietnamese'), ('cy', 'Welsh')], max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PDFAudioCreated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_name', models.CharField(max_length=20)),
                ('mytext', models.TextField()),
                ('lang', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
