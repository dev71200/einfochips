const DARK_BOOTSTRAP_THEME = 'inc-bootstrap/css/bootstrap-dark.min.css';
const LIGHT_BOOTSTRAP_THEME = 'inc-bootstrap/css/bootstrap-light.min.css';

const DARK_einfo_THEME = 'inc-einfochips/css/einfochips-dark.css';
const LIGHT_einfo_THEME = 'inc-einfochips/css/einfochips-light.css';

$(document).ready(() => {
  if (isDarkThemeEnabled()) {
    document.getElementById('theme_checkbox').checked = true
  }
});

/**
 * Load the last theme used by looking into localstorage
 */
function loadLastTheme() {
  if (isDarkThemeEnabled()) {
    setBootstrapTheme(DARK_BOOTSTRAP_THEME)
    seteinfoTheme(DARK_einfo_THEME)
  }
}

/**
 * Toggles between light and dark themes
 */
function toggleTheme() {
  localStorage.setItem('dark_theme_enabled', document.getElementById('theme_checkbox').checked)
  if (document.getElementById('theme_checkbox').checked) {
    this.setBootstrapTheme(DARK_BOOTSTRAP_THEME)
    this.seteinfoTheme(DARK_einfo_THEME)
  }
  else {
    this.setBootstrapTheme(LIGHT_BOOTSTRAP_THEME)
    this.seteinfoTheme(LIGHT_einfo_THEME)
  }
};

/**
 * Toggles between light and dark themes
 */
function toggleTheme() {
  const darkThemeEnabled = document.getElementById('theme_checkbox').checked
  saveIsDarkThemeEnabled(darkThemeEnabled)

  if (darkThemeEnabled) {
    this.setBootstrapTheme(DARK_BOOTSTRAP_THEME)
    this.seteinfoTheme(DARK_einfo_THEME)
  }
  else {
    this.setBootstrapTheme(LIGHT_BOOTSTRAP_THEME)
    this.seteinfoTheme(LIGHT_einfo_THEME)
  }
};

/**
 * Sets the css file location received as the bootstrap theme
 * @param {string} file
 */
function setBootstrapTheme(file) {
  document.getElementById('bootstrap-theme').href = file
}

/**
 * Sets the css file location received as the einfo theme
 * @param {string} file
 */
function seteinfoTheme(file) {
  document.getElementById('einfo-theme').href = file
}

/**
 * Tells us if the dark theme is enabled or not
 * @returns {boolean}
 */
function isDarkThemeEnabled() {
  return localStorage.getItem('dark_theme_enabled') === 'true'
}

/**
 * Saves which theme is selected within the localstorage
 * @param {boolean} isDarkThemeEnabled 
 */
function saveIsDarkThemeEnabled(isDarkThemeEnabled) {
  localStorage.setItem('dark_theme_enabled', isDarkThemeEnabled)
}