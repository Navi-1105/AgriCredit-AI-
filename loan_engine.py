# loan_engine.py

def get_credit_advice(land_size, rainfall, crop_price):
    # Basic rules for loan eligibility based on input parameters
    loan_amount = 0
    interest_rate = 0
    repayment_period = 0

    # Loan eligibility criteria (simplified example)
    if land_size < 1:
        return "Loan not eligible. Land size too small."
    elif rainfall < 50:
        return "Loan recommendation: Low rainfall, caution advised."
    elif crop_price < 2500:
        return "Loan recommendation: Crop price is low. Consider alternative crops."
    else:
        # Calculate loan amount based on land size and crop price
        loan_amount = land_size * 10000  # ₹10,000 per acre
        interest_rate = 8  # Assume 8% annual interest
        repayment_period = 5  # 5 years repayment period

        return (f"Loan eligible: ₹{loan_amount} loan approved for {land_size} acres. "
                f"Interest rate: {interest_rate}% per annum. Repayment period: {repayment_period} years.")
# This function can be expanded with more complex logic and data sources as needed.

