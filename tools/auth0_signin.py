from pprint import pprint

import jwt
from auth0.v3.authentication import GetToken
from auth0.v3.authentication.token_verifier import TokenVerifier, AsymmetricSignatureVerifier


domain = ""
client_id = ""
client_secret = ""
realm = ""

username = ""
password = ""

if __name__ == "__main__":
    token = GetToken(domain)
    ret = token.login(
        client_id=client_id, client_secret=client_secret, username=username, password=password, realm=realm,
        scope="openid", audience=f"https://{domain}/api/v2/", grant_type="password"
    )
    pprint(ret)

    id_token = ret["id_token"]

    sv = AsymmetricSignatureVerifier(f"https://{domain}/.well-known/jwks.json")
    tv = TokenVerifier(signature_verifier=sv, issuer=f"https://{domain}/", audience=client_id)
    tv.verify(id_token)

    decoded_id_toke = jwt.decode(id_token, options={"verify_signature": False})
    pprint(decoded_id_toke)
