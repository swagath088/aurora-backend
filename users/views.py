from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from .models import User


@api_view(['POST'])
def register(request):
    print("REGISTER DATA:", request.data)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        print("USER CREATED:")
        print("USERNAME:", user.username)
        print("EMAIL:", user.email)
        print("PASSWORD:", user.password)

        return Response({"message": "User Registered"})

    print("REGISTER ERRORS:", serializer.errors)

    return Response(serializer.errors, status=400)


@api_view(['POST'])
def login(request):
    email = request.data.get("email", "").strip()
    password = request.data.get("password", "").strip()

    print("LOGIN EMAIL:", email)
    print("LOGIN PASSWORD:", password)

    user = User.objects.filter(email__iexact=email).first()

    print("FOUND USER:", user)

    if not user:
        print("EMAIL NOT FOUND")
        return Response(
            {"message": "Email not found"},
            status=401
        )

    print("DB PASSWORD:", user.password)

    if user.password != password:
        print("PASSWORD MISMATCH")
        return Response(
            {"message": "Incorrect password"},
            status=401
        )

    print("LOGIN SUCCESS")

    return Response({
        "message": "Login Successful",
        "username": user.username,
        "email": user.email,
        "age": user.age,
        "gender": user.gender,
        "height": user.height,
        "weight": user.weight,
    })