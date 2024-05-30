from rest_framework.decorators import APIView
from rest_framework.response import Response
from . serializers import ProductSerializer
from . models import Product
from rest_framework import status


class ProductAPI (APIView):

    def get(self, request, id=None):
        if id is not None:
            try:
                instance = Product.objects.get(id=id)
            except Product.DoesNotExist:
                return Response('{} Entity not Found'.format(Product), status=status.HTTP_404_NOT_FOUND)
            serializer = ProductSerializer(instance=instance)
        else:
            serializer = ProductSerializer(instance=Product.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        try:
            instance = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response('{} Entity not Found'.format(Product), status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

    def delete(self, request, id=None):
        product_obj =  Product.objects.filter(id=id)
        if product_obj.exists():
            return Response('Data deleted Sucessfully', status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(' No product with this id found',status=status.HTTP_400_BAD_REQUEST)
