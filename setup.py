from argostranslate import package

# Update package definitions from remote
package.update_package_index()

# Load available packages from local package index
available_packages = package.get_available_packages()

# Download and install all available packages
for available_package in available_packages:
    download_path = available_package.download()
    print(download_path)
    package.install_from_path(download_path)

