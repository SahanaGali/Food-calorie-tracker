from django import forms
from foodapp.models import food,track

class foodform(forms.ModelForm):
    class Meta:
        model = food
        fields = "__all__"

class editform(forms.ModelForm):
    class Meta:
        model=track
        fields = "__all__"