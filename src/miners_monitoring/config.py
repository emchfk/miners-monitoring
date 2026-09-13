from platformdirs import PlatformDirs

# List of directories for user-specific data, config, cache, etc.
dirs = PlatformDirs("miners-monitoring", "emchfk", ensure_exists=True)
