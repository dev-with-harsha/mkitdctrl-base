POST /v2/merchants/1570616552/orders/order_example_1 HTTP/1.1
Accept: application/json
Content-Type: application/json
Authorization: Bearer 573cec25a87526dcceacad786bbbba83b1a5172

{
  "orderDescription": "description",
  "orderDetailDescription": "detailed desc",
  "paymentMethodId": 1000,
  "amount": {
    "currency": "EUR",
    "amount": 10.50
  },
  "autoCapture": false,
  "transactionChannel": "Web Online",
  "cardInfo": {
    "cardNumber": "4111111111111111",
    "expirationDate": "12-2024"
  },
  "cardVerificationInfo": {
    "cvCode": "123",
    "cvCodeState": "USED"
  }
}
