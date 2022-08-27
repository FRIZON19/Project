class OitoRainhas:
   def __init__(self):
      print self.printInit()
      self.setVars()
      self.loop()
         
   def printInit(self):
      p = \
      " + Problema das Oito Rainhas\n" \
      ">> Para melhor visualizar o conteúdo impresso em tela, o terminal deve esta setado com a coluna em 42.\n"
      return p
      
   def printRainha(self):
      p = \
      "\n==========================================\n" \
      " + " + str(len(self.posRainha)) + " Rainha\n\n" \
      + str(self.t)
      return p
      
   def setVars(self):
      self.TABULEIRO = \
      "########\n" \
      "########\n" \
      "########\n" \
      "########\n" \
      "########\n" \
      "########\n" \
      "########\n" \
      "########\n"
      self.VAZIO, self.ATAQUE, self.RAINHA = "#", "+", "*"
      self.posRainha, self.posAtaque, self.posInvalida, self.posValida = [], [], [], []
      self.t = [list(line) for line in self.TABULEIRO.splitlines()]
      self.posValida = self.setPosValida()
      
   def setPosValida(self):
      l = []
      for y in xrange(len(self.t)):
         for x in xrange(len(self.t)):
            l.append([x,y])
      return l
   
   def setVazio(self, x, y):
      self.t[x][y] = self.VAZIO
      
   def setRainha(self, x=0, y=0):
      if 0 <= x <= 7 and 0 <= y <= 7:
         if self.t[x][y] == self.VAZIO and self.testPos(x, y) == True:
            self.t[x][y] = self.RAINHA
            self.posRainha.append([x, y])
            self.posInvalida.append([x, y])
            self.posValida.remove([x, y])
            if self.moveX(x, y) or self.moveY(x, y) or self.moveXYDir(x, y) or self.moveXYEsq(x, y): pass
            print self.printRainha()
      
   def setAtaque(self, x, y):
      self.t[x][y] = self.ATAQUE
      self.posAtaque.append([x, y])
      self.posInvalida.append([x, y])
      self.posValida.remove([x, y])

   def moveX(self, x=0, y=0):
      if 0 <= x <= 7:
         if self.t[x][y] == self.VAZIO:
            self.setAtaque(x, y)
            if self.moveX(x+1, y) or self.moveX(x-1, y): pass
         elif self.t[x][y] == self.RAINHA:
            if self.moveX(x+1, y) or self.moveX(x-1, y): pass
         else:
            if self.X < 7:
               self.X += 1
               if self.moveX(x+self.X, y) or self.moveX(x-self.X, y): pass
            
   def moveY(self, x=0, y=0):
      if 0 <= y <= 7:
         if self.t[x][y] == self.VAZIO:
            self.setAtaque(x, y)
            if self.moveY(x, y+1) or self.moveY(x, y-1): pass
         elif self.t[x][y] == self.RAINHA:
            if self.moveY(x, y+1) or self.moveY(x, y-1): pass
         else:
            if self.Y < 7:
               self.Y += 1
               if self.moveY(x, y+self.Y) or self.moveY(x, y-self.Y): pass
            
   def moveXYDir(self, x=0, y=0):
      if 0 <= x <= 7 and 0 <= y <= 7:
         if self.t[x][y] == self.VAZIO:
            self.setAtaque(x, y)
            if self.moveXYDir(x+1, y+1) or self.moveXYDir(x-1, y-1): pass
         elif self.t[x][y] == self.RAINHA:
            if self.moveXYDir(x+1, y+1) or self.moveXYDir(x-1, y-1): pass
         else:
            if self.XYD < 7:
               self.XYD += 1
               if self.moveXYDir(x+self.XYD, y+self.XYD) or self.moveXYDir(x-self.XYD, y-self.XYD): pass
   
   def moveXYEsq(self, x=0, y=0):
      if 0 <= x <= 7 and 0 <= y <= 7:
         if self.t[x][y] == self.VAZIO:
            self.setAtaque(x, y)
            if self.moveXYEsq(x+1, y-1) or self.moveXYEsq(x-1, y+1): pass
         elif self.t[x][y] == self.RAINHA:
            if self.moveXYEsq(x+1, y-1) or self.moveXYEsq(x-1, y+1): pass
         else:
            if self.XYE < 7:
               self.XYE += 1
               if self.moveXYEsq(x+self.XYE, y-self.XYE) or self.moveXYEsq(x-self.XYE, y+self.XYE): pass
   
   def testPos(self, x, y):
      r = False
      for i in self.posValida:
         if x == i[0] and y == i[1]:
            r = True
      return r
      
   def loop(self):
      for i in self.posValida:
         self.X, self.Y, self.XYD, self.XYE = 0, 0, 0, 0
         self.setRainha(i[0], i[1])
      if len(self.posRainha) < 8:
         self.loop()

if __name__ == "__main__":
   oitoRainhas = OitoRainhas()