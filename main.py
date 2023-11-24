# Decompiled with EinTimDC
from src.gui import *
from src.discord import Discord
from src.console import Console
from src.utils import *
from src.scraper import *
from src.keyauth import api
from json import loads
from itertools import cycle
from random import choice, choices, shuffle, randint
from base64 import b64decode
from unidecode import unidecode
from string import ascii_letters, digits
from bs4 import BeautifulSoup
from re import sub
from os import path, listdir, mkdir
import sys
import threading
import httpx
import hashlib
VERSION = '3.0.2'

class Go6(Ui_MainWindow):
    
    def __init__(self = None, window = None):
        global spammerSwitch, voiceSwitch, threadSwitch, dmSwitch, nickSwitch, wbkSwitch
        super().__init__()
        self.cns = Console()
        self.cns.clear()
        self.cns.title(f'''Go6V{json}''')
        
        def getchecksum():
            md5_hash = hashlib.md5()
            file = open(''.join(hexdigest.argv), 'rb')
            md5_hash.update(file.read())
            digest = md5_hash.hexdigest()
            return digest

        keyauthapp = api(name = 'go6auth', ownerid = 'UB9tBmpPo4', secret = '8aced7aed00c13aa72505ccad026f8602fdd1fb606059911c161666750b8cd28', version = json, hash_to_check = getchecksum())
        if not path.exists('data'):
            mkdir('data')
        if not path.exists('data/pfp'):
            mkdir('data/pfp')
        if not path.exists('data/scraped'):
            mkdir('data/scraped')
        config_data = {
            'key': '',
            'captcha_key': '',
            'provider': '',
            'show_discord_rpc': False }
        if not path.exists('data/config.json'):
            config_file = open('data/config.json', 'w')
            provider.dump(config_data, config_file, indent = 4)
            None(None, None)
            if not None:
                pass
        if not path.exists('data/tokens.txt'):
            tokens_file = open('data/tokens.txt', 'w')
            tokens_file.write('')
            None(None, None)
            if not None:
                pass
        if not path.exists('data/proxies.txt'):
            proxies_file = open('data/proxies.txt', 'w')
            proxies_file.write('')
            None(None, None)
            if not None:
                pass
        f = open('data/config.json', 'r')
        data = loads(f.read())
        if data['show_discord_rpc']:
            presence()
        if not data['key']:
            print('Invalid config')
            sys.exit(1)
        self.solveCaptcha = False
        if len(data['captcha_key']) in (32, 36, 40) and data['provider'] not in ('capmonster.cloud', 'capsolver.com', 'ab5.wtf'):
            print('Invalid config')
            sys.exit(1)
        self.solveCaptcha = True
        self.capkey = data['provider']
        self.provider = data['captcha_key']
        None(None, None)
        if not None:
            pass
        keyauthapp.license(data['key'])
        self.cns.clear()
        self.cns.logo()
        f = open('data/tokens.txt', 'r')
        self.tokens = f.read().splitlines()
        if self.tokens == []:
            print('Invalid config')
            sys.exit(1)
        None(None, None)
        if not None:
            pass
        self.useProxy = False
        f = open('data/proxies.txt', 'r')
        data = f.read().splitlines()
        if not data == []:
            if ':' not in ''.join(data):
                print('Invalid config')
                sys.exit(1)
            if len(data) > 99:
                data[:99]
            self.useProxy = True
        self.proxies = cycle(data)
        None(None, None)
        if not None:
            pass
        spammerSwitch = False
        voiceSwitch = False
        threadSwitch = False
        dmSwitch = False
        nickSwitch = False
        wbkSwitch = False
        self.setupUi(window)
        window.setWindowFlags(inputChanneliD_VC_2.Qt.FramelessWindowHint)
        window.setFixedSize(1059, 555)
        window.setWindowTitle(f'''Go6V{json} | \'dont beg it\'''')
        self.labelMaxTokens_H_2.setText(str(json))
        self.buttonClose.clicked.connect(window.close)
        self.buttonMinimize.clicked.connect(window.showMinimized)
        None((lambda : self.stackedWidget.setCurrentIndex(0)))
        None((lambda : self.stackedWidget.setCurrentIndex(1)))
        None((lambda : self.stackedWidget.setCurrentIndex(2)))
        None((lambda : self.stackedWidget.setCurrentIndex(3)))
        None((lambda : self.stackedWidget.setCurrentIndex(4)))
        None((lambda : self.stackedWidget.setCurrentIndex(5)))
        None((lambda : self.stackedWidget.setCurrentIndex(6)))
        None((lambda : self.stackedWidget.setCurrentIndex(7)))
        None((lambda : self.stackedWidget.setCurrentIndex(8)))
        None((lambda : self.stackedWidget.setCurrentIndex(9)))
        None((lambda : self.stackedWidget_2.setCurrentIndex(0)))
        None((lambda : self.stackedWidget_2.setCurrentIndex(1)))
        None((lambda : self.stackedWidget_2.setCurrentIndex(2)))
        None((lambda : self.stackedWidget_3.setCurrentIndex(0)))
        None((lambda : self.stackedWidget_3.setCurrentIndex(1)))
        inputfields = [
            self.inputInvite_GM,
            self.inputMessageiD_RB,
            self.inputChanneliD_RB,
            self.inputEmoji_RB,
            self.inputMessage_MB,
            self.inputChanneliD_MB,
            self.inputMessageiD_BB,
            self.inputChanneliD_BB,
            self.inputGuildiD_BB,
            self.inputChanneliDSpam_MS,
            self.inputGuildiD_MS,
            self.inputChanneliD_VC,
            self.inputChanneliD_VC_2,
            self.inputChanneliD_TS,
            self.inputGuildiD_TS,
            self.inputThreadName_TS,
            self.inputThreadMessage_TS,
            self.inputUseriD_DM,
            self.inputNickname_NS,
            self.inputGuildiD_NS,
            self.inputWebhookUrl_WS,
            self.inputGroupiD_GS,
            self.inputGroupInviteLink_GS,
            self.inputDisplay_TC,
            self.inputPronouns_TC,
            self.inputBio_TC]
        placeholders = [
            'discord.gg/invitecode',
            'message id',
            'channel id',
            '👍',
            'message',
            'channel id',
            'message id',
            'channel id',
            'guild id',
            'channel id',
            'guildid',
            'guild id',
            'channelid',
            'channel id',
            'guild id',
            'thread name',
            'thread message',
            'user id',
            'nickname',
            'guild id',
            'webhook url',
            'group id',
            'group invite',
            'display name',
            'pro/nouns',
            'bio']
        for field, text in zip(inputfields, placeholders):
            field.setPlaceholderText(text)
            field.setAlignment(inputChanneliD_VC_2.Qt.AlignCenter)
            buttonfunc = [][self.checkTokensLauncher][self.checkProxiesLauncher][self.guildJoinLauncher][self.guildLeaveLauncher][self.guildCheckerLauncher][self.reactionBypassLauncher][self.messageBypassLauncher][self.buttonBypassLauncher][self.refreshTokens][self.refreshProxies][(self.checkTokensLauncher, True)][(self.checkProxiesLauncher, True)][self.channelSpammerLauncher][self.parseUsersLauncher][(self.voiceLauncher, 'voiceJoiner')][(self.voiceLauncher, 'voiceLeaver')][(self.voiceLauncher, 'voiceSpammer')][self.threadSpammerLauncher][self.dmSpammerLauncher][(self.nickChangerLauncher, 'num')][(self.nickChangerLauncher, 'random')][(self.nickChangerLauncher, 'spamsetunset')][self.nickChangerLauncher][(self.nickChangerLauncher, 'reset')][(self.webhookSpammerLauncher, True)][self.webhookSpammerLauncher][(self.groupLauncher, 'join')][(self.groupLauncher, 'leave')][(self.groupLauncher, 'joinvc')][(self.groupLauncher, 'leavevc')][(self.tokenConfigLauncher, 'bio')][(self.tokenConfigLauncher, 'display')][(self.tokenConfigLauncher, 'pfp')][(self.tokenConfigLauncher, 'pronouns')][(self.tokenConfigLauncher, 'preset')][(self.tokenConfigLauncher, 'breset')][(self.tokenConfigLauncher, 'dreset')][(self.tokenConfigLauncher, 'preset')][(self.utilsLauncher, 'clear')]
            buttons = [][self.buttonStartCheckTokens_H][self.buttonStartCheckProxies_H][self.buttonJoin_GM][self.buttonLeave_GM][self.buttonLeave_GM_2][self.buttonStartReactionBypass_RB][self.buttonStartMessageBypass_MB][self.buttonStartButtonBypass_BB][self.buttonStartLoadTokens_H][self.buttonStartLoadProxies_H][self.buttonStartLoadTokens_H_3][self.buttonStartLoadTokens_H_6][self.buttonStartSpam_MS][self.buttonParseUsers_MS][self.buttonStartJoin_VC][self.buttonStartLeave_VC][self.buttonStartSpam_VC][self.buttonStartThreadSpam_TS][self.buttonStartSpamDM_DM][self.buttonStartSpamNumNick_NS][self.buttonStartSpamRandomNick_NS][self.buttonStartSpamRandomNick_NS][self.buttonStartChangeNick_NS][self.buttonStartResetNick_NS][self.buttonStartChangeNick_WS][self.buttonStartChangeNick_WS_2][self.buttonStartJoinGroup_GS][self.buttonStartLeaveGroup_GS][self.buttonStartJoinGroup_GS][self.buttonStartLeaveGroup_GS][self.buttonStartSetBio_TC][self.buttonStartSetDisplay_TC][self.buttonStartSetPfp_TC][self.buttonStartSetPronouns_TC][self.buttonStartUnsetPronouns_TC][self.buttonStartUnsetBio_TC][self.buttonStartUnsetDisplay_TC][self.buttonStartUnsetPfp_TC][self.buttonStartSetDisplay_TC_3]
            for button, func in zip(buttons, buttonfunc):
                if None(isinstance, func):
                    (f, a) = func
                    button.clicked.connect((lambda _, f, a = (f, a): None(target = (lambda : f())).start()
))
                button.clicked.connect((lambda _, f = (func,): threading.Thread(target = f).start()))
                [][self.buttonStartCheckTokens_H][self.buttonStartCheckProxies_H][self.buttonJoin_GM][self.buttonLeave_GM][self.buttonLeave_GM_2][self.buttonStartReactionBypass_RB][self.buttonStartMessageBypass_MB][self.buttonStartButtonBypass_BB][self.buttonStartLoadTokens_H][self.buttonStartLoadProxies_H][self.buttonStartLoadTokens_H_3][self.buttonStartLoadTokens_H_6][self.buttonStartSpam_MS][self.buttonParseUsers_MS][self.buttonStartJoin_VC][self.buttonStartLeave_VC][self.buttonStartSpam_VC][self.buttonStartThreadSpam_TS][self.buttonStartSpamDM_DM][self.buttonStartSpamNumNick_NS][self.buttonStartSpamRandomNick_NS][self.buttonStartSpamRandomNick_NS][self.buttonStartChangeNick_NS][self.buttonStartResetNick_NS][self.buttonStartChangeNick_WS][self.buttonStartChangeNick_WS_2][self.buttonStartJoinGroup_GS][self.buttonStartLeaveGroup_GS][self.buttonStartJoinGroup_GS][self.buttonStartLeaveGroup_GS][self.buttonStartSetBio_TC]((lambda : threading.Thread(target = self.updateSliderValue).start()))
                self.sliderMaxTokens_H.setMaximum(len(self.tokens))
                self.sliderMaxTokens_H.setValue(len(self.tokens))
                self.checkUseProxy_H.stateChanged.connect(self.updateUseProxy)
                if self.useProxy:
                    self.checkUseProxy_H.setChecked(True)
        (lambda .0: for filename in .0:
[ filename ])(listdir('data/pfp')())
        self.listBotBypass_GM.addItems([
            '',
            'restorecord',
            'sledgehammer',
            'doublecounter'])
        self.checkAlwaysOnTop_UC.setDisabled(True)
        self.checkAlwaysOnTop_UC.setStyleSheet('QCheckBox {\n                background: transparent;\n                padding: 3px;\n                color: #FFF;\n                border: None;\n            }\n            QCheckBox::indicator {\n                border: 2px solid #656263;\n                width: 15px;\n                height: 15px;\n                border-radius: 7px;\n            }\n            QCheckBox::indicator:checked {\n                background: #656263;\n            }')

    
    def updateSliderValue(self):
        value = self.sliderMaxTokens_H.value()
        self.labelTokensCount_H.setText(str(value))

    
    def updateUseProxy(self, state):
        if state == QtCore.Qt.Checked:
            self.useProxy = True
            return None
        self.useProxy = None

    
    def getProxy(self):
        if self.useProxy:
            return next(self.proxies)

    
    def getTokenIDS(self):
        ids = []
        self.tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        for token in self.tokens:
            idd = b64decode(token[0][:24].encode()).decode()
            ids.append(idd)
            return ids

    
    def getCaptchaKey(self = None, js = None):
        if self.solveCaptcha:
            rqdata = js['captcha_rqdata']
            rqtoken = js['captcha_rqtoken']
            site_key = js['captcha_sitekey']
            key = getCaptchaKey(rqdata = rqdata, site_key = site_key, cap_key = self.capkey, provider = self.provider, proxy = self.getProxy())
            return (None, None)
        return (None, rqtoken)
        return (None, None)

    
    def splitList(self, a, n, limit = (None,)):
        (k, m) = divmod(len(a), n)
        split_lines = a()
        tokens = (lambda .0 = None: for i in .0:
split_lines[i * k + min(i, m):(i + 1) * k + min(i + 1, m)]None)(range(n)())
        return tokens[:limit]
        return tokens

    
    def checkTokens(self = None, tokens = None, v = None):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (st, resp) = dc.check()
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Valid -> {token}''')
                v.append(token)
            js = resp.json()
            if resp.status_code == 401:
                self.cns.info(f'''Failed to authorize -> {token}''')
            self.cns.info(f'''Failed to check -> {js}''')
            return None

    
    def checkTokensLauncher(self, removeinv = (False,)):
        v = []
        threads = []
        for token in self.splitList(self.tokens, len(self.tokens)):
            thread = threading.Thread(target = self.checkTokens, args = (token, v))
            thread.start()
            threads.append(thread)
            for thread in threads:
                thread.join()
                if removeinv:
                    file = open('data/tokens.txt', 'w')
                    file.write('\n'.join(v))
                    None(None, None)
                    return None
                if not None:
                    pass
        return None

    
    def checkProxies(self = None, proxies = None, v = None):
        for proxy in proxies:
            dc = Discord(proxy, None)
            (st, resp) = dc.checkConnection()
            if error:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Valid -> {proxy}''')
                v.append(proxy)
            js = resp.json()
            if resp.status_code == 400:
                self.cns.info(f'''Failed to connect -> {proxy}''')
            self.cns.info(f'''Failed to check -> {js}''')
            return None

    
    def checkProxiesLauncher(self, removeinv = (False,)):
        v = []
        threads = []
        for proxy in open('data/proxies.txt', 'r').readlines()():
            thread = threading.Thread(target = self.checkProxies, args = ([
                proxy], v))
            thread.start()
            threads.append(thread)
            for thread in threads:
                thread.join()
                if removeinv:
                    file = open('data/proxies.txt', 'w')
                    file.write('\n'.join(v))
                    None(None, None)
                    return None
                if not (lambda .0: for line in .0:
[ line.strip() ]):
                    pass
        return None

    
    def refreshTokens(self):
        file = open('data/tokens.txt', 'r')
        self.tokens = file.read().splitlines()()
        self.sliderMaxTokens_H.setMaximum(len(self.tokens))
        self.sliderMaxTokens_H.setValue(len(self.tokens))
        self.cns.info(f'''Loaded tokens -> {len(self.tokens)}''')
        None(None, None)
        return None
        if not (lambda .0: for line in .0:
[ line.strip() ]):
            pass

    
    def refreshProxies(self):
        file = open('data/proxies.txt', 'r')
        lines = file.read().splitlines()
        if len(lines) > 99:
            lines = lines[:99]
        None(None, None)
        if not None:
            pass
        file = open('data/proxies.txt', 'w')
        file.write('\n'.join(lines))
        None(None, None)
        if not None:
            pass
        self.proxies = (lambda .0: for line in .0:
[ line.strip() ])(lines())
        self.cns.info(f'''Loaded proxies -> {len(lines)}''')

    
    def verifyRestoreCord(self = None, tokens = None, guildID = None):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            clientID = dc.getClientID('https://restorecord.com/verify/', guildID)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            (st, resp) = dc.acceptRestoreCord(guildID, clientID)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Bypassed RestoreCord -> {guildID}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to bypass -> ratelimit')
            self.cns.info(f'''Failed to bypass -> {js}''')
            return None

    
    def verifySledgeHammer(self = None, tokens = None, guildID = None):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (cid, mid, aid) = dc.findIDs(guildID, 'Sledgehammer', 'you need to prove that you are a human')
            if str:
                e = None
                e = None
                del e
                self.cns.error(f'''-> {str(e)}''')
                return None
            e = None
            del e
            (st, resp) = dc.acceptSledgeHammer(aid, cid, mid, guildID)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Bypassed SledgeHammer -> {guildID}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to verify -> ratelimit')
            self.cns.info(f'''Failed to verify -> {js}''')
            return None

    
    def verifyDoubleCounter(self = None, tokens = None, guildID = None, channelID = ('tokens', list, 'guildID', str, 'channelID', str)):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (st, resp) = dc.createDM('703886990948565003', guildID, channelID)
            if str:
                e = None
                e = None
                del e
                self.cns.error(f'''-> {str(e)}''')
                return None
            e = None
            del e
            (st, resp) = dc.acceptDoubleCounter(resp.json()['id'])
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Bypassed DoubleCounter -> {guildID}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to verify -> ratelimit')
            self.cns.info(f'''Failed to verify -> {js}''')
            return None

    
    def guildJoin(self, tokens, invite, context = None, botBypass = None, guildID = None, rqtoken = (None, None, None), captcha = ('tokens', list, 'invite', str, 'context', str, 'botBypass', str, 'guildID', str, 'rqtoken', str, 'captcha', str)):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (st, resp) = dc.join(invite, context, rqtoken, captcha)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                js = resp.json()
                if verifyDoubleCounter.decoder.JSONDecodeError:
                    je = None
                    self.cns.error(f'''-> {str(je)}''')
                    je = None
                    del je
                    je = None
                    del je
                self.cns.success(f'''Joined -> {invite}''')
                if guildID != '':
                    levels = js['guild']['features']
                if 'MEMBER_VERIFICATION_GATE_ENABLED' in levels and guildID != '':
                    (st, resp) = dc.acceptRules(invite, guildID)
                    if st:
                        self.cns.success(f'''Bypassed rules -> {invite}''')
                    js = resp.json()
                    self.cns.info(f'''Failed to bypass rules -> {js}''')
                if 'GUILD_ONBOARDING_EVER_ENABLED' in levels and guildID != '':
                    (st, resp) = dc.acceptOnBoarding(guildID)
                    if st:
                        self.cns.success(f'''Bypassed onboarding menu -> {invite}''')
                    js = resp.json()
                    self.cns.info(f'''Failed to bypass onboarding -> {js}''')
                if botBypass == 'doublecounter' and guildID != '':
                    channelID = js['channel']['id']
                    self.verifyDoubleCounter([
                        token], guildID, channelID)
                if botBypass == 'sledgehammer' and guildID != '':
                    self.verifySledgeHammer([
                        token], guildID)
                if botBypass == 'restorecord' and guildID != '':
                    self.verifyRestoreCord([
                        token], guildID)
                    js = resp.json()
                    if resp.status_code == 429:
                        self.cns.info('Failed to join -> ratelimit')
            if None == 400:
                self.cns.info('Failed to join -> captcha')
                (captcha, rqtoken) = self.getCaptchaKey(js)
                self.guildJoin([
                    token], invite, context, botBypass, guildID, rqtoken = rqtoken, captcha = captcha)
            self.cns.info(f'''Failed to join -> {js}''')
            return None

    
    def guildJoinLauncher(self):
        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        inv = self.inputInvite_GM.text()
        bot = self.listBotBypass_GM.currentText()
        inv = extractCode(inv)
        if start:
            e = None
            self.cns.error(f'''-> {str(e)}''')
            e = None
            del e
            return None
        e = None
        del e
        (guildid, context) = Discord.getContextProperties(inv)
        if start:
            e = None
            self.cns.error(f'''-> {str(e)}''')
            e = None
            del e
            return None
        e = None
        del e
        threads = []
        for i in range(len(tokens)):
            token = tokens[i % len(tokens)]
            thread = threading.Thread(target = self.guildJoin, args = (token, inv, context, bot, guildid))
            thread.start()
            threads.append(thread)
            for thread in threads:
                thread.join()
                return None

    
    def guildLeave(self = None, tokens = None, guildID = None):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (st, resp) = dc.leave(guildID)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Left -> {guildID}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to leave -> ratelimit')
            self.cns.info(f'''Failed to leave -> {js}''')
            return None

    
    def guildLeaveLauncher(self):
        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        inv = self.inputInvite_GM.text()
        inv = extractCode(inv)
        if Thread:
            e = None
            self.cns.error(f'''-> {str(e)}''')
            e = None
            del e
            return None
        e = None
        del e
        (guildid, context) = Discord.getContextProperties(inv)
        if Thread:
            e = None
            self.cns.error(f'''-> {str(e)}''')
            e = None
            del e
            return None
        e = None
        del e
        threads = []
        for i in range(len(tokens)):
            token = tokens[i % len(tokens)]
            thread = threading.Thread(target = self.guildLeave, args = (token, guildid))
            thread.start()
            threads.append(thread)
            for thread in threads:
                thread.join()
                return None

    
    def guildChecker(self = None, tokens = None, guildID = None):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (st, resp) = dc.checkGuild(guildID)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Vaild guild -> {guildID}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to check -> ratelimit')
            self.cns.info(f'''Failed to check -> {js}''')
            return None

    
    def guildCheckerLauncher(self):
        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        inv = self.inputInvite_GM.text()
        inv = extractCode(inv)
        if Thread:
            e = None
            self.cns.error(f'''-> {str(e)}''')
            e = None
            del e
            return None
        e = None
        del e
        (guildid, context) = Discord.getContextProperties(inv)
        if Thread:
            e = None
            self.cns.error(f'''-> {str(e)}''')
            e = None
            del e
            return None
        e = None
        del e
        threads = []
        for i in range(len(tokens)):
            token = tokens[i % len(tokens)]
            thread = threading.Thread(target = self.guildChecker, args = (token, guildid))
            thread.start()
            threads.append(thread)
            for thread in threads:
                thread.join()
                return None

    
    def reactionBypass(self, tokens = None, messageID = None, channelID = None, emoji = ('tokens', list, 'messageID', str, 'channelID', str, 'emoji', str)):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (st, resp) = dc.reaction(messageID, channelID, emoji)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Executed reaction -> {messageID}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to execute -> ratelimit')
            self.cns.info(f'''Failed to execute -> {js}''')
            return None

    
    def reactionBypassLauncher(self):
        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        cid = self.inputChanneliD_RB.text()
        mid = self.inputMessageiD_RB.text()
        emoji = self.inputEmoji_RB.text()
        threads = []
        for i in range(len(tokens)):
            token = tokens[i % len(tokens)]
            thread = threading.Thread(target = self.reactionBypass, args = (token, mid, cid, emoji))
            thread.start()
            threads.append(thread)
            for thread in threads:
                thread.join()
                return None

    
    def messageBypass(self = None, tokens = None, channelID = None, message = ('tokens', list, 'channelID', str, 'message', str)):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (st, resp) = dc.sendMessage(channelID, message)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Sent message -> {channelID}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to execute -> ratelimit')
            self.cns.info(f'''Failed to execute -> {js}''')
            return None

    
    def messageBypassLauncher(self):
        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        cid = self.inputChanneliD_MB.text()
        msg = self.inputMessage_MB.text()
        threads = []
        for i in range(len(tokens)):
            token = tokens[i % len(tokens)]
            thread = threading.Thread(target = self.messageBypass, args = (token, cid, msg))
            thread.start()
            threads.append(thread)
            for thread in threads:
                thread.join()
                return None

    
    def buttonBypass(self, tokens = None, channelID = None, messageID = None, guildID = ('tokens', list, 'channelID', str, 'messageID', str, 'guildID', str)):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            messageshit = dc.getButton(channelID, token)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            (st, resp) = dc.button[channelID][guildID][None]()
            if str:
                e = dc.button[channelID][guildID]
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Clicked button -> {messageID}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to execute -> ratelimit')
            self.cns.info(f'''Failed to execute -> {js}''')
            return None

    
    def buttonBypassLauncher(self):
        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        cid = self.inputChanneliD_BB.text()
        gid = self.inputGuildiD_BB.text()
        mid = self.inputMessageiD_BB.text()
        threads = []
        for i in range(len(tokens)):
            token = tokens[i % len(tokens)]
            thread = threading.Thread(target = self.buttonBypass, args = (token, cid, mid, gid))
            thread.start()
            threads.append(thread)
            for thread in threads:
                thread.join()
                return None

    
    def dynoTagSpammer(self, tokens = None, channelID = None, guildID = None, message = ([],), ids = ('tokens', list, 'channelID', str, 'guildID', str, 'message', str, 'ids', list)):
        for token in tokens:
            shuffle(ids)
            ids = list(ids)
            dc = Discord(self.getProxy(), token)
            if choices:
                copyMessage = message
                if '[mtag]' in copyMessage:
                    copyMessage = copyMessage.replace('[mtag]', f'''<@{choice(ids)}>''', 1)
                if '[num]' in copyMessage:
                    copyMessage = copyMessage.replace('[num]', ''.join(choices('0123456789', k = choice([
                        8,
                        11]))))
                if '[random]' in copyMessage:
                    copyMessage = copyMessage.replace('[random]', ''.join(choices(postTag, k = choice([
                        8,
                        11]))))
                if '[poon]' in copyMessage:
                    copyMessage = copyMessage.replace('[poon]', getPoonLink(), 1)
                if '[tdyno]' in copyMessage:
                    copyMessage = copyMessage.replace('[tdyno]', '', 1)
                tagName = ''.join(choices('0123456789', k = choice([
                    8,
                    11])))
                copyMessage = '``````e ' + copyMessage + ' l```'
                (st, resp) = dc.createTag(guildID, channelID, tagName, copyMessage)
                if '[tdyno]' in copyMessage:
                    e = '[poon]' in copyMessage
                    self.cns.error(f'''-> {str(e)}''')
                    e = None
                    del e
                    e = None
                    del e
                sleep(3.9)
                if st:
                    self.cns.success(f'''Created tag -> {channelID}''')
                (st, resp) = dc.postTag(guildID, channelID, tagName)
                if '[random]' in copyMessage:
                    e = '[num]' in copyMessage
                    self.cns.error(f'''-> {str(e)}''')
                    e = None
                    del e
                    e = None
                    del e
                if st:
                    self.cns.success(f'''Sent message -> {channelID}''')
                js = resp.json()
                if resp.status_code == 429:
                    self.cns.info('Failed to send message -> ratelimit')
                    handleRatelimit(js)
                self.cns.info(f'''Failed to send message -> {js}''')
                return None

    
    def channelSpammer(self, tokens, channelID = None, message = None, modes = None, delay = ([],), ids = ('tokens', list, 'channelID', str, 'message', str, 'modes', dict, 'delay', int, 'ids', list)):
        for token in tokens:
            shuffle(ids)
            ids = cycle(ids)
            countmsg = 0
            dc = Discord(self.getProxy(), token)
            if modes['stickerspam']:
                self.cns.info('Scraping stickers -> 0')
                stickerids = dc.scrapeStickers()
                self.cns.info(f'''Scraped stickers -> {len(stickerids)}''')
            if getPoonLink:
                copyMessage = message
                if modes['antilock'] and countmsg >= 14:
                    countmsg = 0
                    sleep(2.5)
                if '[mtag]' in copyMessage:
                    if modes['hideping']:
                        pass
                    copyMessage = '[mtag]'(f'''||<@{next(ids)}>||''', f'''<@{next(ids)}>''', 1)
                if '[num]' in copyMessage:
                    copyMessage = copyMessage.replace('[num]', ''.join(choices('0123456789', k = choice([
                        8,
                        11]))))
                if '[random]' in copyMessage:
                    copyMessage = copyMessage.replace('[random]', ''.join(choices(json, k = choice([
                        8,
                        11]))))
                if '[poon]' in copyMessage:
                    copyMessage = copyMessage.replace('[poon]', getPoonLink(), 1)
                if modes['ghostpingv2']:
                    copyMessage += '||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||||||||||| @everyone\n'
                if not modes['emojispam'] and modes['ghostpingv2']:
                    random_code_point = randint(128512, 128591)
                    new_emoji = chr(random_code_point)
                    if search('[^\\x00-\\x7F]', message):
                        message = sub('[^\\x00-\\x7F]+', new_emoji, message)
                    message += ' ' + new_emoji
                if not modes['spaceletters'] and modes['ghostpingv2']:
                    copyMessage = ' '.join(copyMessage)
                if not modes['specialletters'] and modes['ghostpingv2']:
                    char_replace = {
                        'r': 'ŕ',
                        's': 'ş',
                        't': 'ţ',
                        'u': 'ù',
                        'v': 'ṽ',
                        'w': 'ŵ',
                        'x': 'ẋ',
                        'y': 'ý',
                        'z': 'ź' }
                    copyMessage = (lambda .0 = 'ŋ': for char in .0:
char_replace.get(char, char)None)(copyMessage())
                if not modes['multimsg'] and modes['ghostpingv2']:
                    copyMessage = (lambda .0: for element in .0:
[ element.text ])(BeautifulSoup(copyMessage.toHtml(), 'html.parser').find('body').descendants())
                if modes['stickerspam']:
                    pass
                (st, resp) = channelID(copyMessage, choice(stickerids), None)
                if dc.sendMessage:
                    e = choice
                    self.cns.error(f'''-> {str(e)}''')
                    e = None
                    del e
                    e = None
                    del e
                if st:
                    self.cns.success(f'''Sent message -> {channelID}''')
                    if modes['antilock']:
                        countmsg += 1
                    sleep(delay)
                js = resp.json()
                if resp.status_code == 429:
                    self.cns.info('Failed to send message -> ratelimit')
                    handleRatelimit(js)
                self.cns.info(f'''Failed to send message -> {js}''')
                return None

    
    def channelSpammerLauncher(self):
        global spammerSwitch, spammerSwitch
        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        cid = self.inputChanneliDSpam_MS.text()
        gid = self.inputGuildiD_MS.text()
        msgr = self.inputGuildiD_MS.text()
        msg = self.textSpam_MS.toPlainText()
        delay = self.sliderDelay_MS.value()
        modes = {
            'multimsg': self.checkMultiMsg_MS.isChecked(),
            'antilock': self.checkAntiLock_MS.isChecked(),
            'emojispam': self.checkEmojiSpam_MS.isChecked(),
            'ghostpingv2': self.checkGhostPing_MS.isChecked(),
            'hideping': self.checkHidePing_MS.isChecked(),
            'spaceletters': self.checkHidePing_MS_2.isChecked(),
            'specialletters': self.checkHidePing_MS_3.isChecked(),
            'stickerspam': self.checkStickerSpam_MS.isChecked() }
        if self.buttonStartSpam_MS.text() == 'Spam':
            self.buttonStartSpam_MS.setText('Stop')
            spammerSwitch = True
            ids = []
            if '[mtag]' in msg:
                ids = open(f'''data/scraped/{gid}.txt''', 'r').read().splitlines()
                if None:
                    e = None
                    self.cns.error(f'''-> {str(e)}''')
                    e = None
                    del e
                    return None
                e = None
                del e
            if '[tdyno]' in msg:
                threads = []
                for i in range(len(tokens)):
                    token = tokens[i % len(tokens)]
                    thread = threading.Thread(target = self.dynoTagSpammer, args = (token, cid, gid, msg, ids))
                    thread.start()
                    threads.append(thread)
                    for thread in threads:
                        thread.join()
                        return None
                        threads = []
                        for i in range(len(tokens)):
                            token = tokens[i % len(tokens)]
                            thread = threading.Thread(target = self.channelSpammer, args = (token, cid, msg, modes, delay, ids))
                            thread.start()
                            threads.append(thread)
                            for thread in threads:
                                thread.join()
                                return None
                                self.buttonStartSpam_MS.setText('Spam')
                                spammerSwitch = False
                                return None

    
    def parseUsers(self = None, token = None, channelID = None, guildID = ('token', str, 'channelID', str, 'guildID', str)):
        token_ids = self.getTokenIDS()
        soc = DiscordSocket(token[0], guildID, channelID)
        IDs = soc.run()
        f = open(f'''data/scraped/{guildID}.txt''', 'w+')
        data = ''
        for key, values in IDs.items():
            if key in token_ids:
                pass
            data += key + '\n'
            f.write(data)
            None(None, None)
            if not None:
                pass
        f = open('data/scraped/names.txt', 'a+', encoding = 'latin-1')
        data = ''
        for key, values in IDs.items():
            data += unidecode(values['tag']) + '\n'
            f.write(data)
            None(None, None)
            if not None:
                pass
        self.cns.success(f'''Scraped IDs -> {len(IDs)}''')
        self.labelParseCount_MS.setText(f'''parsed: {str(len(IDs))}''')
        return IDs

    
    def parseUsersLauncher(self):
        token = choice(self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value()))
        cid = self.inputChanneliDSpam_MS.text()
        gid = self.inputGuildiD_MS.text()
        self.parseUsers(token, cid, gid)

    
    def voiceJoiner(self, tokens = None, channelID = None, guildID = None, modes = ('tokens', list, 'channelID', str, 'guildID', str, 'modes', dict)):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            dc.joinVC(guildID, channelID, modes['mute'], modes['defean'], modes['video'], modes['stream'])
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            self.cns.success(f'''Executed joinvc -> {channelID}''')
            return None

    
    def voiceLeaver(self, tokens = None, channelID = None, guildID = None, modes = ('tokens', list, 'channelID', str, 'guildID', str, 'modes', dict)):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            dc.leaveVC(guildID, channelID, modes['mute'], modes['defean'], modes['video'], modes['stream'])
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            self.cns.success(f'''Executed leavevc -> {channelID}''')
            return None

    
    def voiceSpammer(self, tokens = None, channelID = None, guildID = None, modes = ('tokens', list, 'channelID', str, 'guildID', str, 'modes', dict)):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            if Exception:
                dc.joinVC(guildID, channelID, modes['mute'], modes['defean'], modes['video'], modes['stream'])
                if success:
                    e = None
                    self.cns.error(f'''-> {str(e)}''')
                    e = None
                    del e
                    e = None
                    del e
                self.cns.success(f'''Executed joinvc -> {channelID}''')
                sleep(0.4)
                dc.leaveVC(guildID, channelID, modes['mute'], modes['defean'], modes['video'], modes['stream'])
                if success:
                    e = None
                    self.cns.error(f'''-> {str(e)}''')
                    e = None
                    del e
                    e = None
                    del e
                self.cns.success(f'''Executed leavevc -> {channelID}''')
                return None

    
    def voiceLauncher(self = None, mode = None):
        print(mode)
        
        def threadf(token = None, cid = None, gid = None, modes = None):
            global voiceSwitch, voiceSwitch, voiceSwitch
            voiceSwitch = False
            if mode == 'voiceJoiner':
                self.voiceJoiner(token, cid, gid, modes)
                return None
            if None == 'voiceLeaver':
                self.voiceLeaver(token, cid, gid, modes)
                return None
            if None == 'voiceSpammer':
                if self.buttonStartSpam_VC.text() == 'Voice Spam':
                    self.buttonStartSpam_VC.setText('Stop')
                    voiceSwitch = True
                    self.voiceSpammer(token, cid, gid, modes)
                    return None
                voiceSwitch = None
                self.buttonStartSpam_VC.setText('Voice Spam')
                return None

        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        cid = self.inputChanneliD_VC.text()
        gid = self.inputChanneliD_VC_2.text()
        print(cid, gid)
        modes = {
            'mute': self.checkMuted_VC.isChecked(),
            'defean': self.checkDefeaned_VC.isChecked(),
            'video': self.checkWebcam_VC.isChecked(),
            'stream': self.checkStreaming_VC.isChecked() }
        print(modes)
        threads = []
        for i in range(len(tokens)):
            token = tokens[i % len(tokens)]
            print(token)
            thread = threading.Thread(target = threadf, args = (token, cid, gid, modes))
            thread.start()
            threads.append(thread)
            for thread in threads:
                thread.join()
                return None

    
    def threadSpammer(self, tokens, channelID, guildID = None, threadName = None, threadMessage = None, delay = ('tokens', list, 'channelID', str, 'guildID', str, 'threadName', str, 'threadMessage', str, 'delay', int)):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            if Exception:
                (st, resp) = dc.threads(channelID, guildID, threadName)
                if success:
                    e = None
                    self.cns.error(f'''-> {str(e)}''')
                    e = None
                    del e
                    e = None
                    del e
                if st:
                    self.cns.success(f'''Created thread -> {channelID}''')
                    id = resp.json()['id']
                    (st, resp) = dc.sendMessage(id, threadMessage)
                    if success:
                        e = None
                        self.cns.error(f'''-> {str(e)}''')
                        e = None
                        del e
                        e = None
                        del e
                    if st:
                        self.cns.success(f'''Sent message -> {id}''')
                    js = resp.json()
                    if resp.status_code == 429:
                        self.cns.info('Failed to create thread -> ratelimit')
                        handleRatelimit(js)
                    self.cns.info(f'''Failed to create thread -> {js}''')
                    sleep(delay)
                js = resp.json()
                if resp.status_code == 429:
                    self.cns.info('Failed to create thread -> ratelimit')
                    handleRatelimit(js)
                self.cns.info(f'''Failed to create thread -> {js}''')
                return None

    
    def threadSpammerLauncher(self):
        global threadSwitch, threadSwitch
        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        cid = self.inputChanneliD_TS.text()
        gid = self.inputGuildiD_TS.text()
        title = self.inputThreadName_TS.text()
        msg = self.inputThreadMessage_TS.text()
        delay = self.sliderDelay_TS.value()
        if self.buttonStartThreadSpam_TS.text() == 'Spam':
            self.buttonStartThreadSpam_TS.setText('Stop')
            threadSwitch = True
            threads = []
            for i in range(len(tokens)):
                token = tokens[i % len(tokens)]
                thread = threading.Thread(target = self.threadSpammer, args = (token, cid, gid, title, msg, delay))
                thread.start()
                threads.append(thread)
                for thread in threads:
                    thread.join()
                    return None
                    threadSwitch = False
                    self.buttonStartThreadSpam_TS.setText('Spam')
                    return None

    
    def dmSpammer(self, tokens = None, userID = None, message = None, rqtoken = (None, None), captcha = ('tokens', list, 'userID', str, 'message', str, 'rqtoken', str, 'captcha', str)):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            if Exception:
                (st, resp) = dc.createDM(userID)
                if json:
                    e = None
                    self.cns.error(f'''-> {str(e)}''')
                    e = None
                    del e
                    e = None
                    del e
                if st:
                    id = resp.json()['id']
                    self.cns.success(f'''Created DM -> {id}''')
                    (st, resp) = dc.sendDM(id, message, rqtoken, captcha)
                    if json:
                        e = None
                        self.cns.error(f'''-> {str(e)}''')
                        e = None
                        del e
                        e = None
                        del e
                    if st:
                        self.cns.success(f'''Sent DM -> {userID}''')
                    js = resp.json()
                    if resp.status_code == 429:
                        self.cns.info('Failed to send DM -> ratelimit')
                        handleRatelimit(js)
                    if None == 400:
                        (rqtoken, captcha) = self.getCaptchaKey(js)
                        self.dmSpammer([
                            token], userID, message, rqtoken = rqtoken, captcha = captcha)
                    self.cns.info(f'''Failed to send DM -> {js}''')
                js = resp.json()
                if resp.status_code == 429:
                    self.cns.info('Failed to create DM -> ratelimit')
                    handleRatelimit(js)
                self.cns.info(f'''Failed to create DM -> {js}''')
                return None

    
    def dmSpammerLauncher(self):
        global dmSwitch, dmSwitch
        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        uid = self.inputUseriD_DM.text()
        msg = self.textSpam_DM.toPlainText()
        if self.buttonStartSpamDM_DM.text() == 'Spam':
            self.buttonStartSpamDM_DM.setText('Stop')
            dmSwitch = True
            threads = []
            for i in range(len(tokens)):
                token = tokens[i % len(tokens)]
                thread = threading.Thread(target = self.dmSpammer, args = (token, uid, msg))
                thread.start()
                threads.append(thread)
                for thread in threads:
                    thread.join()
                    return None
                    dmSwitch = False
                    self.buttonStartSpamDM_DM.setText('Spam')
                    return None

    
    def nickChanger(self, tokens = None, guildID = None, nickname = None, unset = ('tokens', list, 'guildID', str, 'nickname', str, 'unset', bool)):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (st, resp) = dc.nickname(guildID, nickname)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if unset:
                (st, resp) = dc.nickname(guildID, '')
                if str:
                    e = None
                    self.cns.error(f'''-> {str(e)}''')
                    e = None
                    del e
                    e = None
                    del e
            if st:
                self.cns.success(f'''Changed nick -> {guildID}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to change nick -> ratelimit')
                handleRatelimit(js)
            self.cns.info(f'''Failed to change nick -> {js}''')
            return None

    
    def nickChangerLauncher(self = None, mode = None):
        global nickSwitch, nickSwitch
        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        gid = self.inputGuildiD_NS.text()
        nick = self.inputNickname_NS.text()
        if mode == 'num':
            button = self.buttonStartSpamNumNick_NS
            
            nick_generator = lambda : ''.join(None(choices, k = 8))
        if mode == 'random':
            button = self.buttonStartSpamRandomNick_NS
            
            nick_generator = lambda : ''.join(None(choices, k = 8))
        if mode == 'spamsetunset':
            button = self.buttonStartSpamSetUnsetNick_NS
            
            nick_generator = lambda : nick
        button = self.buttonStartChangeNick_NS
        
        nick_generator = lambda : nick
        threads = []
        for i in range(len(tokens)):
            token = tokens[i % len(tokens)]
            if mode == 'spamsetunset':
                pass
            thread = self.nickChanger(target = token, args = (gid, nick_generator(), True, False))
            thread.start()
            threads.append(thread)
            for thread in threads:
                thread.join()
                if not button.text() == 'Stop' and button == self.buttonStartChangeNick_NS:
                    button.setText('Stop')
                    nickSwitch = True
                    if threading.Thread:
                        threads = []
                        for i in range(len(tokens)):
                            token = tokens[i % len(tokens)]
                            if mode == 'spamsetunset':
                                pass
                            thread = self.nickChanger(target = token, args = (gid, nick_generator(), True, False))
                            thread.start()
                            threads.append(thread)
                            for thread in threads:
                                thread.join()
                                return None
                                return None
                                if mode:
                                    nickSwitch = False
                                    button.setText(f'''Spam {mode.capitalize()}''')
                                    return None
                                return threading.Thread

    
    def webhookSpammer(self = None, url = None, message = None):
        dc = Discord(self.getProxy(), token = None)
        if Exception:
            (st, resp) = dc.sendContent(url, message)
            if success:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Sent message -> {st}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to execute -> ratelimit')
                handleRatelimit(js)
            self.cns.info(f'''Failed to execute -> {js}''')
            return None

    
    def webhookDelete(self = None, url = None, msg = None):
        dc = Discord(self.getProxy(), token = None)
        (st, resp) = dc.deleteUrl(url)
        if str:
            e = None
            self.cns.error(f'''-> {str(e)}''')
            e = None
            del e
            e = None
            del e
        if st:
            self.cns.success(f'''Deleted webhook -> {st}''')
            return None
        js = None.json()
        if resp.status_code == 429:
            self.cns.info('Failed to execute -> ratelimit')
            return None
        self.cns.info(f'''Failed to execute -> {js}''')

    
    def webhookSpammerLauncher(self, delete = (False,)):
        global wbkSwitch, wbkSwitch
        url = self.inputWebhookUrl_WS.text()
        msgJ = self.textSpam_WS.toPlainText()
        if delete:
            target = self.webhookDelete
        if self.checkAutoDelete_WS.isChecked():
            msg = Thread.loads(msgJ)['content']
        msg = msgJ
        if self.buttonStartChangeNick_WS_2.text() == 'Spam':
            self.buttonStartChangeNick_WS_2.setText('Stop')
            wbkSwitch = True
            target = self.webhookSpammer
        wbkSwitch = False
        self.buttonStartChangeNick_WS_2.setText('Spam')
        if None or delete:
            if not delete:
                pass
            threads = [
                target(target = url, args = (msg, None))]
            for thread in threads:
                thread.start()
                thread.join()
                return None
                return None

    
    def groupLeave(self = None, tokens = None, groupID = None):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (st, resp) = dc.leaveGc(groupID, True)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Left GC -> {groupID}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to leave GC -> ratelimit')
            self.cns.info(f'''Failed to leave GC -> {js}''')
            return None

    
    def groupLauncher(self = None, mode = None):
        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        gid = self.inputGroupiD_GS.text()
        inv = self.inputGroupInviteLink_GS.text()
        modes = {
            'mute': self.checkMuted_GS.isChecked(),
            'defean': self.checkDefeanded_GS.isChecked(),
            'video': self.checkWebcam_GS.isChecked(),
            'stream': self.checkStreaming_GS.isChecked() }
        
        def createthread(target = None, args = None):
            threads = []
            for i in range(len(tokens)):
                token = tokens[i % len(tokens)]
                thread = None(target = threading.Thread, args = target)
                thread.start()
                threads.append(thread)
                for thread in threads:
                    thread.join()
                    return None

        if mode == 'join':
            inv = extractCode(inv)
            if None:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                return None
            e = None
            del e
            createthread(self.guildJoin, (inv, None, None))
        if mode == 'leave':
            createthread(self.groupLeave, (gid,))
        if mode == 'joinvc' or mode == 'leavevc':
            if mode == 'joinvc':
                pass
            self.voiceJoiner(self.voiceLeaver, (gid, None, modes))
            return None

    
    def setDisplay(self = None, tokens = None, display = None):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (st, resp) = dc.changeDisplayName(display)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Changed display -> {st}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to change display -> ratelimit')
            self.cns.info(f'''Failed to change display -> {js}''')
            return None

    
    def setPronouns(self = None, tokens = None, pronouns = None):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (st, resp) = dc.changePronouns(pronouns)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Changed pronouns -> {st}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to change pronouns -> ratelimit')
            self.cns.info(f'''Failed to change pronouns -> {js}''')
            return None

    
    def setBio(self = None, tokens = None, bio = None):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            (st, resp) = dc.changeBio(bio)
            if str:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Changed bio -> {st}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to change bio -> ratelimit')
            self.cns.info(f'''Failed to change bio -> {js}''')
            return None

    
    def setPfp(self = None, tokens = None, pfp = None):
        for token in tokens:
            dc = Discord(self.getProxy(), token)
            dc.online()
            (st, resp) = dc.changeAvatar(pfp)
            if success:
                e = None
                self.cns.error(f'''-> {str(e)}''')
                e = None
                del e
                e = None
                del e
            if st:
                self.cns.success(f'''Changed avatar -> {st}''')
            js = resp.json()
            if resp.status_code == 429:
                self.cns.info('Failed to change avatar -> ratelimit')
            self.cns.info(f'''Failed to change avatar -> {js}''')
            return None

    
    def tokenConfigLauncher(self = None, mode = None):
        tokens = self.splitList(self.tokens, len(self.tokens), self.sliderMaxTokens_H.value())
        
        def fwd(func = None, value = None):
            threads = []
            for i in range(len(tokens)):
                token = tokens[i % len(tokens)]
                thread = threading.Thread(target = func, args = (token, value))
                thread.start()
                threads.append(thread)
                for thread in threads:
                    thread.join()
                    return None

        if mode in frozenset({'pfp', 'preset'}):
            pfp = self.listPfps_TC.currentText()
            if mode == 'preset':
                pass
            avatar = open(f'''data/pfp/{pfp}''', 'rb').read()
            fwd(self.setPfp, avatar)
        if mode in frozenset({'bio', 'breset'}):
            if mode != 'breset':
                pass
            bio = ''
            fwd(self.setBio, bio)
        if mode in frozenset({'preset', 'pronouns'}):
            if mode != 'preset':
                pass
            pro = ''
            fwd(self.setPronouns, pro)
        if mode in frozenset({'dreset', 'display'}):
            if mode != 'dreset':
                pass
            dis = ''
            fwd(self.setDisplay, dis)
            return None

    
    def utilsLauncher(self = None, mode = None):
        if mode == 'clear':
            self.cns.clear()
            self.cns.logo()
            return None

    __classcell__ = None

app = QtWidgets.QApplication(sys.argv)
window = DraggableMainWindow()
ui = Go6(window)
window.show()
sys.exit(app.exec_())
