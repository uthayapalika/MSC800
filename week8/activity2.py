from abc import ABC, abstractmethod

# ==========================================
# 1. ABSTRACT PRODUCT
# ==========================================
class Notification(ABC):

    @abstractmethod
    def send(self):
        pass


# ==========================================
# 2. CONCRETE PRODUCTS
# ==========================================
class Email(Notification):
    def send(self):
        print("Sending Email notification!")


class SMS(Notification):
    def send(self):
        print("Sending SMS notification!")


class Push(Notification):
    def send(self):
        print("Sending Push notification!")


# ==========================================
# 3. ABSTRACT FACTORY / CREATOR
# ==========================================
class NotificationFactory(ABC):

    @abstractmethod
    def create_notification(self):
        pass


# ==========================================
# 4. CONCRETE FACTORIES
# ==========================================
class EmailFactory(NotificationFactory):

    def create_notification(self):
        return Email()


class SMSFactory(NotificationFactory):

    def create_notification(self):
        return SMS()


class PushFactory(NotificationFactory):

    def create_notification(self):
        return Push()


# ==========================================
# 5. CLIENT
# ==========================================

factory = EmailFactory()

notification = factory.create_notification()

notification.send()