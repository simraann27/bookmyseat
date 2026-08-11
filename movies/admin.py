from django.contrib import admin
from .models import Movie, Theater, Seat, Booking

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rating', 'cast', 'description']
    search_fields = ['name', 'cast']

@admin.action(description='Generate 30 default seats (A1-A10, B1-B10, C1-C10)')
def generate_seats(modeladmin, request, queryset):
    rows = ['A', 'B', 'C']
    for theater in queryset:
        for row in rows:
            for i in range(1, 11):
                seat_num = f"{row}{i}"
                Seat.objects.get_or_create(theater=theater, seat_number=seat_num)
    modeladmin.message_user(request, "Seats generated successfully.")

@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'movie', 'time', 'price']
    list_filter = ['movie', 'time']
    search_fields = ['name', 'movie__name']
    actions = [generate_seats]

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['id', 'theater', 'seat_number', 'is_booked']
    list_filter = ['theater', 'is_booked']
    search_fields = ['seat_number', 'theater__name']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'seat', 'movie', 'theater', 'price', 'status', 'booked_at']
    list_filter = ['status', 'theater', 'booked_at']
    search_fields = ['user__username', 'seat__seat_number', 'movie__name']
