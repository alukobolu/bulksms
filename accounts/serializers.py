from rest_framework import serializers
from .models import Account
import re 	#This is for the username validator 

#Register a user
class RegisterSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = [ 'fullname','email', 'password', 'password2']
        extra_kwarg = {
            'password' : {'write_only' : True}
        }

    def save(self):
        account = Account (email=self.validated_data['email'],fullname=self.validated_data['fullname'])
        password = self.validated_data['password']    
        password2 = self.validated_data['password2'] 
    
        #Add validations before saving
        if password != password2:
            raise serializers.ValidationError({'password' : 'Passwords do not match.'})                                                     #Make sure that passwords match

        account.set_password(password)
        account.save()
        return account


#Check user with username
class AccountSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'email', 'fullname' ]

    # This is to update user details 
    def update(self, instance, validated_data):

        instance.email              = self.validated_data['email']
        instance.fullname           = self.validated_data['fullname']   
        
        # Save the instance 
        instance.save()
        return instance