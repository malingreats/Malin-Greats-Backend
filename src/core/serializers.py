from rest_framework import serializers
from .models import Items, Details, Customer, SiteImages, Articles



class ItemsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Items
		fields = (
			'id', 'image', 'title', 'cost', 'description', 'description_large'
			)


class DetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Details
		fields = (
			'name', 'city', 'email', 'phone', 'company', 'choice'
			)

class SiteImagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = SiteImages
		fields = (
			'id', 'alt_text', 'image'
			)



class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = (
			'name', 'city', 'email', 'phone', 'company', 'choice', 'themessage'
			)


class ArticlesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Articles
		fields = (
			'id', 'title', 'excerpt', 'content1', 'content2', 'content3', 'content4', 'subContent1', 'subContent2', 'image1', 'image2', 'published', 'publishedDay', 'isFeatured'
			)