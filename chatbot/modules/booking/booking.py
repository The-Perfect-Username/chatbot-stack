from booking_data import dates
import datetime
class Booking:

    def __init__(self):
        self.datetime = datetime.datetime
        self.dates = dates

    def slot_is_available(self, chosen_date, chosen_time):
        try:
            breakout = False

            date = self.dates[chosen_date]

            if date['times'][chosen_time] is None:
                return True
            else:
                breakout = True
                return False
        except KeyError:
            return "Unable to book that day"

    def book_user_into_slot(self, user, date, time):
        if self.dates[date] is None:
            return "Unable to book that day"

        if self.dates[date]['times'][time] is None:
            self.dates[date]['times'][time] = user
            return True

        return "That time is already booked by someone"


    def make_booking(self):
        user = {
            "name": "Lachlan Enderlin",
            "order": {
                "type": "table",
                "number_of_seats": 5
            }
        }

        chosen_date = "2018-02-05"
        chosen_time = "1100"

        is_available = self.slot_is_available(chosen_date, chosen_time)

        if is_available:
            booked = self.book_user_into_slot(user, chosen_date, chosen_time)
            if not booked:
                return "That slot was just taken"
            return booked
        return "This date and time are not available"

Booking = Booking()
