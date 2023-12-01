class sentido():
  def __init__(self,piso_ingresados,actual):
    self.piso_ingresados=piso_ingresados
    self.actual=actual

  def minimo(self):
    min=29
    if len(self.piso_ingresados)>0:
      for x in self.piso_ingresados:
        if x<min:
          min=x
    return min

  def maximo(self):
    max=0
    if len(self.piso_ingresados)>0:
      for x in self.piso_ingresados:
        if x>max:
          max=x
    return max

class ascenso():
  def __init__(self, actual, piso_ingresado):
    
    self.piso_ingresado=piso_ingresado
    self.actual=actual
    piso=sentido(self.piso_ingresado,self.actual)
    min=piso.minimo()
    sube=True
    while(sube==True and actual == 29 ):
      if self.actual == min:
          print("para el ascensor en el piso: " + self.actual)
      else:
        self.actual=+1
        
        #para_bajar=int ()

a=[5,29,13,10]
b=4
#subir1=sentido(a,b)
#c=subir1.minimo()
#d=subir1.maximo()
subir2=ascenso(b,a)

    
    
