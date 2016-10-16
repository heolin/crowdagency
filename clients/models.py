from __future__ import unicode_literals


from django.contrib.auth.models import User

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200)
    package_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    is_embeded = models.BooleanField(default=True)




SATISFACTION_LEVELS = ((None, ""),
                       (1, "1 - Bardzo źle"),
                       (2, "2 - Źle"),
                       (3, "3 - Tak sobie"),
                       (4, "4 - Dobrze"),
                       (5, "5 - Bardzo dobrze"))

EXPERIENCES = ((None, ""),
               (1, "Bardzo rzadko (rzadziej niż raz w miesiącu)"),
               (2, "Rzadko (co najmniej raz w miesiącu)"),
               (3, "Raz na jakiś czas (kilka razy w miesiącu)"),
               (4, "Często (co najmniej raz w tygodniu)"),
               (5, "Bardzo często (kilka razy w tygodniu)"))

class Survey(models.Model):
    user = models.ForeignKey(User)
    satisfaction_level = models.IntegerField(choices=SATISFACTION_LEVELS, default=None)
    satisfaction_comment = models.TextField()
    experience = models.IntegerField(choices=EXPERIENCES, default=None)
    timestamp = models.TimeField(auto_now_add=True)

