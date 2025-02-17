#!/usr/bin/python3 -i
import os

# These are imported from the Vulkan-Headers
# (Might need your editor to add the registry folder path in order to get intellisense)
from vulkan_object import (Format)
from base_generator import BaseGenerator

class FormatGenerator(BaseGenerator):
    def __init__(self):
        BaseGenerator.__init__(self)

    #
    # Called at beginning of processing as file is opened
    def generate(self):
        self.write(f'''// *** THIS FILE IS GENERATED - DO NOT EDIT ***
// See {os.path.basename(__file__)} for modifications\n''')

        out = []
        out.append('''
#pragma once

bool HasLargeBlockSize(VkFormat format) {
    swtich (format) {\n''')

        for format in self.vk.formats.values():
            if format.blockSize >= 16:
                out.append(f'        case {format.name}: // block size = {format.blockSize}\n')

        out.append('''
            return true;
        default: break;
    }
    return false;
}''')

        self.write("".join(out))