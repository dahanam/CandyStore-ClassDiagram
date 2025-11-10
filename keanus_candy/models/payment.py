class PaymentMethod:
    """Base class for payment types."""
    
    def __init__(self, method_name: str):
        self.method_name = method_name

    def process_payment(self, amount: float) -> bool:
        """Abstract method to process payments."""
        raise NotImplementedError
        # new method implemented by Dahana Moz Ruiz
    def validate_payment_info(self) -> bool:
    """Basic validation method to be overridden by subclasses."""
    raise NotImplementedError

class CreditCard(PaymentMethod):
    """Implements credit card payment."""
    
    def __init__(self, card_number: str, holder_name: str):
        super().__init__("Credit Card")
        self.card_number = card_number
        self.holder_name = holder_name

    def process_payment(self, amount: float) -> bool:
        """Process a credit card payment."""
        print(f"Charging ${amount:.2f} to card {self.card_number[-4:]}...")
        return True


class PayPal(PaymentMethod):
    """Implements PayPal payment."""
    
    def __init__(self, email: str):
        super().__init__("PayPal")
        self.email = email
# this method was modified by Dahana Moz Ruiz
    def process_payment(self, amount: float) -> bool:
    """Process a PayPal payment."""
    if not self.validate_payment_info():
        print("Invalid PayPal account.")
        return False
    print(f"Processing PayPal payment of ${amount:.2f} from {self.email}...")
    return True
