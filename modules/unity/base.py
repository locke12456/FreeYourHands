from guide import *
Settings.OcrTextSearch = True
Settings.OcrTextRead = True
class Verify(object):
    """description of class"""
    def Exists(self,pic):
        verify = exists(pic)
        return verify is not None
    def Find(self,pic):
        if self.Exists(pic):
            return find(pic)
        return None
    def MoveTo(self,pic):
        if self.Exists(pic):
            return hover(pic)
        return None
        
    def Paste(self , str):
        paste(str)
    def KeyEnter(self):
        type( Key.ENTER )
    def Counting(self,pic):
        lst = list(findAll(pic))
        return len(lst)
    def Wait(self , pic):
        try:
            wait(pic)
            return True
        except:
            return False

    def Click(self , pic):
        print pic
        if self.Exists(pic):
            click(pic)
    def WaitFor(self , pic , state = True , retry = 60 ):
        check = state
        for try_cnt in range(1,retry):  
            check = self.Wait(pic)
            if check is not state:
                return True
            time.sleep(1) 
        return False   
    def UntilDisappear(self, pic , retry = 60 ):
        return self.WaitFor(pic , False , retry)

    def UntilAppear(self, pic , retry = 60 ):
        return self.WaitFor(pic , True , retry)
    
    def SelectAll(self,verify):
        if self.Exists(verify) : 
            type("a", KeyModifier.CTRL) 

