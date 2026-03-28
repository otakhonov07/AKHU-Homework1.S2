class TimeDuration:
    def __init__(self, hours, minutes):
        total_minutes = hours * 60 + minutes
        self.hours = hours + minutes//60
        self.hours = total_minutes // 60
        self.minutes = minutes

    def __str__(self):
        return f"{self.hours}h {self.minutes}m"

    def __repr__(self):
        return f"TimeDuration({self.hours}, {self.minutes})"

    def __add__(self, other):
        if isinstance(other, TimeDuration):
            total_minutes = (self.hours * 60 + self.minutes) + \
                            (other.hours * 60 + other.minutes)
            return TimeDuration(0, total_minutes)

        elif isinstance(other, int) or isinstance(other, float):
            total_minutes = self.hours * 60 + self.minutes + other
            return TimeDuration(0, total_minutes)

        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, TimeDuration):
            return self.hours == other.hours and self.minutes == other.minutes
        return NotImplemented

    def __bool__(self):
        return (self.hours * 60 + self.minutes) > 0