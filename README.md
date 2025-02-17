# Vulkan-Code-Gen-Example

Show how to use Vulkan Object inside the Vulkan Headers

- Files [vulkan_object.py](https://github.com/spencer-lunarg/Vulkan-Headers/blob/spencer-lunarg-vulkan-object/registry/vulkan_object.py) and [base_generator.py](https://github.com/spencer-lunarg/Vulkan-Headers/blob/spencer-lunarg-vulkan-object/registry/base_generator.py)
- [Background info](./Vulkan_Code_Gen.pdf)

# How to setup demo

First clone and get the beta header with the `vulkan_object.py` file

```bash
https://github.com/spencer-lunarg/Vulkan-Code-Gen-Example.git
cd Vulkan-Code-Gen-Example
git submodule update --init --depth 1
```

## Simple code gen

run `python generate_code.py` and check the `generated_files/` folder afterwards
