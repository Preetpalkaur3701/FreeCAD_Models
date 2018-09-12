import FreeCAD as App
import FreeCADGui
import Part


def bishop_base(bottom_base_radius, top_base_radius,
				base_height, mid_height,  mid_top_radius, 
				mid_bottom_radius, ring_height_from_bottom,
				top_radius, base_radius, 
				top_ring_height, bottom_ring_height,
				head_radius,head_height, top_ball_radius,
				cut_length, cut_width, cut_height,
				cut_height_from_bottom):
	""" First time while triying this code:
	Give the dimension as written: (5,4,3,18,3,2,16,2.5,3,1,1,4,6,1,13,2,7)"""
	base_1 = make_bishop_base(bottom_base_radius,
							  top_base_radius,
							  base_height,
							  mid_height,  
							  mid_top_radius, 
							  mid_bottom_radius, 
			   				  ring_height_from_bottom, 
			   				  top_radius, 
			   				  base_radius, 
			   				  top_ring_height, 
			   				  bottom_ring_height,
			   				  head_radius,
			   				  head_height, 
			   				  top_ball_radius,
			   				  cut_length, 
			   				  cut_width,
			   				  cut_height,
			   				  cut_height_from_bottom,
			                  App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),0)))
	

	base_1[2].ViewObject.Visibility = False
	base_1[3].ViewObject.Visibility = False
	base_1[4].ViewObject.Visibility = False
	
	
	lofts = []
	loft_top = App.ActiveDocument.addObject('Part::Loft','Loft')
	loft_top.Sections=(base_1[2], base_1[3] )
	loft_top.Solid=False
	loft_top.Ruled=True
	loft_top.Closed=False
	lofts.append(loft_top)
	App.ActiveDocument.recompute() 
	

	loft_bottom = App.ActiveDocument.addObject('Part::Loft','Loft')
	loft_bottom.Sections=[base_1[3], base_1[4] ]
	loft_bottom.Solid=False
	loft_bottom.Ruled=True
	loft_bottom.Closed=False
	lofts.append(loft_bottom)
	App.ActiveDocument.recompute()

	ring = App.ActiveDocument.addObject('Part::Compound','ring')
	ring.Links = lofts
	ring.Placement.Base.z = ring_height_from_bottom
	
	head = App.ActiveDocument.addObject('Part::Compound','head')
	head.Links = (base_1[5], base_1[6])
	head.Placement.Base.z = (mid_height + top_base_radius)


	hole = App.activeDocument().addObject("Part::Cut","Cut")
 	hole.Base = App.activeDocument().head
 	hole.Tool = App.activeDocument().Box

 	compound = App.activeDocument().addObject("Part::Compound","Compound")
	compound.Links = [App.activeDocument().Cone,
					  App.activeDocument().Cone001,
					  App.activeDocument().Sphere001,
					  App.activeDocument().ring,
					  App.activeDocument().Cut] 
	compound.ViewObject.DisplayMode = u"Shaded"
	FreeCADGui.activeDocument().activeView().viewRight()

 	App.ActiveDocument.recompute()
	return (ring, head, hole, compound)



def make_bishop_base(radius1, 
					 radius2, 
					 height1, 
					 height2, 
					 radius3,
					 radius4,  
					 height3, 
					 radius5, 
					 radius6, 
					 height4, 
					 height5,
					 radius7,
					 height6,
					 radius8,
					 length,
					 width,
					 height7,
					 height8, 
					 placement):
	Cone = App.ActiveDocument.addObject("Part::Cone","Cone")
	App.ActiveDocument.ActiveObject.Label = "Cone"
	Cone.Radius1 = radius1
	Cone.Radius2 = radius2
	Cone.Height = height1
	Cone.Placement.Base.z = 1
	App.ActiveDocument.recompute()
	

	Cone001 = App.ActiveDocument.addObject("Part::Cone","Cone")
	App.ActiveDocument.ActiveObject.Label = "Cone"
	Cone001.Radius1 = radius3
	Cone001.Radius2 = radius4
	Cone001.Height = height2
	Cone001.Height = height3
	Cone001.Placement.Base.z = height1
	App.ActiveDocument.recompute()
	

	circle1 = App.ActiveDocument.addObject("Part::Circle","Circle")
 	App.ActiveDocument.Circle.Label = "circle1"
 	circle1.Radius = radius5
 	circle1.Placement.Base.z = -height4
 	App.ActiveDocument.recompute()

	circle2 = App.ActiveDocument.addObject("Part::Circle","Circle")
 	App.ActiveDocument.Circle.Label = "circle2"
 	circle2.Radius = radius6
 	circle2.Placement.Base.z = 0
 	circle2.Placement.Base.y = 0
 	circle2.Placement.Base.x = 0
 	App.ActiveDocument.recompute()
	
	circle3 = App.ActiveDocument.addObject("Part::Circle","Circle")
 	App.ActiveDocument.Circle.Label = "circle3"
 	circle3.Radius = radius5
 	circle3.Placement.Base.z = height5
 	App.ActiveDocument.recompute()

 	sphere=App.ActiveDocument.addObject("Part::Sphere","Sphere")
	cone = App.ActiveDocument.addObject("Part::Cone","Cone")
	App.ActiveDocument.ActiveObject.Label = "Sphere"
	App.ActiveDocument.ActiveObject.Label = "Cone"
	cone.Radius2 = '0 mm'
	cone.Radius1 = radius7
	cone.Height = height6
	sphere.Radius = radius7
	sphere.Angle2 = 0.00 
	App.ActiveDocument.recompute()

	sphere1=App.ActiveDocument.addObject("Part::Sphere","Sphere")
	App.ActiveDocument.ActiveObject.Label = "Sphere1"
	sphere1.Radius = radius8
	sphere1.Placement.Base.z = height6+height2+height1+1
	App.ActiveDocument.recompute()

	cube = App.ActiveDocument.addObject("Part::Box","Box")
	App.ActiveDocument.ActiveObject.Label = "Cube"
	cube.Length = length
	cube.Width = width
	cube.Height = height7
	cube.Placement = App.Placement(App.Vector(1,0,0),App.Rotation(App.Vector(1,0,0),31))
	cube.Placement.Base.z = 21
	cube.Placement.Base.y = 0
	cube.Placement.Base.x = -7
	App.ActiveDocument.recompute()
	
	return (Cone, Cone001, circle1, circle2, circle3, sphere, cone, sphere1, cube)