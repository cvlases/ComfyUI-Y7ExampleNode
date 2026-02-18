# In this example, the node : 
# 1) takes an image as input (required)
# 2) takes a strength parameter as input (optional)
# 3) Applies a simple brightness adjustment using the strength parameter
# 4) Returns the processed image
# 5) Returns a string defined by user, the strength of the brightness is 
#    appended to that string.  String is used for filename_prefix when saving

class Y7ExampleNode:
    def __init__(self):
        # Define default values
        pass
    
    # ====================================================
    # Defines what inputs your node accepts
    @classmethod  # This decorator makes it a class method instead of instance method
    def INPUT_TYPES(cls):  # cls is the class itself, like ExampleNode
        return {
            "required": {  # These inputs must be provided
                # Simple input type
                "image": ("IMAGE",),  # Tuple with trailing comma
                
                # Complex input type with configuration
                "strength": ("FLOAT", {  # Type is FLOAT
                    "default": 1.0,      # Initial value shown
                    "min": 0.0,         # Minimum allowed value
                    "max": 3.0,         # Maximum allowed value
                    "step": 0.01        # Slider/input step size
                }),
            },
           "optional": {
               "filename_prefix": ("STRING", {
                   "default": "",
                   "multiline": False,  # Single line text input
                   "description": "filename prefix that includes brightness strength"  # Tooltip in UI
               })
           }                  
        }
    
    # Return types (tuple). Specifies what type of data your node outputs 
    # (note the trailing comma, without it, it would not be a tuple, esp. for single item)
    RETURN_TYPES = ("IMAGE","STRING",)
    # Name of the method that will be called
    FUNCTION = "process_image"
    # Determines where your node appears in the UI
    CATEGORY = "image/processing"
    
    #  ==========================================
    # Main function of this node 
    # Optional parameters must have default values
    def process_image(self, image, strength, filename_prefix=""):  
        # processed image
        processed_image = image * strength
        
        # Use the string for a filename prefix for when saving. 
        if filename_prefix:
           fname_prefix = f"{filename_prefix}_{strength}"

        # return a tuple with a single item...
        return (processed_image,fname_prefix,)
