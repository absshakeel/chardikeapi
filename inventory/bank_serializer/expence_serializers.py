
from inventory.bank_model.baccounts import Expenses

from rest_framework import serializers

'''
Expence serilizers
        - create api
        - update api
'''
class ExpenceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ['id','name','outlet','reference','date','account','expence_amount','type','description']
    
 
'''
Expence serializers
        - list api
'''
class ExpenceListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ['id','name','outlet','reference','date','account','expence_amount','type','description','created_at']
        depth = 1
 


