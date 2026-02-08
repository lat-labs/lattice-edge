"""
latlab Custom Theme for JupyterLab

Provides dark mode with purple accents matching the latlab logo.
"""

import json
from pathlib import Path

# latlab purple palette based on logo
latlab_COLORS = {
    "primary": "#9B59B6",      # Main purple
    "primary_dark": "#8E44AD",  # Darker purple
    "primary_light": "#BB8FCE", # Lighter purple
    "accent": "#E74C3C",        # Red accent
    "success": "#27AE60",       # Green
    "warning": "#F39C12",       # Orange
    "info": "#3498DB",          # Blue
    "background": "#1C1E26",    # Dark background
    "background_alt": "#2D3142", # Alternate background
    "text": "#E8E9EB",          # Light text
    "text_muted": "#A6ACBE"     # Muted text
}

def create_latlab_theme():
    """Create latlab custom theme configuration."""
    
    theme = {
        "name": "latlab Dark",
        "displayName": "latlab Dark",
        "theme": {
            # Base colors
            "background": latlab_COLORS["background"],
            "foreground": latlab_COLORS["text"],
            "selection": latlab_COLORS["primary"] + "40",  # 40% opacity
            
            # UI colors
            "activityBar.background": latlab_COLORS["background_alt"],
            "activityBar.foreground": latlab_COLORS["text"],
            "activityBarBadge.background": latlab_COLORS["primary"],
            "activityBarBadge.foreground": latlab_COLORS["text"],
            
            # Sidebar
            "sideBar.background": latlab_COLORS["background"],
            "sideBar.foreground": latlab_COLORS["text"],
            "sideBarTitle.foreground": latlab_COLORS["primary_light"],
            
            # Editor
            "editor.background": latlab_COLORS["background"],
            "editor.foreground": latlab_COLORS["text"],
            "editor.lineHighlightBackground": latlab_COLORS["background_alt"],
            "editor.selectionBackground": latlab_COLORS["primary"] + "40",
            
            # Tabs
            "tab.activeBackground": latlab_COLORS["background_alt"],
            "tab.activeForeground": latlab_COLORS["text"],
            "tab.inactiveBackground": latlab_COLORS["background"],
            "tab.inactiveForeground": latlab_COLORS["text_muted"],
            "tab.activeBorderTop": latlab_COLORS["primary"],
            
            # Status bar
            "statusBar.background": latlab_COLORS["primary_dark"],
            "statusBar.foreground": latlab_COLORS["text"],
            "statusBar.noFolderBackground": latlab_COLORS["background_alt"],
            
            # Buttons
            "button.background": latlab_COLORS["primary"],
            "button.foreground": latlab_COLORS["text"],
            "button.hoverBackground": latlab_COLORS["primary_light"],
            
            # Input
            "input.background": latlab_COLORS["background_alt"],
            "input.foreground": latlab_COLORS["text"],
            "input.border": latlab_COLORS["primary"] + "60",
            "inputOption.activeBorder": latlab_COLORS["primary"],
            
            # Lists and trees
            "list.activeSelectionBackground": latlab_COLORS["primary"] + "40",
            "list.activeSelectionForeground": latlab_COLORS["text"],
            "list.inactiveSelectionBackground": latlab_COLORS["primary"] + "20",
            "list.hoverBackground": latlab_COLORS["primary"] + "20",
            
            # Notifications
            "notificationCenter.border": latlab_COLORS["primary"],
            "notifications.background": latlab_COLORS["background_alt"],
            "notifications.foreground": latlab_COLORS["text"],
            
            # Terminal
            "terminal.background": latlab_COLORS["background"],
            "terminal.foreground": latlab_COLORS["text"],
            "terminal.ansiBlack": "#000000",
            "terminal.ansiRed": latlab_COLORS["accent"],
            "terminal.ansiGreen": latlab_COLORS["success"],
            "terminal.ansiYellow": latlab_COLORS["warning"],
            "terminal.ansiBlue": latlab_COLORS["info"],
            "terminal.ansiMagenta": latlab_COLORS["primary"],
            "terminal.ansiCyan": "#17A2B8",
            "terminal.ansiWhite": latlab_COLORS["text"],
            
            # Jupyter specific
            "jupyter.cellBorderColor": latlab_COLORS["primary"] + "40",
            "jupyter.cellSelectionBackground": latlab_COLORS["primary"] + "20",
            "jupyter.outputBackground": latlab_COLORS["background_alt"],
        }
    }
    
    return theme


def install_latlab_theme(jupyter_data_dir: Path):
    """Install latlab theme in JupyterLab.

    Pass the Jupyter data dir (from `jupyter --data-dir`).
    """
    
    # Create labextensions directory for the theme package
    theme_dir = jupyter_data_dir / "labextensions" / "@latlab" / "theme-latlab-dark"
    theme_dir.mkdir(parents=True, exist_ok=True)
    
    # Create theme file
    theme = create_latlab_theme()
    theme_file = theme_dir / "index.css"
    
    # Generate CSS from theme
    css = generate_theme_css(theme["theme"])
    
    with open(theme_file, "w") as f:
        f.write(css)
    
    # Create package.json
    package = {
        "name": "@latlab/theme-latlab-dark",
        "version": "1.0.0",
        "description": "latlab dark theme for JupyterLab",
        "keywords": ["jupyterlab-theme"],
        "jupyterlab": {
            "themePath": "index.css"
        }
    }
    
    with open(theme_dir / "package.json", "w") as f:
        json.dump(package, f, indent=2)
    
    return theme_file


def install_latlab_custom_css(jupyter_config_dir: Path):
    """Install latlab custom CSS override for JupyterLab.

    Pass the Jupyter config dir (from `jupyter --config-dir`).
    """

    custom_dir = jupyter_config_dir / "custom"
    custom_dir.mkdir(parents=True, exist_ok=True)

    css = generate_theme_css()
    custom_css_file = custom_dir / "custom.css"

    with open(custom_css_file, "w") as f:
        f.write(css)

    return custom_css_file


def generate_theme_css(theme_config=None):
    """Generate CSS from theme configuration."""
    
    if theme_config is None:
        theme_config = {}
    
    css = """
/* latlab Dark Theme for JupyterLab */

:root {
    /* latlab Brand Colors */
    --latlab-primary: #9B59B6;
    --latlab-primary-dark: #8E44AD;
    --latlab-primary-light: #BB8FCE;
    --latlab-accent: #E74C3C;
    --latlab-success: #27AE60;
    --latlab-warning: #F39C12;
    --latlab-info: #3498DB;
    
    /* Background Colors */
    --latlab-bg-primary: #1C1E26;
    --latlab-bg-secondary: #2D3142;
    --latlab-bg-tertiary: #3A3F51;
    
    /* Text Colors */
    --latlab-text-primary: #E8E9EB;
    --latlab-text-secondary: #BDC3C7;
    --latlab-text-muted: #95A5A6;
    
    /* Borders */
    --latlab-border: #4A5568;
    --latlab-divider: #2D3748;
    
    /* Override JupyterLab theme variables */
    --jp-layout-color0: var(--latlab-bg-primary);
    --jp-layout-color1: var(--latlab-bg-secondary);
    --jp-layout-color2: var(--latlab-bg-tertiary);
    --jp-layout-color3: var(--latlab-bg-tertiary);
    
    --jp-brand-color0: var(--latlab-primary-dark);
    --jp-brand-color1: var(--latlab-primary);
    --jp-brand-color2: var(--latlab-primary-light);
    
    --jp-ui-font-color0: var(--latlab-text-primary);
    --jp-ui-font-color1: var(--latlab-text-secondary);
    --jp-ui-font-color2: var(--latlab-text-muted);
    
    --jp-content-font-color0: var(--latlab-text-primary);
    --jp-content-font-color1: var(--latlab-text-secondary);
    
    /* Cell borders */
    --jp-cell-editor-border-color: var(--latlab-border);
    --jp-cell-editor-active-border-color: var(--latlab-primary);
    
    /* Toolbar */
    --jp-toolbar-background: var(--latlab-bg-secondary);
    --jp-toolbar-border-color: var(--latlab-border);
    
    /* Sidebar */
    --jp-sidebar-min-width: 250px;
}

/* Main Shell */
.jp-LabShell {
    background: var(--latlab-bg-primary);
}

/* Top Panel */
#jp-top-panel {
    background: var(--latlab-bg-primary);
    border-bottom: 1px solid var(--latlab-border);
}

/* Menu Bar */
.lm-MenuBar {
    background: var(--latlab-bg-secondary);
}

.lm-MenuBar-item.lm-mod-active {
    background: var(--latlab-primary);
}

/* Sidebar */
.jp-SideBar {
    background: var(--latlab-bg-secondary);
}

.jp-SideBar .lm-mod-current {
    background: var(--latlab-primary);
}

/* File Browser */
.jp-FileBrowser {
    background: var(--latlab-bg-secondary);
}

.jp-DirListing-item.jp-mod-selected {
    background: var(--latlab-primary);
    color: white;
}

/* Notebook */
.jp-Notebook {
    background: var(--latlab-bg-primary);
}

/* Cell styling */
.jp-Cell {
    background: var(--latlab-bg-secondary);
    border: 1px solid var(--latlab-border);
    border-radius: 8px;
    margin-bottom: 12px;
}

.jp-Cell.jp-mod-selected {
    border-color: var(--latlab-primary);
    box-shadow: 0 0 0 2px var(--latlab-primary-light);
}

.jp-Cell.jp-mod-active {
    border-color: var(--latlab-primary);
}

/* Code Cells */
.jp-CodeCell .jp-InputArea {
    background: var(--latlab-bg-tertiary);
    border-radius: 6px;
}

.jp-OutputArea {
    background: var(--latlab-bg-primary);
    border-radius: 6px;
    margin-top: 8px;
}

/* Markdown Cells */
.jp-MarkdownCell .jp-InputArea {
    background: transparent;
}

.jp-MarkdownOutput {
    color: var(--latlab-text-primary);
}

.jp-MarkdownOutput h1,
.jp-MarkdownOutput h2,
.jp-MarkdownOutput h3 {
    color: var(--latlab-primary-light);
}

/* Code Mirror Theme */
.cm-s-jupyter {
    background: var(--latlab-bg-tertiary);
    color: var(--latlab-text-primary);
}

.cm-s-jupyter .CodeMirror-gutters {
    background: var(--latlab-bg-secondary);
    border-right: 1px solid var(--latlab-border);
}

.cm-s-jupyter .cm-keyword { color: var(--latlab-primary-light); }
.cm-s-jupyter .cm-string { color: var(--latlab-success); }
.cm-s-jupyter .cm-number { color: var(--latlab-warning); }
.cm-s-jupyter .cm-def { color: var(--latlab-info); }
.cm-s-jupyter .cm-variable { color: var(--latlab-text-primary); }
.cm-s-jupyter .cm-comment { color: var(--latlab-text-muted); }
.cm-s-jupyter .cm-operator { color: var(--latlab-primary-light); }

/* Notebook Toolbar */
.jp-NotebookPanel-toolbar {
    background: var(--latlab-bg-secondary);
    border-bottom: 1px solid var(--latlab-border);
}

/* Tabs */
.lm-DockPanel-tabBar {
    background: var(--latlab-bg-secondary);
}

.lm-DockPanel-tab {
    background: var(--latlab-bg-tertiary);
    border: 1px solid var(--latlab-border);
    color: var(--latlab-text-secondary);
}

.lm-DockPanel-tab.lm-mod-current {
    background: var(--latlab-primary);
    color: white;
    border-color: var(--latlab-primary);
}

/* Buttons */
.jp-Button {
    background: var(--latlab-primary);
    border: none;
    color: white;
}

.jp-Button:hover {
    background: var(--latlab-primary-dark);
}

.jp-Button.jp-mod-styled.jp-mod-warn {
    background: var(--latlab-warning);
}

.jp-Button.jp-mod-styled.jp-mod-reject {
    background: var(--latlab-accent);
}

/* Terminal */
.jp-Terminal {
    background: var(--latlab-bg-primary);
    border: 1px solid var(--latlab-border);
}

.jp-Terminal-body {
    background: var(--latlab-bg-primary);
}

/* Status Bar */
#jp-main-statusbar {
    background: var(--latlab-bg-secondary);
    border-top: 1px solid var(--latlab-border);
}

/* Launcher */
.jp-Launcher {
    background: var(--latlab-bg-primary);
}

.jp-LauncherCard {
    background: var(--latlab-bg-tertiary);
    border: 1px solid var(--latlab-border);
    border-radius: 8px;
}

.jp-LauncherCard:hover {
    background: var(--latlab-bg-secondary);
    border-color: var(--latlab-primary);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(155, 89, 182, 0.3);
}

/* Scrollbars */
::-webkit-scrollbar {
    width: 12px;
    height: 12px;
}

::-webkit-scrollbar-track {
    background: var(--latlab-bg-secondary);
}

::-webkit-scrollbar-thumb {
    background: var(--latlab-bg-tertiary);
    border-radius: 6px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--latlab-primary);
}

/* Tooltips */
.jp-Tooltip {
    background: var(--latlab-bg-tertiary);
    border: 1px solid var(--latlab-primary);
    color: var(--latlab-text-primary);
}

/* Dialogs */
.jp-Dialog {
    background: var(--latlab-bg-secondary);
    border: 1px solid var(--latlab-border);
    border-radius: 8px;
}

.jp-Dialog-header {
    background: var(--latlab-bg-tertiary);
    border-bottom: 1px solid var(--latlab-border);
}

/* Context Menus */
.lm-Menu {
    background: var(--latlab-bg-tertiary);
    border: 1px solid var(--latlab-border);
}

.lm-Menu-item.lm-mod-active {
    background: var(--latlab-primary);
}

/* Progress Bars */
.jp-ProgressBar > .jp-ProgressBar-progress {
    background: var(--latlab-primary);
}

/* Links */
a {
    color: var(--latlab-primary);
}

a:hover {
    color: var(--latlab-primary-light);
}

/* Selection */
::selection {
    background: var(--latlab-primary);
    color: white;
}

/* Jupyter Widgets Styling */
.widget-label {
    color: var(--latlab-text-primary) !important;
}

.widget-readout {
    background: var(--latlab-bg-tertiary) !important;
    color: var(--latlab-text-primary) !important;
    border: 1px solid var(--latlab-border) !important;
}

.widget-slider {
    background: var(--latlab-bg-tertiary) !important;
}

.ui-slider-handle {
    background: var(--latlab-primary) !important;
    border: 2px solid var(--latlab-primary-dark) !important;
}

.widget-button {
    background: var(--latlab-primary) !important;
    color: white !important;
    border: none !important;
    border-radius: 4px !important;
}

.widget-button:hover {
    background: var(--latlab-primary-dark) !important;
}

.widget-tab > .widget-tab-bar {
    background: var(--latlab-bg-secondary) !important;
}

.widget-tab > .widget-tab-bar .widget-tab {
    background: var(--latlab-bg-tertiary) !important;
    color: var(--latlab-text-secondary) !important;
}

.widget-tab > .widget-tab-bar .widget-tab.lm-mod-current {
    background: var(--latlab-primary) !important;
    color: white !important;
}

/* latlab Branding */
.latlab-branding {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-weight: 600;
    background: linear-gradient(135deg, var(--latlab-primary-dark), var(--latlab-primary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Custom Animations */
@keyframes latlab-pulse {
    0% { opacity: 1; }
    50% { opacity: 0.6; }
    100% { opacity: 1; }
}

.latlab-processing {
    animation: latlab-pulse 2s ease-in-out infinite;
}
"""
    
    return css


def apply_latlab_defaults():
    """Apply latlab default settings."""
    
    settings = {
        # Default to dark theme
        "theme": "latlab Dark",
        
        # Code cell settings
        "codeCellConfig": {
            "lineNumbers": True,
            "lineWrap": False,
            "matchBrackets": True,
            "autoClosingBrackets": True
        },
        
        # Notebook settings
        "notebookConfig": {
            "kernelShutdown": False,
            "recordTiming": True,
            "scrollPastEnd": True
        },
        
        # Terminal settings
        "terminalConfig": {
            "fontSize": 13,
            "lineHeight": 1.2,
            "theme": "dark"
        }
    }
    
