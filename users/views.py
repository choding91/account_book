from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer


# 유저 회원가입 / 회원탈퇴
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if request.user.is_authenticated:
            request.user.delete()
            return Response({"message": "회원탈퇴가 완료되었습니다."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "회원탈퇴 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
