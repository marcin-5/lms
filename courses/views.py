from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from . import models
from .permissions import OwnerRequiredMixin


class CoursesListView(ListView):
    model = models.Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = models.Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'


class CourseUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = models.Course
    fields = ('title', 'slug', 'subject', 'overview')
    template_name = 'courses/course_create.html'
    login_url = reverse_lazy('users:login')

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse('courses:course-detail', kwargs={'pk': pk})


class CourseDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = models.Course
    template_name = 'courses/course_delete.html'
    context_object_name = 'course'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('courses:course-list')


class CourseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Course
    fields = ('title', 'slug', 'subject', 'overview', 'course_image')
    template_name = 'courses/course_create.html'
    success_url = reverse_lazy('courses:course-list')
    login_url = reverse_lazy('users:login')
    permission_required = 'courses.add_course'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
