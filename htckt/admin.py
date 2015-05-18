
from django.contrib import admin
from django.conf import settings
from .models import Student,StudentResource


from import_export.admin import ImportExportModelAdmin



def send_email_to(modeladmin, request, queryset):
   stds_associate = queryset.filter(branch='Computer Science & Engineering' ).filter(agg_10th_percntge='>60').filter(agg_12th_percntge='>60').filter(agg_BE_percntge='>60')
   stds_mgmt = queryset.exclude(branch='Computer Science & Engineering' ).exclude(agg_10th_percntge='>60').exclude(agg_12th_percntge='>60').exclude(agg_BE_percntge='>60')
   std = queryset.filter(first_name='zizoo')

   from django.core.mail import EmailMultiAlternatives
   from django.template.loader import render_to_string
   from django.utils.html import strip_tags

   subject, from_email, to = 'Hi', 'ravi.keshare@gmail.com', std[0].email

   html_content = render_to_string('htckt/email.html', {'varname':'value'}) # ...
   text_content = strip_tags(html_content) # this strips the html, so people will have the text as well.

   # create the email, and attach the HTML version as well.
   msg = EmailMultiAlternatives(subject, text_content, from_email, [std[0].email])
   msg.attach_alternative(html_content, "text/html")
   msg.send()
 
   
class MGTListFilter(admin.SimpleListFilter):
    title = 'Position'
    parameter_name = 'Position'
	
    def lookups(self, request, model_admin):

        POSITION=(('MT', 'Managment Trainee'),('AS', 'Associate Engineer'),
	    
	)
        return POSITION
    def queryset(self, request, queryset):
	
        if(self.value() == "MT"):
            stds_mgmt = queryset.exclude(branch='Computer Science & Engineering' ).exclude(branch='Information Technology' ).exclude(agg_10th_percntge='<50%').exclude(agg_12th_percntge='<50%').exclude(agg_BE_percntge='<50%')
            queryset = stds_mgmt
        elif(self.value() == "AS"):
            stds_associate = queryset.filter(branch='Computer Science & Engineering').exclude(agg_10th_percntge='>50%').exclude(agg_10th_percntge='<50%').exclude(agg_12th_percntge='>50%').exclude(agg_12th_percntge='<50%').exclude(agg_BE_percntge='>50%').exclude(agg_BE_percntge='<50%')
            queryset = stds_associate
#        print stds_associate

        return queryset


class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    actions = [send_email_to]
    list_display = ('first_name','branch','passing_yr', 'agg_10th_percntge', 'agg_12th_percntge', 'agg_BE_percntge', )
    list_filter = (MGTListFilter,'branch','passing_yr', 'agg_10th_percntge', 'agg_12th_percntge', 'agg_BE_percntge',  )
    pass





admin.site.register(Student,StudentAdmin)


# Register your models here.
