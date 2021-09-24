from pushover import Client
from sys import argv

client = Client("ID", api_token="")
client.send_message("Your Text", title=argv[1])
