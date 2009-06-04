""" Default ImageKit configuration """

from imagekit.specs import ImageSpec
from imagekit import processors
    
class ResizeThumbnail(processors.Resize):
    width = 200
    height = 100
    crop = True
    
class EnhanceSmall(processors.Adjustment):
    contrast = 1.2
    sharpness = 1.1
    
class SampleReflection(processors.Reflection):
    size = 0.5
    background_color = "#000000"
    
class DjangoAdminThumbnail(ImageSpec):
    access_as = 'admin_thumbnail'
    processors = [ResizeThumbnail, EnhanceSmall, SampleReflection]
