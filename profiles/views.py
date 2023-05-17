from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Profile
from .serializer import ProfileSerializer
from .permissions import isOwnerOrReadOnly


class ProfileList(ListAPIView):
    permission_classes = (isOwnerOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (isOwnerOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
