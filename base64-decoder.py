import base64

encoded_text = "IklmIHlvdSBvbmx5IGtuZXcgdGhlIHBvd2VyIG9mIHRoZSBkYXJrIHNpZGUuIiDigJQoVGhlIEVtcGlyZSBTdHJpa2VzIEJhY2spCgo="
decoded_text = base64.b64decode(encoded_text).decode()

print(decoded_text)

