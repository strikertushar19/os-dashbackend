from django.shortcuts import render
from  rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Organisation  # Import your Organisation model

from .serializers import OrganisationSerializer  # Import your OrganisationSerializer

# # Create your views here.
def index(request):
     return render(request,'index.html')


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'

class organisationapiview(APIView):

    def get(self, request):
        organisation_data = Organisation.objects.all()
        serializer = OrganisationSerializer(organisation_data, many=True)
        return Response({"Message": "Organisation data fetched successfully", "data": serializer.data})

    def post(self, request):
        serializer = OrganisationSerializer(data=request.data)
        if serializer.is_valid():
            Organisation.objects.create( id=request.data["id"],
                organisation=request.data["organisation"],
                email=request.data["email"],
                 given_name=request.data["given_name"],
                 middle_name=request.data["middle_name"],
                 family_name=request.data["family_name"],
                full_name=request.data["full_name"],
                address1=request.data["address1"],
                address2=request.data["address2"],
                city=request.data["city"],
                region=request.data["region"],
                postal_code=request.data["postal_code"],
                user_note=request.data["user_note"],
                phone_no=request.data["phone_no"],
                country=request.data["country"],
            )
            serializer.save()

            organisation_data=Organisation.objects.all().filter(organisation=request.data["id"]).values()

            return Response({"Message": "Organisation created successfully", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)