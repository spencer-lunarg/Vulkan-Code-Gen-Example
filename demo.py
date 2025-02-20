#!/usr/bin/env python3

import os
import sys
from xml.etree import ElementTree

# These live in the Vulkan-Docs repo, but are also published in the Vulkan-Headers repo in the registry folder
# At runtime we inject python path to find these helper scripts
registry_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Vulkan-Headers', 'registry'))
sys.path.insert(0, registry_path)
try:
    from reg import Registry
    from base_generator import BaseGenerator, BaseGeneratorOptions, SetOutputDirectory, SetOutputFileName, SetTargetApiName, SetMergedApiNames
    from vulkan_object import Format
except:
    print("ModuleNotFoundError: No module named 'reg'") # normal python error message
    print(f'{registry_path} is not pointing to the Vulkan-Headers registry directory.')
    print("Inside Vulkan-Headers there is a registry/reg.py file that is used.")
    sys.exit(1) # Return without call stack so easy to spot error

class DemoGenerator(BaseGenerator):
    def __init__(self):
        BaseGenerator.__init__(self)

    #
    # Called at beginning of processing as file is opened
    def generate(self):
        # Can write to the file anytime
        self.write("Hello from DemoGenerator")

        # |self.vk| is the |VulkanObject| defined in the vulkan_object.py file

        # Some found stats (and demo of using VulkanObject)
        print(f'''
There are currently:
    {len(self.vk.extensions)} extensions
    {len(self.vk.commands)} commands
    {len(self.vk.formats)} formats
        ''')

        # Loop all extensions, commands, enums, etc to extract value
        instance_count = 0
        device_count = 0
        for extension in self.vk.extensions.values():
            if extension.instance:
                instance_count += 1
            if extension.device:
                device_count += 1
        print(f"{instance_count} extensions are instance level, {device_count} are device level")

        print("\n-------------------------\n")

        print("All versions found:")
        for version in self.vk.versions.values():
            print(f"\t{version.name}")

        print("\n-------------------------\n")

        # Lets say you have a specific command you want to look up
        crp2 = self.vk.commands['vkCreateRenderPass2']
        print(f'{crp2.name} has {len(crp2.params)} parameters')
        for param in crp2.params:
            print(f'\t{param.name}')

        print("\n-------------------------\n")

        copy_ext = self.vk.extensions['VK_KHR_copy_commands2']
        print('VK_KHR_copy_commands2 contains:')
        for command in copy_ext.commands:
            print(f"command {command.name}")

if __name__ == '__main__':
    output_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'generated_files'))

    # Parse the specified registry XML into an ElementTree object
    vk_xml = os.path.abspath(os.path.join(registry_path, 'vk.xml'))
    tree = ElementTree.parse(vk_xml)

    # Currently there are no default, so these 4 fields must be set
    # (These apply for all generators)
    SetOutputDirectory(output_directory)
    SetOutputFileName("demo.txt")
    SetTargetApiName('vulkan')
    SetMergedApiNames(None)

    # Create an instance of our generator
    generator = DemoGenerator()
    # Additonal setting can be made here
    # The options are set before XML loading as they may affect how it is parsed
    base_options = BaseGeneratorOptions()

    # The is the "core" object
    reg = Registry(generator, base_options)

    # Load the XML tree into the registry object
    reg.loadElementTree(tree)

    # Runs the reg.py script, will call the `generate()` funciton when VulkanObject is created
    reg.apiGen()