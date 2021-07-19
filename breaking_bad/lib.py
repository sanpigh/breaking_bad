import requests


def get_quote():
    url = "https://breaking-bad-quotes.herokuapp.com/v1/quotes"
    response = requests.get(url).json()[0]
    return f"{response.get('quote', 'ERROR IN QUOTE')} \n AUTHOR: {response.get('author', 'ERROR IN AUTHOR')}"


if __name__ == "__main__":
    quote = get_quote()
    print(quote)
