from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

@api_view(['POST'])
def subscribe(request):
    email = request.data.get('email')
    if email:
        try:
            send_mail(
                # 메일 제목
                'Welcome to Finance Navigator - Your Personal Finance Guide!',
                # 메일 본문
                """
                Hello,

                Thank you for subscribing to Finance Navigator!

                At Finance Navigator, we are committed to helping you find the best financial products tailored to your needs. Here are some of the features we offer:

                - Compare Financial Products: Whether you're looking for savings accounts, fixed deposits, mortgage loans, or home equity loans, we provide comprehensive comparisons to help you make informed decisions.
                - Exchange Rate Information: Stay updated with the latest exchange rates to make the best financial decisions when dealing with foreign currencies.
                - Bank Search: Easily find and compare different banks to discover the best financial services available.

                We are dedicated to providing you with reliable and accurate information to guide you in your financial journey.

                Thank you for trusting Finance Navigator. We look forward to helping you achieve your financial goals.

                Best regards,
                The Finance Navigator Team

                ---

                Finance Navigator
                FinanceNavigator@ssafy.com
                """,
                # 발신인
                'FinanceNavigator@ssafy.com',  
                [email],
                fail_silently=False,
            )
            return Response({'message': 'Subscription successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
