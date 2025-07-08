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

def test_password_special_characters():
    """Şifre oluşturulurken en az bir özel karakter bulunduğunu test eder"""
    password = generate_password(10)
    special_characters = set(string.punctuation)
    assert any(char in special_characters for char in password), "Şifre en az bir özel karakter içermelidir"
    
def test_password_uppercase():
    """Şifre oluşturulurken en az bir büyük harf bulunduğunu test eder"""
    password = generate_password(10)
    assert any(char.isupper() for char in password), "Şifre en az bir büyük harf içermelidir"   