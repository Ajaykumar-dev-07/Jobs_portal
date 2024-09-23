from rest_framework import serializers
from .models import JobPost, Application, UserProfile

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['id', 'company', 'title', 'description', 'location', 'salary', 'posted_on', 'last_date']

    def validate_last_date(self, value):
        if value < self.instance.posted_on:
            raise serializers.ValidationError("Last date must be after the posted date.")
        return value

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'job', 'applicant', 'cover_letter', 'applied_on']
        
    def validate(self, data):
        if not UserProfile.objects.filter(id=data['applicant'].id).exists():
            raise serializers.ValidationError("Applicant must exist.")
        if not JobPost.objects.filter(id=data['job'].id).exists():
            raise serializers.ValidationError("Job must exist.")
        return data
