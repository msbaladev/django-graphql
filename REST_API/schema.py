import graphene
from graphene_django import DjangoObjectType
from .models import *


class ProductType(DjangoObjectType):
    class Meta:
        model = products
        fields = "__all__"
        

class createProduct(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
        image=graphene.String(required=True)
        price=graphene.String(required=True)
        quantity=graphene.String(required=True)
        
    post_data=graphene.Field(ProductType)
    
    def mutate(self,info,name,image,price,quantity):
        post_data=products(name=name,image=image,price=price,quantity=quantity)
        post_data.save()
        
        return createProduct(post_data=post_data)
        
        
        
    
    
    
class Query(graphene.ObjectType):
    product_data=graphene.List(ProductType)
    def resolve_product_data(self, info):
        return products.objects.all()
    
    
    
    
    
class Mutation(graphene.ObjectType):
    createPost = createProduct.Field()
  


schema = graphene.Schema(query=Query, mutation=Mutation)