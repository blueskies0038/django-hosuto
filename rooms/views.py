from django.shortcuts import render, redirect, reverse
from django.http import Http404
from django.views.generic import ListView, DetailView, UpdateView, FormView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from .forms import *
from users import mixins as users_mixins

class HomeView(ListView):
    model = Room
    paginate_by = 12
    paginate_orphans = 3
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    model = Room


def search(request):

    city = request.GET.get("city")

    if not city:
        form = SearchForm(request.GET)
        if form.is_valid():
            city = form.cleaned_data.get("city")
            country = form.cleaned_data.get("country")
            room_type = form.cleaned_data.get("room_type")
            price = form.cleaned_data.get("price")
            guests = form.cleaned_data.get("guests")
            bedrooms = form.cleaned_data.get("bedrooms")
            beds = form.cleaned_data.get("beds")
            baths = form.cleaned_data.get("baths")


            filter_args = {}

            if city != "Anywhere":
                filter_args["city__startswith"] = city

            if country != "Anywhere":
                filter_args["country"] = country

            if room_type is not None:
                filter_args["room_type"] = room_type

            if price is not None:
                filter_args["price__lte"] = price

            if guests is not None:
                filter_args["guests__gte"] = guests

            if bedrooms is not None:
                filter_args["bedrooms__gte"] = bedrooms

            if beds is not None:
                filter_args["beds__gte"] = beds

            if baths is not None:
                filter_args["baths__gte"] = baths

            qset = Room.objects.filter(**filter_args).order_by("-created")
            paginator = Paginator(qset, 6, orphans=3)
            page = request.GET.get("page", 1)
            rooms = paginator.get_page(page)

            return render(request, "rooms/search.html", {"form": form, "rooms": rooms,})
        
        return render(request, "rooms/search.html", {"form": form,})

    else:
        filter_args = {}
        filter_args["city__startswith"] = city

        qset = Room.objects.filter(**filter_args).order_by("-created")
        paginator = Paginator(qset, 6, orphans=3)
        page = request.GET.get("page", 1)
        rooms = paginator.get_page(page)

        form = SearchForm()

        return render(request, "rooms/search.html", {"form": form, "rooms": rooms,})


class EditRoomView(users_mixins.LoggedInOnlyView, UpdateView):
    model = Room
    template_name = "rooms/room_edit.html"
    fields = ("name", "description", "country", "city", "price", "address", "guests", "beds", "bedrooms", "baths", "check_in",
              "check_out", "instant_book", "room_type", "amenities", "facilities", "house_rules",)

    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.host.pk != self.request.user.pk:
            raise Http404("Nothing found...")
        return room


class RoomPhotosView(users_mixins.LoggedInOnlyView, DetailView):
    model = Room
    template_name="rooms/room_photos.html"

    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.host.pk != self.request.user.pk:
            raise Http404("Nothing found...")
        return room

@login_required
def delete_photo(request, room_pk, photo_pk):
    user = request.user
    try:
        room = Room.objects.get(pk=room_pk)
        if room.host.pk != user.pk:
            messages.error(request, "Can't delete photo")
        else:
            Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, "Photo Deleted")
        return redirect(reverse("rooms:photos", kwargs={'pk': room_pk}))
    except:
        return redirect(reverse("core:home"))

class EditPhotoView(users_mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):
    model = Photo
    template_name = "rooms/photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "Photo Updated"
    fields = "caption"
    
    def get_success_url(self):
        room_pk = self.kwargs.get("room_pk")
        messages.success
        return reverse("rooms:photos", kwargs={"pk": room_pk})

class AddPhotoView(users_mixins.LoggedInOnlyView, FormView):
    model = Photo
    template_name = "rooms/photo_create.html"
    fields = ("caption", "file",)
    form_class = CreatePhotoForm

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        messages.success(self.request, "Photo Uploaded")
        return redirect(reverse("rooms:photos", kwargs={"pk": pk}))

class CreateRoom(users_mixins.LoggedInOnlyView, FormView):
    form_class = CreateRoomForm
    template_name = "rooms/room_create.html"

    def form_valid(self, form):
        room = form.save()
        room.host = self.request.user
        room.save()
        form.save_m2m()
        messages.success(self.request, "Room Created")
        return redirect(reverse("rooms:detail", kwargs={"pk": room.pk}))
