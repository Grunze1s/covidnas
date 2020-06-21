from rest_framework import serializers

class NepalStatusSerializer(serializers.Serializer):
    sample_tested = serializers.IntegerField(source='samples_tested',required=False)
    positive = serializers.IntegerField(required=False)
    negative = serializers.IntegerField(required=False)
    death = serializers.IntegerField(source='deaths',required=False)
    recovered = serializers.IntegerField(source='extra1',required=False)
    isolation = serializers.IntegerField(source='extra2',required=False)
    quartine = serializers.IntegerField(source='extra8',required=False)
    rdt_test = serializers.IntegerField(source='extra7',required=False)
    today_death = serializers.IntegerField(required=False)
    today_newcase = serializers.IntegerField(required=False)
    today_recovered = serializers.IntegerField(required=False)
    today_pcr = serializers.IntegerField(required=False)
    today_rdt = serializers.IntegerField(required=False)
    date = serializers.DateField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    class Meta:
        fields = ('__all__')

class HealthFacilitySerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    province = serializers.CharField(source='province_name',required=False)
    district = serializers.CharField(source='district_name',required=False)
    municipality = serializers.CharField(source='municiaplity_name', required=False)
    contact_number = serializers.CharField(source='contact_num',required=False)
    total_tested = serializers.IntegerField(required=False)
    total_positive = serializers.IntegerField(required=False)
    total_death = serializers.IntegerField(required=False)
    total_in_isolation = serializers.IntegerField(required=False)
    lat = serializers.DecimalField(max_digits=10,decimal_places=8, required=False)
    long = serializers.DecimalField(max_digits=10,decimal_places=8, required=False)
    used_for_corona_response = serializers.IntegerField(required=False)

class HealthFacilitiesListSerializer(serializers.ListSerializer):
    child = HealthFacilitySerializer()