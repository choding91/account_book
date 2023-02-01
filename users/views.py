from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer


# 회원가입 / 로그아웃
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):  # JS localStorage.clear() or localStorage.removeItem("") 처리 필요
        if request.user.is_authenticated:
            response = Response({"message": "로그아웃이 완료되었습니다."}, status=status.HTTP_204_NO_CONTENT)
            response.delete_cookie("access")
            response.delete_cookie("refresh")
            return response
        else:
            return Response({"message": "로그인 정보를 확인해 주세요."}, status=status.HTTP_400_BAD_REQUEST)
