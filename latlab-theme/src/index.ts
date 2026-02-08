import { IThemeManager } from '@jupyterlab/apputils';

const style = '@latlab/theme-latlab-dark/index.css';

const plugin = {
  id: '@latlab/theme-latlab-dark:plugin',
  autoStart: true,
  requires: [IThemeManager],
  activate: (_app: unknown, manager: IThemeManager) => {
    manager.register({
      name: 'latlab Dark',
      isLight: false,
      themeScrollbars: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve()
    });
  }
};

export default plugin;
