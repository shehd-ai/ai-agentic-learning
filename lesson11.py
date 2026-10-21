from fastapi import FastAPI
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


def get_shop_info() -> str:
    """Returns the shop's address, opening hours, phone number and policies. Use this for any question about the shop itself."""
    print("[tool used] get_shop_info")
    try:
        with open("shop_info.txt", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "The shop information file was not found."


config = types.GenerateContentConfig(
    system_instruction=(
        "You are a friendly salesperson at a jewellery shop in Kozhikode. "
        "Use your tools for prices, stock and shop details. "
        "You only know what your tools tell you. "
        "Never guess or invent anything else, such as what the pieces look "
        "like or photos. "
        "If the customer asks about something your tools do not cover, say "
        "you are not sure and that the owner can confirm. "
        "The stock tool counts pieces, not designs, so say 'pieces'."
    ),
    tools=[gold_price, check_stock, get_shop_info],
)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "The shop assistant is open. Use /ask?question=your question"}


@app.get("/ask")
def ask(question: str):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=question,
            config=config,
        )
        return {"question": question, "answer": response.text}
    except Exception as error:
        print("Error:", error)
        return {
            "question": question,
            "answer": "Sorry, the system is busy right now. Please try again in a moment.",
        }