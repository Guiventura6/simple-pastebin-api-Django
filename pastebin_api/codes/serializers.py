from codes.models import LANGUAGE_CHOICES, STYLE_CHOICES, Code
from django.contrib.auth.models import User
from rest_framework import serializers


class CodeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='code-highlight', format='html')
    
    class Meta:
        model = Code
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']
        
    
class UserSerializer(serializers.HyperlinkedModelSerializer):    
    codes = serializers.HyperlinkedIdentityField(many=True, view_name='code-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'codes']
    