from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, ContactSerializer, ContactUpdateSerializer
from .models import Category, Contact 
from rest_framework import status
# Create your views here.


class ContactsView(APIView):
    def get(self, request, contact_id=None):

        if contact_id is not None:
            contact = Contact.objects.get(pk=contact_id)
            serializer = ContactSerializer(contact, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass

    def put(self, request, contact_id):
        contact = Contact.objects.get(pk=contact_id)
        serializer = ContactUpdateSerializer(contact, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
