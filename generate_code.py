#!/usr/bin/env python3

import os
import sys
from xml.etree import ElementTree

# |registry| is the the folder where the vk.xml and other scripts live
# |output_directory| is the folder to write the generated files too
def RunGenerators(registry_path: str, output_directory: str):

    # These live in the Vulkan-Docs repo, but are pulled in via the
    # Vulkan-Headers/registry folder
    # At runtime we inject python path to find these helper scripts
    sys.path.insert(0, registry_path)
    try:
        from reg import Registry
    except:
        print("ModuleNotFoundError: No module named 'reg'") # normal python error message
        print(f'{registry_path} is not pointing to the Vulkan-Headers registry directory.')
        print("Inside Vulkan-Headers there is a registry/reg.py file that is used.")
        sys.exit(1) # Return without call stack so easy to spot error

    from base_generator import BaseGeneratorOptions
    from generators.format_generator import FormatGenerator

    # These set fields that are needed by both OutputGenerator and BaseGenerator,
    # but are uniform and don't need to be set at a per-generated file level
    from base_generator import SetOutputDirectory, SetTargetApiName, SetMergedApiNames
    SetOutputDirectory(output_directory)
    # The base_generator works for other APIs (ex VulkanSC) so need specify just care about Vulkan
    SetTargetApiName('vulkan')
    SetMergedApiNames(None)

    # First grab a class contructor object and create an instance
    generator = FormatGenerator()

    # Set name of output for the code generation
    target = 'formats.h'
    base_options = BaseGeneratorOptions(customFileName = target)

    # Create the registry object with the specified generator and generator
    # options. The options are set before XML loading as they may affect it.
    reg = Registry(generator, base_options)

    # Parse the specified registry XML into an ElementTree object
    vk_xml = os.path.abspath(os.path.join(registry_path, 'vk.xml'))
    tree = ElementTree.parse(vk_xml)

    # Load the XML tree into the registry object
    reg.loadElementTree(tree)

    # Runs the reg.py script, but for most people, this will just call the `generate()` funciton for you
    reg.apiGen()


if __name__ == '__main__':
    # For sake of the demo, hardcode both the path the Vulkan-Headers and the generated file output
    registry_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Vulkan-Headers', 'registry'))
    output_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'generated_files'))

    if not os.path.isdir(registry_path):
        print(f'{registry_path} does not exist')
        sys.exit(-1)

    RunGenerators(registry_path, output_directory)

