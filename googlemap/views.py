from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponseRedirect
from googlemap.forms import GoogleMapForm
from googlemap.models import GoogleMapModel

class GoogleMapView(View):
    form_class = GoogleMapForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            map_obj = GoogleMapModel()
            response = map_obj.save_data(form.cleaned_data)
            if response:
                return HttpResponseRedirect('/success/')
            else:
                form.add_error('url', 'Something went wrong')
        return render(request, self.template_name, {'form': form})


class GoogleMapShowView(View):

    def get(self, request, *args, **kwargs):
        gmap_obj = GoogleMapModel.objects.all()
        marker_list = []
        for marker in gmap_obj:
            transform = marker.location
            marker_list.append([transform.x, transform.y])
        return render(request, 'googlemap.html', {'marker_list': marker_list})
