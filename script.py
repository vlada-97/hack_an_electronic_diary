import random
from django.core.exceptions import ObjectDoesNotExist

from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Subject
from datacenter.models import Commendation
from datacenter.models import Teacher


def fix_marks(schoolkid_):
    ocenki = Mark.objects.filter(schoolkid=schoolkid_, points__in=[2,3])
    for i in ocenki:
        i.points=5
        i.save()


def remove_chastisements(schoolkid_):
    comment = Chastisement.objects.filter(schoolkid=schoolkid_)
    for i in comment:
        i.delete()


def create_commendation(schoolkid, subject):
    comments =  [
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
    this_schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid).get()
    lesson = Lesson.objects.filter(year_of_study = this_schoolkid.year_of_study, group_letter=this_schoolkid.group_letter, subject__title__contains=subject).order_by('date')
    lesson_one = lesson.first()
    Commendation.objects.create(text=random.choice(comments),schoolkid= this_schoolkid, created= lesson_one.date, teacher=lesson_one.teacher, subject=lesson_one.subject)