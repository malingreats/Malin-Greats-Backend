from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime



from .serializers import ItemsSerializer, DetailsSerializer, CustomerSerializer, SiteImagesSerializer, ArticlesSerializer
from .models import Items, Details, Customer, SiteImages, Articles
from .utils import Util



class ItemsViewSet(viewsets.ModelViewSet):
	queryset = Items.objects.all()
	serializer_class = ItemsSerializer


class DetailsViewSet(viewsets.ModelViewSet):
	queryset = Details.objects.all()
	serializer_class = DetailsSerializer


class CustomerView(APIView):
	def get(self, request, *args, **kwargs):
		qs = Customer.objects.all()
		serializer = CustomerSerializer(qs, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		serializer = CustomerSerializer(data = request.data)
		if	serializer.is_valid():
			serializer.save()
			customer_data = serializer.data
			customer = Customer.objects.get(email=customer_data['email'])

			email_body = 'Someone Just Submitted a Form @malingreats.org \n\n\n NAME:		'+customer.name+'\n CITY:		'+customer.city+'\n EMAIL:		'+customer.email+'\n PHONE:		'+customer.phone+'\n COMPANY:	'+customer.company+'\n CHOICE:		'+customer.choice+'\n MESSAGE:	'+customer.themessage
			data={'email_body': email_body, 'subject': 'Potential Client'}
			Util.send_email(data)
			return Response(serializer.data)
		return Response(serializer.errors)


class SiteImagesView(APIView):

	def get(self, request, *args, **kwargs):
		qs = SiteImages.objects.all()
		serializer = SiteImagesSerializer(qs, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		print(request.data)
		serializer = SiteImagesSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.error)


class SiteImageView(APIView):

	def get(self, request, pk):
		qs = SiteImages.objects.get(id=pk)
		serializer = SiteImagesSerializer(qs, many=False)
		return Response(serializer.data)


	def patch(self, request, pk):
		qs = SiteImages.objects.get(id=pk)
		data = request.data

		qs.alt_text = data.get('alt_text', qs.alt_text)
		qs.image = data.get('image', qs.image)

		qs.save()
		serializer = SiteImagesSerializer(qs)

		return Response(serializer.data)


class ArticlesView(APIView):

	def get(self, request, *args, **kwargs):
		qs = Articles.objects.all()
		serializer = ArticlesSerializer(qs, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ArticlesSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.error)


class ArticleView(APIView):

	def get(self, request, pk):
		qs = Articles.objects.get(id=pk)
		serializer = ArticlesSerializer(qs, many=False)
		return Response(serializer.data)

	def patch(self, request, pk):
		qs = Articles.objects.get(id=pk)
		data = request.data

		qs.title = data.get('title', qs.title)
		qs.excerpt = data.get('excerpt', qs.excerpt)
		qs.content1 = data.get('content1', qs.content1)
		qs.content2 = data.get('content2', qs.content2)
		qs.content3 = data.get('content3', qs.content3)
		qs.content4 = data.get('content4', qs.content4)
		qs.subContent1 = data.get('subContent1', qs.subContent1)
		qs.subContent2 = data.get('subContent2', qs.subContent2)
		qs.image1 = data.get('image1', qs.image1)
		qs.image2 = data.get('image2', qs.image2)
		qs.published = data.get('published', qs.published)
		qs.publishedDay = data.get('publishedDay', qs.publishedDay)
		qs.isFeatured = data.get('isFeatured', qs.isFeatured)


		qs.save()
		serializer = ArticlesSerializer(qs)

		return Response(serializer.data)