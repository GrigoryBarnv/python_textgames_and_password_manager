from requests import get
BASE_URL = "https://api.frankfurter.dev/v2"


def get_currencies_with_rates(base_currency="EUR"):
    currencies_response = get(f"{BASE_URL}/currencies", timeout=10)
    currencies_response.raise_for_status()
    currencies = currencies_response.json()
    rates_response = get(f"{BASE_URL}/rates", params={"base": base_currency}, timeout=10)
    rates_response.raise_for_status()
    rates = rates_response.json()

    rates_by_quote = {item["quote"]: item for item in rates}
    combined_results = []
    for currency in currencies:
        rate_info = rates_by_quote.get(currency["iso_code"])
        rate = 1.0 if currency["iso_code"] == base_currency else rate_info["rate"] if rate_info else None
        combined_results.append(
            {
                "iso_code": currency["iso_code"],
                "name": currency["name"],
                "symbol": currency["symbol"],
                "rate": rate,
            }
        )
    return sorted(combined_results, key=lambda item: item["name"])


def print_available_currencies(currencies):
    print("\nAvailable currencies:\n")
    for currency in currencies:
        symbol = currency["symbol"] or "-"
        print(f'{currency["iso_code"]} | {currency["name"]} | Symbol: {symbol}')



def convert_eur_to_currency(eur_amount, chosen_currency, currencies):
    currency = next(
        (item for item in currencies if item["iso_code"] == chosen_currency),
        None,
    )
    if currency is None or currency["rate"] is None:
        raise ValueError("Currency rate is not available.")
    return eur_amount * currency["rate"]


def run_converter():
    currencies = get_currencies_with_rates()
    available_codes = {currency["iso_code"] for currency in currencies if currency["rate"] is not None}

    while True:
        print_available_currencies(currencies)

        chosen_currency = input(
            "\nChoose the currency you would like to convert EUR to "
            "(for example USD or VUV, or press q to quit): "
        ).strip().upper()

        if chosen_currency == "Q":
            print("Program ended.")
            break

        if chosen_currency not in available_codes:
            print("Invalid currency code. Please choose one from the list.")
            continue

        eur_amount_input = input("Enter the EUR amount to convert: ").strip()
        try:
            eur_amount = float(eur_amount_input)
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        converted_amount = convert_eur_to_currency(eur_amount, chosen_currency, currencies)
        print(f"\n{eur_amount:.2f} EUR = {converted_amount:.2f} {chosen_currency}")

        repeat_choice = input(
            "\nPress Enter to convert again or type q to quit: "
        ).strip().lower()
        if repeat_choice == "q":
            print("Program ended.")
            break


if __name__ == "__main__":
    run_converter()
