import libs.Paramify as Paramify
config = Paramify.ConfigFile("./component_config.json" if __name__ == "__main__" else "./Component_manager/component_config.json")
components = config.load_param("components", "")
for component in components:
    name = component["name"]
    enabled = component["enabled"]
    if enabled:
        exec(f"import components.{name}")