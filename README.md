# Vulkan-Code-Gen-Example

Show how to use Vulkan Object inside the Vulkan Headers

- Files [vulkan_object.py](https://github.com/spencer-lunarg/Vulkan-Headers/blob/spencer-lunarg-vulkan-object/registry/vulkan_object.py) and [base_generator.py](https://github.com/spencer-lunarg/Vulkan-Headers/blob/spencer-lunarg-vulkan-object/registry/base_generator.py)
- [Background info](./Vulkan_Code_Gen.pdf)

> Note - Python 3.10+ required
>
> This is only currently supported as a python script due to current workflows using python. If python is not possible to use for your code generation, please let us know and maybe it is possible to support other scripting langauges.

# How to setup demo

First clone and get the beta header with the `vulkan_object.py` file

```bash
https://github.com/spencer-lunarg/Vulkan-Code-Gen-Example.git
cd Vulkan-Code-Gen-Example
git submodule update --init --depth 1
```

## Simple code gen

run `python generate_code.py` and check the `generated_files/` folder afterwards

## How to integrate into your code

1. Make sure you have the [Vulkan Headers](https://github.com/KhronosGroup/Vulkan-Headers) repo 1.4.309 or higher somewhere on your machine. (The Vulkan SDK will not contain these files because people doing code generation almost always want the lastet version of the headers)

2. Inside your python script you will use `sys.path.insert(0, registry_path)` to add the path to `Vulkan-Headers/registry/` where the scripts live

3. The underlying framework uses a concept of `Generators` which is just a python class that will be in charge of writing a single file out. The `BaseGenerator` is just a generator that will parse the `vk.xml` out to a `VulkanObject` for you

See [demo.py](./demo.py) for example of the workflow where we inject the path at the start so the code can work as normal.