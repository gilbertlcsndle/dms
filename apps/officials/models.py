from django.db import models
from django.contrib.auth.models import User
from apps.residents.models import Resident

class Official(models.Model):
    POSITION_CHOICES = (
        ('chair', 'Chairman'),
        ('sec', 'Secretary'),
        ('treasure', 'Treasurer'),
        ('council', 'Councilor'),
    )
    QUESTION1_CHOICES = (
        ('question1_1', 'What is the first name of your best friend in high school?'),
        ('question1_2', 'What was the name of your first pet?'),
        ('question1_3', 'What was the first thing you learned to cook?'),
        ('question1_4', 'What was the first film you saw in the theater?'),
        ('question1_5', 'Where did you go the first time you flew on a plane?'),
        ('question1_6', 'What is the last name of your favorite elementary school teacher?'),
    )
    QUESTION2_CHOICES = (
        ('question2_1', 'What is your dream job?'),
        ('question2_2', 'What is your favorite children’s book?'),
        ('question2_3', 'What was the model of your first car?'),
        ('question2_4', 'What was your childhood nickname?'),
        ('question2_5', 'Who was your favorite film star or character in school?'),
        ('question2_6', 'Who was your favorite singer or band in high school?'),
    )
    QUESTION3_CHOICES = (
        ('question3_1', 'In what city did your parents meet?'),
        ('question3_2', 'What was the first name of your first boss?'),
        ('question3_3', 'What is the name of the street where you grew up?'),
        ('question3_4', 'What is the name of the first beach you visited?'),
        ('question3_5', 'What was the first album that you purchased?'),
        ('question3_6', 'What is the name of your favorite sports team?'),
    )

    user = models.OneToOneField(User)
    resident = models.ForeignKey(Resident, verbose_name='Name')
    position = models.CharField(choices=POSITION_CHOICES, max_length=50, default='')
    question1 = models.CharField(choices=QUESTION1_CHOICES, 
                                 verbose_name='Security Question 1', 
                                 max_length=50)
    question2 = models.CharField(choices=QUESTION2_CHOICES, 
                                 verbose_name='Security Question 2', 
                                 max_length=50)
    question3 = models.CharField(choices=QUESTION3_CHOICES, 
                                 verbose_name='Security Question 3', 
                                 max_length=50)
    answer1 = models.CharField(verbose_name='Answer', max_length=50)
    answer2 = models.CharField(verbose_name='Answer', max_length=50)
    answer3 = models.CharField(verbose_name='Answer', max_length=50)

    def __str__(self):
        return '%s - %s' %(
            self.user,
            self.resident
        )