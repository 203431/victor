from rest_framework import serializers

from Profile.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('__all__')
        
    # def create(self, file, user):
    #     Profile.objects.create(
    #         url_img = file,
    #         id_user = user
    #     )