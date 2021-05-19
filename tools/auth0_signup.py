from pprint import pprint

from auth0.v3.authentication import Database

from tools import domain, client_id, realm


# https://github.com/auth0/auth0-python

username = ""
password = ""

if __name__ == "__main__":
    database = Database(domain=domain)
    ret = database.signup(client_id=client_id, email=username, password=password, connection=realm)
    pprint(ret)
