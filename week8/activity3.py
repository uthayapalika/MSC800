from abc import ABC, abstractmethod


# ==========================================
# 1. ABSTRACT PRODUCTS
# ==========================================

class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class Checkbox(ABC):

    @abstractmethod
    def check(self):
        pass


# ==========================================
# 2. CONCRETE PRODUCTS - WINDOWS
# ==========================================

class WindowsButton(Button):

    def click(self):
        print("Windows Button clicked")


class WindowsCheckbox(Checkbox):

    def check(self):
        print("Windows Checkbox checked")


# ==========================================
# 3. CONCRETE PRODUCTS - MAC
# ==========================================

class MacButton(Button):

    def click(self):
        print("Mac Button clicked")


class MacCheckbox(Checkbox):

    def check(self):
        print("Mac Checkbox checked")


# ==========================================
# 4. ABSTRACT FACTORY
# ==========================================

class GUIFactory(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# ==========================================
# 5. CONCRETE FACTORY - WINDOWS
# ==========================================

class WindowsFactory(GUIFactory):

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


# ==========================================
# 6. CONCRETE FACTORY - MAC
# ==========================================

class MacFactory(GUIFactory):

    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


# ==========================================
# 7. CLIENT
# ==========================================

factory = WindowsFactory()

button = factory.create_button()
checkbox = factory.create_checkbox()

button.click()
checkbox.check()