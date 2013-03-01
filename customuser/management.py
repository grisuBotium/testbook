#!/usr/bin/env python
# coding: utf8


from django.core.exceptions import ObjectDoesNotExist
from django.db.models import signals
from customuser.models import *


def init_data(sender, **kwargs):

    if 'django.contrib.auth.models' == kwargs['app'].__name__:
        user_count = 10

        # populate n users to db
        print 'Adding Users ...'
        for i in range(1, user_count + 1):
            username = 'user_%s' % i
            user, created = CustomUser.objects.get_or_create(username=username)
            if created:
                user.email = '%s@student.tuwien.ac.at.' % i
                user.first_name = 'firstname_%s' % i
                user.last_name = 'lastname_%s' % i
                user.nickname = 'nickname_%s' % i
                user.set_password(username)
                user.save()

        # create an admin user with password amanaman
        user, created = CustomUser.objects.get_or_create(username='amanaman')
        if created:
            user.set_password('amanaman')
            user.is_staff = True
            user.is_superuser = True
            user.save()

signals.post_syncdb.connect(init_data)