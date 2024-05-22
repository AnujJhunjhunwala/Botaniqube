import os 
from kedro.framework.context import KedroContext
from kedro.config import OmegaConfigLoader 

class ProjectContext(KedroContext): 
    '''Loads project configuration and registers pipelines''' 
    def get_config_loader(self): 
        """Loads configuration files from the 'conf' directory. """ 
        conf_paths = ["conf/base", "conf/local"] 
        # Load 'base' and 'local' configuration 
        conf_loader = OmegaConfigLoader(conf_paths) 
        return conf_loader 