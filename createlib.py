import os
import subprocess
import shutil

class RustProject:
    def __init__(self, project_name: str, project_type: str = "lib", dependencies: list = None):
        """
        Initializes a new Rust project with the specified name and type.

        :param str project_name: The name of the project.
        :param str project_type: The type of project to create. Must be "lib" or "bin".
        :param list dependencies: Optional list of dependencies to add to the project.

        :return: None
        """
        self.project_name = project_name
        self.project_type = project_type
        self.project_path = None
        self.dependencies = dependencies if dependencies else []

    def _check_cargo_installed(self):
        """
        Checks if Cargo is installed and available in the system's PATH.

        :return: True if Cargo is installed, False otherwise
        """
        try:
            subprocess.run(["cargo", "--version"], check=True)
        except FileNotFoundError:
            print("Error: Cargo is not installed. Please install Rust and Cargo.")
            return False
        return True

    def create_project(self):
        """
        Creates a new Rust project with the specified name and type.

        :param str project_type: The type of project to create. Must be "lib" or "bin".
        :param list dependencies: Optional list of dependencies to add to the project.

        :return: None
        :raises CalledProcessError: If there is an error creating the project.
        """
        if not self._check_cargo_installed():
            return

        project_type_flag = "--lib" if self.project_type == "lib" else "--bin"
        try:
            subprocess.run(["cargo", "new", project_type_flag, self.project_name], check=True)
            self.project_path = self.project_name
            self._add_dependencies()
        except subprocess.CalledProcessError as e:
            print(f"Error creating new Rust {self.project_type} project: {str(e)}")

    def _add_dependencies(self):
        """
        Adds the specified dependencies to the project's Cargo.toml file.

        If the project has no dependencies, this method does nothing.

        :raises CalledProcessError: If there is an error running the `cargo add` command.
        """
        if not self.dependencies:
            return

        try:
            for dependency in self.dependencies:
                subprocess.run(["cargo", "add", dependency], check=True, cwd=self.project_path)
        except subprocess.CalledProcessError as e:
            print(f"Error adding dependency: {str(e)}")

    def write_code(self, rust_code: str):
    """
    Writes the provided Rust code to the appropriate source file in the project.
    
    This method determines the correct file name (either 'lib.rs' or 'main.rs')
    based on the project type ('lib' or 'bin') and writes the given Rust code 
    to that file within the project's 'src' directory. If the project has not 
    been created, it prints an error message and returns.
    
    Parameters:
    rust_code (str): The Rust code to be written to the source file.
    """
        if self.project_path is None:
            print("Error: Rust project not created.")
            return

        src_file_name = "lib.rs" if self.project_type == "lib" else "main.rs"
        src_file_path = os.path.join(self.project_path, "src", src_file_name)
        with open(src_file_path, "w") as rust_file:
            rust_file.write(rust_code)

    def build_and_run(self):
        """
        Builds and runs the created Rust project using Cargo.

        If the project was not created (i.e., project_path is None), or if Cargo is not installed,
        an error message is printed and the function does nothing.

        :return:
        """
        if self.project_path is None:
            print("Error: Rust project not created.")
            return

        if not self._check_cargo_installed():
            return

        try:
            subprocess.run(["cargo", "run"], check=True, cwd=self.project_path)
        except subprocess.CalledProcessError as e:
            print(f"Error running Rust code: {str(e)}")

    def cleanup(self):
    """
    Removes the created Rust project directory and resets the project path.

    This method deletes the directory specified by `self.project_path`, effectively
    cleaning up the resources created during the project setup. It then sets 
    `self.project_path` to `None` to indicate that there is no active project.
    """
        if self.project_path is not None:
            shutil.rmtree(self.project_path)
            self.project_path = None
