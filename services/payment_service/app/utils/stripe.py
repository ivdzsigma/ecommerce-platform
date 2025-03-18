# services/payment_service/app/utils/stripe.py
import stripe

stripe.api_key = "sk_test_XXXXXXXXXXXXXXXX"

def create_payment_intent(amount: int, currency: str = "usd"):
    return stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
    )