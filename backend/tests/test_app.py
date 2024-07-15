def test_register(test_client):
    response = test_client.post('/api/register', json={
        'username': 'newuser',
        'email': 'new@example.com',
        'password': 'newpassword'
    })
    assert response.status_code == 201, f"Error: {response.json}"
    assert response.json == {"message": "User registered successfully"}

def test_login(test_client, init_database):
    # Use different username and email for registration
    response = test_client.post('/api/register', json={
        'username': 'testuser2',
        'email': 'testuser2@example.com',
        'password': 'testpassword'
    })
    assert response.status_code == 201, f"Error: {response.json}"
    assert response.json == {"message": "User registered successfully"}

    # Now, try to login with the newly registered user
    response = test_client.post('/api/login', json={
        'username': 'testuser2',
        'password': 'testpassword'
    })
    assert response.status_code == 200, f"Error: {response.json}"
    assert response.json == {"message": "Login successful"}

    # Try to login with incorrect password
    response = test_client.post('/api/login', json={
        'username': 'testuser2',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401, f"Error: {response.json}"
    assert response.json == {"message": "Login failed"}
