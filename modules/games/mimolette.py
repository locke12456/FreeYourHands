from guide import *
import modules.login.account

from modules.games.idmm_game import idmm_game, igame_state
from modules.unity.base import Verify
class mimolette_status(igame_state):
    MISSION_STAGE_1 = 111
    MISSION_STAGE_2 = 112
    MISSION_STAGE_3 = 113
    MISSION_STAGE_4 = 114
    MISSION_STAGE_5 = 115
    MISSION_STAGE_9 = 119
    MISSION_CHANGE_PAGE     = 110
    MISSION_CAN_START       = 120
    MISSION_HEALTH          = 140
    MISSION_BATTLE          = 150
    MISSION_BATTLE_STARTED  = 160
    MISSION_BATTLE_FINISH   = 190
    CHURCH_CHANGE_TO_MAIN   = 205
    CHURCH_MAIN             = 210
    CHURCH_CHOICE           = 211
    CHURCH_CHOICE_ACCEPT    = 212
    CHURCH_COMPLETE         = 220
    def __init__(self, *args, **kwargs):
        super(mimolette_status, self).__init__(*args, **kwargs)
        self._state_map = {    str(self.LOGIN)                  : self._state_connection_lost , 
                               str(self.CONNECTED)              : self._state_misson ,
                               str(self.MISSION)                : self._state_mission_can_start , 
                               str(self.MISSION_CHANGE_PAGE)    : self._state_mission_can_start ,                   
                               str(self.MISSION_HEALTH)         : self._state_mission_can_start ,     
                               str(self.MISSION_BATTLE)         : self._state_misson_battle ,
                               str(self.MISSION_BATTLE_STARTED) : self._state_misson_end_of_battle  ,
                               str(self.MISSION_BATTLE_FINISH)  : self._state_misson_success  ,
                               str(self.MISSION_SUCCESS)        : self._state_misson_success  ,
                               str(self.CHURCH_CHANGE_TO_MAIN ) : self._state_misson_end_of_battle  ,
                               str(self.CHURCH_MAIN           ) : self._state_misson_end_of_battle  ,
                               str(self.CHURCH_CHOICE         ) : self._state_misson_end_of_battle  ,
                               str(self.CHURCH_CHOICE_ACCEPT  ) : self._state_misson_end_of_battle  ,
                               str(self.CHURCH_COMPLETE       ) : self._state_misson_end_of_battle
                               }
    def GetAP(self):
        verify = Verify()
        ap = verify.Find(Pattern("1445255974921.png").similar(0.50))
        if ap is None:
            self.STATE = self.CONNECTION_LOST
            return ap
        texts = ap.text().split("/")
        if len(texts) > 0:
            return texts[0]
        else:
            print ap.text()
            return None
    def _state_mission_can_start(self, verify):
        result = verify.Exists("1445520015094.png")
        if result :
            result = verify.Counting("1445520015094.png") is not 0
        return self.MISSION_CAN_START if result is False else self.MISSION_HEALTH

    def _state_connection_lost_check_ap(self, verify):
        return verify.Exists( Pattern("1445255974921.png").similar(0.50) ) is False
    def _state_connection_lost_check_default(self, verify):
        return verify.Exists( "1445866289186.png" )
    def _state_connection_lost_check_alert(self, verify):
        return verify.Exists( "1445904056874.png" )    

    def _state_connection_lost(self , verify ):
        lost_check = [self._state_connection_lost_check_ap , self._state_connection_lost_check_default , self._state_connection_lost_check_alert ]
        for chk in lost_check:
            if chk(verify) :
                return self.CONNECTION_LOST
        return self.CONNECTED
    
    def _state_misson_battle(self, verify):
        result = verify.UntilAppear( Pattern("1445665196076.png").exact().targetOffset(164,3) , 10 )
        return self.MISSION_BATTLE_STARTED
    
    def _state_misson_end_of_battle(self, verify):
        if verify.Exist("1445256328434.png"):
            return self.MISSION_BATTLE_STARTED
        if verify.Exist("1445256351915.png"):
            return self.MISSION_BATTLE_FINISH
        return self.MISSION_BATTLE_STARTED
    def _state_misson_success(self, verify):
        if verify.Exist("1445256328434.png"):
            return self.MISSION_SUCCESS
    def _state_misson(self, verify):
        result = verify.UntilAppear( Pattern("1445665196076.png").exact().targetOffset(164,3) , 3 )
        return self.MISSION if result else self.MISSION_CHANGE_PAGE

    def state( self ):
        
        verify = Verify()
        if self._state_map.has_key(str(self.STATE)):
            self.STATE = self._state_map[str(self.STATE)](verify)
        return self.STATE
class mimolette(idmm_game):
    """description of class"""

    def __init__(self, *args, **kwargs):
        return super(mimolette, self).__init__(*args, **kwargs)
    
    
    

