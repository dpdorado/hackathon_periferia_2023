from rest_framework import serializers
import re
from .models import Person, Stats

class PersonCreateSerializer(serializers.ModelSerializer):
    dna = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Person
        fields = ('id', 'dna', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
    
    def create(self, validated_data):
        dna = validated_data.get('dna', [])
        is_mutant = Person.isMutant(dna)
        validated_data['is_mutant'] = is_mutant
        person = super().create(validated_data)
        stats = Stats.get_instance()
        stats.update_data(is_mutant)
        return person

    def validate_dna(self, value):
        if len(value) != 6:
            raise serializers.ValidationError('The "dna" field must have exactly 6 elements.')
        
        for element in value:
            if not re.match("^[ATCG]+$", element):
                raise serializers.ValidationError('Each element in the "dna" field must contain only the letters "A", "T", "C", and "G" in uppercase.')
            if len(element) != 6:
                raise serializers.ValidationError('Tring length must be 6.')

        return value

class PersonRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'dna', 'is_mutant', 'created_at', 'updated_at')

class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ('count_mutant_dna', 'count_human_dna', 'ratio')
    