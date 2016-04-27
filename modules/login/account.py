
from guide import *
from modules.unity.base import Verify
__firefox_url_bar__ = Pattern("1446023529436.png").similar(0.85).targetOffset(-36,1)

__default_browser__ = __firefox_url_bar__

def login_dmm():
    find(Pattern("1445652952275.png").similar(0.50).targetOffset(54,0))
    click(Pattern("1445652952275.png").similar(0.50).targetOffset(54,0))
    type("a", KeyModifier.CTRL) 
    paste("https://www.dmm.co.jp/my/-/login/=/path=ShVfSUkJPlVZWAAWBwBQAFJQAQMeCFIPUlcDUgtcDh5UVQQMVANQAAtQ/")
    type( Key.ENTER )
    time.sleep(2)
    account = exists("1445652619502.png")
    if account is not None:
        return 
    account = exists(Pattern("1445652341876.png").targetOffset(226,-251))
    if account is not None:
        click(account) 
    wait("1445652157607.png")
    account = exists("1445652157607.png")
    if account is not None:
        click(account) 
        time.sleep(5)

class account(object):
    """description of class"""
    __verify__ = None
    @property
    def Verify(self):
        return self.__verify__
    @Verify.setter
    def Verify(self, verify ):
        self.__verify__ = verify
    def __init__(self, *args, **kwargs):
        return super(account, self).__init__(*args, **kwargs)

class facebook(account):
    
    def __init__(self, verify , *args, **kwargs):
        super(facebook, self).__init__(*args, **kwargs)
        self.Verify = verify
    def _change_to_login_page(self, verify):

        verify.Click(__default_browser__)
        verify.SelectAll(__default_browser__)
        verify.Paste("https://www.dmm.co.jp/my/-/login/=/path=ShVfSUk_/")
        verify.KeyEnter()
        time.sleep(2)
        verify.Click(Pattern("1445652341876.png").targetOffset(226,-251))


    def login(self):
        verify = Verify()
        self._change_to_login_page(verify)
        if verify.UntilAppear("1445652157607.png" , 3):
            verify.Click("1445652157607.png")
        state = verify.UntilAppear("1445652619502.png" , 3)
        return state