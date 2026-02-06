import { IThemeManager } from '@jupyterlab/apputils';

const style = '@delab/theme-delab-dark/index.css';

const plugin = {
  id: '@delab/theme-delab-dark:plugin',
  autoStart: true,
  requires: [IThemeManager],
  activate: (_app: unknown, manager: IThemeManager) => {
    manager.register({
      name: 'DeLab Dark',
      isLight: false,
      themeScrollbars: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve()
    });
  }
};

export default plugin;
