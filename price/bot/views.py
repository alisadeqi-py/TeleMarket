from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import g4f




class AskQuestionView(APIView):
    # Ensure the view is accessible only to authenticated users
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            # Extract the question from the request data
            question = request.data.get('question', '')
            prompt = f'''
                    تو یک مربی تریدینگ حرفه ای هستی و مهربان و حرفه ای به سوالا پاسخ میدهی دانشجوی تو از تو سوالی دارد سوال به شرح زیر است 
                    {question}
            '''

            if not question:
                return Response({'error': 'No question provided'}, status=status.HTTP_400_BAD_REQUEST)

            # Use g4f to get a response from the OpenAI model
            response = g4f.ChatCompletion.create(
                model='gpt-4',  # Adjust model if needed
                messages=[{'role': 'user', 'content': prompt}]
            )

            # Return the response
            return Response({'response': response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
