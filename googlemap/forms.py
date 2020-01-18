from django import forms
from urllib.parse import parse_qs, urlparse
from django.contrib.gis.geos import GEOSGeometry

class GoogleMapForm(forms.Form):
   url = forms.URLField(label='URL', required=True)

   def clean(self):
        data = self.cleaned_data
        if bool(data):
            url = urlparse(data['url'])
            extract_url = parse_qs(url.query)
            
            if not extract_url.get('latitude') or not extract_url.get('longitude'):
                raise forms.ValidationError(
                            "URL must have latitude and longitude params."
                        )
            try:
                data['location'] = GEOSGeometry(
                                            'POINT('+extract_url.get('latitude')[0]+' \
                                            '+extract_url.get('longitude')[0]+')'
                                           )
            except Exception as e:
                raise forms.ValidationError(
                                "Given latitude or longitude was in wrong format."
                            )
        return data
