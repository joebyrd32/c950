
# This class is just a simple time class to keep the hours and minutes.
class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def add_minutes(self, minutes):
        self.minute += minutes
        if self.minute >= 60:
            self.hour = self.hour + (self.minute // 60)
            self.minute = self.minute % 60

    def __str__(self):
        return str(int(self.hour)) + ":" + str(int(self.minute)).zfill(2)

    def __eq__(self, other):
        if self.hour == other.hour and self.minute == other.minute:
            return True
        return False

    def __lt__(self, other):
        if int(self.hour) < int(other.hour):
            return True
        elif int(self.hour) > int(other.hour):
            return False
        elif int(self.minute) < int(other.minute):
            return True
        return False

    def __gt__(self, other):
        if int(self.hour) < int(other.hour):
            return False
        elif int(self.hour) > int(other.hour):
            return True
        elif int(self.minute) < int(other.minute):
            return False
        return True

    def __ge__(self, other):
        if self.hour == other.hour and self.minute == other.minute:
            return True
        elif int(self.hour) < int(other.hour):
            return False
        elif int(self.hour) > int(other.hour):
            return True
        elif int(self.minute) < int(other.minute):
            return False
        return True
