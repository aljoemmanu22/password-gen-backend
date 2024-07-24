import random
import string
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Password
from .serializers import PasswordSerializer

@api_view(['POST'])
def generate_password(request):
    """
    Generate a random password based on user specifications.

    Parameters:
    - length: int (default: 8)
    - include_uppercase: bool (default: True)
    - include_lowercase: bool (default: True)
    - include_numbers: bool (default: True)
    - include_special: bool (default: True)

    Returns:
    - generated_password: str
    """
    data = request.data
    length = data.get('length', 8)
    include_uppercase = data.get('include_uppercase', True)
    include_lowercase = data.get('include_lowercase', True)
    include_numbers = data.get('include_numbers', True)
    include_special = data.get('include_special', True)
    
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        return Response({"error": "No character sets selected."}, status=status.HTTP_400_BAD_REQUEST)

    password = ''.join(random.choice(characters) for _ in range(length))

    password_instance = Password.objects.create(
        length=length,
        include_uppercase=include_uppercase,
        include_lowercase=include_lowercase,
        include_numbers=include_numbers,
        include_special=include_special,
        generated_password=password
    )

    serializer = PasswordSerializer(password_instance)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
