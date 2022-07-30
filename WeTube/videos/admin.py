from django.contrib import admin
from .models import *

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Ticket)
admin.site.register(TicketResponse)
