from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.core.mail import send_mail
import datetime


from .serializers import ItemsSerializer, DetailsSerializer, CustomerSerializer, SiteImagesSerializer, ArticlesSerializer, AgricultureSignUpSerializer, RetailSignUpSerializer, EducationSignUpSerializer, ContactEmailSerializer, EnquiryEmailSerializer, NewsletterSerializer
from .models import Items, Details, Customer, SiteImages, Articles, AgricultureSignUp, RetailSignUp, EducationSignUp, ContactEmail, EnquiryEmail, Newsletter
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
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            customer_data = serializer.data
            customer = Customer.objects.get(email=customer_data['email'])

            email_body = 'Someone Just Submitted a Form @malingreats.org \n\n\n NAME:		'+customer.name+'\n CITY:		'+customer.city+'\n EMAIL:		' + \
                customer.email+'\n PHONE:		'+customer.phone+'\n COMPANY:	'+customer.company + \
                '\n CHOICE:		'+customer.choice+'\n MESSAGE:	'+customer.themessage
            data = {'email_body': email_body, 'subject': 'Potential Client'}
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
        serializer = ArticlesSerializer(data=request.data)
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


@api_view(['POST'])
def AgricSignUpEmail(request):
    serializer = AgricultureSignUpSerializer(data=request.data)
    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    body = fullName + 'New Sign Up \n\t Agriculture \n\n ' + fullName + '\n' + email
    if serializer.is_valid():
        send_mail('SmartFarma SignUp HURRY', body, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def RetailSignUpEmail(request):
    serializer = RetailSignUpSerializer(data=request.data)
    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    body = 'New Sign Up \n Retail \n\n ' + fullName + '\n' + email
    if serializer.is_valid():
        send_mail('SmartFarma SignUp HURRY', body, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def EduSignUpEmail(request):
    serializer = EducationSignUpSerializer(data=request.data)
    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    body = 'New Sign Up \n Education \n\n ' + fullName + '\n' + email
    if serializer.is_valid():
        send_mail('SmartFarma SignUp HURRY', body, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def ContactEmail(request):
    serializer = ContactEmailSerializer(data=request.data)
    data = request.data
    fullName = data.get('fullName')
    companyName = data.get('companyName')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    message = data.get('message')

    if serializer.is_valid():
        send_mail('Malin Greats Contact Form', fullName + '\n' + companyName + '\n' + email + '\n' + phoneNumber + '\n' + '\n\n' + message, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def EnquiryEmail(request):
    serializer = EnquiryEmailSerializer(data=request.data)
    data = request.data
    fullName = data.get('fullName')
    email = data.get('email')
    body = fullName + '\n' + email
    if serializer.is_valid():
        send_mail('Malin Greats Enquiry', body, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)


@api_view(['POST'])
def Newsletter(request):
    serializer = NewsletterSerializer(data=request.data)
    data = request.data
    email = data.get('email')
    body = 'Hello' + '\n' + email + 'just joined the newsleter mail list'
    if serializer.is_valid():
        send_mail('Malin Newsletter Subscriptions', body, 'malingreatsdev@gmail.com',
                  ['malingreatsdev@gmail.com', 'benjaminnyakambangwe@gmail.com'], fail_silently=False)
        # send_mail('', body , 'fastdcomga@gmail.com',
        #           ['fastdcomga@gmail.com'], fail_silently=False)
        serializer.save()

    else:
        return Response('serializer not valid')
    return Response(serializer.data)
