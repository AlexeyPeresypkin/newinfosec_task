from django.shortcuts import redirect


class IsAuthorMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().owner:
            return redirect("index")
        return super().dispatch(request, *args, **kwargs)
