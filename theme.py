"""
DeLab Custom Theme for JupyterLab

Provides dark mode with purple accents matching the DeLab logo.
"""

import json
from pathlib import Path

# DeLab purple palette based on logo
DELAB_COLORS = {
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

def create_delab_theme():
    """Create DeLab custom theme configuration."""
    
    theme = {
        "name": "DeLab Dark",
        "displayName": "DeLab Dark",
        "theme": {
            # Base colors
            "background": DELAB_COLORS["background"],
            "foreground": DELAB_COLORS["text"],
            "selection": DELAB_COLORS["primary"] + "40",  # 40% opacity
            
            # UI colors
            "activityBar.background": DELAB_COLORS["background_alt"],
            "activityBar.foreground": DELAB_COLORS["text"],
            "activityBarBadge.background": DELAB_COLORS["primary"],
            "activityBarBadge.foreground": DELAB_COLORS["text"],
            
            # Sidebar
            "sideBar.background": DELAB_COLORS["background"],
            "sideBar.foreground": DELAB_COLORS["text"],
            "sideBarTitle.foreground": DELAB_COLORS["primary_light"],
            
            # Editor
            "editor.background": DELAB_COLORS["background"],
            "editor.foreground": DELAB_COLORS["text"],
            "editor.lineHighlightBackground": DELAB_COLORS["background_alt"],
            "editor.selectionBackground": DELAB_COLORS["primary"] + "40",
            
            # Tabs
            "tab.activeBackground": DELAB_COLORS["background_alt"],
            "tab.activeForeground": DELAB_COLORS["text"],
            "tab.inactiveBackground": DELAB_COLORS["background"],
            "tab.inactiveForeground": DELAB_COLORS["text_muted"],
            "tab.activeBorderTop": DELAB_COLORS["primary"],
            
            # Status bar
            "statusBar.background": DELAB_COLORS["primary_dark"],
            "statusBar.foreground": DELAB_COLORS["text"],
            "statusBar.noFolderBackground": DELAB_COLORS["background_alt"],
            
            # Buttons
            "button.background": DELAB_COLORS["primary"],
            "button.foreground": DELAB_COLORS["text"],
            "button.hoverBackground": DELAB_COLORS["primary_light"],
            
            # Input
            "input.background": DELAB_COLORS["background_alt"],
            "input.foreground": DELAB_COLORS["text"],
            "input.border": DELAB_COLORS["primary"] + "60",
            "inputOption.activeBorder": DELAB_COLORS["primary"],
            
            # Lists and trees
            "list.activeSelectionBackground": DELAB_COLORS["primary"] + "40",
            "list.activeSelectionForeground": DELAB_COLORS["text"],
            "list.inactiveSelectionBackground": DELAB_COLORS["primary"] + "20",
            "list.hoverBackground": DELAB_COLORS["primary"] + "20",
            
            # Notifications
            "notificationCenter.border": DELAB_COLORS["primary"],
            "notifications.background": DELAB_COLORS["background_alt"],
            "notifications.foreground": DELAB_COLORS["text"],
            
            # Terminal
            "terminal.background": DELAB_COLORS["background"],
            "terminal.foreground": DELAB_COLORS["text"],
            "terminal.ansiBlack": "#000000",
            "terminal.ansiRed": DELAB_COLORS["accent"],
            "terminal.ansiGreen": DELAB_COLORS["success"],
            "terminal.ansiYellow": DELAB_COLORS["warning"],
            "terminal.ansiBlue": DELAB_COLORS["info"],
            "terminal.ansiMagenta": DELAB_COLORS["primary"],
            "terminal.ansiCyan": "#17A2B8",
            "terminal.ansiWhite": DELAB_COLORS["text"],
            
            # Jupyter specific
            "jupyter.cellBorderColor": DELAB_COLORS["primary"] + "40",
            "jupyter.cellSelectionBackground": DELAB_COLORS["primary"] + "20",
            "jupyter.outputBackground": DELAB_COLORS["background_alt"],
        }
    }
    
    return theme


def install_delab_theme(jupyter_data_dir: Path):
    """Install DeLab theme in JupyterLab.

    Pass the Jupyter data dir (from `jupyter --data-dir`).
    """
    
    # Create labextensions directory for the theme package
    theme_dir = jupyter_data_dir / "labextensions" / "@delab" / "theme-delab-dark"
    theme_dir.mkdir(parents=True, exist_ok=True)
    
    # Create theme file
    theme = create_delab_theme()
    theme_file = theme_dir / "index.css"
    
    # Generate CSS from theme
    css = generate_theme_css(theme["theme"])
    
    with open(theme_file, "w") as f:
        f.write(css)
    
    # Create package.json
    package = {
        "name": "@delab/theme-delab-dark",
        "version": "1.0.0",
        "description": "DeLab dark theme for JupyterLab",
        "keywords": ["jupyterlab-theme"],
        "jupyterlab": {
            "themePath": "index.css"
        }
    }
    
    with open(theme_dir / "package.json", "w") as f:
        json.dump(package, f, indent=2)
    
    return theme_file


def install_delab_custom_css(jupyter_config_dir: Path):
    """Install DeLab custom CSS override for JupyterLab.

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
/* DeLab Dark Theme for JupyterLab */

:root {
    /* DeLab Brand Colors */
    --delab-primary: #9B59B6;
    --delab-primary-dark: #8E44AD;
    --delab-primary-light: #BB8FCE;
    --delab-accent: #E74C3C;
    --delab-success: #27AE60;
    --delab-warning: #F39C12;
    --delab-info: #3498DB;
    
    /* Background Colors */
    --delab-bg-primary: #1C1E26;
    --delab-bg-secondary: #2D3142;
    --delab-bg-tertiary: #3A3F51;
    
    /* Text Colors */
    --delab-text-primary: #E8E9EB;
    --delab-text-secondary: #BDC3C7;
    --delab-text-muted: #95A5A6;
    
    /* Borders */
    --delab-border: #4A5568;
    --delab-divider: #2D3748;
    
    /* Override JupyterLab theme variables */
    --jp-layout-color0: var(--delab-bg-primary);
    --jp-layout-color1: var(--delab-bg-secondary);
    --jp-layout-color2: var(--delab-bg-tertiary);
    --jp-layout-color3: var(--delab-bg-tertiary);
    
    --jp-brand-color0: var(--delab-primary-dark);
    --jp-brand-color1: var(--delab-primary);
    --jp-brand-color2: var(--delab-primary-light);
    
    --jp-ui-font-color0: var(--delab-text-primary);
    --jp-ui-font-color1: var(--delab-text-secondary);
    --jp-ui-font-color2: var(--delab-text-muted);
    
    --jp-content-font-color0: var(--delab-text-primary);
    --jp-content-font-color1: var(--delab-text-secondary);
    
    /* Cell borders */
    --jp-cell-editor-border-color: var(--delab-border);
    --jp-cell-editor-active-border-color: var(--delab-primary);
    
    /* Toolbar */
    --jp-toolbar-background: var(--delab-bg-secondary);
    --jp-toolbar-border-color: var(--delab-border);
    
    /* Sidebar */
    --jp-sidebar-min-width: 250px;
}

/* Main Shell */
.jp-LabShell {
    background: var(--delab-bg-primary);
}

/* Top Panel */
#jp-top-panel {
    background: var(--delab-bg-primary);
    border-bottom: 1px solid var(--delab-border);
}

/* Menu Bar */
.lm-MenuBar {
    background: var(--delab-bg-secondary);
}

.lm-MenuBar-item.lm-mod-active {
    background: var(--delab-primary);
}

/* Sidebar */
.jp-SideBar {
    background: var(--delab-bg-secondary);
}

.jp-SideBar .lm-mod-current {
    background: var(--delab-primary);
}

/* File Browser */
.jp-FileBrowser {
    background: var(--delab-bg-secondary);
}

.jp-DirListing-item.jp-mod-selected {
    background: var(--delab-primary);
    color: white;
}

/* Notebook */
.jp-Notebook {
    background: var(--delab-bg-primary);
}

/* Cell styling */
.jp-Cell {
    background: var(--delab-bg-secondary);
    border: 1px solid var(--delab-border);
    border-radius: 8px;
    margin-bottom: 12px;
}

.jp-Cell.jp-mod-selected {
    border-color: var(--delab-primary);
    box-shadow: 0 0 0 2px var(--delab-primary-light);
}

.jp-Cell.jp-mod-active {
    border-color: var(--delab-primary);
}

/* Code Cells */
.jp-CodeCell .jp-InputArea {
    background: var(--delab-bg-tertiary);
    border-radius: 6px;
}

.jp-OutputArea {
    background: var(--delab-bg-primary);
    border-radius: 6px;
    margin-top: 8px;
}

/* Markdown Cells */
.jp-MarkdownCell .jp-InputArea {
    background: transparent;
}

.jp-MarkdownOutput {
    color: var(--delab-text-primary);
}

.jp-MarkdownOutput h1,
.jp-MarkdownOutput h2,
.jp-MarkdownOutput h3 {
    color: var(--delab-primary-light);
}

/* Code Mirror Theme */
.cm-s-jupyter {
    background: var(--delab-bg-tertiary);
    color: var(--delab-text-primary);
}

.cm-s-jupyter .CodeMirror-gutters {
    background: var(--delab-bg-secondary);
    border-right: 1px solid var(--delab-border);
}

.cm-s-jupyter .cm-keyword { color: var(--delab-primary-light); }
.cm-s-jupyter .cm-string { color: var(--delab-success); }
.cm-s-jupyter .cm-number { color: var(--delab-warning); }
.cm-s-jupyter .cm-def { color: var(--delab-info); }
.cm-s-jupyter .cm-variable { color: var(--delab-text-primary); }
.cm-s-jupyter .cm-comment { color: var(--delab-text-muted); }
.cm-s-jupyter .cm-operator { color: var(--delab-primary-light); }

/* Notebook Toolbar */
.jp-NotebookPanel-toolbar {
    background: var(--delab-bg-secondary);
    border-bottom: 1px solid var(--delab-border);
}

/* Tabs */
.lm-DockPanel-tabBar {
    background: var(--delab-bg-secondary);
}

.lm-DockPanel-tab {
    background: var(--delab-bg-tertiary);
    border: 1px solid var(--delab-border);
    color: var(--delab-text-secondary);
}

.lm-DockPanel-tab.lm-mod-current {
    background: var(--delab-primary);
    color: white;
    border-color: var(--delab-primary);
}

/* Buttons */
.jp-Button {
    background: var(--delab-primary);
    border: none;
    color: white;
}

.jp-Button:hover {
    background: var(--delab-primary-dark);
}

.jp-Button.jp-mod-styled.jp-mod-warn {
    background: var(--delab-warning);
}

.jp-Button.jp-mod-styled.jp-mod-reject {
    background: var(--delab-accent);
}

/* Terminal */
.jp-Terminal {
    background: var(--delab-bg-primary);
    border: 1px solid var(--delab-border);
}

.jp-Terminal-body {
    background: var(--delab-bg-primary);
}

/* Status Bar */
#jp-main-statusbar {
    background: var(--delab-bg-secondary);
    border-top: 1px solid var(--delab-border);
}

/* Launcher */
.jp-Launcher {
    background: var(--delab-bg-primary);
}

.jp-LauncherCard {
    background: var(--delab-bg-tertiary);
    border: 1px solid var(--delab-border);
    border-radius: 8px;
}

.jp-LauncherCard:hover {
    background: var(--delab-bg-secondary);
    border-color: var(--delab-primary);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(155, 89, 182, 0.3);
}

/* Scrollbars */
::-webkit-scrollbar {
    width: 12px;
    height: 12px;
}

::-webkit-scrollbar-track {
    background: var(--delab-bg-secondary);
}

::-webkit-scrollbar-thumb {
    background: var(--delab-bg-tertiary);
    border-radius: 6px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--delab-primary);
}

/* Tooltips */
.jp-Tooltip {
    background: var(--delab-bg-tertiary);
    border: 1px solid var(--delab-primary);
    color: var(--delab-text-primary);
}

/* Dialogs */
.jp-Dialog {
    background: var(--delab-bg-secondary);
    border: 1px solid var(--delab-border);
    border-radius: 8px;
}

.jp-Dialog-header {
    background: var(--delab-bg-tertiary);
    border-bottom: 1px solid var(--delab-border);
}

/* Context Menus */
.lm-Menu {
    background: var(--delab-bg-tertiary);
    border: 1px solid var(--delab-border);
}

.lm-Menu-item.lm-mod-active {
    background: var(--delab-primary);
}

/* Progress Bars */
.jp-ProgressBar > .jp-ProgressBar-progress {
    background: var(--delab-primary);
}

/* Links */
a {
    color: var(--delab-primary);
}

a:hover {
    color: var(--delab-primary-light);
}

/* Selection */
::selection {
    background: var(--delab-primary);
    color: white;
}

/* Jupyter Widgets Styling */
.widget-label {
    color: var(--delab-text-primary) !important;
}

.widget-readout {
    background: var(--delab-bg-tertiary) !important;
    color: var(--delab-text-primary) !important;
    border: 1px solid var(--delab-border) !important;
}

.widget-slider {
    background: var(--delab-bg-tertiary) !important;
}

.ui-slider-handle {
    background: var(--delab-primary) !important;
    border: 2px solid var(--delab-primary-dark) !important;
}

.widget-button {
    background: var(--delab-primary) !important;
    color: white !important;
    border: none !important;
    border-radius: 4px !important;
}

.widget-button:hover {
    background: var(--delab-primary-dark) !important;
}

.widget-tab > .widget-tab-bar {
    background: var(--delab-bg-secondary) !important;
}

.widget-tab > .widget-tab-bar .widget-tab {
    background: var(--delab-bg-tertiary) !important;
    color: var(--delab-text-secondary) !important;
}

.widget-tab > .widget-tab-bar .widget-tab.lm-mod-current {
    background: var(--delab-primary) !important;
    color: white !important;
}

/* DeLab Branding */
.delab-branding {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-weight: 600;
    background: linear-gradient(135deg, var(--delab-primary-dark), var(--delab-primary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Custom Animations */
@keyframes delab-pulse {
    0% { opacity: 1; }
    50% { opacity: 0.6; }
    100% { opacity: 1; }
}

.delab-processing {
    animation: delab-pulse 2s ease-in-out infinite;
}
"""
    
    return css


def apply_delab_defaults():
    """Apply DeLab default settings."""
    
    settings = {
        # Default to dark theme
        "theme": "DeLab Dark",
        
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
    
