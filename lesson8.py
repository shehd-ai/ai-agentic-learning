from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client()

GOLD_RATE_PER_GRAM = 7000

stock = {
    "chain": 5,
    "ring": 0,
    "bangle": 3,
}


def gold_price(grams: int) -> int:
    """Returns the price in rupees for this many grams of gold at today's rate."""
    print("[tool used] gold_price for", grams, "grams")
    return grams * GOLD_RATE_PER_GRAM


def check_stock(design: str) -> str:
    """Checks how many pieces of a design (chain, ring or bangle) are in the shop right now."""
    print("[tool used] check_stock for", design)
    count = stock.get(design.lower())
    if count is None:
        return "We do not sell that design."
    if count == 0:
        return "Out of stock."
    return str(count) + " pieces in stock."


chat = client.chats.create(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a friendly salesperson at a jewellery shop in Kozhikode. "
            "Use your tools for prices and stock. "
            "You only know what your tools tell you. "
            "Never guess or invent anything else, such as the shop address, "
            "opening hours, what the pieces look like, or photos. "
            "If the customer asks about something you do not know, say you are "
            "not sure and that the owner can confirm. "
            "The stock tool counts pieces, not designs, so say 'pieces'."
        ),
        tools=[gold_price, check_stock],
    ),
)

print("Welcome to the shop. Type quit when you want to leave.")

while True:
    message = input("Customer: ")

    if message.lower() == "quit":
        print("Thank you, visit again!")
        break

    try:
        response = chat.send_message(message)
        print("Salesperson:", response.text)
    except Exception as error:
        print("Sorry, the system is busy right now. Please ask again in a moment.")
        print("(details:", error, ")")
    print()