# used to read/write cross-module variables 
import OCC.Quantity
from OCC.Graphic3d import *
from OCC import TopExp, BRepPrimAPI, TopAbs, TopoDS, BRep
from OCCUtils.Topology import Topo
from OCC.BRepAlgo import *
from OCC.TopoDS import TopoDS_Compound

curr_tab = 0
objs = []
consoles = []
displays = []
file_names = []
edges = []

def log(msg):
  print msg
  consoles[curr_tab].append(str(msg))
  
def display(topo):
  #http://www.opencascade.org/org/forum/thread_18374/
  #http://adl.serveftp.org/lab/opencascade/pdf/visu.pdf
  #shape = displays[curr_tab].DisplayShape(topo, update=False).GetObject()
  #shape.SetDisplayMode(0)
  #displays[curr_tab].DisplayColoredShape(topo, 'BLUE', False)
  mat = Graphic3d_MaterialAspect(Graphic3d_NOM_SILVER)
  displays[curr_tab].DisplayShape(topo, material=mat, update=False)
  
  t = Topo(topo)
  wires =t.wires()
  for w in wires:
    #print w
    #displays[curr_tab].DisplayColoredShape(w, 'BLACK', False)
    edges.append(w) 
  
def display_edges():  
  comp = TopoDS_Compound()
  builder = BRep.BRep_Builder()
  builder.MakeCompound(comp)
  
  for e in edges:
    #contour = BRepAlgo_Fuse(contour, e).Shape()
    builder.Add(comp, e)
    
  displays[curr_tab].DisplayColoredShape(comp, 'BLACK', False)
    
def fitAll():
  displays[curr_tab].FitAll()
  
def add_obj(data):
  objs[curr_tab].append(data)

def remove_all_objs():
  objs[curr_tab][:] = []
  edges[:] = []

def get_objs():
  return objs[curr_tab]

def set_file_name(name):
  file_names[curr_tab] = name
  
def get_file_name():
  return file_names[curr_tab]
