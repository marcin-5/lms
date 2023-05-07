from django.contrib.auth.mixins import AccessMixin


class OwnerRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        course = self.get_queryset().get(pk=kwargs.get('pk'))
        if request.user != course.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
