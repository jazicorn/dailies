from rest_framework import serializers
from apps.daily.models import Daily

class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily
        read_only_fields = (
            'id',
            'created_at',
            'modified'

        )
        fields = (
            'id',
            'created_at',
            'modified', 
            'title', 
            'description', 
            'completed'
        )