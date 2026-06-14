from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from .models import User


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User Registered"})

    return Response(serializer.errors, status=400)


@api_view(['POST'])
def login(request):
    email = request.data.get("email", "").strip()
    password = request.data.get("password", "").strip()

    user = User.objects.filter(email__iexact=email).first()

    if not user:
        return Response(
            {"message": "Email not found"},
            status=401
        )

    if user.password != password:
        return Response(
            {"message": "Incorrect password"},
            status=401
        )

    return Response({
        "message": "Login Successful",
        "username": user.username,
        "email": user.email
    })