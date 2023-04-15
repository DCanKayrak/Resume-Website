from django.contrib import admin
from .models import Header,Project,SocialMedia,Certificate,Education,Skill,OtherSkill,WorkExperience

# Register your models here.
admin.site.register(Header)
admin.site.register(Project)
admin.site.register(SocialMedia)
admin.site.register(Certificate)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(OtherSkill)
admin.site.register(WorkExperience)
