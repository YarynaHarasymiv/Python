from abc import ABC, abstractmethod


class NetworkPrinter(ABC):
    @abstractmethod
    def printer(self):
        pass

class NetworkScaner(ABC):
    @abstractmethod
    def scaner(self):
        pass

class NetworkCopy(ABC):
    @abstractmethod
    def copy(self):
        pass


class Printer(NetworkPrinter):
    def printer(self):
        print("You can print...")

class Scanner(NetworkScaner, NetworkCopy):
    def copy(self):
        print("We are copying...waite a few minutes...")
    def scaner(self):
        print("You can scanning..")

print_try = Printer()
scan = Scanner()

print_try.printer()
scan.copy()
scan.scaner()