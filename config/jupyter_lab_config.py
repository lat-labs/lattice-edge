# JupyterLab Configuration for DeLab
c = get_config()

# Server settings
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.port = 8888
c.ServerApp.open_browser = False
c.ServerApp.root_dir = '/home/delab/work'

# Security settings (token set via environment variable)
c.ServerApp.token = ''
c.ServerApp.password = ''
c.ServerApp.allow_origin = '*'
c.ServerApp.allow_credentials = True

# Disable XSRF for API access
c.ServerApp.disable_check_xsrf = True

# Terminal settings
c.ServerApp.terminals_enabled = True
