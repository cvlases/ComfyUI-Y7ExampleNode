# this file registers your custom node with comfyui
# y7_example_node is the y7_example_node.py module.  
# the preceding dot (.) means current dir.
# Y7ExampleNode is the class name in y7_example_node.py
from .y7_example_node import Y7ExampleNode

NODE_CLASS_MAPPINGS = {
    "Y7ExampleNode": Y7ExampleNode  
}

# Key: string identifier, Value: actual class name

# This dictionary tells ComfyUI:
# The key "Y7ExampleNode" is the internal identifier for our node
# The value Y7ExampleNode points to the actual class we created
# This mapping lets ComfyUI know which class to instantiate when the node is used


#  =================================================================================
NODE_DISPLAY_NAME_MAPPINGS = {
    "Y7ExampleNode": "Y7 Example Custom Node" # Key: same identifier, Value: display name that users see
}
# This dictionary defines hHow our node will appear in the ComfyUI interface
# The key must match the one in NODE_CLASS_MAPPINGS above
# The value is the human-readable name shown in the UI.  This can be anything you want. 
