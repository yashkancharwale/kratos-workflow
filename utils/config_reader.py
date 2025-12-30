"""Configuration reader for YAML files"""

import yaml
import os
from typing import Any, Dict


class ConfigReader:
    """Read and manage configuration from YAML files"""
    
    @staticmethod
    def read_yaml(file_path: str) -> Dict[str, Any]:
        """
        Read YAML file and return as dictionary
        
        Args:
            file_path: Path to YAML file
            
        Returns:
            Dictionary containing YAML content
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Config file not found: {file_path}")
        
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    
    @staticmethod
    def get_env_config(config_dir: str = "config") -> Dict[str, Any]:
        """Get environment configuration"""
        return ConfigReader.read_yaml(os.path.join(config_dir, "env.yaml"))
    
    @staticmethod
    def get_credentials(config_dir: str = "config") -> Dict[str, Any]:
        """Get credentials configuration"""
        return ConfigReader.read_yaml(os.path.join(config_dir, "credentials.yaml"))
    
    @staticmethod
    def get_tenants(config_dir: str = "config") -> Dict[str, Any]:
        """Get tenants configuration"""
        return ConfigReader.read_yaml(os.path.join(config_dir, "tenants.yaml"))
