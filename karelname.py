from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for move"""
    move()
  
  def tl(self):
    """Turn Left"""
    turn_left()

  def tr(self):
    """Turn Right"""
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

  def A(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()
    
      

  def L(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.m()
    self.tl()
    self.put2()
    self.m()
    self.m()
   

  def E(self):
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.tr()
    self.m()
    self.m()
    self.tr()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.put2()
    self.m()
    self.m()

  def X(self):
    self.put()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.ta()
    self.m()
    self.m()
    self.m()
    self.m()
    self.put()
    self.tl()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.tr()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.tr()
    self.m()
    self.put()
    self.m()
    self.tl()
    self.m()
    self.put()
    self.m()
    self.m()

def main():
    """Karel code goes here!"""
    kt = ktools()
    kt.A()
    kt.L()
    kt.E()
    kt.X()
   
    
    
    
    pass

if __name__ == "__main__":
    run_karel_program()
