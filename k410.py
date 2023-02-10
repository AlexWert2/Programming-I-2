from stanfordkarel import *

class ktools:
  def m(self):
    """Shorthand for move"""
    move()

  
  def tl(self):
      """Turn Left"""
      turn_left()

  
  def tr(self):
      """turn_Right"""
      self.tl()
      self.tl()
      self.tl()
  
  def ta(self):
      """Turn Around"""
      self.tl()
      self.tl()
  
  def pick(self):
    """Pick Beeper"""
    pick_beeper()

  def put(self):
    """Put Beeper"""
    put_beeper()

  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def fic(self):
   """Front is Clear"""
   return front_is_clear()
    
  def fib(self):
    """Front is Blocked"""
    return not self.fic()
     

  def ric(self):
    """Right is Clear"""
    self.tr()
    if self.fic():
       self.tl()
       return True # Immediately exit the function
    self.tl()
    return False

  def rib(self):
    """Right is Blocked"""
    return not self.ric()


  def mazemove(self):
    """Maze move"""
    if self.fib():
      self.tl()
    else: # Otherwise...
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():  
          self.tr()
          self.m()
        pass

  def mm(self, num):
    """Move Multiple"""
    for number in range(num):
      self.m()

  def pickm(self, num):
    """Pick Multiple"""
    for step in range(num-1):
      self.pick()
      self.m()
    self.pick()

  def putm(self, num):
    """Put Multiple"""
    for _ in range(0, num-1):
     self.put()
     self.m()
    self.put()
     


     
def main():  
    """Karel code goes here!"""
    kt = ktools()
    kt.m()   
    kt.pickm(2)
    kt.tl()
    kt.m()
    kt.pickm(3)
    kt.tr()  
    kt.mm(2)
    kt.tr()
    kt.m()
    kt.m()
    kt.pickm(2)
    kt.tl()
    kt.mm(2)
    kt.m()
    kt.pick()
    kt.m()
  
    
  
    
  

    pass

if __name__ == "__main__":
   run_karel_program()