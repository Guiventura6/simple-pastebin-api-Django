from codes.models import Code
from codes.permissions import IsOwnerOrReadOnly
from codes.serializers import CodeSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class CodeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        code = self.get_object()
        return Response(code.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    
       
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and ``retrieve` actions.
    """    
    queryset = User.objects.all()
    serializer_class = UserSerializer


