from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
# internal fs
from ..models import Share
from ..serializers import ShareSerializer, ShareSerializer_POST, ShareActionSerializer


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def shareView(request, *args, **kwargs):
    serializer = ShareSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serial = serializer.save(user=request.user)
        serial = ShareSerializer_POST(serial)
        return Response(serial.data, status=201)
    return Response({}, status=400)

# _________________________________________________________________________________________________


def get_paginated_queryset_response(qs, request):

    paginator = PageNumberPagination()
    paginator.page_size = 20
    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = ShareSerializer(paginated_qs, many=True, context={"request":request})
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def commit_feed(request, *args, **kwargs):
    user = request.user
    qs = Share.objects.feed(user)
    return get_paginated_queryset_response(qs, request)

# _______________________________________________________________________________________________


@api_view(['GET'])
def commit_list(request, *args, **kwargs):
    qs = Share.objects.all()
    username = request.GET.get('username')  # ?username=ades||telos
    if username != None:
        qs = qs.by_username(username)
    return get_paginated_queryset_response(qs, request)


@api_view(['GET'])
def commit_detail(request, share_id, *args, **kwargs):

    qs = Share.objects.filter(id=share_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = ShareSerializer_POST(obj)
    return Response(serializer.data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def shareactionview(request, *args, **kwargs):

    serializer = ShareActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):

        data = serializer.validated_data
        Share_id = data.get('id')
        action = data.get('action')
        qs = Share.objects.filter(id=Share_id)

        if not qs.exists():
            return Response({}, status=404)

        obj = qs.first()

        if action == 'like':
            obj.likes.add(request.user)
            serializer = ShareSerializer_POST(obj)
            return Response(serializer.data, status=200)

        elif action == 'unlike':
            obj.likes.remove(request.user)
            serializer = ShareSerializer_POST(obj)
            return Response(serializer.data, status=200)

        elif action == 'recommit':
            new_commit = Share.objects.create(
                user=request.user, parent=obj, content=obj.content)
            serializer = ShareSerializer_POST(new_commit)
            return Response(serializer.data, status=201)

    return Response({}, status=200)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def commit_delete(request, pk, *args, **kwargs):
    qs = Share.objects.filter(id=pk)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({'message': 'You do not have permission for delete this commit'}, status=401)
    qs.delete()
    return Response({'message': 'Commit removed'}, status=200)
