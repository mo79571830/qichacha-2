#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import time

class Cookies():

    def choice_cookie(self):
        #企查查cookie信息
        cookies = {
            'ce': 'UM_distinctid=1676042da8a11e-081f1de99494d4-4a516c-1aeaa0-1676042da8b4fa; CNZZDATA1254842228=1111069007-1543505761-https%253A%252F%252Fwww.baidu.com%252F%7C1557103492; zg_did=%7B%22did%22%3A%20%221676042da9931f-0a259511f28114-4a516c-1aeaa0-1676042da9c128%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201557106689441%2C%22updated%22%3A%201557108538394%2C%22info%22%3A%201556716028145%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%223a998caa5ca0accb1f4184f6b68e57a3%22%7D; _uab_collina=154350825368885713109512; saveFpTip=true; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1556263172,1556417724,1556507953,1556510512; acw_tc=77a7faa015560908499696153e502395127a88b7bc15659bfe9ab6821d; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1557108539; QCCSESSID=ktavm0dupd0vh5bvpu0m3ot5q6; hasShow=1',
            # 'mz': 'Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1556941051; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1556095214,1556243803,1556416533,1556941012; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201556941011624%2C%22updated%22%3A%201556941050953%2C%22info%22%3A%201556941011626%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%220d5e574ae46348b49ca801ac59271b09%22%7D; zg_did=%7B%22did%22%3A%20%2216a1c60e4cc3d2-00a1b4b8de93fa8-481d3500-1aeaa0-16a1c60e4cdd46%22%7D; CNZZDATA1254842228=1727294940-1555251478-%7C1556941038; QCCSESSID=j1u77e9l68damm79h01e8mico6; hasShow=1; acw_tc=2be0b8cc15552542736802412e8754f57dc139f11741df5b651dc16265; UM_distinctid=1680ef97502434-0a1e1aa9a12ab58-481c3400-1aeaa0-1680ef97503e8a; _uab_collina=154643945647369939717233; saveFpTip=true',
            # 'lx': 'UM_distinctid=1676042da8a11e-081f1de99494d4-4a516c-1aeaa0-1676042da8b4fa; CNZZDATA1254842228=1111069007-1543505761-https%253A%252F%252Fwww.baidu.com%252F%7C1557103492; zg_did=%7B%22did%22%3A%20%221676042da9931f-0a259511f28114-4a516c-1aeaa0-1676042da9c128%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201557106689441%2C%22updated%22%3A%201557107995351%2C%22info%22%3A%201556716028145%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%22cb80f2f681d0145c874ffa8eebfcc1f0%22%7D; _uab_collina=154350825368885713109512; saveFpTip=true; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1556263172,1556417724,1556507953,1556510512; acw_tc=77a7faa015560908499696153e502395127a88b7bc15659bfe9ab6821d; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1557107995; QCCSESSID=ktavm0dupd0vh5bvpu0m3ot5q6; hasShow=1',
            # 'gl': 'Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1556941437; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1556095214,1556243803,1556416533,1556941012; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201556941011624%2C%22updated%22%3A%201556941437109%2C%22info%22%3A%201556941011626%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%221c56a983c1edb0b0ff65f8f052ba0f8d%22%7D; zg_did=%7B%22did%22%3A%20%2216a1c60e4cc3d2-00a1b4b8de93fa8-481d3500-1aeaa0-16a1c60e4cdd46%22%7D; CNZZDATA1254842228=1727294940-1555251478-%7C1556941038; QCCSESSID=j1u77e9l68damm79h01e8mico6; hasShow=1; acw_tc=2be0b8cc15552542736802412e8754f57dc139f11741df5b651dc16265; UM_distinctid=1680ef97502434-0a1e1aa9a12ab58-481c3400-1aeaa0-1680ef97503e8a; _uab_collina=154643945647369939717233; saveFpTip=true'
        }
        # cookies = {'ce':'UM_distinctid=1676042da8a11e-081f1de99494d4-4a516c-1aeaa0-1676042da8b4fa; CNZZDATA1254842228=1111069007-1543505761-https%253A%252F%252Fwww.baidu.com%252F%7C1556930640; zg_did=%7B%22did%22%3A%20%221676042da9931f-0a259511f28114-4a516c-1aeaa0-1676042da9c128%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201556932969967%2C%22updated%22%3A%201556933055190%2C%22info%22%3A%201556716028145%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%221c56a983c1edb0b0ff65f8f052ba0f8d%22%7D; _uab_collina=154350825368885713109512; saveFpTip=true; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1556263172,1556417724,1556507953,1556510512; acw_tc=77a7faa015560908499696153e502395127a88b7bc15659bfe9ab6821d; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1556933041; QCCSESSID=ktavm0dupd0vh5bvpu0m3ot5q6'}
        name_li = list(cookies.keys())
        name = random.choice(name_li) # 随机获取一条cookie值
        cookie = cookies[name]
        return cookie














if __name__ == '__main__':
    ck = Cookies()
    ck.choice_cookie()