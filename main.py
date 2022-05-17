import random
import os
import requests

class Proxymetr:

    def __init__(self):
        self.ip = self.get_ip()

    def get_urls(self, url):
        response = requests.get(url, headers=agents, timeout=5)
        return response

    def get_proks(self, proxy):
        print("Getting info...")
        Parsers = ['http://proxyjudge.us/azenv.php', 'http://mojeip.net.pl/asdfa/azenv.php']
        TypeOfProxy = []
        data = {}
        for htpsb in ['https','http']:
            for protocol in ['http', 'socks4', 'socks5']:
                adr = f'{protocol}://{proxy}',
                response = requests.get(random.choice(Parsers), proxies={htpsb: adr}, headers=agents, timeout=10)
                if response.status_code == 200:
                    data['status'] = True
                    TypeOfProxy.append(protocol)
                    data['type'] = TypeOfProxy
                    if str(self.ip) in response.text:
                        data['anonymity'] = 'Transparent'
                    else:
                        data['anonymity'] = 'Anonymous'
                    if protocol == 'http':
                        return data

            if 'status' not in data.keys():
                data['status'] = False
                return data
            else:
                return data

    def get_ip(self):
        print("Getting ip...")
        IP_sites = [ 'http://ifconfig.io/ip', 'http://ipinfo.io/ip']
        ip = self.get_urls(url=random.choice(IP_sites))
        return ip.text

    def get_geo(self, ip):
        print("Getting geo")
        urls = ['http://ipwhois.app/json/', 'http://ip-api.com/json/']
        link = f'{random.choice(urls)}{ip}'
        resp = self.get_urls(url=link)
        return resp

    def start(self, proxy):
        print("Proxymetr working")
        inIP = proxy.split(':')
        resp = self.get_proks(proxy=proxy)

        if resp['status'] == True:
            result = {}
            result['anonymity'] = resp['anonymity']
            result['type'] = resp['type']
            result['status'] = resp['status']
            geo = self.get_geo(inIP[0])
            geo_info = geo.json()
            result['country'] = geo_info['country']
            result['city'] = geo_info['city']
            try:
                result['country_code'] = geo_info['countryCode']
            except:
                result['country_code'] = geo_info['country_code']
            os.system('cls' if os.name == 'nt' else 'clear')
            return result

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            return resp

while(1):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Введите вашу операционную систему обращения(Linux(0), Windows(1)) или завершите выполнение программы(2): ")
    c = int(input())

    if c==2:
        break

    if c==0:
        agents = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/58.0.1',}
        print("Ввести адресс(1) или закончить работу(0) ? ")
        b = int(input())

        if b != 0 and b != 1:
            print("Неверное значеие, введите 0 или 1")
            b = int(input())

        if b == 1:
            print("Please enter your (<ip>:<port>):")
            danie = str(input())
            print("Please wait a moment...")
            print()
            checker = Proxymetr()
            r = checker.start(danie)
            print(r)
            print()
            print('Введите любой символ, чтобы вернуться в меню')
            input()
            print()

        if b == 0:
            print("program finished")
            break

    if c==1:
        agents = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',}
        print("Ввести адресс(1) или вернуться назад(0) ? ")
        b = int(input())

        if b != 0 and b != 1:
            print("Неверное значение, введите 0 или 1")
            b = int(input())

        if b == 1:
            print("Please enter your (<ip>:<port>):")
            danie = str(input())
            print("Please wait a moment...")
            print()
            checker = Proxymetr()
            r = checker.start(danie)
            print(r)
            print()
            print('Введите любой символ, чтобы вернуться в меню')
            input()
            print()

        if b == 0:
            print("program finished")
            break

##########################################################################
#############Зависимости, которые нужно установить
#pip install -r requirments.txt

#pip install requests
#pip install urllib3
#pip install certifi
#pip install PySocks
#pip install idna
#pip install chardet
#pip install pycurl


#########################################################################
#############Примеры команд
#r = checker.check_proxy('<ip>:<port>')
#r = checker.check_proxy('184.178.172.5:15303')

#########################################################################
#############Список прокси
#184.178.172.5:15303 - socks5, anon
#169.46.126.192:80 - http, anon
#122.155.165.191:3128 - http, Transparent
#98.162.25.23:4145 - socks4-5, anon
#72.210.252.137:4145 - socks4-5m anon
#176.99.2.43:1080 - socks4, anon, rus

#переборка юзерагента и переборка