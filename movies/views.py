from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Theater, Seat, Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError, transaction

def movie_list(request):
    search_query = request.GET.get('search')
    if search_query:
        movies = Movie.objects.filter(name__icontains=search_query)
    else:
        movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def theater_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    theaters = Theater.objects.filter(movie=movie)
    return render(request, 'movies/theater_list.html', {'movie': movie, 'theaters': theaters})

@login_required(login_url='login')
def book_seats(request, theater_id):
    theater = get_object_or_404(Theater, id=theater_id)
    seats = Seat.objects.filter(theater=theater)

    # Auto-generate default seats if theater has no seats configured
    if not seats.exists():
        rows = ['A', 'B', 'C']
        created_seats = []
        for row in rows:
            for i in range(1, 11):
                created_seats.append(Seat(theater=theater, seat_number=f"{row}{i}"))
        Seat.objects.bulk_create(created_seats)
        seats = Seat.objects.filter(theater=theater)

    if request.method == 'POST':
        selected_seat_ids = request.POST.getlist('seats')
        if not selected_seat_ids:
            return render(request, "movies/seat_selection.html", {
                'theater': theater,
                'seats': seats,
                'error': "Please select at least one seat before proceeding."
            })

        error_seats = []
        booked_count = 0
        with transaction.atomic():
            for seat_id in selected_seat_ids:
                seat = get_object_or_404(Seat, id=seat_id, theater=theater)
                if seat.is_booked:
                    error_seats.append(seat.seat_number)
                    continue
                try:
                    Booking.objects.create(
                        user=request.user,
                        seat=seat,
                        movie=theater.movie,
                        theater=theater,
                        price=theater.price,
                        status='BOOKED'
                    )
                    seat.is_booked = True
                    seat.save()
                    booked_count += 1
                except IntegrityError:
                    error_seats.append(seat.seat_number)

        if error_seats:
            error_message = f"The following seats could not be booked: {', '.join(error_seats)}"
            return render(request, 'movies/seat_selection.html', {
                'theater': theater,
                'seats': seats,
                'error': error_message
            })

        messages.success(request, f"Successfully booked {booked_count} ticket(s)!")
        return redirect('profile')

    return render(request, 'movies/seat_selection.html', {'theater': theater, 'seats': seats})

@login_required(login_url='login')
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status == 'BOOKED':
        with transaction.atomic():
            booking.status = 'CANCELLED'
            booking.save()
            seat = booking.seat
            seat.is_booked = False
            seat.save()
        messages.success(request, f"Booking for seat {booking.seat.seat_number} has been cancelled successfully.")
    else:
        messages.warning(request, "This booking is already cancelled.")
    return redirect('profile')





