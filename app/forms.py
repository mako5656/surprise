from django import forms
from .models import Item
class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ("shop_name","urls","address","genre_name","genre_catch","catch","image_url","insta_tag_name","budget","budget_str","area","area_str","map_shop","map_station","good")
        widgets = {
            "shop_name": forms.TextInput(attrs={'placeholder':'記入例：カフェ Surprise'}),
            "urls": forms.TextInput(),
            "address":  forms.TextInput(),
            "genre_name":  forms.TextInput(),
            "genre_catch":  forms.TextInput(),
            "catch":  forms.TextInput(),
            "image_url": forms.TextInput(),
            "insta_tag_name":  forms.TextInput(),
            "budget":  forms.RadioSelect(),
            "budget_str":  forms.TextInput(),
            "area":  forms.RadioSelect(),
            "area_str":  forms.TextInput(),
            "map_shop" : forms.TextInput(),
            "map_station" : forms.TextInput(),
            "good":  forms.NumberInput(),
        }