def funct():
    Buff1 = arcpy.Buffer_analysis("2","thiss","10 feet")
    Buff2 = arcpy.Buffer_analysis("road._Export_Outpu1t","road123","10 meters")
    
funct()

