from rest_framework import serializers

class MarsPhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    sol = serializers.IntegerField()
    camera = serializers.DictField()
    img_src = serializers.URLField()
    earth_date = serializers.DateField()
    rover = serializers.DictField()
