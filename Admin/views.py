from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Student, Course, Level, Module, Content, Lecturer
from .forms import StudentCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.views.generic.list import ListView
from .forms import CourseCreationForm, ProfileCreationForm, ProfileCreationForm2
from django.views.generic import View, TemplateView
from django.forms.models import modelform_factory
from django.apps import apps
from django.views.generic.base import TemplateResponseMixin, View
from .forms import ModuleFormSet
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView


# ---------------------Authentication views-------------------------------


@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,  password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin')
            else:
                return redirect('student')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'registration/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def register(request):
    form = StudentCreationForm()
    if request.method == 'POST':

        form = StudentCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            group = Group.objects.get(name='Student')

            user.groups.add(group)

            Student.objects.create(
                user=user,
                name=username,
                email=email
            )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/SignUpPage.html', context)


# ------------------general Views-----------------------


def home(request):
    return render(request, 'Admin/Templates/General/general.html')


def courses(request):
    return render(request, 'General/courses.html')


def cert(request):
    return render(request, 'General/certificateLevel.html')


def op(request):
    return render(request, 'General/operational_level.html')


def mgt(request):
    return render(request, 'General/managementlevel.html')


def strat(request):
    return render(request, 'General/strategic_level.html')


# ------------------Admin Views----------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def admin(request):
    return render(request, 'admin/admin.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def view_courses(request):
    user = request.user
    courses = Course.objects.filter(lecturer=user.lecturer)
    context = {'courses': courses}
    return render(request, 'admin/view_courses.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def update_course(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseCreationForm(instance=course)

    if request.method == 'POST':
        form = CourseCreationForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('v_courses')

    context = {'form': form}
    return render(request, 'admin/create_course.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def delete_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == "POST":
        course.delete()
        return redirect('v_courses')
    context = {'course': course}
    return render(request, 'admin/delete_courses.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def content(request):
    return render(request, 'admin/content.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def drop_lectures(request):
    return render(request, 'admin/Drop Lectures.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def lecture_notes(request):
    user = request.user
    courses = Course.objects.filter(lecturer=user.lecturer)
    level1 = courses.filter(level=1)
    level2 = courses.filter(level=2)
    level3 = courses.filter(level=3)
    level4 = courses.filter(level=4)
    context = {'course': courses,
               'level1': level1,
               'level2': level2,
               'level3': level3,
               'level4': level4}
    return render(request, 'admin/lecture_notes.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def student_profile(request):
    users = request.user
    lecturer = Lecturer.objects.get(user=users)
    students = Student.objects.filter(lecturer=lecturer.id).order_by('id')
    return render(request, 'admin/stdprofile.html', {'students': students})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def student_details(request):
    return render(request, 'admin/Student Details.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def student_edit(request):
    levels = Level.objects.all()
    return render(request, 'admin/StuEdit.html', {'levels': levels})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def create_course(request):
    form = CourseCreationForm()
    if request.method == 'POST':
        form = CourseCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('v_courses')

    context = {'form': form}
    return render(request, 'admin/create_course.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def load_course(request):
    levels_get = request.GET.get('level')
    user = Level.objects.get(level=levels_get)
    course = Course.objects.filter(level_id=user).order_by('name')
    d = {'course': course}
    return render(request, 'admin/course_dropdown.html', d)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def stud_data(request):
    levels_get = request.GET.get('level')
    user = Level.objects.get(level=levels_get)
    students = Student.objects.filter(level=user)
    d = {'students': students}
    return render(request, 'admin/studentdata.html', d)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def course_modules_1(request):
    user = request.user
    courses = Course.objects.filter(lecturer=user.lecturer)
    level1 = courses.filter(level=1)
    level2 = courses.filter(level=2)
    level3 = courses.filter(level=3)
    level4 = courses.filter(level=4)
    context = {'course': courses,
               'level1': level1,
               'level2': level2,
               'level3': level3,
               'level4': level4}
    return render(request, 'admin/view_modules.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Lecturer'])
def course_modules_2(request, course_id):
    modules = Module.objects.filter(course_id=course_id)
    courses = Course.objects.get(id=course_id)
    context = {'modules': modules,
               'course': courses}
    return render(request, 'admin/view_modules_2.html', context)


# -----------------------Student views---------------------


@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def student_form(post):
    return render(post, 'Student/form.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def std_lectures(request):
    return render(request, 'Student/student_my_lectures.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def student(request):
    obj = get_object_or_404(Student, user=request.user)
    std = Student.objects.get(user=request.user)
    form = ProfileCreationForm()
    form1 = ProfileCreationForm2()
    if std.lecturer is None:
        if request.method == "POST":
            form = ProfileCreationForm2(data=request.POST, instance=request.user)
            form2 = ProfileCreationForm(data=request.POST or None, instance=obj)
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
                update = form.save(commit=False)
                update.user = request.user
                update.save()
                return redirect('profilepage')

        user = request.user
        student = Student.objects.get(user=user)
        context = {'student': student,
                    'form': form,
                    'form1': form1
                    }
        return render(request, 'Student/profile.html', context)
    else:
        return redirect('profilepage')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def students_profile(request):
    user = request.user
    student_det = Student.objects.get(user=request.user)
    context = {'student': student_det,
                 'user': user
                 }
    return render(request, 'Student/profilepage.html', context)


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'Student/student_dashboard.html'

    def get_queryset(self):
        student = Student.objects.get(user=self.request.user)
        level = student.level
        qs = super(StudentCourseListView, self).get_queryset()
        return qs.filter(level=level)


class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'Student/detail.html'

    def get_queryset(self):
        student = Student.objects.get(user=self.request.user)
        level = student.level
        qs = super(StudentCourseDetailView, self).get_queryset()
        return qs.filter(level=level)

    def get_context_data(self, **kwargs):
        context = super(StudentCourseDetailView,
                        self).get_context_data(**kwargs)
        # get course object
        course = Course.objects.get(id=self.kwargs["pk"])
        modules = Module.objects.filter(course=course.id)
        if 'module_id' in self.kwargs:
            # get current module
            context['modules'] = Module.objects.get(
                                    id=self.kwargs['module_id'])
        else:
            # get first module
            context['module'] = modules
        return context




# ------------------Content Management--------------------------


class ManageCourseListView(ListView):
    model = Course
    template_name = 'admin/manage/content_list.html'

    def get_queryset(self):
        qs = super(ManageCourseListView, self).get_queryset()
        return qs.filter(owner=self.request.user.lecturer)


class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'admin/manage/module_form.html'
    course = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course,
                             data=data)

    def dispatch(self, request, pk):
        user = request.user
        self.course = get_object_or_404(Course,
                                        id=pk,
                                        lecturer=user.lecturer)
        return super(CourseModuleUpdateView,
                     self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'course': self.course,
                                        'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('addNotes')
        return self.render_to_response({'course': self.course,
                                        'formset': formset})


class ContentCreateUpdateView(TemplateResponseMixin, View):
    module = None
    model = None
    obj = None
    template_name = 'admin/manage/content_form.html'

    def get_model(self, model_name):
        if model_name in ['video', 'image', 'file']:
            return apps.get_model(app_label='Admin', model_name=model_name)
        return None

    def get_form(self, model, *args, **kwargs):
        form = modelform_factory(model, exclude=['owner', 'order', 'created', 'updated', 'lecturer'])
        return form(*args, **kwargs)

    def dispatch(self, request, module_id, model_name, id=None):
        m_id = module_id
        crs_id = Module.objects.get(id=m_id)
        courses = Course.objects.get(id=crs_id.course_id)        
        self.module = get_object_or_404(Module, id=m_id, course=courses)
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model, id=id, lec=request.user.lecturer)
        return super(ContentCreateUpdateView, self).dispatch(request, m_id, model_name, id)

    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({'form': form,
                                        'object': self.obj})

    def post(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model,
                             instance=self.obj,
                             data=request.POST,
                             files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user.lecturer
            obj.save()
            if not id:
                # new content
                Content.objects.create(module=self.module,
                                       item=obj)
            return redirect('module_content_list', self.module.id)

        return self.render_to_response({'form': form,
                                        'object': self.obj})


class ContentDeleteView(View):
    def post(self, request, id):
        contents = Content.objects.get(id=id)
        modules = Module.objects.get(id=contents.module_id)
        content = get_object_or_404(Content,
                               id=id,
                               module=modules)
        module = content.module
        content.item.delete()
        content.delete()
        return redirect('module_content_list', module.id)


class ModuleContentListView(TemplateResponseMixin, View):
    template_name = 'admin/manage/content_list.html'

    def get(self, request, module_id):
        m_id = module_id
        crs_id = Module.objects.get(id=m_id)
        crs = Module.objects.filter(course_id=crs_id.course_id)
        module = get_object_or_404(Module,
                                   id=m_id)

        return self.render_to_response({'module': module,
                                        'crs': crs})


