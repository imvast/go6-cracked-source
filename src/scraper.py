# Decompiled with EinTimDC
import websocket
import json
import threading
import time

class Utils:
    __qualname__ = 'Utils'
    
    def rangeCorrector(ranges):
        if [
            0,
            99] not in ranges:
            ranges.insert(0, [
                0,
                99])
        return ranges

    
    def getRanges(index, multiplier, memberCount):
        initialNum = int(index * multiplier)
        rangesList = [
            [
                initialNum,
                initialNum + 99]]
        if memberCount > initialNum + 99:
            rangesList.append([
                initialNum + 100,
                initialNum + 199])
        return None.rangeCorrector(rangesList)

    
    def parseGuildMemberListUpdate(response):
        memberdata = {
            'online_count': response['d']['online_count'],
            'member_count': response['d']['member_count'],
            'id': response['d']['id'],
            'guild_id': response['d']['guild_id'],
            'hoisted_roles': response['d']['groups'],
            'types': [],
            'locations': [],
            'updates': [] }
        for chunk in response['d']['ops']:
            memberdata['types'].append(chunk['op'])
            if chunk['op'] in ('SYNC', 'INVALIDATE'):
                memberdata['locations'].append(chunk['range'])
                if chunk['op'] == 'SYNC':
                    memberdata['updates'].append(chunk['items'])
                memberdata['updates'].append([])
            if chunk['op'] in ('INSERT', 'UPDATE', 'DELETE'):
                memberdata['locations'].append(chunk['index'])
                if chunk['op'] == 'DELETE':
                    memberdata['updates'].append([])
                memberdata['updates'].append(chunk['item'])
                return memberdata



class DiscordSocket(websocket.WebSocketApp):
    __qualname__ = 'DiscordSocket'
    
    def __init__(self = None, token = None, guild_id = None, channel_id = None):
        self.token = token
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.socket_headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0' }
        None(None, header = None, on_open = None, on_message = None, on_close = (lambda ws = None, close_code = None, close_msg = None: self.sock_close(ws, close_code, close_msg)))
        self.endScraping = False
        self.guilds = { }
        self.members = { }
        self.ranges = [
            [
                0,
                0]]
        self.lastRange = 0
        self.packets_recv = 0

    
    def run(self):
        self.run_forever()
        return self.members

    
    def scrapeUsers(self):
        if self.endScraping == False:
            self.send('{"op":14,"d":{"guild_id":"' + self.guild_id + '","typing":true,"activities":true,"threads":true,"channels":{"' + self.channel_id + '":' + json.dumps(self.ranges) + '}}}')
            return None

    
    def sock_open(self, ws):
        self.send('{"op":2,"d":{"token":"' + self.token + '","capabilities":125,"properties":{"os":"Windows","browser":"Firefox","device":"","system_locale":"it-IT","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0","browser_version":"94.0","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":103981,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')

    
    def heartbeatThread(self, interval):
        self.send('{"op":1,"d":' + str(self.packets_recv) + '}')
        time.sleep(interval)
        if None:
            e = None
            e = None
            del e
            return None
        e = None
        del e

    
    def sock_message(self, ws, message):
        decoded = json.loads(message)
        if decoded['op'] != 11:
            (self.packets_recv += 1).packets_recv = decoded
        if decoded['op'] == 10:
            threading.Thread(target = self.heartbeatThread, args = (decoded['d']['heartbeat_interval'] / 1000,), daemon = True).start()
        if decoded['t'] == 'READY':
            for guild in decoded['d']['guilds']:
                self.guilds[guild['id']] = {
                    'member_count': guild['member_count'] }
                if decoded['t'] == 'READY_SUPPLEMENTAL':
                    self.ranges = endScraping.getRanges(0, 100, self.guilds[self.guild_id]['member_count'])
                    self.scrapeUsers()
                    return None
                if None['t'] == 'GUILD_MEMBER_LIST_UPDATE':
                    parsed = endScraping.parseGuildMemberListUpdate(decoded)
                    if parsed['guild_id'] == self.guild_id:
                        if 'SYNC' in parsed['types'] or 'UPDATE' in parsed['types']:
                            for elem, index in enumerate(parsed['types']):
                                if index == 'SYNC':
                                    if len(parsed['updates'][elem]) == 0:
                                        self.endScraping = True
                                    for item in parsed['updates'][elem]:
                                        if 'member' in item:
                                            mem = item['member']
                                            obj = {
                                                'tag': mem['user']['username'],
                                                'avatar': mem['user']['avatar'] }
                                            self.members[mem['user']['id']] = obj
                                            if index == 'UPDATE':
                                                for item in parsed['updates'][elem]:
                                                    if 'member' in item:
                                                        mem = item['member']
                                                        obj = {
                                                            'tag': mem['user']['username'],
                                                            'id': mem['user']['id'],
                                                            'avatar': mem['user']['avatar'] }
                                                        self.members[mem['user']['id']] = obj
                                                        (self.lastRange += 1).lastRange = None
                                                        self.ranges = endScraping.getRanges(self.lastRange, 100, self.guilds[self.guild_id]['member_count'])
                                                        time.sleep(0.35)
                                                        self.scrapeUsers()
                                                        if self.endScraping:
                                                            self.close()
                                                            return None
                                                        return None
                                                    return None

    
    def sock_close(self, ws, close_code, close_msg):
        pass

    __classcell__ = None

