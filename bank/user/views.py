from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from bank.utils.data_types import RegisterInformation
from bank.user.services import create_account
from bank.user.models import Accounts


class AccountRegister(APIView):
    class InputSerializer(serializers.Serializer):
        account_name = serializers.CharField()
        email = serializers.EmailField()
        name = serializers.CharField()
        age = serializers.IntegerField()
        phone_number = serializers.CharField()
        description = serializers.CharField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Accounts
            fields = "__all__"

    def post(self, request):
        data = request.data
        input_serializer = self.InputSerializer(data=data)
        input_serializer.is_valid(raise_exception=True)
        valid_data = input_serializer.validated_data

        print(valid_data)
        account = create_account(RegisterInformation(**valid_data))
        output_data = self.OutputSerializer(instance=account).data
        return Response(output_data)
