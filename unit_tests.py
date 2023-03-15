from bike_rental import ClientType, Client 

class TestClient:
    
    def test_add_valid_client(self):
        client = Client(1)
        client.add_client(1, "Alice", "alice@example.com", "0676789041", "password", ClientType.INDIVIDUAL)
        assert client.clients == [{'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'phone': '0676789041', 'password': 'password', 'client_type': 1}]
        assert client.clients[0]["phone"] == "0676789041"
        assert client.clients[0]["name"] == "Alice"
        assert client.clients[0]["client_type"] == ClientType.INDIVIDUAL

    def test_edit_client(self):
         client = Client(1)
         client.add_client(1, "John", "John@example.com", "1234567890", "password", ClientType.INDIVIDUAL)

         client.edit_client(1, name="Bob")
         assert  client.clients[0]["name"] == "Bob"
        
         client.edit_client(2, name="Bob")
         assert client.clients[0]["id"] == 1

         result = client.edit_client(1, name="Francois")
         assert result == "Client information updated successfully."
         assert client.clients[0]["name"] == "Francois"

         phone = client.edit_client(1, phone="06760410")
         assert phone == "Invalid phone number format."
         assert client.clients[0]["phone"] == "1234567890"

         result = client.edit_client(1, phone="0678904986")
         assert result == "Client information updated successfully."
         assert client.clients[0]["phone"] == "0678904986"
    
    def test_validate_phone(self):
        pass
        