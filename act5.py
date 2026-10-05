class MarketTrip:
    def __init__(self, student, wallet):
        self.student = student
        self.wallet = wallet
        self._entries = []

    def buy(self, choice):
        cost = choice.price()

        if cost < 0 or cost > self.wallet.remaining:
            return False

        self.wallet.remaining -= cost

        self._entries.append({
            "choice": choice,
            "cost": cost
        })

        return True

    def summary(self):
        return {
            "student": self.student,
            "remaining": self.wallet.remaining,
            "completed_count": len(self._entries),
            "choices": [
                entry["choice"].name
                for entry in self._entries
            ]
        }