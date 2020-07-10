#*************************************************
#Script Title: AcresWebProject.py
#Script Author: Tripp Corbin, GISP
#Script Created on: 09/24/2015
#Last Updated on: 05/11/2020
#Last Updated by: Tripp Corbin, GISP
#Purpose: This script calculates the parcels area in acres and updates the acres field. It the projects the parcels to the WGS 84 Web Mercator coordinate system so it can be used within the City’s web application. 
#Software: ArcGIS Pro 2.5
#**************************************************

#Imports the ArcPy module for ArcGIS
import arcpy

#Specifies the input variables for the script tools
#If the data is moved or in a different database then these paths will need to be updated
Parcels = "C:\\Student\\IntroArcPro\\Databases\\Trippville_GIS.gdb\\Base\\Parcels"
Parcels_Web = "C:\\Student\\IntroArcPro\\Chapter10\\Ex10.gdb\\Parcels_Web"

#Calculates the area in acres for each parcel and updates the Acres field.
arcpy.CalculateField_management (Parcels, "Acres", "!Shape_Area! / 43560", "PYTHON_9.3", "")

# Projects Parcels from State Plane to Web Mercator Coordinate System creating a new feature class
arcpy.Project_management(Parcels, Parcels_Web, "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]", "WGS_1984_(ITRF00)_To_NAD_1983", "PROJCS['NAD_1983_StatePlane_Georgia_West_FIPS_1002_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',2296583.333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-84.16666666666667],PARAMETER['Scale_Factor',0.9999],PARAMETER['Latitude_Of_Origin',30.0],UNIT['Foot_US',0.3048006096012192]]")


