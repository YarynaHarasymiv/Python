from abc import ABC, abstractmethod


class Send(ABC):
    @abstractmethod
    def sent_text(self, text):
        pass


class SendEmail(Send):
    def sent_text(self, text):
        print(f"Your text: '{input(f"You should wright a tex for email: {text} :")}' send on your email: {text}")

class SendSms(Send):
    def sent_text(self, text):
        print(f"Your sms containing a text: {text}")


class Analysis:
    def __init__(self, sender: Send):
        self.sender = sender

    def analyze_and_send(self, text):
        self.sender.sent_text(text)

send_sms = SendSms()
send_email = SendEmail()


analysis = Analysis(send_sms)
analysis.analyze_and_send(input("You need to write a text for sms..."))
print("Sms sending...")

analysis = Analysis(send_email)
analysis.analyze_and_send(input("You need to write an email..."))



