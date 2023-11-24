# Decompiled with EinTimDC
import json
import uuid
import base64
import httpx
import random
import tls_client
import re
from random import randint as rd
from colorama import Fore

class Client:
    __qualname__ = 'Client'
    
    def __init__(self = None):
        buildinfo = self.get_build()
        self.build_number = buildinfo['build_number']
        self._app_version = buildinfo['app_version']
        self._go6__darwin_ver = self.get_darwin()
        print(self.build_number)
        print(self._app_version)
        print(self._go6__darwin_ver)

    
    def mobile_xprops(self):
        u = uuid.uuid4().hex
        vendor_uuid = f'''{u[0:8]}-{u[8:12]}-{u[12:16]}-{u[16:20]}-{u[20:36]}'''
        iphone_models = [
            '11,2',
            '11,4',
            '11,6',
            '11,8',
            '12,1',
            '12,3',
            '12,5',
            '12,8',
            '13,1',
            '13,2',
            '13,3',
            '13,4',
            '14,2',
            '14,3',
            '14,4',
            '14,5',
            '14,6',
            '14,7',
            '14,8',
            '15,2',
            '15,3']
        return base64.b64encode(json.dumps({
            'os': 'iOS',
            'browser': 'Discord iOS',
            'device': 'iPhone' + random.choice(iphone_models),
            'system_locale': 'sv-SE',
            'client_version': self._app_version,
            'release_channel': 'stable',
            'device_vendor_id': vendor_uuid,
            'browser_user_agent': '',
            'browser_version': '',
            'os_version': self.iv1 + '.' + self.iv2,
            'client_build_number': self.build_number,
            'client_event_source': None,
            'design_id': 0 }).encode()).decode()

    
    def get_build(self):
        body = httpx.get('https://apps.apple.com/us/app/discord-chat-talk-hangout/id985746746', headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' }).text
        app_version = re.search('latest__version">Version (.*?)</p>', body).group(1)
        build_number = httpx.get(f'''https://discord.com/ios/{app_version}/manifest.json''').json()['metadata']['build']
        None(f'''{print.RED}discord hasnt added manifest for {app_version} fire''')
        app_version = float(app_version) - 1
        return {
            'build_number': int(build_number),
            'app_version': str(app_version) }

    
    def get_darwin(self):
        darwin_wiki = httpx.get('https://en.wikipedia.org/wiki/Darwin_(operating_system)').text
        return re.search('Latest release.*?<td class="infobox-data">(.*?) /', darwin_wiki).group(1)

    
    def get_session(self = None, token = None, proxy = None):
        user_agent = f'''Discord/{self.build_number} CFNetwork/1408.0.4 Darwin/{self._go6__darwin_ver}'''
        self.iv1 = str(rd(1, 5))
        self.iv2 = str(rd(15, 16))
        session = tls_client.Session(client_identifier = f'''safari_ios_{self.iv1}_{self.iv2}''', random_tls_extension_order = True)
        session.headers = {
            'Host': 'discord.com',
            'x-debug-options': 'bugReporterEnabled',
            'Content-Type': 'application/json',
            'Accept': '/',
            'User-Agent': user_agent,
            'Accept-Language': 'sv-SE',
            'x-discord-locale': 'sv-SE',
            'x-super-properties': self.mobile_xprops() }
        if token:
            session.headers['Authorization'] = token
        cookies = dict(session.get('https://discord.com').cookies)
        session.headers.update({
            'Cookie': f'''__cfruid={cookies['__cfruid']}; __dcfduid={cookies['__dcfduid']}; __sdcfduid={cookies['__sdcfduid']}''' })
        if proxy:
            session.proxies = proxy
            session.timeout_seconds = 0
        return session


