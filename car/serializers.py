from rest_framework import serializers
import collections

from .models import Car

class AccidentRiskSerializer(serializers.ModelSerializer):
    
    author = serializers.CharField(source='author.username', read_only=True)
    votes = serializers.IntegerField(read_only=True)
    thumb = serializers.SerializerMethodField()

    class Meta:
        model = Ref
        fields = ['id', 'title', 'link', 'node', 'author', 'votes', 'thumb']
        read_only_fields = ['id', 'author', 'votes', 'thumb']
    
    def get_thumb(self, obj):
        current_user = self.context['request'].user
        if current_user.is_anonymous:
            return 0
        else:
            vote = current_user.refvotes.filter(ref=obj)
            if vote.exists():
                return vote.first().voteparam
            else:
                return 0
