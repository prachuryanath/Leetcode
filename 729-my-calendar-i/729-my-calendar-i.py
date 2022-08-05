
class MyCalendar:
  def __init__(self):
    self.arr=[]
  def book(self, start: int, end: int) -> bool:
      for item in self.arr:
        overlap=min(end,item[1])-max(start,item[0])
        if overlap>0:
          return False
      self.arr.append([start,end])
      return True
        
      
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)