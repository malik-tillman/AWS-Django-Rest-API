from rest_framework import serializers
from .models import Project


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'status',
            'importance',
            'level',
            'keywords',
            'summary',
            'languages',
            'media'
        )
