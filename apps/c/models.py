# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.

class CourseManager(models.Manager):
    def validate(self, postData):
        print '~~~~~~~~~~~'
        errors = {}
        print postData
        if len(postData['name']) < 5:
            errors['name'] = "Name must be at least 5 characters"

        if len(postData['desc']) < 15:
            errors['desc'] = "description name must be at least 15 characters"

        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
    def __repr__(self):
        return "Course: \n{}\n{}\n{}\n".format(self.id, self.name, self.description)


