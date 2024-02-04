def sip_calculator(sip_amount, rate_of_interest, num_of_years):
    # Convert rate of interest to a decimal
    rate_of_interest_decimal = rate_of_interest / 100.0

    # Monthly interest rate
    monthly_interest_rate = rate_of_interest_decimal / 12

    # Initialize wealth for each year
    wealth_per_year = []

    for year in range(1, num_of_years + 1):
        # Total number of SIPs for the current year
        total_sips = year * 12

        # Calculate future value for the current year using the formula for compound interest
        future_value = sip_amount * (((1 + monthly_interest_rate)**total_sips - 1) / monthly_interest_rate) * (1 + monthly_interest_rate)

        # Append the wealth for the current year to the list
        wealth_per_year.append(future_value)

    return wealth_per_year

def main():
    # Get user inputs
    sip_amount = float(input("Enter SIP amount per month: "))
    rate_of_interest = float(input("Enter annual rate of interest (%): "))
    num_of_years = int(input("Enter number of years: "))

    # Calculate wealth for each year
    wealth_per_year = sip_calculator(sip_amount, rate_of_interest, num_of_years)

    # Display the wealth for each year
    print("\nWealth at the end of each year:")
    for year, wealth in enumerate(wealth_per_year, start=1):
        print(f"Year {year}: $ {wealth:.2f}")

if __name__ == "__main__":
    main()
