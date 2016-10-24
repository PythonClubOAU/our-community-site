from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=100, default='', blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False, max_length=1000)

    def __unicode__(self):
        return "{0} with {1} sent a message saying '{}'".format(self.name, self.email, self.message)


class Member(models.Model):
    name = models.CharField(max_length=100, default='', blank=False)
    email = models.EmailField(blank='')
    sex_choice = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('N', "I'd rather not disclose",)
    )
    sex = models.CharField(max_length=1, choices=sex_choice, blank=False)
    level_options = (
        ('1', 'Part 1'),
        ('2', 'Part 2'),
        ('3', 'Part 3'),
        ('4', 'Part 4'),
        ('5', 'Part 5'),
    )
    level = models.CharField(max_length=1, choices=level_options, blank=False)
    knowledge_options = (
        ('BEG', 'I have never used it before'),
        ('AMA', 'I have used it once or twice'),
        ('BUI', 'I have built some stuff with Python')
    )
    knowledge = models.CharField(blank=False, choices=knowledge_options, max_length=3)
    # pythonic_name = models.CharField(max_length=100, default=False, blank=False)
    display_image = models.BooleanField(blank=False, default=False)
    message = models.TextField(blank=False, default='', max_length=500)
    bio = models.TextField(blank=False, default='', max_length=100)
    interest_options = (
        ('PYT', 'Pure Python Scripting'),
        ('WEB', 'Web Programming'),
        ('DTS', 'Data Science'),
        ('APP', 'App Development(Mostly Kivy and other GUIs libraries)'),
        ('NET', 'Networking'),
        ('NDI', "I do not know for now."),
    )
    interest = models.CharField(blank=False, choices=interest_options, max_length=3)
    image = models.ImageField(upload_to='members/image', blank=False, default='members/image/mathhew.png')

    def __unicode__(self):
        return "{0} with {1} sent a message saying '{}'".format(self.name, self.email, self.message)


class Post(models.Model):
    author = models.ForeignKey(Member)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Event(models.Model):
    event_title = models.CharField(default='', max_length=300, blank=False)
    start_date = models.CharField(default='', max_length=2, blank=False)
    end_date = models.CharField(default='', max_length=2, blank=True)
    details = models.TextField(default='', blank=True)
    event_type = (
        ('PYT', 'Python Club Event'),
        ('GEN', 'General Event'),
    )
    event = models.CharField(blank=False, choices=event_type, max_length=3)

    def __str__(self):
        return self.event_title

    def __unicode__(self):
        return "{0}".format(self.event_title)





