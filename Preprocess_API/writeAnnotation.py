#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: avasquez
"""
import xml.etree.ElementTree as ET
import xml.dom.minidom

class WriteAnnotation:
    def __init__(self, writepath, bboxDict):
        self.bboxDict = bboxDict
        self.writepath = writepath

    def GenerateXML(self) :
        if self.bboxDict['file'] != None:
            for i in range(len(self.bboxDict['name'])):
                if self.bboxDict['file'][i] != None:
                    root = ET.Element("annotation")
                      
                    E1 = ET.Element("folder")
                    E1.text = "JPEGImages"
                    root.append(E1)
                    
                    E2 = ET.Element("filename")
                    E2.text = self.bboxDict['file'][i]
                    root.append(E2)
                    
                    E3 = ET.Element('source')
                    root.append(E3)
                    
                    SE1_E3 = ET.SubElement(E3, 'database')
                    SE1_E3.text = 'NA'
                    SE2_E3 = ET.SubElement(E3, 'author')
                    SE2_E3.text = 'PC-AVASQUEZ'
                    
                    E4 = ET.Element('size')
                    root.append(E4)
                    
                    SE1_E4 = ET.SubElement(E4, 'width')
                    SE1_E4.text = str(self.bboxDict['imageWidth'][i])
                    SE2_E4 = ET.SubElement(E4, 'height')
                    SE2_E4.text = str(self.bboxDict['imageHeight'][i])
                    SE3_E4 = ET.SubElement(E4, 'depth')
                    SE3_E4.text = str(self.bboxDict['imageDepth'][i])
                    
                    E5 = ET.Element('object')
                    root.append(E5)
                    
                    SE1_E5 = ET.SubElement(E5, 'name')
                    SE1_E5.text = self.bboxDict['name'][i]
                    SE2_E5 = ET.SubElement(E5, 'difficult')
                    SE2_E5.text = str(0)
                    
                    SE3_E5 = ET.SubElement(E5, 'bndbox')
                    
                    SE1_SE3_E5 = ET.SubElement(SE3_E5, 'xmin')
                    SE1_SE3_E5.text = str(self.bboxDict['xmin'][i]) 
                    SE2_SE3_E5 = ET.SubElement(SE3_E5, 'ymin')
                    SE2_SE3_E5.text = str(self.bboxDict['ymin'][i])
                    SE3_SE3_E5 = ET.SubElement(SE3_E5, 'xmax')
                    SE3_SE3_E5.text = str(self.bboxDict['xmax'][i]) 
                    SE4_SE3_E5 = ET.SubElement(SE3_E5, 'ymax')
                    SE4_SE3_E5.text = str(self.bboxDict['xmax'][i])
                      
                    tree = ET.ElementTree(root)
                    
                    ##write bytes
                    writename = self.writepath + self.bboxDict['file'][i] + '.xml'
                    with open(writename, "wb") as f:
                        tree.write(f)
                
                if self.bboxDict['file'][i] != None:
                    ##make it pretty
                    dom = xml.dom.minidom.parse(writename) # or xml.dom.minidom.parseString(xml_string)
                    pretty_xml_as_string = dom.toprettyxml()
                    lines = pretty_xml_as_string.replace('\t', '    ')
                    with open(writename, 'w') as f:
                        f.write(lines)
    