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
      if self.ric()
        self.tr()
        self.m()
        if self.ric()  
          self.tr()
          self.m()
      
    

  def main():
    """Karel code goes here!"""
    kt = ktools()

    pass

if __name__ == "__main__":
    run_karel_program()