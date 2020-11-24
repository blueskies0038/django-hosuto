from django import forms
from django_countries.fields import CountryField
from .models import *

class SearchForm(forms.Form):
    city = forms.CharField(required=False, initial="Anywhere")
    country = CountryField(default="US").formfield()
    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=RoomType.objects.all()
    )
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

class CreatePhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ("caption", "file",)

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        room = Room.objects.get(pk=pk)
        photo.room = room
        photo.save()

class CreateRoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ("name", "description", "country", "city", "price", "address", "guests", "beds", "bedrooms", "baths", "check_in",
                  "check_out", "instant_book", "room_type", "amenities", "facilities", "house_rules")
        widgets = {'amenities': forms.CheckboxSelectMultiple,
                   'facilities': forms.CheckboxSelectMultiple,
                   'house_rules': forms.CheckboxSelectMultiple}
    
    def save(self, *args, **kwargs):
        room = super().save(commit=False)
        return room