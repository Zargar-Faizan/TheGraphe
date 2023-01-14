from django.contrib import admin

from task.models import Movie, Moviedesc, Moviedialogue

# Register your models here.
admin.site.register(Movie)
admin.site.register(Moviedesc)
admin.site.register(Moviedialogue)
