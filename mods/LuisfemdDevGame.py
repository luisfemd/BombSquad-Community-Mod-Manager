import bs

# so the game knows to ignore out-of-date ones.
def bsGetAPIVersion():
    return 4
# how BombSquad asks us what games we provide
def bsGetGames():
    return [LuisfemdDevGame]

class PlayerLleva(bs.PlayerSpaz):

    def handleMessage(self, message):
        if isinstance(message,bs.HitMessage):
            name = self.getName()
            bs.sreenMessage(name + " la lleva")


class LuisfemdDevGame(bs.TeamGameActivity):

    @classmethod
    def getName(cls):
        return 'Initial Dev Game'

    @classmethod
    def getDescription(cls,sessionType):
        return 'My first bombsquad bomb game: La lleva.'

    def onBegin(self):
        bs.TeamGameActivity.onBegin(self)
        # game's starting - let's just set a timer to end it in 5 seconds
        bs.screenMessage("La lleva... Ending in 60 seconds...")
        #bs.Powerup(self, position=(10, 21, 30), powerupType='curse', expire=False)
        bs.Powerup(position=(0,0,0),powerupType='health').autoRetain()
        self._endGameTimer = bs.Timer(60000, bs.WeakCall(self.endGame))

    def endGame(self):
        # game's over - set a score for each team and tell our activity to finish
        ourResults = bs.TeamGameResults()
        for team in self.teams: ourResults.setTeamScore(team,0)
        self.end(results=ourResults)

    def onPlayerJoin(self, player):
        #bs.TeamGameActivity.onPlayerJoin(self, player)
        self.spawnPlayer(player)

        
    def spawnPlayer(self, player):
        #spaz = self.spawnPlayerSpaz(player)
        spaz = PlayerLleva(color=player.color, highlight=player.highlight, character=player.character, player=player)


        # lets reconnect this player's controls to this
        # spaz but *without* the ability to attack or pick stuff up
        #spaz.connectControlsToPlayer(enablePunch=True, enableBomb=False, enablePickUp=True)
        player.setActor(spaz)
        #spaz.curse()


        
