import random

from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation

COMMENDATIONS = [
    'Хвалю!',
    'Отлично!',
    'Молодец!',
    'Так держать!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Именно этого я давно ждал от тебя!',
    'Ты меня очень обрадовал!',
    'Уже существенно лучше!',
    'Я вижу, как ты стараешься!',
    'С каждым разом у тебя получается всё лучше!',
    'Ты сегодня прыгнул выше головы!'
    ]

def get_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return schoolkid
    except Schoolkid.DoesNotExist:
        print('Schoolkid matching query does not exist!')
    except Schoolkid.MultipleObjectsReturned:
        print('Return more than one Schoolkid!')


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3]).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, subject_title):
    lesson = Lesson.objects.filter(year_of_study = schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject__title__contains=subject_title).order_by('-date').first()
    Commendation.objects.create(text=random.choice(COMMENDATIONS),schoolkid= schoolkid, created= lesson.date, teacher=lesson.teacher, subject=lesson.subject)
   
