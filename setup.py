import os

from argostranslate import package

# Update package definitions from remote
package.update_package_index()

# Load available packages from local package index
available_packages = package.get_available_packages()

# Download and install all available packages
currently_installed_packagers = package.get_installed_packages()
for available_package in available_packages:
    print(available_package, "available...")
    if available_package not in currently_installed_packagers:
        download_path = available_package.download()
        print("installing", available_package)
        package.install_from_path(download_path)
        print('done.')
    else:
        print('already installed.')

# read the setup script and change what you need to change
with open("translation_wrapper_template.sh", "r") as template_file:
    wrapper_contents = template_file.read().replace("/path/to", os.getcwd())

with open('translation_wrapper.sh', "w") as wrapper_script:
    wrapper_script.write(wrapper_contents)

with open("translate.py", "r") as translate_dot_py:
    script_contents = translate_dot_py.read()
    my_path = "#!/home/patrickpragman/PycharmProjects/models/translate/venv/bin/python"
    your_path = rf"#!{os.getcwd()}/venv/bin/python"
    planned_output = script_contents.replace(my_path, your_path)

with open("translate.py", "w") as translate_dot_py:
    translate_dot_py.write(planned_output)

