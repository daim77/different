import os
import requests


def get_secret_message():
    url = os.environ["127.0.0.1:5000"]
    response = requests.get(url)
    print(f"The secret message is: {response.text}")


if __name__ == "__main__":
    get_secret_message()