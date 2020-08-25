from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'probability/home.html') 

def about(request):
	return render(request, 'probability/cheese.html')

def answer(request):

	#this is for the the pairs AA to 88 any suit

	if request.GET.get('card_one_number') == 'A' and request.GET.get('card_two_number') == 'A':
		stat = '85%'
	elif request.GET.get('card_one_number') == 'K' and request.GET.get('card_two_number') == 'K':
		stat = '83%'
	elif request.GET.get('card_one_number') == 'Q' and request.GET.get('card_two_number') == 'Q':
		stat = '80%'
	elif request.GET.get('card_one_number') == 'J' and request.GET.get('card_two_number') == 'J':
		stat = '78%'
	elif request.GET.get('card_one_number') == '10' and request.GET.get('card_two_number') == '10':
		stat = '75%'
	elif request.GET.get('card_one_number') == '9' and request.GET.get('card_two_number') == '9':
		stat = '72%'
	elif request.GET.get('card_one_number') == '8' and request.GET.get('card_two_number') == '8':
		stat = '69%'

	#this is for the top suited hands 	


	elif request.GET.get('card_one_suit') == 'spade' and request.GET.get('card_two_suit') == 'spade' or request.GET.get('card_one_suit') == 'club' and request.GET.get('card_two_suit') == 'club' or request.GET.get('card_one_suit') == 'heart' and request.GET.get('card_two_suit') == 'heart' or request.GET.get('card_one_suit') == 'diamond' and request.GET.get('card_two_suit') == 'diamond':
		if request.GET.get('card_one_number') == 'A' and request.GET.get('card_two_number') == 'K' or request.GET.get('card_one_number') == 'K' and request.GET.get('card_two_number') == 'A' :
			stat = "68%"
		elif request.GET.get('card_one_number') == 'A' and request.GET.get('card_two_number') == 'Q' or request.GET.get('card_one_number') == 'Q' and request.GET.get('card_two_number') == 'A' :
			stat = "67%"
		elif request.GET.get('card_one_number') == 'A' and request.GET.get('card_two_number') == 'J' or request.GET.get('card_one_number') == 'J' and request.GET.get('card_two_number') == 'A' :
			stat = "66%"
		elif request.GET.get('card_one_number') == 'A' and request.GET.get('card_two_number') == '10' or request.GET.get('card_one_number') == '10' and request.GET.get('card_two_number') == 'A' :
			stat = "66%"
		elif request.GET.get('card_one_number') == 'A' and request.GET.get('card_two_number') == '9' or request.GET.get('card_one_number') == '9' and request.GET.get('card_two_number') == 'A' :
			stat = "64%"
		elif request.GET.get('card_one_number') == 'A' and request.GET.get('card_two_number') == '8' or request.GET.get('card_one_number') == '8' and request.GET.get('card_two_number') == 'A' :
			stat = "63%"
		elif request.GET.get('card_one_number') == 'A' and request.GET.get('card_two_number') == '7' or request.GET.get('card_one_number') == '7' and request.GET.get('card_two_number') == 'A' :
			stat = "63%"
		elif request.GET.get('card_one_number') == 'A' and request.GET.get('card_two_number') == '6' or request.GET.get('card_one_number') == '6' and request.GET.get('card_two_number') == 'A' :
			stat = "62%"
		elif request.GET.get('card_one_number') == 'A' and request.GET.get('card_two_number') == '5' or request.GET.get('card_one_number') == '5' and request.GET.get('card_two_number') == 'A' :
			stat = "62%"
		elif request.GET.get('card_one_number') == 'A' and request.GET.get('card_two_number') == '4' or request.GET.get('card_one_number') == '4' and request.GET.get('card_two_number') == 'A' :
			stat = "61%"
		elif request.GET.get('card_one_number') == 'A' and request.GET.get('card_two_number') == '3' or request.GET.get('card_one_number') == '3' and request.GET.get('card_two_number') == 'A' :
			stat = "60%"
		else:
			return render(request, 'probability/fold.html')





	#this is for hands with a probability of < 50% of winning (need to alter if your're small/big blind)	

	else:
		return render(request, 'probability/fold.html')
		
		
	return render(request, 'probability/answer.html', {'statistic' : stat})
        