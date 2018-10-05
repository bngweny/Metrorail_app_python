# just comment out one of the two lines below to switch between the two implementations (prac1 and prac2)
#from metrorail_network1 import *

import turtle
from metrorail_network2 import *
station_coordinates=[[-325.0, 60.0,cpt],[-267.0, 83.0, esp],[-238.0,105.0,yst]]
stns=[cpt,cpt]

state=['from','to']

index=0
run=turtle.Turtle()
run.shape('circle')
run.shapesize(0.5,0.5,1)
##print(eval('cpt'))




reader=open('coordinates.txt',mode='r')
for i in reader.readlines():
   if i not in station_coordinates:
      a=i.split(',')
      a[-1]=eval((a[-1].split('\n')[0]))
      ##print(a[-1,])
      station_coordinates.append(a)
reader.close()
##print(station_coordinates)



'''
route_on_single_line = central_BLV.number_stops_and_direction(uni, esp)
print("Unibell to Esplanade on central_BLV: direction {0}, {1} stops\n".format(route_on_single_line[1].name, route_on_single_line[0]))

uni.route_to(esp)
ooz.route_to(cpt)
uni.route_to(pen)
cpt.route_to(blv)
yst.route_to(chn)

uni.route_to(sto)
uni.route_to(slt)

# the test below is very inefficient with the first version of the function (going through Cape Town, total of 30 stops)
kuy.route_to(kpt)

# now best routes (you can see that the output differs between different runs when using the second version of the prac):
kuy.best_route_to(kpt)
uni.best_route_to(slt)
clr.best_route_to(haz)
'''
allStations=[]
lines=cpt.get_lines()
for i in lines:
   stations=i.get_stations()
   for j in stations:
      if j not in allStations:
         allStations.append(j)

def route(x,y):

  if state[0]=='from':
      run.clear()
      stns[0]=whichStation(x,y)
      run.color('red')
      run.goto(x,y)
      run.stamp()


  if state[0] =='to':
      stns[1]=whichStation(x,y)
      run.color('purple')
      run.goto(x,y)
      temp=state[1]
      state[1]=state[0]
      state[0]=temp
      return stns[0].best_route_to(stns[1])
  temp=state[1]
  state[1]=state[0]
  state[0]=temp



def whichStation(x,y):
   add=[]
   if state=='to':
      print('hello')

   for i in station_coordinates:
      dist=int(sqdist(float(x),float(y),float(i[0]),float(i[1])))
      ##print(dist)
      add.append(dist)
   lowest=add[0]
   ind=0
   for j in range(len(add)):
      if add[j]<lowest:
         lowest=add[j]
         ind=j
   if add[ind]>10:

      print('doesnt exist')
      stn=input('Enter 3 letter code').upper()
      print(stn)

      for i in allStations:  ##AllStations has the string of all the object names
         ##cc=exec(str(i)+'.code')
         ##print(i.code)##Its printing None
         if i.code.lstrip()==stn:
            station_coordinates.append([x,y,(i)])
            print('done')
            ind=len(station_coordinates)-1
            break
   return(station_coordinates[ind][2])



def sqdist(x1,y1,x2,y2):
   return(((x2-x1)**2)+((y2-y1)**2))**(0.5)





def where(x,y):
   print(x,y)

def pwrite(x,y):
   stream=open('coordinates.txt',mode='w')
   for i in station_coordinates:
      stream.write('{},{},{}\n'.format(i[0],i[1],i[2]))
   stream.close()
   print('printed')






run.penup()
win=turtle.Screen()

win.bgpic('CT_RailMap1.gif')
win.setup(width=900 , height=650, startx=None, starty=0)
win.onclick(route)

##win.onclick(pwrite,btn=3).

win.listen()
win.mainloop()

   ##print(clr.get_connecting_time(southern, central_BLV)) # raises one of our user-defined exceptions
##while(stnfrom==None):