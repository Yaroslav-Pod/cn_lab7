class Calculator:
    def add(self, a, b):
        """Метод додавання."""
        return a + b

    def subtract(self, a, b):
        """Метод віднімання."""
        return a - b

    def multiply(self, a, b):
        """Метод множення."""
        return a * b

    def divide(self, a, b):
        """Метод ділення з перевіркою на нуль."""
        if b == 0:
            raise ValueError("На нуль ділити не можна!")
        return a / b