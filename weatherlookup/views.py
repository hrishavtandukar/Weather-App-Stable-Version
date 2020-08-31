from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	if request.method == "POST":

		
		zipcode = request.POST['zipcode']
		#districtnepal = request.POST['districtnepal']
		
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=504CB3FD-B442-47D4-A1E0-BC30B0F3CCED")
		api_request_nepal = requests.get("https://nepal-weather-api.herokuapp.com/api/?place=all")

		try:
			api = json.loads(api_request.content)
			api_nepal = json.loads(api_request_nepal.content)

		except Exception as e:
			api = "Error in calling API...."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0-50) Air quality is considered satisfactory."
			category_color = "good"

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51-100) Air quality is acceptable."
			category_color = "moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101-150) Although general public is not likely to be affected at this AQI range, people with lung disease, elderly people and children are at a greatest risk point."
			category_color = "usg"

		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151-200) Everyone may begin to experience health effects."
			category_color = "unhealthy"

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201-300) Health alert."
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(300-500) Health warning of emergency condition."
			category_color = "hazardous"
		
		return render(request, 'home.html', {'api':api, 'api_nepal':api_nepal, 'category_description':category_description, 'category_color':category_color})



	else:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=504CB3FD-B442-47D4-A1E0-BC30B0F3CCED")
		api_request_nepal = requests.get("https://nepal-weather-api.herokuapp.com/api/?place=all")

		try:
			api = json.loads(api_request.content)
			api_nepal = json.loads(api_request_nepal.content)

		except Exception as e:
			api = "Error in calling API...."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0-50) Air quality is considered satisfactory."
			category_color = "good"

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51-100) Air quality is acceptable."
			category_color = "moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101-150) Although general public is not likely to be affected at this AQI range, people with lung disease, elderly people and children are at a greatest risk point."
			category_color = "usg"

		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151-200) Everyone may begin to experience health effects."
			category_color = "unhealthy"

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201-300) Health alert."
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(300-500) Health warning of emergency condition."
			category_color = "hazardous"
		
		return render(request, 'home.html', {'api':api, 'api_nepal':api_nepal, 'category_description':category_description, 'category_color':category_color})

def about_us(request):
	return render(request, 'about_us.html', {})

# def api_request_for_nepal():
# 	import json
# 	import requests
# 	api_request_nepal = requests.get("https://nepal-weather-api.herokuapp.com/api/?place=all")

# 	try:
# 		api_nepal = json.loads(api_request_nepal.content)

# 	except Exception as e:
# 		api_nepal = "Error in calling API...."

# 	return render(request, 'home.html', {'api_nepal':api_nepal})