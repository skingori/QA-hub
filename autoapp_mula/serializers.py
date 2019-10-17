from abc import ABC

from rest_framework import serializers


class CheckoutCallSerial(serializers.Serializer):
    """Your data serializer, define your fields here.
    """
    requestStatusCode = serializers.CharField(max_length=200, required=True)
    requestStatusDescription = serializers.CharField(max_length=200)
    MSISDN = serializers.CharField(max_length=200, required=True)
    amountPaid = serializers.CharField(max_length=200, required=True)
    # cpgTransactionID = serializers.IntegerField(required=False)
    serviceCode = serializers.CharField(max_length=200)
    # payerTransactionID = serializers.CharField(max_length=200, required=False)
    accountNumber = serializers.CharField(max_length=200)
    currencyCode = serializers.CharField(max_length=200)
    # customerName = serializers.CharField(max_length=200, required=False)
    # payerClientCode = serializers.CharField(max_length=200, required=False)
    # datePaymentReceived = serializers.CharField(max_length=200, required=False)
    merchantTransactionID = serializers.CharField(max_length=200)
    requestDate = serializers.CharField(max_length=200)
    checkoutRequestID = serializers.CharField(max_length=200, required=True)
    requestAmount = serializers.CharField(max_length=200)


class ResponseCallSerial(serializers.Serializer):
    merchantTransactionID = serializers.CharField(max_length=200)
    checkoutRequestID = serializers.CharField(max_length=200)
    receiptNumber = serializers.CharField(max_length=200)
    statusCode = serializers.CharField(max_length=200)
    statusDescription = serializers.CharField(max_length=200)
