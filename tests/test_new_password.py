import string
from password.new_password import generate_password

def test_password_characters():
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Daha güvenli bir doğrulama için uzun bir şifre oluşturuluyor
    for char in password:
        assert char in valid_characters

def test_password_length():
    for length in range(1, 21): 
        assert len(generate_password(length)) == length

def test_password_randomness():
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2

