# Decompiled with EinTimDC
from typing import Union
from re import search
from time import sleep
from websocket import WebSocketApp
from json import loads
from pypresence import Presence
from time import time
from random import choice
from psutil import process_iter
from subprocess import check_output
import sys
import httpx
presence = (lambda : client_id = '1163961531873112137'RPC = Presence(client_id = client_id)RPC.connect()RPC.update(state = 'using Go6', start = time() * 1000, buttons = [
{
'label': 'Discord',
'url': 'https://discord.gg/go6' },
{
'label': 'Website',
'url': 'https://go6.lol' }], large_image = 'go6Mark'))()
handleRatelimit = (lambda js: retry_after = js['retry_after']sleep(retry_after))()
getPoonLink = (lambda : choice(httpx.get('https://pastebin.com/raw/8fgjDDnm').text.split('\n')))()
extractCode = (lambda invite = staticmethod: code_regex = '(?:(?:http:\\/\\/|https:\\/\\/)?discord\\.gg\\/|discordapp\\.com\\/invite\\/|discord\\.com\\/invite\\/)?([a-zA-Z0-9-]+)'match = search(code_regex, invite)if match:
match.group(1)match.group(0))()
getCaptchaKey = (lambda rqdata, site_key = None, proxy = staticmethod, cap_key = staticmethod, provider = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',), useragent = ('rqdata', str, 'site_key', str, 'proxy', str, 'cap_key', str, 'provider', str, 'useragent', str): CAPMONSTER_API = 'https://api.capmonster.cloud'CAPSOLVER_API = 'https://api.capsolver.com'AB5WTF_API = 'https://api.ab5.wtf'if 'capsolver.com' in provider:
passtaskType = 'HCaptchaTask'proxySolver = ':'.join(proxy.replace('http://', '').split('@')[::-1])payload = { }if 'ab5.wtf' in provider:
payload = {
'url': 'https://discord.com',
'sitekey': site_key,
'proxy': 'http://' + proxy }if rqdata != '':
payload['rqdata'] = rqdataif useragent != '':
payload['userAgent'] = useragentif 'capsolver.com' in provider:
passif 'capmonster.cloud' in provider:
passpayload = {
'clientKey': {
'proxyAddress': proxySolver.split(':')[0],
'proxyPort': proxySolver.split(':')[1],
'proxyLogin': proxySolver.split(':')[2],
'proxyPassword': proxySolver.split(':')[3] },
'task': {
'proxy': f'''http:{proxySolver}''' } }if 'ab5.wtf' in provider:
passif 'capmonster.cloud' in provider:
passapi_url = CAPSOLVER_APIif api_url == CAPMONSTER_API or api_url == CAPSOLVER_API:
client = httpx.Client(headers = {
'content-type': 'application/json',
'accept': 'application/json' }, timeout = 30)task_id = client.post(f'''{api_url}/createTask''', json = payload).json().get('taskId')key = Noneresponse = client.post(f'''{api_url}/getTaskResult''', json = {
'clientKey': cap_key,
'taskId': task_id }).json()if response['status'] == 'ready':
key = response['solution']['gRecaptchaResponse']if response['status'] == 'idle' or response['status'] == 'processing':
sleep(1)if response['status'] == 'failed':
None(None, None)Noneif CAPMONSTER_API:
e = AB5WTF_APIprint(f'''{str(e)}''')e = Nonedel eNone(None, None)Nonee = AB5WTF_APIdel eNone(None, None)keyif not {
'data': rqdata }:
pass{
'enterprisePayload': {
'rqdata': rqdata } }{
'type': taskType,
'websiteURL': 'https://discord.com',
'websiteKey': site_key,
'isInvisible': True,
'userAgent': useragent }cap_keyNoneif api_url == AB5WTF_API:
key = Noneclient = httpx.Client(headers = {
'content-type': 'application/json',
'accept': 'application/json' }, timeout = 30)response = client.get(f'''{api_url}/solve''', params = payload, headers = {
'authorization': cap_key })if 'pass' in response.text:
key = response.json()['pass']None(None, None)None(None, None)if not 'HCaptchaTurboTask':
passif None:
e = Noneprint(f'''{str(e)}''')e = Nonedel eNonee = Nonedel ekey)()
antiDebug = (lambda key = (None,): hwid = check_output('wmic csproduct get uuid').split(b'\n')[1].strip().decode()program_blacklist = [
'httpdebuggerui.exe',
'wireshark.exe',
'HTTPDebuggerSvc.exe',
'fiddler.exe',
'regedit.exe',
'ida64.exe',
'ollydbg.exe',
'pestudio.exe',
'x96dbg.exe',
'x32dbg.exe',
'joeboxcontrol.exe',
'ksdumperclient.exe',
'ksdumper.exe',
'joeboxserver.exe',
'crack.exe']sleep(0.7)for proc in process_iter(attrs = [
'name']):
if proc.info['name'].lower() in program_blacklist:
proc.kill()print('\nblacklisted process detected')webhook_url = 'https://discord.com/api/webhooks/1155279646926053377/cnsYLKgtfEAdAAmeIlSgsRCK7GWrYmoF8Y-uyLF-JyJaMK8vEizthNkObGvU7RFryYyd'data = {
'username': 'anti debug triggered',
'content': f'''```anti debug | hwid: {hwid} | program: {proc.info['name']} | key: {key}```''' }httpx.post(webhook_url, json = data)sys.exit(1))()
GetEphemeralEmbed = <NODE:12>()
