from tools.travel_info_generator import get_flights
from tools.hotel_picker import suggest_hotels

class BookingAgent:
    def book_trip(self, destination):
        flights = get_flights(destination)
        hotels = suggest_hotels(destination)
        return {
            'flight': flights[0],
            'hotel': hotels[0]
        } 