from abc import ABC, abstractmethod

class Member(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def monthly_fee(self):
        pass

class Basic(Member):
    def monthly_fee(self):
        return 200_000

class Premium(Member):
    def monthly_fee(self):
        return 500_000

class Vip(Member):
    def monthly_fee(self):
        return 1_000_000

class Storage(ABC):

    @abstractmethod
    def save(self, members):
        pass

class FileStorage(Storage):

    def save(self, members):
        for member in members:
            print(f"[FILE] {member.name},{member.monthly_fee()}")

class Notifier(ABC):

    @abstractmethod
    def notify(self, members):
        pass

class EmailNotifier(Notifier):

    def notify(self, members):
        for member in members:
            print(
                f"[EMAIL → {member.name}] "
                f"Your fee: {member.monthly_fee()} $"
            )

class GymManager:

    def __init__(self):
        self.members = []

    def add(self, member):
        self.members.append(member)

    def run(self, storage, notifier):
        storage.save(self.members)
        notifier.notify(self.members)

gym = GymManager()

gym.add(Basic("Frodo"))
gym.add(Premium("Aragorn"))
gym.add(Vip("Legolas"))

gym.run(FileStorage(), EmailNotifier())