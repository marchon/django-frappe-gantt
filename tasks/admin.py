# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from tasks.models import Task


class AdminTask(TreeAdmin):
    form = movenodeform_factory(Task)

admin.site.register(Task, AdminTask)
