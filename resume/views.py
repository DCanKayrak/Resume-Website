from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Header,Project,SocialMedia,Certificate,Education,Skill,OtherSkill,WorkExperience
# Create your views here. from .models import Header,Project,SocialMedia,Certificate,Education,Skill
def index(request):

    header = Header.objects.get()
    projects = Project.objects.all()
    socialMedia = SocialMedia.objects.get()
    certificates = Certificate.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    otherSkill = OtherSkill.objects.all()
    workExperience = WorkExperience.objects.all()

    context = {
        "header": header,
        "projects":projects,
        "socialMedia":socialMedia,
        "certificates":certificates,
        "educations":educations,
        "skills":skills,
        "otherSkills":otherSkill,
        "workExperiences":workExperience
    }

    return render(request,'index.html',context)

def detail(request,id):
    project = Project.objects.get(id=id)
    header = Header.objects.get()
    socialMedia = SocialMedia.objects.get()

    template = loader.get_template('details.html')
    context = {
    'project': project,
    'header':header,
    "socialMedia":socialMedia,
    }
    return HttpResponse(template.render(context, request))
