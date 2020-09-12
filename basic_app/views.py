from django.shortcuts import render
from django.views.generic import  View,TemplateView, ListView, DetailView
from . import models
# Create your views here.


#def index(request):
#    return render(request,'basic_app/index.html')

# new type of view using classes
'''
#This is a very good method to get the view working (there is not need to get the paths and other methods)
class IndexView(TemplateView):
    #Call the template name in the class (make sure to add the folder if its insdie one)
    template_name = 'basic_app/index.html'

    #Here you can create the function to get the data added to the to the tempalte html (make sure to add the {{ 'name' }} in the html)
    #Below I added injectme in the html so I added it to the contect below
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION !!!!!'
        return context
'''
class IndexView(TemplateView):
    template_name = 'basic_app/index.html'


class SchoolListView(ListView):
    #context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school_list.html'

class SchoolDeailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_details.html'



