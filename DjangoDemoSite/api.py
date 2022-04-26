
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import time

@api_view(['GET', 'POST'])
def demo_data(request):
    """
    Get just a simple json object
    """
    if request.method == 'GET':
        if len(request.query_params)>=2:
            qs = list(request.query_params.values())
            return Response({'a':qs[0],'b':qs[1]})
        return Response({'a':3,'b':None})

    elif request.method == 'POST':
        data=request.data
        data['a']=data['a']*10
        return Response(data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def long_run(request):
        qs = list(request.query_params.values())
        if len(qs)>0:
            time.sleep(int(qs[0]))
        return Response(qs, status=status.HTTP_201_CREATED)