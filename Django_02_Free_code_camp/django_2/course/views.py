# Django class-based views (when you subclass View), you can define methods for any HTTP verb that you want to handle:
#
# get(self, request, *args, **kwargs) → handles GET requests
# post(self, request, *args, **kwargs) → handles POST requests
# put(self, request, *args, **kwargs) → handles PUT requests
# patch(self, request, *args, **kwargs) → handles PATCH requests
# delete(self, request, *args, **kwargs) → handles DELETE requests
# head(self, request, *args, **kwargs) → handles HEAD requests
# options(self, request, *args, **kwargs) → handles OPTIONS requests
# trace(self, request, *args, **kwargs) → handles TRACE requests

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .form import CourseModelForm
from .models import Course

class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj

class CourseDeleteView(CourseObjectMixin, View):
    template_name = "course/course_delete.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/course/')
        return render(request, self.template_name, context)


class CourseUpdateView(CourseObjectMixin, View):
    template_name = "course/course_update.html" # DetailView
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        print('get')
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        print('post')
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)



class CourseCreateView(View):
    template_name = 'course/course_create.html'
    def get(self, request):
        form = CourseModelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        return render(request, self.template_name, {'form': form})


class CourseListView(View):
    template_name = 'course/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

class ActiveListView(CourseListView):
    queryset = Course.objects.filter(active=True)

class CourseView(View):
    template_name = 'course/course_details.html'

    def get(self, request, id = None):
        return render(request, self.template_name)

    # def post(self, request):
    #     return render(request, self.template_name)


def course_view(request, *args, **keywords):
    return render(request, 'course/course_details.html', locals())