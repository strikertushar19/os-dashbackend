from rest_framework import serializers


class OrganisationSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    organisation = serializers.CharField(label="Organisation")
    email = serializers.EmailField(label="Email")
    given_name = serializers.CharField(label="Given Name")
    middle_name = serializers.CharField(label="Middle Name" )
    family_name = serializers.CharField(label="Family Name")
    full_name = serializers.CharField(label="Full Name" )
    address1 = serializers.CharField(label="Address1" )
    address2 = serializers.CharField(label="Address2"  )
    city = serializers.CharField(label="City")
    region = serializers.CharField(label="Region")
    postal_code = serializers.CharField(label="Postal Code")
    user_note=serializers.CharField(label="User Note" )

    phone_no =serializers.IntegerField(label="Phone No only integer please")
    country = serializers.CharField(label="Country")